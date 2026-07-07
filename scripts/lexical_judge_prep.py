#!/usr/bin/env python3
"""Prepare judge-input chunks for the lexical-layer judge pass (H276 WS-2).

The judged set is the book aggregate's `subtype == "lexical"` notes (611 as of
v1.7.0) — the print-bound lexical/etymological gloss layer drafted 2026-06-27.
For each note the chunk bundles everything a judge needs offline:

  - the note itself (verbatim);
  - the verse (IAST + Leonov's Russian подстрочник) from the SamudraManthanam
    corpus (sibling repo, hardcoded path like the other sundara_* scripts);
  - the non-triviality baseline: Leonov/Kostina's own tier-1 notes on that
    verse (data/leonov_own_notes.json) + every OTHER book-aggregate note on
    the same verse (Phase-1 / cross_text / commentator layers);
  - `anchor_precheck`: a deterministic stem-match of the lemma against the
    verse IAST (exact / stem / absent) — the judges' anchoring axis starts
    from this signal instead of re-deriving it.

Output: data/analysis/lexical_judge/chunk_{NN}_input.json (12 chunks balanced
by note count, whole chapters only) + an accounting line per chunk.

Usage: python scripts/lexical_judge_prep.py
"""
import sys
import os
import re
import json
import unicodedata
from collections import defaultdict

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
DATA = os.path.join(REPO, "data")
OUT = os.path.join(DATA, "analysis", "lexical_judge")
CORPUS = os.path.join(os.path.dirname(os.path.dirname(REPO)), "GitHub",
                      "SamudraManthanam", "web", "corpus_builder", "jsonl",
                      "05_ramayana-sundarakanda.jsonl")
if not os.path.exists(CORPUS):  # normal layout: REPO already sits inside GitHub/
    CORPUS = os.path.join(os.path.dirname(REPO), "SamudraManthanam", "web",
                          "corpus_builder", "jsonl",
                          "05_ramayana-sundarakanda.jsonl")

N_CHUNKS = 12


def load(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def norm_iast(s):
    """Lowercase, NFC, strip punctuation/dandas/digits — keep diacritics."""
    s = unicodedata.normalize("NFC", s).lower()
    s = re.sub(r"[०-९0-9॥।'\"“”‘’,;:!?()\[\]—–-]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def lemma_stems(lemma):
    """Candidate stems for anchoring: full form + trimmed final endings."""
    lemma = norm_iast(lemma)
    # a lemma field may carry several words / a compound path like 'sundara-'
    parts = re.split(r"[\s/+·]+", lemma.replace("-", " "))
    stems = set()
    for p in parts:
        p = p.strip(".–- ")
        if len(p) < 3:
            continue
        stems.add(p)
        # strip common final vowels/visarga/anusvara so inflected verse forms match
        stems.add(re.sub(r"(aḥ|am|au|ā|a|i|ī|u|ū|ḥ|ṃ|e|o)$", "", p))
    return {s for s in stems if len(s) >= 3}


def anchor_precheck(lemma, verse_iast):
    if not verse_iast:
        return "no_verse"
    text = norm_iast(verse_iast)
    stems = lemma_stems(lemma or "")
    if not stems:
        return "no_lemma"
    for s in sorted(stems, key=len, reverse=True):
        if s in text:
            return "exact" if s == norm_iast(lemma) else "stem"
    return "absent"


def main():
    os.makedirs(OUT, exist_ok=True)

    # ---- corpus verses ----
    verses = defaultdict(dict)  # "ch.v" -> {"sa":…, "ru":…}
    with open(CORPUS, encoding="utf-8") as fh:
        for line in fh:
            r = json.loads(line)
            if r.get("seg") in ("sa", "ru") and not r.get("deleted"):
                verses[r["passage"]][r["seg"]] = r["text"]

    # ---- tier-1 baseline ----
    leonov = load(os.path.join(DATA, "leonov_own_notes.json"))
    l_notes = leonov["notes"] if isinstance(leonov, dict) else leonov
    tier1 = defaultdict(list)
    for n in l_notes:
        if not isinstance(n, dict):
            continue
        key = n.get("verse_id") or n.get("shloka") or ""
        key = re.sub(r"^V\.", "", str(key))
        tier1[key].append({"author": n.get("author"), "note": n.get("note_ru")
                           or n.get("text") or n.get("note")})

    # ---- book aggregate ----
    book = load(os.path.join(DATA, "sundara_commentary_to_add.json"))
    notes = [n for n in book if "_meta" not in n]
    lexical = [n for n in notes if n.get("subtype") == "lexical"]
    other_by_verse = defaultdict(list)
    for n in notes:
        if n.get("subtype") == "lexical":
            continue
        key = re.sub(r"^V\.", "", str(n.get("shloka", "")))
        other_by_verse[key].append({"subtype": n.get("subtype", "base"),
                                    "lemma_iast": n.get("lemma_iast"),
                                    "note_ru": n.get("note_ru")})

    # ---- bundle per chapter ----
    per_ch = defaultdict(list)
    for n in lexical:
        m = re.match(r"^V\.(\d+)\.(\d+[ab]?)", str(n.get("shloka", "")))
        if not m:
            sys.exit(f"ERROR: unparseable shloka {n.get('shloka')}")
        ch, v = m.group(1), m.group(2)
        key = f"{ch}.{re.sub(r'[ab]$', '', v)}"
        vv = verses.get(key, {})
        per_ch[int(ch)].append({
            "note": n,
            "verse_id": key,
            "verse_iast": vv.get("sa"),
            "leonov_ru": vv.get("ru"),
            "anchor_precheck": anchor_precheck(n.get("lemma_iast"), vv.get("sa")),
            "tier1_notes": tier1.get(key, []),
            "other_layer_notes": other_by_verse.get(key, []),
        })

    total = sum(len(v) for v in per_ch.values())
    pre = defaultdict(int)
    for items in per_ch.values():
        for it in items:
            pre[it["anchor_precheck"]] += 1
    print(f"lexical notes bundled: {total} across {len(per_ch)} chapters; "
          f"anchor_precheck: {dict(pre)}")

    # ---- balanced chunks of whole chapters ----
    target = total / N_CHUNKS
    chunks, cur, cur_n = [], [], 0
    for ch in sorted(per_ch):
        cur.append(ch)
        cur_n += len(per_ch[ch])
        if cur_n >= target and len(chunks) < N_CHUNKS - 1:
            chunks.append(cur)
            cur, cur_n = [], 0
    if cur:
        chunks.append(cur)

    for i, chs in enumerate(chunks, 1):
        items = [it for c in chs for it in per_ch[c]]
        doc = {"_meta": {
                   "chunk": i, "chapters": chs, "notes_count": len(items),
                   "generated_by": "scripts/lexical_judge_prep.py",
                   "date": "2026-07-07",
                   "task": "H276 WS-2 lexical judge pass (rubric: PHASE2_METHOD §3.4, "
                           "contrastive_value -> lexical_value)"},
               "items": items}
        path = os.path.join(OUT, f"chunk_{i:02d}_input.json")
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(doc, fh, ensure_ascii=False, indent=2)
        print(f"chunk {i:02d}: chapters {chs[0]}–{chs[-1]} "
              f"({len(chs)} ch, {len(items)} notes) -> {os.path.basename(path)}")


if __name__ == "__main__":
    main()
