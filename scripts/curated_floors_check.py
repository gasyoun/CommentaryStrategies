#!/usr/bin/env python3
"""Curated-record floors — the live files may never shrink below the pins.

H4351 (08-09-2026). `tests/curated_floors.py` freezes, as literals, the curated record
count of every file the ten destructive appliers write (read from the live
files at authoring time). The pytest suite itself is hermetic — it never opens
`data/` — so this script is where those literals become load-bearing: it reads
the live files READ-ONLY and fails when any count sits below its floor, the
FINDINGS class where regenerating a derived file erased curated facts.

Usage:
    python scripts/curated_floors_check.py            # --check is the default
    python scripts/curated_floors_check.py --print    # live counts, to re-pin

Wired into the `corpus` job of .github/workflows/ci.yml. Raising a floor is a
deliberate edit of CURATED_FLOORS_2026_09_08 in tests/curated_floors.py, reviewed
like any other data claim; lowering one needs the reason in the same commit.
"""
from __future__ import annotations

import argparse
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(REPO, "tests"))

from curated_floors import CURATED_FLOORS_2026_09_08  # noqa: E402


def _load(rel: str):
    with open(os.path.join(REPO, rel), encoding="utf-8") as fh:
        return json.load(fh)


def _records(doc) -> list:
    return [x for x in doc if isinstance(x, dict) and "_meta" not in x]


def live_count(rel: str, measure: str) -> int:
    doc = _load(rel)
    if measure == "entries":
        return len(doc["entries"])
    if measure in ("cards", "notes") and isinstance(doc, dict):
        return len(doc[measure])
    if measure in ("cards", "notes"):
        return len(_records(doc))
    if measure == "cross_text":
        return sum(1 for n in _records(doc) if n.get("subtype") == "cross_text")
    if measure.startswith("type_"):
        want = measure[len("type_"):]
        return sum(1 for n in _records(doc) if n.get("type") == want)
    raise ValueError(f"unknown measure {measure!r} for {rel}")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true", default=True)
    ap.add_argument("--print", dest="print_only", action="store_true",
                    help="print live counts next to the pins; never fails")
    args = ap.parse_args(argv)

    bad = []
    for key, floor in sorted(CURATED_FLOORS_2026_09_08.items()):
        rel, measure = key.rsplit(":", 1)
        try:
            live = live_count(rel, measure)
        except FileNotFoundError:
            bad.append((key, floor, "MISSING FILE"))
            print(f"  {key:70} floor {floor:>6}  live MISSING")
            continue
        flag = "" if live >= floor else "  <-- BELOW FLOOR"
        print(f"  {key:70} floor {floor:>6}  live {live:>6}{flag}")
        if live < floor:
            bad.append((key, floor, live))
    if args.print_only:
        return 0
    if bad:
        print(f"FAIL: {len(bad)} curated file(s) shrank below the H4351 floor:",
              file=sys.stderr)
        for key, floor, live in bad:
            print(f"  {key}: floor {floor}, live {live}", file=sys.stderr)
        return 1
    print(f"OK: {len(CURATED_FLOORS_2026_09_08)} curated floors hold")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
