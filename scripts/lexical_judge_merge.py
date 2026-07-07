#!/usr/bin/env python3
"""Merge lexical-judge verdicts (H276 WS-2) back into the canonical data files.

Reads data/analysis/lexical_judge/chunk_*_input.json (judged in place by the
Sonnet 5 judge agents) and grafts each note's `judge` object into:

  1. the book aggregate data/sundara_commentary_to_add.json (all judged notes
     originate there — every one must match);
  2. the per-chapter lexical file data/lexical/ch{N}.json (matched by
     (shloka, lemma_iast); ch-file entries that never made the book aggregate
     are left untouched and counted).

Also writes data/analysis/lexical_judge/summary.json (verdict counts overall +
per chapter) for the review-sheet builder, and stamps each touched ch-file's
_meta with the judge-pass provenance. Deterministic, stdlib-only, idempotent.

Usage: python scripts/lexical_judge_merge.py
"""
import sys
import os
import glob
import json
from collections import Counter, defaultdict

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
DATA = os.path.join(REPO, "data")
LEX = os.path.join(DATA, "lexical")
JDIR = os.path.join(DATA, "analysis", "lexical_judge")
BOOK = os.path.join(DATA, "sundara_commentary_to_add.json")


def load(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def dump(path, obj):
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(obj, fh, ensure_ascii=False, indent=2)


def main():
    judged = {}  # (shloka, lemma) -> judge object
    for path in sorted(glob.glob(os.path.join(JDIR, "chunk_*_input.json"))):
        doc = load(path)
        if not doc["_meta"].get("judged"):
            sys.exit(f"ERROR: {os.path.basename(path)} not judged yet")
        for it in doc["items"]:
            n = it["note"]
            if "judge" not in n:
                sys.exit(f"ERROR: {n.get('shloka')} {n.get('lemma_iast')} "
                         f"in {os.path.basename(path)} has no judge object")
            key = (n["shloka"], n.get("lemma_iast"))
            if key in judged:
                sys.exit(f"ERROR: duplicate judged key {key}")
            judged[key] = n["judge"]
    print(f"judged notes collected: {len(judged)}")

    # ---- book aggregate ----
    book = load(BOOK)
    matched = 0
    for n in book:
        if "_meta" in n or n.get("subtype") != "lexical":
            continue
        key = (n["shloka"], n.get("lemma_iast"))
        if key not in judged:
            sys.exit(f"ERROR: book lexical note {key} was never judged")
        n["judge"] = judged[key]
        matched += 1
    if matched != len(judged):
        sys.exit(f"ERROR: {len(judged)} judged vs {matched} matched in book")
    verdicts = Counter(j["verdict"] for j in judged.values())
    bm = book[0]["_meta"]
    bm["lexical_judge"] = {"date": "2026-07-07", "step": "lexical_judge_h276",
                           "judged_by": "claude-sonnet-5 (3-wide, drafter≠judge)",
                           "notes_judged": matched,
                           "verdicts": dict(verdicts)}
    dump(BOOK, book)
    print(f"book aggregate: {matched} judge objects grafted; verdicts {dict(verdicts)}")

    # ---- per-chapter lexical files ----
    per_ch = defaultdict(dict)
    for (shloka, lemma), j in judged.items():
        ch = int(shloka.split(".")[1])
        per_ch[ch][(shloka, lemma)] = j
    total_ch_matched, not_in_book = 0, 0
    for ch in sorted(per_ch):
        path = os.path.join(LEX, f"ch{ch}.json")
        doc = load(path)
        ch_verdicts = Counter()
        for n in doc:
            if "_meta" in n:
                continue
            key = (n["shloka"], n.get("lemma_iast"))
            if key in per_ch[ch]:
                n["judge"] = per_ch[ch][key]
                ch_verdicts[per_ch[ch][key]["verdict"]] += 1
                total_ch_matched += 1
            else:
                not_in_book += 1
        doc[0]["_meta"]["lexical_judge"] = {
            "date": "2026-07-07", "judged_by": "claude-sonnet-5",
            "verdicts": dict(ch_verdicts)}
        dump(path, doc)
    print(f"lexical ch files: {total_ch_matched} grafted; "
          f"{not_in_book} ch-file notes not in book aggregate (left unjudged)")

    dump(os.path.join(JDIR, "summary.json"),
         {"_meta": {"generated_by": "scripts/lexical_judge_merge.py",
                    "date": "2026-07-07",
                    "rubric": "PHASE2_METHOD §3.4, contrastive_value→lexical_value",
                    "judged_by": "claude-sonnet-5 ×12 chunks (≤3-wide)",
                    "orchestration": "claude-fable-5"},
          "notes_judged": len(judged),
          "verdicts": dict(verdicts),
          "per_chapter": {str(ch): dict(Counter(
              j["verdict"] for j in per_ch[ch].values()))
              for ch in sorted(per_ch)}})
    print(f"summary -> {os.path.join('data', 'analysis', 'lexical_judge', 'summary.json')}")


if __name__ == "__main__":
    main()
