#!/usr/bin/env python3
"""Adjudicate a gold transcription against a second engine, diacritics folded.

H2832. The model-vision transcription and the Tesseract transcription fail in
disjoint ways: vision restores diacritics but can silently normalise or skip a
line; Tesseract keeps the line structure but flattens every diacritic. Folding
IAST to bare ASCII therefore isolates the *content* disagreements — the only
ones that can make a gold file wrong.

    python scripts/goldman_adjudicate_gold.py --a DIR/vision/p0250.txt \
        --b DIR/tesseract-eng/p0250.txt

Every reported hunk must be re-checked against the page image before the `a`
side is promoted to gold. Read-only.
"""

from __future__ import annotations

import argparse
import difflib
import sys
import unicodedata

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

FOLD = str.maketrans(
    {
        "‘": "'", "’": "'", "‛": "'", "´": "'", "`": "'",
        "“": '"', "”": '"', "„": '"', "‟": '"',
        "–": "-", "—": "-", "‒": "-", "―": "-",
        "ṃ": "m", "ṁ": "m", "ṅ": "n", "ñ": "n", "ṇ": "n",
        "ṭ": "t", "ḍ": "d", "ś": "s", "ṣ": "s", "ḥ": "h",
        "ṛ": "r", "ṝ": "r", "ḷ": "l", "ḹ": "l",
    }
)


def fold(s: str) -> list[str]:
    s = unicodedata.normalize("NFD", s.translate(FOLD))
    s = "".join(c for c in s if not unicodedata.combining(c))
    return s.lower().split()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--a", required=True, help="candidate gold")
    ap.add_argument("--b", required=True, help="second engine")
    ap.add_argument("--context", type=int, default=4)
    args = ap.parse_args()

    with open(args.a, encoding="utf-8") as fh:
        a_raw = fh.read()
    with open(args.b, encoding="utf-8") as fh:
        b_raw = fh.read()

    a, b = fold(a_raw), fold(b_raw)
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    ratio = sm.ratio()
    hunks = 0
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            continue
        hunks += 1
        c = args.context
        print(f"[{tag}] a[{i1}:{i2}] b[{j1}:{j2}]")
        print(f"   A …{' '.join(a[max(0, i1 - c):i2 + c])}…")
        print(f"   B …{' '.join(b[max(0, j1 - c):j2 + c])}…")
    print(f"\ntokens A={len(a)} B={len(b)}  folded token similarity={ratio:.4f}  hunks={hunks}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
