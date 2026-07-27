#!/usr/bin/env python3
"""H1685 step 1 — build INDEPENDENT evidence for every queued Sundarakāṇḍa card.

The four sheets (batch2 38 · batch3 227 · lexical 611 · edition-footnotes 1013)
carry 1 889 cards waiting on a human. Ruling В2 (MG, 26-07-2026) says an agent
adjudicates them all with cited evidence and the human verifies the adjudicator
on a sample. This script produces the *evidence*, not the verdict: per card, a
set of deterministic checks that can each be re-run and pointed at.

The checks are deliberately INDEPENDENT of whatever produced the card — a check
that re-derives a claim from the same source that generated it proves nothing:

  absences   the generator kept a southern shloka when its Jaccard to the
             LOCALLY-aligned critical shloka was < 0.25. We instead search the
             WHOLE critical Sundarakāṇḍa (2 488 shlokas) for the best match.
             This is the "нечёткое глобальное назначение" that
             data/edition_comparison/README.md § Оговорки names as the next step
             and marks NOT DONE: a shloka that has a variant twin elsewhere in
             the critical edition is a разночтение, not an absence, and must not
             carry a «отсутствует в критическом издании» footnote.
  variants   the akṣara-level aligner (H776) proposed reading pairs. We check
             each side actually OCCURS in its own edition's verse, and that the
             two sides really differ once orthography is folded away.
  notes      the drafter named commentators and a lemma. We check the named
             commentator actually has text at that verse (the batch-3 judge
             caught a fabricated Tilaka attribution this way at 5.1.3), that the
             lemma really stands in the verse, and how much of the note is
             already given by the подстрочник / tier-1 / Phase-1 layers.
  lexical    additionally: every `dic_mw:<slp1>` the note cites is looked up in
             the MW headword list, and a quoted English gloss is checked against
             that entry's text.

Canonicalization is the org toolkit via scripts/sa_align.py (SHARED_CODE §1-2 —
sanskrit_util.nfold), never a local re-implementation.

Deterministic and stdlib-only apart from sa_align. Writes
data/analysis/h1685_adjudication/evidence.json.

Usage: python scripts/h1685_evidence.py [--limit-fn N]
"""
import sys
import os
import re
import json
import time
import argparse
import difflib
from collections import defaultdict, Counter

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
DATA = os.path.join(REPO, "data")
OUTDIR = os.path.join(DATA, "analysis", "h1685_adjudication")
OUT = os.path.join(OUTDIR, "evidence.json")

sys.path.insert(0, HERE)
from sa_align import canon, backend as align_backend  # noqa: E402
from compare_editions import load_critical, load_southern  # noqa: E402

try:
    import sanskrit_util as _su
    def from_slp1(s):
        try:
            return _su.from_slp1(s or "")
        except Exception:
            return s or ""
except Exception:                                    # pragma: no cover
    def from_slp1(s):
        return s or ""

SM = None
for _up in range(1, 7):
    _c = os.path.join(REPO, *([".."] * _up), "SamudraManthanam")
    if os.path.isdir(_c):
        SM = os.path.abspath(_c)
        break
MW = os.path.join(SM, "web", "corpus_builder", "jsonl", "dic_mw.jsonl") if SM else ""

# Absence thresholds are NOT picked here — they are calibrated in
# h1685_calibrate.py against the concordance's own labelled pairs and written
# into calibration.json, which the adjudicator reads. These two are the
# generator's inherited vocabulary, kept only so the evidence can be compared
# with what the sheet already claims.
SIM_VARIANT = 0.60
SIM_ABSENT = 0.25
EMPTY_READING = {"∅", "", "-", "—"}      # the apparatus' "omitted here" marker


def load(p):
    with open(p, encoding="utf-8") as fh:
        return json.load(fh)


def sheet_payload(p):
    txt = open(p, encoding="utf-8").read()
    m = re.search(r"const\s+D\s*=\s*", txt)
    return json.JSONDecoder().raw_decode(txt, m.end())[0]


