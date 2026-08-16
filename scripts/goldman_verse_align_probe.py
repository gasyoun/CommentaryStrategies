#!/usr/bin/env python3
"""Is a verse-number join between Goldman and our apparatus sound? — H2832.

Goldman/Princeton translates the **Baroda critical edition**; our Sundarakāṇḍa
text follows the southern/vulgate numbering the Gita Supersite scrape uses.
The two recensions do not agree on verse count, so `verse N` is only the same
verse in both while no passage has been inserted or dropped between them. This
probe prints, for a sample of verse numbers, our IAST + Leonov's Russian next to
Goldman's note lemma for the same number, so a reader can see where the two
series start to drift.

    python scripts/goldman_verse_align_probe.py --apparatus data/apparatus/sarga_01_kostina.json \
        --collate data/goldman/collate_sarga01.json --verses 1,6,20,50,100,150,183

Read-only.
"""

from __future__ import annotations

import argparse
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apparatus", required=True)
    ap.add_argument("--collate", required=True)
    ap.add_argument("--verses", default="1,6,20,50,100,150,183")
    args = ap.parse_args()

    with open(args.apparatus, encoding="utf-8") as fh:
        appd = json.load(fh)
    ours = {str(v["verse"]): v for v in appd["verses"]}

    with open(args.collate, encoding="utf-8") as fh:
        col = json.load(fh)
    theirs = {r["verse"]: r["goldman_lemmas"] for r in col["rows"]}

    for key in [v.strip() for v in args.verses.split(",")]:
        v = ours.get(key)
        print(f"\n=== verse {key} " + "=" * 50)
        if v:
            print("  IAST   :", (v.get("sanskrit_iast") or "")[:180])
            print("  Leonov :", (v.get("leonov_ru") or "")[:180])
        else:
            print("  (absent from our apparatus)")
        g = theirs.get(key)
        print("  Goldman:", " | ".join(g)[:180] if g else "(no note at this number)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
