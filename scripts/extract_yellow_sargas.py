#!/usr/bin/env python3
"""Phase-2 Sundarakāṇḍa: deterministic commentary segmenter (no LLM).

Segments the licensed Gita Supersite Sanskrit commentaries (Tilaka / Bhūṣaṇa /
Śiromaṇi) for the Sundarakāṇḍa by their embedded verse markers ``।। 5.s.v ।।``,
aligns each verse's commentary with the verse text (IAST) and Leonov's Russian
подстрочник from the sibling SamudraManthanam corpus, and writes per-verse
bundles that the Sonnet drafting step consumes.

This is step 1 of the Phase-2 build (see docs/PHASE2_SUNDARA_HANDOFF.md).
Deterministic and stdlib-only; it does NOT write any candidate notes.

Usage:
    python scripts/extract_yellow_sargas.py                 # pilot sargas 35 36 37
    python scripts/extract_yellow_sargas.py 22 24 26        # custom sargas
"""
import sys
import os
import re
import json

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
COMM_DIR = os.path.join(REPO, "data", "valmiki_commentaries", "kanda_5_sundarakanda")
sys.path.insert(0, HERE)
from sa_align import find_sibling  # noqa: E402

_SM = find_sibling("SamudraManthanam")
JSONL = os.path.join(
    _SM or os.path.join(REPO, "..", "SamudraManthanam"),
    "web", "corpus_builder", "jsonl", "05_ramayana-sundarakanda.jsonl",
)
OUT = os.path.join(REPO, "data", "analysis", "sundara_commentary_segmented.json")

COMMENTATORS = ["tilaka", "bhusana", "siromani", "tattvadipika"]
PILOT_SARGAS = [35, 36, 37]

# Content-anchor thresholds (H268 WS-C2, calibrated on the 10 gated sargas):
# verify keeps the marker/pratīka assignment when the verse is the local
# containment argmax; move fires only on a clear margin over the current verse.
CONTENT_WINDOW = 3          # verses each side considered as anchor candidates
CONTENT_VERIFY_MIN = 0.15   # containment needed to count a chunk as verified
CONTENT_MOVE_MIN = 0.20     # best-candidate containment needed to move a chunk
CONTENT_MOVE_MARGIN = 0.08  # how much the best must beat the current verse by

# ।। 5.<sarga>.<verse> ।।  — verse group may be a merged range scraped as one token
MARKER = re.compile(r"।।\s*5\.(\d+)\.(\d+)\s*।।")

sys.path.insert(0, HERE)
from sa_align import canon_tokens, deva_to_iast, containment, backend as _align_backend  # noqa: E402

# pratīka = the verse catchword a gloss opens with; used to verify/repair which
# verse a commentary chunk actually belongs to (§11 alignment accuracy).
_PRATIKA_STOP = re.compile(r"[।॥\-—]|इति")


def leading_pratika_tokens(deva_text):
    head = _PRATIKA_STOP.split((deva_text or "").strip(), 1)[0]
    return canon_tokens(deva_to_iast(head))[:4]


def _iti_stems(p):
    """A pratīka is usually quoted fused with 'iti': rakṣitā+iti→'raksiteti',
    rāja+iti→'rajeti'. Yield the token plus its de-iti'd stems so it can still
    prefix-match the verse word (raksiteti→raksit ⊂ raksita)."""
    out = [p]
    if len(p) > 4 and p.endswith("ti"):
        for s in (p[:-2], p[:-3]):
            if len(s) >= 3:
                out.append(s)
    return out


def _pratika_hit(pt_tokens, verse_tokens):
    """Match a pratīka token to a verse word by prefix (sandhi truncates), after
    stripping a fused trailing 'iti'."""
    cands = [s for p in pt_tokens for s in _iti_stems(p)]
    vt = [w for w in verse_tokens if len(w) >= 3]
    for p in cands:
        if len(p) < 3:
            continue
        for w in vt:
            if w == p or w.startswith(p) or p.startswith(w):
                return True
    return False


