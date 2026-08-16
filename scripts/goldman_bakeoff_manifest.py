#!/usr/bin/env python3
"""Rights-safe manifest of the H2832 bake-off engine outputs.

The handoff asks the bake-off to be provable with "the saved output of each
engine over the same page sample". Those outputs are OCR of a copyrighted book
(© 1996 Princeton University Press) and must not enter a public repository, so
what is committed instead is a fingerprint per file: page number, byte size,
character count, IAST-diacritic count, and a SHA-256. That is enough to prove

* every engine saw the **same** page sample (identical page-number sets), and
* the headline "0 IAST characters" claims are properties of real files,

while carrying none of the text.

    python scripts/goldman_bakeoff_manifest.py --root <scratchpad>/goldman \\
        --json data/goldman/bakeoff_outputs_manifest.json

`--root` defaults to the session scratchpad layout the bake-off wrote. Missing
directories are reported, not fatal: the manifest is a record of what a given
run produced, and a later machine will not have the scratchpad at all.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import unicodedata
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

# Engine output directories, in the order the report's table lists them.
ENGINES = ("embedded", "pdfminer", "tesseract-eng", "tesseract-engsan", "vision")
PAGE_FILE = re.compile(r"^p(\d{4})\.txt$")

# The IAST inventory, spelled out rather than derived from combining marks.
# A mark-based heuristic ("Latin letter + any diacritic") over-counts here: the
# Bibliography page carries German and French names (Bühler, Söhne, Émile)
# whose umlauts and acutes are not IAST at all. Counting those as IAST would
# have contradicted the report's "0 diacritics from Tesseract" for the wrong
# reason, so the set is explicit and auditable.
IAST_LETTERS = set("āĀīĪūŪṛṚṝṜḷḶḹḸṃṂḥḤṅṄñÑṭṬḍḌṇṆśŚṣṢ")
# Latin letters carrying any combining mark — the wider set, reported beside
# the IAST count so the difference between the two is visible, not hidden.
COMBINING_MARKS = {"̄", "̣", "́", "̀", "̃", "̈", "̇", "̌", "̂"}


def iast_chars(text: str) -> int:
    """Characters belonging to the IAST inventory proper."""
    return sum(1 for ch in text if ch in IAST_LETTERS)


def latin_diacritic_chars(text: str) -> int:
    """Latin letters with any combining mark, IAST or European alike."""
    total = 0
    for ch in text:
        decomposed = unicodedata.normalize("NFD", ch)
        if len(decomposed) > 1 and decomposed[0].isascii() and decomposed[0].isalpha():
            if COMBINING_MARKS.intersection(decomposed[1:]):
                total += 1
    return total


def fingerprint(path: Path) -> dict:
    raw = path.read_bytes()
    text = raw.decode("utf-8", errors="replace")
    return {
        "bytes": len(raw),
        "chars": len(text),
        "iast_chars": iast_chars(text),
        "latin_diacritic_chars": latin_diacritic_chars(text),
        "devanagari_chars": sum(1 for c in text if "ऀ" <= c <= "ॿ"),
        "sha256": hashlib.sha256(raw).hexdigest(),
    }


def scan(root: Path) -> dict:
    engines: dict[str, dict] = {}
    missing: list[str] = []
    for engine in ENGINES:
        directory = root / "bakeoff" / engine
        if not directory.is_dir():
            missing.append(engine)
            continue
        pages: dict[str, dict] = {}
        for path in sorted(directory.glob("*.txt")):
            match = PAGE_FILE.match(path.name)
            if not match:
                continue  # scratch files such as _tess_tmp.txt
            pages[str(int(match.group(1)))] = fingerprint(path)
        engines[engine] = {
            "pages": pages,
            "page_count": len(pages),
            "iast_chars_total": sum(p["iast_chars"] for p in pages.values()),
            "latin_diacritic_chars_total": sum(
                p["latin_diacritic_chars"] for p in pages.values()
            ),
            "chars_total": sum(p["chars"] for p in pages.values()),
        }

    gold: dict[str, dict] = {}
    gold_dir = root / "gold"
    if gold_dir.is_dir():
        for path in sorted(gold_dir.glob("*.txt")):
            match = PAGE_FILE.match(path.name)
            if match:
                gold[str(int(match.group(1)))] = fingerprint(path)
    else:
        missing.append("gold")

    return {"engines": engines, "gold": gold, "missing": missing}


def main() -> int:
    default_root = (
        Path(__file__).resolve().parent.parent.parent
        / "_scratchpad_goldman_not_present"
    )
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=default_root)
    parser.add_argument("--json", type=Path, help="write the manifest here")
    args = parser.parse_args()

    if not args.root.is_dir():
        print(f"! no such root: {args.root}", file=sys.stderr)
        print(
            "  The engine outputs live in a session scratchpad and are never "
            "committed; pass --root to a directory holding bakeoff/<engine>/pNNNN.txt.",
            file=sys.stderr,
        )
        return 2

    result = scan(args.root)
    engines = result["engines"]

    print(f"root: {args.root}")
    for name, data in engines.items():
        print(
            f"  {name:18s} {data['page_count']:3d} pages  "
            f"{data['chars_total']:8,d} chars  {data['iast_chars_total']:5d} IAST  "
            f"({data['latin_diacritic_chars_total']:5d} Latin+diacritic)"
        )
    if result["gold"]:
        print(f"  {'gold':18s} {len(result['gold']):3d} pages")
    if result["missing"]:
        print(f"  missing: {', '.join(result['missing'])}")

    page_sets = {name: set(d["pages"]) for name, d in engines.items() if d["pages"]}
    reference = max(page_sets.values(), key=len) if page_sets else set()
    strays = {
        name: sorted(pages - reference, key=int)
        for name, pages in page_sets.items()
        if pages - reference
    }
    subsets = {
        name: sorted(reference - pages, key=int)
        for name, pages in page_sets.items()
        if reference - pages and not pages - reference
    }

    listed = ", ".join(sorted(reference, key=int))
    print(f"\nfull sample ({len(reference)} pages): {listed}")
    if strays:
        # A page nobody else read makes the comparison invalid — the handoff's
        # named fail condition ("engines compared on different pages").
        print("INVALID — these engines read pages outside the sample:")
        for name, pages in strays.items():
            print(f"  {name}: {', '.join(pages)}")
    elif subsets:
        print("VALID with a documented subset — every engine read pages from the")
        print("same sample; these covered only part of it:")
        for name, pages in subsets.items():
            covered = len(reference) - len(pages)
            absent = ", ".join(pages)
            print(f"  {name}: {covered}/{len(reference)} pages, absent {absent}")
    else:
        print("VALID — every engine read exactly the same pages.")

    verdict = "invalid" if strays else ("subset" if subsets else "identical")

    if args.json:
        payload = {
            "_note": (
                "Fingerprints only. The engine outputs are OCR of Goldman & "
                "Goldman 1996 (© Princeton University Press) and are deliberately "
                "not committed; see docs/GOLDMAN_PDF_EXTRACTION_BAKEOFF_2026.md §5."
            ),
            "sample_verdict": verdict,
            "full_sample": sorted(reference, key=int),
            "partial_coverage": subsets,
            "outside_sample": strays,
            "engines": engines,
            "gold": result["gold"],
            "missing": result["missing"],
        }
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        print(f"wrote {args.json}")
    return 1 if strays else 0


if __name__ == "__main__":
    raise SystemExit(main())