# ---------------------------------------------------------------- text utils
RU_STOP = set("и в во не что он на я с со как а то все она так его но да ты к у "
              "же вы за бы по только ее мне было вот от меня еще нет о из ему "
              "теперь когда даже ну вдруг ли если уже или ни быть был него до "
              "вас нибудь опять уж вам ведь там потом себя ничего ей может они "
              "тут где есть надо ней для мы тебя их чем была сам чтоб без будто "
              "чего раз тоже себе под будет ж тогда кто этот того потому этого "
              "какой совсем ним здесь этом один почти мой тем чтобы нее сейчас "
              "были куда зачем всех никогда можно при наконец два об другой хоть "
              "после над больше тот через эти нас про всего них какая много "
              "разве три эту моя впрочем хорошо свою этой перед иногда лучше "
              "чуть том нельзя такой им более всегда конечно всю между".split())


def ru_tokens(text):
    return [t for t in re.findall(r"[а-яёa-zāīūṛṝḷḹṅñṭḍṇśṣḥṃ]+", (text or "").lower())
            if len(t) > 3 and t not in RU_STOP]


def containment(a_tokens, b_tokens):
    """Fraction of A's distinct tokens that also occur in B."""
    a, b = set(a_tokens), set(b_tokens)
    if not a:
        return 0.0
    return round(len(a & b) / len(a), 3)


def lemma_alternatives(lemma):
    """The verse-word candidates hiding in a `lemma_iast` field.

    That field is NOT always a single word of the verse. Drafters used it for
    variant pairs ('durjayā / nirjitā'), for exegetical categories with no verse
    exponent at all ('kavivākya / hanumadabhiprāyānuvāda', 'punarukti (dṛṣṭvā …
    dadarśa)', 'prakṣipta-pāṭha'), and for Russian asides ('hrasvatā, не
    veśāntara'). Scoring those as one string made 57 of batch-3's 210 `keep`
    notes look unanchored, which is a defect of the check, not of the notes.
    So: drop parentheticals and Cyrillic, split on / and comma, and let ANY
    alternative anchor the note.
    """
    s = re.sub(r"\([^)]*\)", " ", lemma or "")
    s = re.sub(r"[А-Яа-яЁё]+", " ", s)
    alts = [a.strip() for a in re.split(r"[/,;]| или ", s) if a.strip()]
    return alts or ([lemma] if lemma else [])


def _match_in(alt, cv, cvt):
    parts = [p for p in canon(alt).split() if p]
    if not parts:
        return None, ""
    if all(p in cvt for p in parts):
        return "exact", "whole-token match"
    hits, misses = [], []
    for p in parts:
        probe = p[:-1] if len(p) > 5 else p          # tolerate one final letter
        if len(probe) >= 4 and probe in cv:
            hits.append(p)
        elif len(p) >= 4 and p[:4] in cv:
            hits.append(p)
        else:
            misses.append(p)
    if not misses:
        return "stem", "substring match: " + ",".join(hits)
    return None, "not found: " + ",".join(misses)


def lemma_anchor(lemma, verse_iast, neighbour_texts=(), commentary_text=""):
    """Where does this lemma actually stand?

    exact / stem   — in THIS verse
    neighbour      — in an adjacent verse: the flag_anchor signal (the note may
                     be filed one śloka off)
    commentary_only— only in the ṭīkā at this verse: normal for an exegetical
                     term the commentator introduces, not evidence of an error
    absent         — nowhere; the note has no textual foothold
    """
    if not verse_iast:
        return "no_verse", ""
    cv, cvt = canon(verse_iast), set(canon(verse_iast).split())
    alts = lemma_alternatives(lemma)
    details = []
    for a in alts:
        state, det = _match_in(a, cv, cvt)
        if state:
            return state, f"{a!r}: {det}"
        details.append(f"{a!r}: {det}")
    for nid, nt in neighbour_texts:
        ncv, ncvt = canon(nt), set(canon(nt).split())
        for a in alts:
            state, _ = _match_in(a, ncv, ncvt)
            if state:
                return "neighbour", f"{a!r} stands in {nid}, not in this verse"
    if commentary_text:
        cc = canon(commentary_text)
        for a in alts:
            ca = canon(a)
            if len(ca) >= 4 and ca in cc:
                return "commentary_only", f"{a!r} occurs in the ṭīkā, not the verse"
    return "absent", "; ".join(details[:3])