def best_verse_for(pt, sarga, orig_v, cts):
    """Verse in this sarga whose tokens the pratīka matches, nearest to orig_v."""
    best = None
    for vid, toks in cts.items():
        parts = vid.split(".")
        if int(parts[1]) != sarga:
            continue
        if _pratika_hit(pt, toks):
            vv = int(parts[2]) if parts[2].isdigit() else None
            dist = abs(vv - orig_v) if (vv is not None and orig_v is not None) else 999
            if best is None or dist < best[0]:
                best = (dist, vid)
    return best[1] if best else None


def segment_file(path, sarga):
    """Return {verse_token: commentary_text} for one commentary file.

    Text preceding a marker glosses that marker's verse. Text before the first
    marker is the commentator's preamble (maṅgala), stored under '<sarga>.pre'.
    """
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    out = {}
    last = 0
    seen_first = False
    for m in MARKER.finditer(text):
        s, v = int(m.group(1)), m.group(2)
        chunk = text[last:m.start()].strip()
        last = m.end()
        if s != sarga:
            continue
        if not seen_first and chunk:
            out[f"{sarga}.pre"] = chunk
        seen_first = True
        if not chunk:
            continue
        out.setdefault(v, "")
        out[v] = (out[v] + "\n" + chunk).strip() if out[v] else chunk
    return out


