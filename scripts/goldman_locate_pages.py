#!/usr/bin/env python3
"""Locate structural landmarks in a Goldman/Princeton Rāmāyaṇa volume PDF.

H2832 helper. The embedded OCR layer of the Princeton volumes is diacritically
destroyed but structurally intact enough to find section boundaries, which is
all we need to pick a *fixed, reproducible* page sample for the bake-off.

    python scripts/goldman_locate_pages.py <pdf> --toc
    python scripts/goldman_locate_pages.py <pdf> --grep "SARGA 1$" --max 20
    python scripts/goldman_locate_pages.py <pdf> --stats-range 300-360

Read-only.
"""

from __future__ import annotations

import argparse
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

import fitz  # noqa: E402


def clean(s: str) -> str:
    """Bookmark titles in these files are NUL-padded."""
    return s.replace("\x00", "").strip()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("pdf")
    ap.add_argument("--toc", action="store_true", help="print bookmarks with their PDF page")
    ap.add_argument("--grep", help="regex to find, page by page (MULTILINE)")
    ap.add_argument("--max", type=int, default=40)
    ap.add_argument("--context", type=int, default=0, help="chars of context around a hit")
    ap.add_argument("--stats-range", help="A-B: per-page char/image stats for that PDF page range")
    args = ap.parse_args()

    doc = fitz.open(args.pdf)

    if args.toc:
        for lvl, title, page in doc.get_toc():
            print(f"{'  ' * (lvl - 1)}p{page:>4}  {clean(title)}")

    if args.grep:
        rx = re.compile(args.grep, re.MULTILINE)
        hits = 0
        for pno in range(doc.page_count):
            text = doc.load_page(pno).get_text("text")
            m = rx.search(text)
            if not m:
                continue
            hits += 1
            if args.context:
                a = max(0, m.start() - args.context)
                snippet = text[a : m.end() + args.context].replace("\n", " ⏎ ")
            else:
                snippet = m.group(0)
            print(f"pdf p{pno + 1:>4}: {snippet}")
            if hits >= args.max:
                break

    if args.stats_range:
        a, b = (int(x) for x in args.stats_range.split("-"))
        for pno in range(a - 1, min(b, doc.page_count)):
            page = doc.load_page(pno)
            t = page.get_text("text")
            head = " ".join(t.split()[:9])
            print(f"p{pno + 1:>4}  chars={len(t):>5}  imgs={len(page.get_images())}  {head}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