# ------------------------------------------------------- global absence search
def build_global_matcher(crit):
    """Token-set prefilter over the whole critical book, then difflib on top-K."""
    crit_canon = [canon(t) for _, _, t in crit]
    crit_ids = [f"5.{s}.{v}" for s, v, _ in crit]
    crit_tok = [set(c.split()) for c in crit_canon]
    postings = defaultdict(list)
    for i, toks in enumerate(crit_tok):
        for t in toks:
            if len(t) > 3:
                postings[t].append(i)

    def best_match(text, topk=40):
        """Best critical counterpart ANYWHERE in the book.

        Scored by token Jaccard — the same family of measure the generator used
        (`best_crit_jaccard`), so the numbers are commensurable with the card's
        own stated basis, but computed globally instead of at the LCS-aligned
        position. Character difflib is reported alongside because it is what
        concordance.json's `similarity` uses, but Jaccard is the discriminator:
        two unrelated Sanskrit ślokas share enough letters to sit near 0.5 on
        difflib, which is why the first cut of this script found 169/174 cards
        "borderline" and nothing separable.
        """
        q = canon(text)
        qt = {t for t in q.split() if len(t) > 3}
        if not qt:
            return None, 0.0, 0.0, []
        score = Counter()
        for t in qt:
            for i in postings.get(t, ()):
                score[i] += 1
        cands = [i for i, _ in score.most_common(topk)]
        if not cands:                                # no lexical overlap at all
            return None, 0.0, 0.0, []
        ranked = []
        for i in cands:
            ct = crit_tok[i]
            inter = len(qt & ct)
            union = len(qt | ct) or 1
            jac = inter / union
            ranked.append((jac, i))
        ranked.sort(reverse=True)
        best_j, best_i = ranked[0]
        dl = difflib.SequenceMatcher(None, q, crit_canon[best_i]).ratio()
        top3 = [{"crit_id": crit_ids[i], "jaccard": round(j, 3)} for j, i in ranked[:3]]
        return crit_ids[best_i], round(best_j, 3), round(dl, 3), top3

    return best_match


# ------------------------------------------------------------------ MW lookup
def _skeleton(s):
    """Lossy consonant skeleton — de-aspirate, collapse doubles.

    The notes cite headwords in a HYBRID notation (partly strict SLP1 `fddhi`,
    partly IAST-ish `skandha`, partly mis-transliterated `paTTiSa` for paṭṭiśa),
    while MW's top-level `slp1` is strict SLP1 (ai→E, ṇ→R). Matching those
    exactly produced 131 spurious "headword missing" hits on words as ordinary
    as taila and maṇi. This fold deliberately throws away aspiration, gemination
    and the retroflex/dental/palatal distinctions that nfold already flattens,
    so a citation only fails when the WORD is wrong, not its spelling.
    """
    s = re.sub(r"(?<=[bcdgjkptv])h", "", s or "")
    s = re.sub(r"(.)\1+", r"\1", s)
    return s


def hw_keys(raw):
    """Every key a headword could be found/filed under."""
    out = set()
    for form in {raw or "", from_slp1(raw or "")}:
        c = canon(form)
        if c:
            out.add(c)
            out.add(_skeleton(c))
    return {k for k in out if k}


def mw_index(wanted):
    """One streaming pass; keep any entry whose keys meet a cited headword."""
    idx = defaultdict(str)
    if not (MW and os.path.exists(MW)) or not wanted:
        return idx
    want = set()
    for w in wanted:
        want |= hw_keys(w)
    with open(MW, encoding="utf-8") as fh:
        for line in fh:
            if not line.strip():
                continue
            try:
                d = json.loads(line)
            except Exception:
                continue
            forms = d.get("forms") or {}
            keys = set()
            for cand in (d.get("slp1"), forms.get("slp1")):
                keys |= hw_keys(cand)
            for cand in (forms.get("iast"),):
                if cand:
                    c = canon(cand)
                    keys |= {c, _skeleton(c)}
            hit = keys & want
            if hit:
                text = d.get("text", "") or d.get("html", "")
                for k in hit:
                    if len(idx[k]) < 4000:
                        idx[k] += " " + text
    return idx


def mw_lookup(idx, raw):
    for k in hw_keys(raw):
        if idx.get(k):
            return idx[k]
    return ""


def cited_mw_headwords(source):
    return re.findall(r"dic_mw:([A-Za-z~]+)", source or "")


def quoted_glosses(note_ru):
    """English glosses the note puts in quotes — the checkable dictionary claim."""
    out = []
    for m in re.findall(r"[«\"']([a-zA-Z][a-zA-Z ,;/()\-']{3,60})[»\"']", note_ru or ""):
        s = m.strip().strip(",;")
        if len(s) > 3 and re.search(r"[a-zA-Z]{3}", s):
            out.append(s)
    return out[:4]