def load_corpus(sargas):
    """Return {passage: {'sa': iast, 'ru': russian}} for the given sargas."""
    corpus = {}
    if not os.path.exists(JSONL):
        sys.stderr.write(f"WARN: sibling corpus not found: {JSONL}\n")
        return corpus
    want = {str(s) for s in sargas}
    with open(JSONL, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                d = json.loads(line)
            except json.JSONDecodeError:
                continue
            passage = d.get("passage", "")
            if "." not in passage:
                continue
            if passage.split(".", 1)[0] not in want:
                continue
            corpus.setdefault(passage, {})[d.get("seg", "")] = d.get("text", "")
    return corpus


def is_ambiguous(v):
    """A verse token like '810' (merged 8–10) — Sundara sargas have < ~120 vv."""
    return len(v) >= 3 and v.isdigit() and int(v) > 120


def _window_candidates(sarga, base, cts):
    """Verse ids of the same sarga within ±CONTENT_WINDOW of base (marker pos)."""
    out = []
    if base is None:
        return out
    for d in range(-CONTENT_WINDOW, CONTENT_WINDOW + 1):
        vid = f"5.{sarga}.{base + d}"
        if vid in cts:
            out.append(vid)
    return out


def main():
    args = sys.argv[1:]
    outdir = None
    if "--outdir" in args:
        i = args.index("--outdir")
        outdir = args[i + 1]
        args = args[:i] + args[i + 2:]
    sargas = [int(a) for a in args] if args else PILOT_SARGAS

    verses = {}   # verse_token -> {sarga, commentary:{c:txt}}
    preambles = {}
    for sarga in sargas:
        for c in COMMENTATORS:
            path = os.path.join(COMM_DIR, f"{c}_sarga_{sarga:02d}.txt")
            if not os.path.exists(path):
                sys.stderr.write(f"WARN: missing {path}\n")
                continue
            for tok, txt in segment_file(path, sarga).items():
                if tok.endswith(".pre"):
                    preambles.setdefault(tok, {})[c] = txt
                    continue
                key = (sarga, tok)
                verses.setdefault(key, {"sarga": sarga, "verse": tok, "commentary": {}})
                verses[key]["commentary"][c] = txt

    corpus = load_corpus(sargas)

    # corpus token-sets for every verse in these sargas (reassignment targets)
    cts = {}
    for passage, segs in corpus.items():
        s = int(passage.split(".", 1)[0])
        if s in sargas and segs.get("sa"):
            cts[f"5.{passage}"] = set(canon_tokens(segs["sa"]))

    # ---- reassignment (§11 item 1b): move each commentary chunk to the verse
    #      its leading pratīka actually matches (nearest in the sarga), fixing
    #      systematic marker offsets. Chunks that already match, or whose pratīka
    #      matches no verse, stay put. Collisions merge (concatenate). ----
    from collections import defaultdict as _dd
    newmap = _dd(dict)      # verse_id -> {commentator: [texts]}
    moves = kept = content_moves = 0
    for (sarga, tok), rec in verses.items():
        src_vid = f"5.{sarga}.{tok}"
        base = int(tok) if tok.isdigit() else None
        for c, text in rec["commentary"].items():
            pt = leading_pratika_tokens(text)
            tgt = src_vid
            vt = cts.get(src_vid)
            if pt and vt is not None and not _pratika_hit(pt, vt):
                bv = best_verse_for(pt, sarga, base, cts)
                if bv:
                    tgt, moves = bv, moves + 1
                else:
                    # pratīka matches no verse (pronoun/paraphrase) — fall back
                    # to the content anchor: move only on a clear local margin.
                    ck = set(canon_tokens(deva_to_iast(text)))
                    cur = containment(ck, vt)
                    best_vid, best_cont = None, 0.0
                    for cand in _window_candidates(sarga, base, cts):
                        cc = containment(ck, cts[cand])
                        if cc > best_cont:
                            best_vid, best_cont = cand, cc
                    if (best_vid and best_vid != src_vid
                            and best_cont >= CONTENT_MOVE_MIN
                            and best_cont - cur >= CONTENT_MOVE_MARGIN):
                        tgt, content_moves = best_vid, content_moves + 1
                    else:
                        kept += 1
            else:
                kept += 1
            newmap[tgt].setdefault(c, []).append(text)
    cmap = {vid: {c: "\n".join(t) for c, t in d.items()} for vid, d in newmap.items()}

    def _vk(vid):
        p = vid.split(".")
        return (int(p[1]), int(p[2]) if p[2].isdigit() else 0)

    bundles = []
    for vid in sorted(cmap, key=_vk):
        s = int(vid.split(".")[1])
        tok = vid.split(".")[2]
        cs = corpus.get(f"{s}.{tok}", {})
        bundles.append({
            "verse_id": vid,
            "sarga": s,
            "verse": tok,
            "ambiguous_marker": is_ambiguous(tok),
            "sanskrit_iast": cs.get("sa", ""),
            "leonov_ru": cs.get("ru", ""),
            "commentary": cmap[vid],
        })

    # ---- anchoring check: verify each chunk sits on the right verse (§11).
    #      Two independent signals (H268 WS-C2): the leading pratīka (quotation
    #      link) and the content anchor (containment argmax in a local window,
    #      covers pronominal pratīkas + paraphrasing ṭīkās). ----
    vtok = {b["verse_id"]: set(canon_tokens(b["sanskrit_iast"])) for b in bundles if b["sanskrit_iast"]}
    checkable = matched = verified = 0
    for b in bundles:
        vt = vtok.get(b["verse_id"])
        if not vt:
            continue
        chk = {}
        base = int(b["verse"]) if b["verse"].isdigit() else None
        for c, txt in b["commentary"].items():
            pt = leading_pratika_tokens(txt)
            if not pt:
                continue
            checkable += 1
            hit = _pratika_hit(pt, vt)
            if hit:
                matched += 1
            entry = {"pratika_iast": " ".join(pt), "matches_verse": hit}
            if not hit:
                # content anchor: is the assigned verse the local containment
                # argmax (and non-trivially quoted)?
                ck = set(canon_tokens(deva_to_iast(txt)))
                cur = containment(ck, vt)
                best_vid, best_cont = b["verse_id"], cur
                for cand in _window_candidates(b["sarga"], base, vtok):
                    cc = containment(ck, vtok[cand])
                    if cc > best_cont:
                        best_vid, best_cont = cand, cc
                entry["content_containment"] = round(cur, 3)
                if cur >= CONTENT_VERIFY_MIN and best_vid == b["verse_id"]:
                    entry["content_anchor"] = True
                elif base is not None:            # suggest the verse the pratīka fits
                    for d in (-1, 1, -2, 2, -3, 3):
                        nb = vtok.get(f"5.{b['sarga']}.{base + d}")
                        if nb and _pratika_hit(pt, nb):
                            entry["suggest_verse"] = f"5.{b['sarga']}.{base + d}"
                            break
            if hit or entry.get("content_anchor"):
                verified += 1
            chk[c] = entry
        if chk:
            b["pratika_check"] = chk
    precision = round(matched / checkable, 3) if checkable else None
    precision_verified = round(verified / checkable, 3) if checkable else None

    payload = {
        "_meta": {
            "generated_by": "scripts/extract_yellow_sargas.py",
            "purpose": "Phase-2 deterministic commentary segmentation (no LLM); input to Sonnet drafting",
            "sargas": sargas,
            "commentators": COMMENTATORS,
            "verse_count": len(bundles),
            "verses_all_three": sum(1 for b in bundles if len(b["commentary"]) == 3),
            "ambiguous_markers": sum(1 for b in bundles if b["ambiguous_marker"]),
            "corpus_aligned": sum(1 for b in bundles if b["sanskrit_iast"]),
            "align_backend": _align_backend(),
            "reassigned_moves": moves,
            "content_moves": content_moves,
            "pratika_checkable": checkable,
            "pratika_matched": matched,
            "alignment_precision": precision,
            "anchor_verified": verified,
            "alignment_precision_verified": precision_verified,
            "rights": "Gita Supersite, used by permission (CC BY 4.0); see data/valmiki_PERMISSION.md",
        },
        "preambles": preambles,
        "verses": bundles,
    }

    if outdir:
        # per-sarga split for wide drafting batches: each agent reads only its
        # sarga's bundles instead of one giant combined file.
        os.makedirs(outdir, exist_ok=True)
        for s in sargas:
            sb = [b for b in bundles if b["sarga"] == s]
            sp = {k: v for k, v in preambles.items() if k.startswith(f"{s}.")}
            sub = {"_meta": {**payload["_meta"], "sargas": [s],
                             "verse_count": len(sb),
                             "verses_all_three": sum(1 for b in sb if len(b["commentary"]) >= 3),
                             "ambiguous_markers": sum(1 for b in sb if b["ambiguous_marker"]),
                             "corpus_aligned": sum(1 for b in sb if b["sanskrit_iast"])},
                   "preambles": sp, "verses": sb}
            p = os.path.join(outdir, f"sarga_{s:02d}_segmented.json")
            with open(p, "w", encoding="utf-8") as fh:
                json.dump(sub, fh, ensure_ascii=False, indent=2)
        print(f"wrote {len(sargas)} per-sarga files to {outdir}")
    else:
        os.makedirs(os.path.dirname(OUT), exist_ok=True)
        with open(OUT, "w", encoding="utf-8") as fh:
            json.dump(payload, fh, ensure_ascii=False, indent=2)
        print(f"wrote {OUT}")

    m = payload["_meta"]
    print(f"sargas {sargas}: {m['verse_count']} verses "
          f"({m['verses_all_three']} with all 3 commentaries, "
          f"{m['corpus_aligned']} corpus-aligned, "
          f"{m['ambiguous_markers']} ambiguous markers)")
    print(f"reassigned {m['reassigned_moves']} chunks (+{m['content_moves']} content-anchor); "
          f"pratīka precision: {m['alignment_precision']} "
          f"({m['pratika_matched']}/{m['pratika_checkable']}); "
          f"verified (pratīka ∪ content): {m['alignment_precision_verified']} "
          f"({m['anchor_verified']}/{m['pratika_checkable']}) via {m['align_backend']}")


if __name__ == "__main__":
    main()
