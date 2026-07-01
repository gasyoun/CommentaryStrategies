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
JSONL = os.path.join(
    REPO, "..", "SamudraManthanam", "web", "corpus_builder", "jsonl",
    "05_ramayana-sundarakanda.jsonl",
)
OUT = os.path.join(REPO, "data", "analysis", "sundara_commentary_segmented.json")

COMMENTATORS = ["tilaka", "bhusana", "siromani"]
PILOT_SARGAS = [35, 36, 37]

# ।। 5.<sarga>.<verse> ।।  — verse group may be a merged range scraped as one token
MARKER = re.compile(r"।।\s*5\.(\d+)\.(\d+)\s*।।")


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


def main():
    args = sys.argv[1:]
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

    bundles = []
    for (sarga, tok), rec in sorted(verses.items(), key=lambda kv: (kv[0][0], int(kv[0][1]) if kv[0][1].isdigit() else 0)):
        passage = f"{sarga}.{tok}"
        cs = corpus.get(passage, {})
        bundles.append({
            "verse_id": f"5.{sarga}.{tok}",
            "sarga": sarga,
            "verse": tok,
            "ambiguous_marker": is_ambiguous(tok),
            "sanskrit_iast": cs.get("sa", ""),
            "leonov_ru": cs.get("ru", ""),
            "commentary": rec["commentary"],
        })

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
            "rights": "Gita Supersite, used by permission (CC BY 4.0); see data/valmiki_PERMISSION.md",
        },
        "preambles": preambles,
        "verses": bundles,
    }

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=2)

    m = payload["_meta"]
    print(f"sargas {sargas}: {m['verse_count']} verses "
          f"({m['verses_all_three']} with all 3 commentaries, "
          f"{m['corpus_aligned']} corpus-aligned, "
          f"{m['ambiguous_markers']} ambiguous markers)")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
