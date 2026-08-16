#!/usr/bin/env python3
"""Measure the verse-number offset between Goldman's critical edition and our
vulgate-numbered Sundarakāṇḍa text — H2832.

Why this exists. Goldman & Goldman translate the **Baroda critical edition**;
our text and apparatus follow the southern/vulgate numbering that the Gita
Supersite scrape uses. Wherever the critical editors relegated a line to a star
passage, the two verse series slip by one, and they never resynchronise. A join
on `verse N` therefore compares different verses — silently, and more often the
further into the sarga you go.

Method. Each Goldman note carries a transliterated lemma right after its English
gloss (`6. "great serpents" nāga-:`). We fold that lemma to bare ASCII, fold our
own `sanskrit_iast` the same way, and ask: at which of our verse numbers does
that lemma actually occur? The difference between that number and Goldman's is
the offset for that note. The distribution over all matched notes is the answer.

    python scripts/goldman_verse_offset_measure.py \
        --apparatus data/apparatus/sarga_01_kostina.json \
        --goldman-dir <scratch>/sarga01_notes --json data/goldman/offset_sarga01.json

Read-only apart from --json.
"""

from __future__ import annotations

import argparse
import collections
import glob
import json
import os
import re
import sys
import unicodedata

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

# The lemma sits between the closing quote of the English gloss and the colon
# that introduces the discussion: `"great serpents" nāga- (used twice…):`
LEMMA_LINE = re.compile(
    r'(?m)^[ \t]*([IlJ1-9]\d{0,2})(?:-\d{1,3})?\.\s+["“][^"”]{1,90}["”]\s+([^:\n]{2,60}?):'
)
_OCR_ONE = str.maketrans({"I": "1", "l": "1", "J": "1"})

# The embedded Acrobat layer renders IAST as ASCII debris in a *systematic* way:
# ā→ii, ṇ→r:i / r.i, ṣ→~ / f, ḥ→f! …  We do not try to restore it — we fold both
# sides down to the letters that survive on both, which is enough to locate a
# lemma inside a verse.
_DEBRIS = re.compile(r"[^a-z]+")


def fold(s: str) -> str:
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.replace("ii", "a").replace("ṃ", "m")
    return _DEBRIS.sub("", s)


def our_verses(path: str) -> list[tuple[int, str]]:
    with open(path, encoding="utf-8") as fh:
        doc = json.load(fh)
    out = []
    for v in doc["verses"]:
        num = str(v.get("verse"))
        if not num.isdigit():
            continue
        out.append((int(num), fold(v.get("sanskrit_iast") or "")))
    return sorted(out)


def goldman_lemmas(directory: str) -> list[tuple[int, str, str]]:
    out = []
    for path in sorted(glob.glob(os.path.join(directory, "*.txt"))):
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        for num, lemma in LEMMA_LINE.findall(text):
            n = num.translate(_OCR_ONE).lstrip("0")
            if not n.isdigit() or int(n) > 250:
                continue
            # strip a parenthetical aside, keep the head word
            head = lemma.split("(")[0].strip().strip("-—,;")
            f = fold(head)
            if len(f) >= 6:                      # too short to locate reliably
                out.append((int(n), head, f))
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apparatus", required=True)
    ap.add_argument("--goldman-dir", required=True)
    ap.add_argument("--json")
    ap.add_argument("--window", type=int, default=8, help="± verses to search around N")
    args = ap.parse_args()

    verses = our_verses(args.apparatus)
    by_num = dict(verses)
    lemmas = goldman_lemmas(args.goldman_dir)

    matches, unmatched, ambiguous = [], [], []
    for n, raw, f in lemmas:
        hits = [num for num, text in verses if abs(num - n) <= args.window and f in text]
        if not hits:
            unmatched.append({"goldman_verse": n, "lemma": raw})
            continue
        if len(hits) > 1:
            ambiguous.append({"goldman_verse": n, "lemma": raw, "our_verses": hits})
            continue
        matches.append({"goldman_verse": n, "our_verse": hits[0], "offset": hits[0] - n, "lemma": raw})

    dist = collections.Counter(m["offset"] for m in matches)
    by_region = collections.defaultdict(collections.Counter)
    for m in matches:
        by_region[(m["goldman_verse"] - 1) // 25 * 25][m["offset"]] += 1

    report = {
        "apparatus": args.apparatus,
        "lemmas_extracted": len(lemmas),
        "located": len(matches),
        "ambiguous": len(ambiguous),
        "unmatched": len(unmatched),
        "offset_distribution": dict(sorted(dist.items())),
        "offset_by_region": {str(k): dict(sorted(v.items())) for k, v in sorted(by_region.items())},
        "matches": sorted(matches, key=lambda m: m["goldman_verse"]),
        "ambiguous_rows": ambiguous,
        "unmatched_rows": unmatched,
        "our_verse_count": len(verses),
        "our_max_verse": max(by_num) if by_num else 0,
    }
    if args.json:
        os.makedirs(os.path.dirname(args.json) or ".", exist_ok=True)
        with open(args.json, "w", encoding="utf-8", newline="\n") as fh:
            json.dump(report, fh, ensure_ascii=False, indent=1)
        print(f"-> {args.json}")

    print(f"lemmas extracted : {len(lemmas)}")
    print(f"located uniquely : {len(matches)}   ambiguous {len(ambiguous)}   unmatched {len(unmatched)}")
    print("offset (our verse - Goldman verse):")
    for off, cnt in sorted(dist.items()):
        print(f"  {off:+d}  {cnt:>3}  {'#' * cnt}")
    print("\nby region of the sarga (Goldman verse number):")
    for start, c in sorted(by_region.items()):
        top = ", ".join(f"{o:+d}×{n}" for o, n in sorted(c.items()))
        print(f"  vv {start + 1:>3}-{start + 25:<3}  {top}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
