#!/usr/bin/env python3
"""Census of `Goldman <year>` citations across the corpus (H2832).

Why this exists: the first pass of H2832 stated a headline figure ("445
occurrences in data/apparatus") that no one could reproduce, and the figure was
wrong on both the count and the location. Rather than hand-count again, the
number now comes from a script anybody can re-run:

    python scripts/goldman_citation_census.py

`--json <path>` writes the machine-readable census beside the report.

Two things are counted and deliberately kept apart:

* **occurrences** — raw string hits. The apparatus ships each sarga twice
  (`sarga_NN.json` is the generated twin of `sarga_NN_kostina.json`) and again
  as `.html`, so the raw number over-counts a single authored note fourfold.
* **distinct notes** — hits inside `verses[].notes[]` of the `*_kostina.json`
  files only, which is the authored side of the apparatus. This is the number
  that matters when asking "how many notes would a citation-form change touch".

The script is read-only.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

REPO = Path(__file__).resolve().parent.parent
CITATION = re.compile(r"Goldman (\d{4})")
TEXT_SUFFIXES = {".json", ".html", ".md"}
SKIP_DIRS = {".git", "node_modules", "__pycache__"}


def iter_text_files(root: Path):
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        if SKIP_DIRS.intersection(path.parts):
            continue
        yield path


def occurrences(root: Path) -> tuple[Counter, dict[str, Counter]]:
    """Raw `Goldman <year>` hits, totalled and broken down by directory."""
    totals: Counter = Counter()
    by_dir: dict[str, Counter] = defaultdict(Counter)
    for path in iter_text_files(root):
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for match in CITATION.finditer(text):
            year = match.group(1)
            totals[year] += 1
            by_dir[str(path.relative_to(root).parent).replace("\\", "/")][year] += 1
    return totals, by_dir


def distinct_notes(root: Path) -> tuple[Counter, dict[str, list[str]]]:
    """Authored notes that cite Goldman, counted once per note.

    Only `data/apparatus/sarga_NN_kostina.json` is read: `sarga_NN.json` is its
    generated twin and the `.html` files are rendered from both.
    """
    counts: Counter = Counter()
    loci: dict[str, list[str]] = defaultdict(list)
    apparatus = root / "data" / "apparatus"
    for path in sorted(apparatus.glob("sarga_*_kostina.json")):
        try:
            doc = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            print(f"  ! unreadable {path.name}: {exc}", file=sys.stderr)
            continue
        for verse in doc.get("verses", []):
            verse_id = verse.get("verse_id") or verse.get("verse") or "?"
            for note in verse.get("notes", []):
                blob = json.dumps(note, ensure_ascii=False)
                years = {m.group(1) for m in CITATION.finditer(blob)}
                for year in years:
                    counts[year] += 1
                    loci[year].append(verse_id)
    return counts, loci


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", type=Path, help="write the census as JSON")
    args = parser.parse_args()

    totals, by_dir = occurrences(REPO)
    note_counts, loci = distinct_notes(REPO)

    print("Occurrences of `Goldman <year>` across the repository")
    for year, n in sorted(totals.items()):
        print(f"  Goldman {year}: {n}")

    print("\nBy directory (top 12 for the dominant year):")
    dominant = max(totals, key=totals.get) if totals else None
    rows = sorted(
        ((d, c.get(dominant, 0)) for d, c in by_dir.items()),
        key=lambda kv: -kv[1],
    )
    for directory, n in rows[:12]:
        if n:
            print(f"  {n:6d}  {directory}")

    print("\nDistinct authored notes citing Goldman (sarga_*_kostina.json only):")
    for year, n in sorted(note_counts.items()):
        print(f"  Goldman {year}: {n} notes")
    total_notes = sum(note_counts.values())
    print(f"  total: {total_notes} notes")

    if args.json:
        payload = {
            "occurrences": dict(sorted(totals.items())),
            "occurrences_by_dir": {
                d: dict(sorted(c.items())) for d, c in sorted(by_dir.items())
            },
            "distinct_notes": dict(sorted(note_counts.items())),
            "distinct_notes_total": total_notes,
            "note_loci": {y: sorted(set(v)) for y, v in sorted(loci.items())},
        }
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        print(f"\nwrote {args.json}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