# ==============================================================================
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit-fn", type=int, default=0,
                    help="cap the footnote cards (smoke runs only)")
    args = ap.parse_args()
    t0 = time.time()
    os.makedirs(OUTDIR, exist_ok=True)

    print(f"align backend: {align_backend()}")
    crit = load_critical()
    south = load_southern()
    south_by_id = {f"5.{s}.{v}": t for s, v, t in south}
    crit_by_id = {f"5.{s}.{v}": t for s, v, t in crit}
    print(f"critical shlokas: {len(crit)} | southern shlokas: {len(south)}")
    best_match = build_global_matcher(crit)

    book = load(os.path.join(DATA, "sundara_commentary_to_add.json"))
    book_notes = [n for n in book if "_meta" not in n]
    book_keys = Counter((n.get("shloka"), n.get("lemma_iast")) for n in book_notes)

    leonov = defaultdict(list)
    for n in load(os.path.join(DATA, "leonov_own_notes.json"))["notes"]:
        leonov[n["verse_id"]].append(n.get("raw_text", ""))

    def neighbours_of(vid, span=2):
        """Adjacent southern ślokas as (id, text) — a mis-filed note's real home.

        Returning the id, not just the text, is what makes a `neighbour` verdict
        actionable: the reviewer is told WHICH śloka to re-anchor to.
        """
        out = []
        m = re.match(r"5\.(\d+)\.(\d+)", vid or "")
        if not m:
            return out
        ch, vn = int(m.group(1)), int(m.group(2))
        for d in range(-span, span + 1):
            if d == 0:
                continue
            nid = f"5.{ch}.{vn + d}"
            t = south_by_id.get(nid)
            if t:
                out.append((nid, t))
        return out

    cards = []

    # ---------------------------------------------------------------- batch2/3
    for batch, sheet_rel in (
            ("batch2", os.path.join("analysis", "phase2_batch2",
                                    "commentarystrategies-sundarakanda-commentaries_batch2_review.html")),
            ("batch3", os.path.join("analysis", "phase2_batch3",
                                    "commentarystrategies-sundarakanda-commentaries_batch3_review.html"))):
        payload = sheet_payload(os.path.join(DATA, sheet_rel))
        for n in payload["notes"]:
            vid = n["verse_id"]
            comm = n.get("commentary_at_verse") or {}
            named = list(n.get("source_commentary") or [])
            attested = [c for c in named if (comm.get(c) or "").strip()]
            missing = [c for c in named if c not in attested]
            neigh = neighbours_of(vid)
            anchor, anchor_detail = lemma_anchor(
                n.get("lemma_iast", ""), n.get("sanskrit_iast", ""),
                neighbour_texts=neigh,
                commentary_text=" ".join(v for v in comm.values() if v))
            nt = ru_tokens(n.get("note_ru", ""))
            tier1_here = [t.get("note", "") if isinstance(t, dict) else str(t)
                          for t in (n.get("leonov_here") or [])] + leonov.get(vid, [])
            phase1_here = [p.get("note_ru", "") if isinstance(p, dict) else str(p)
                           for p in (n.get("phase1_here") or [])]
            cards.append({
                "card_id": f"{batch}|{vid}|{n.get('lemma_iast','')}",
                "queue": batch,
                "key": vid,
                "lemma": n.get("lemma_iast", ""),
                "verse_id": vid,
                "note_ru": n.get("note_ru", ""),
                "judge": n.get("judge"),
                "evidence": {
                    "commentators_named": named,
                    "commentators_attested": attested,
                    "commentators_missing": missing,
                    "commentator_attribution_ok": not missing,
                    "anchor": anchor,
                    "anchor_detail": anchor_detail,
                    # both directions: how much of the NOTE is already in the
                    # crib (note_in_X) and how much of the crib the note simply
                    # echoes (X_in_note). Restatement shows up in the first.
                    "note_in_podstrochnik": containment(nt, ru_tokens(n.get("leonov_ru", ""))),
                    "podstrochnik_in_note": containment(ru_tokens(n.get("leonov_ru", "")), nt),
                    "note_in_tier1": containment(nt, ru_tokens(" ".join(tier1_here))),
                    "tier1_in_note": containment(ru_tokens(" ".join(tier1_here)), nt),
                    "note_in_phase1": containment(nt, ru_tokens(" ".join(phase1_here))),
                    "tier1_notes_here": len(tier1_here),
                    "duplicate_in_book": book_keys.get(
                        (f"V.{vid[2:]}" if vid.startswith("5.") else vid,
                         n.get("lemma_iast")), 0) > 0,
                    "note_chars": len(n.get("note_ru", "")),
                },
            })
        print(f"{batch}: {len(payload['notes'])} cards")

    # ---------------------------------------------------------------- lexical
    lex_sheet = sheet_payload(os.path.join(
        DATA, "analysis", "lexical_judge",
        "commentarystrategies-sundarakanda-lexical_all68_review.html"))
    lex_items = [(i, False) for i in lex_sheet["notes"]] + \
                [(i, True) for i in lex_sheet["parked"]]
    wanted_hw = set()
    for it, _ in lex_items:
        wanted_hw.update(cited_mw_headwords(it.get("source", "")))
    print(f"lexical: {len(lex_items)} cards, {len(wanted_hw)} distinct MW headwords cited")
    mw = mw_index(wanted_hw)
    _res = sum(1 for h in wanted_hw if mw_lookup(mw, h))
    print(f"  MW headwords resolved: {_res}/{len(wanted_hw)}")

    for it, parked in lex_items:
        shloka = it.get("shloka", "")
        vid = re.sub(r"^V\.", "5.", shloka)
        vid_plain = re.sub(r"[ab]$", "", vid)
        verse = it.get("verse_iast") or south_by_id.get(vid_plain, "")
        anchor, anchor_detail = lemma_anchor(it.get("lemma", ""), verse,
                                             neighbour_texts=neighbours_of(vid_plain))
        hws = cited_mw_headwords(it.get("source", ""))
        hw_found = [h for h in hws if mw_lookup(mw, h)]
        hw_missing = [h for h in hws if not mw_lookup(mw, h)]
        glosses = quoted_glosses(it.get("note_ru", ""))
        entry_text = " ".join(mw_lookup(mw, h) for h in hw_found).lower()
        gloss_hits = [g for g in glosses if g.lower()[:24] in entry_text]
        nt = ru_tokens(it.get("note_ru", ""))
        tier1_here = [t.get("note", "") if isinstance(t, dict) else str(t)
                      for t in (it.get("tier1") or [])] + leonov.get(vid_plain[2:], [])
        cards.append({
            "card_id": f"lexical|{it.get('key')}",
            "queue": "lexical",
            "key": it.get("key"),
            "lemma": it.get("lemma", ""),
            "verse_id": vid_plain,
            "note_ru": it.get("note_ru", ""),
            "judge": it.get("judge"),
            "evidence": {
                "parked_ws3b": parked,
                "reanchored": bool(it.get("reanchored")),
                "anchor": anchor,
                "anchor_detail": anchor_detail,
                "mw_headwords_cited": hws,
                "mw_headwords_found": hw_found,
                "mw_headwords_missing": hw_missing,
                "mw_source_ok": (not hws) or not hw_missing,
                "quoted_glosses": glosses,
                "quoted_glosses_confirmed": gloss_hits,
                "gloss_check": ("n/a" if not glosses else
                                "confirmed" if gloss_hits else "unconfirmed"),
                "note_in_podstrochnik": containment(nt, ru_tokens(it.get("leonov_ru", ""))),
                "podstrochnik_in_note": containment(ru_tokens(it.get("leonov_ru", "")), nt),
                "note_in_tier1": containment(nt, ru_tokens(" ".join(tier1_here))),
                "tier1_in_note": containment(ru_tokens(" ".join(tier1_here)), nt),
                "tier1_notes_here": len(tier1_here),
                "duplicate_in_book": book_keys.get((shloka, it.get("lemma")), 0) > 1,
                "note_chars": len(it.get("note_ru", "")),
            },
        })

    # -------------------------------------------------------------- footnotes
    fn_sheet = sheet_payload(os.path.join(
        DATA, "edition_footnotes",
        "commentarystrategies-edition-footnotes_v1_review.html"))
    items = fn_sheet["items"]
    if args.limit_fn:
        items = items[:args.limit_fn]
    print(f"footnotes: {len(items)} cards — global critical re-search "
          f"(this is the slow part)")
    done = 0
    for it in items:
        kind = it.get("kind")
        anchor_id = it.get("anchor")
        ev = {"kind": kind,
              "leonov_note_here": bool(it.get("leonov_note_here")),
              "leonov_edition_note_here": bool(it.get("leonov_edition_note_here")),
              "generator_confidence": it.get("confidence")}
        if kind in ("verse_range", "single", "sarga_absence"):
            per_verse = []
            for vv in (it.get("verses_iast") or []):
                sid = vv.get("verse_id")
                cid, jac, dl, top3 = best_match(vv.get("iast", ""))
                per_verse.append({"southern_id": sid, "best_crit_id": cid,
                                  "best_jaccard": jac, "best_difflib": dl,
                                  "top3": top3})
            jacs = [p["best_jaccard"] for p in per_verse] or [0.0]
            ev.update({
                "verses_checked": len(per_verse),
                "per_verse": per_verse,
                "max_global_jaccard": max(jacs),
                "min_global_jaccard": min(jacs),
                "mean_global_jaccard": round(sum(jacs) / len(jacs), 3) if jacs else 0.0,
            })
        elif kind == "variant_reading":
            cv = canon(crit_by_id.get(anchor_id, ""))
            sv = canon(south_by_id.get(it.get("southern_id", ""), ""))
            checks = []
            for r in (it.get("readings") or []):
                raw_c, raw_s = (r.get("crit") or "").strip(), (r.get("southern") or "").strip()
                # '∅' is the apparatus' OMISSION marker, not a string to find:
                # "X ] ∅" means the southern edition drops X. Treating it as a
                # missing string flagged 231 sound cards on the first pass.
                c_empty, s_empty = raw_c in EMPTY_READING, raw_s in EMPTY_READING
                c_r, s_r = canon(raw_c), canon(raw_s)
                c_ok = True if c_empty else (bool(c_r) and c_r in cv)
                s_ok = True if s_empty else (bool(s_r) and s_r in sv)
                checks.append({
                    "crit": raw_c, "southern": raw_s,
                    "omission": c_empty or s_empty,
                    "crit_located": c_ok, "southern_located": s_ok,
                    "distinct_after_fold": c_r != s_r,
                })
            ev.update({
                "verse_texts_available": bool(cv) and bool(sv),
                "readings_checked": len(checks),
                "reading_checks": checks,
                "n_omission_markers": sum(1 for c in checks if c["omission"]),
                "all_readings_located": (all(c["crit_located"] and c["southern_located"]
                                             for c in checks) if checks else False),
                "n_readings_unlocated": sum(
                    1 for c in checks if not (c["crit_located"] and c["southern_located"])),
                "n_readings_distinct": sum(1 for c in checks if c["distinct_after_fold"]),
                "difflib_similarity": it.get("difflib_similarity"),
            })
        cards.append({
            "card_id": f"footnotes|{kind}|{anchor_id}|{it.get('range')}",
            "queue": "footnotes",
            "key": f"{kind}|{anchor_id}",
            "lemma": "",
            "verse_id": anchor_id,
            "note_ru": it.get("note_ru", ""),
            "judge": None,
            "evidence": ev,
        })
        done += 1
        if done % 200 == 0:
            print(f"  …{done}/{len(items)} ({time.time()-t0:.0f}s)")

    doc = {
        "_meta": {
            "handoff": "H1685",
            "generated_by": "scripts/h1685_evidence.py",
            "align_backend": align_backend(),
            "critical_shlokas": len(crit),
            "southern_shlokas": len(south),
            "thresholds": {"sim_variant": SIM_VARIANT, "sim_absent": SIM_ABSENT},
            "cards": len(cards),
            "by_queue": dict(Counter(c["queue"] for c in cards)),
            "runtime_s": round(time.time() - t0, 1),
            "note": ("evidence only — no verdicts here; see h1685_adjudicate.py. "
                     "Absence checks are a GLOBAL re-search of the whole critical "
                     "book (edition_comparison/README.md § Оговорки names this as "
                     "the un-done next step), not a re-read of the generator's "
                     "local alignment."),
        },
        "cards": cards,
    }
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, ensure_ascii=False, indent=1)
    print(f"\nwrote {OUT}")
    print(f"cards: {doc['_meta']['by_queue']} total {len(cards)} "
          f"in {doc['_meta']['runtime_s']}s")


if __name__ == "__main__":
    main()
