#!/usr/bin/env python
"""Q4.1 pilot (H541) — root -> gita-tm `commentary-citation` Type-D concordance.

Links Sanskrit verb roots to the Bhagavadgita-TM commentary loci where they are
cited, per TYPED_LINK_ID_GRAMMAR.md §4c (Uprava, Type-D "commentary-citation"
subtype). Consumes the fixed record shape rather than inventing one:

    anchor_type      : root
    anchor_id        : root:<SLP1>
    anchor_key_slp1  : <SLP1>
    target_locus     : commentary:gita-tm:<chapter.verse>
    link_type        : commentary-citation
    source_dataset   : CommentaryStrategies/data/gita_tm.json
    match_method     : exact | floor | relaxed | fuzzy
    confidence       : TIER_CONFIDENCE[match_method]
    evidence_count   : gloss occurrences backing this (root, verse) pair
    date             : DD-MM-YYYY

Root anchor inventory: WhitneyRoots/crosswalk/mw_roots.json (750 MW-numbered
roots, 704 distinct SLP1 keys) — a sibling checkout, never re-derived here.

Matching: reuses kosha/scripts/concordance_core.py's TieredMatcher (never a
re-rolled matcher, TYPED_LINK_ID_GRAMMAR.md §6.3) against
data/gita_tm_slp1.json, the crosswalk_gita_tm.py output (SLP1-keyed Gita-TM
glosses). Lossy tiers (relaxed/fuzzy) stay unique-match-only — TieredMatcher's
own quarantine rule.

Verse loci are extracted from the glosses' embedded "(BG <ch>.<v> <code>)"
citation markers (gita_tm.json's own provenance convention), carried verbatim
into target_locus's tail.

Usage:
    python scripts/build_root_gita_concordance.py [--report]

Output:
    data/typed_link_commentary_citation.tsv  — TYPE_D_RECORD_FIELDS rows (TSV,
    the typed_link_lint.py / SubjectConcordance / VisualDCS convention)
"""
import argparse
import csv
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

REPO = Path(__file__).parent.parent
GITA_TM_SLP1 = REPO / "data" / "gita_tm_slp1.json"
ROOTS = REPO.parent / "WhitneyRoots" / "crosswalk" / "mw_roots.json"
OUT = REPO / "data" / "typed_link_commentary_citation.tsv"
DATE = "11-07-2026"
SOURCE_DATASET = "CommentaryStrategies/data/gita_tm.json"

sys.path.insert(0, str(REPO.parent / "sanskrit-util" / "py"))
from sanskrit_util import from_slp1  # noqa: E402

sys.path.insert(0, str(REPO.parent / "kosha" / "scripts"))
from concordance_core import TieredMatcher, TIER_CONFIDENCE, TYPE_D_RECORD_FIELDS  # noqa: E402

VERSE_RE = re.compile(r"\(BG\s+(\d+\.\d+)\s*[a-zA-Z]*\)")


def load_roots():
    rows = json.loads(ROOTS.read_text(encoding="utf-8"))
    slp1_keys = sorted({r["slp1"] for r in rows if r.get("slp1")})
    return slp1_keys


def build_matcher(root_slp1_keys):
    m = TieredMatcher()
    for slp1_key in root_slp1_keys:
        m.add_anchor(slp1_key, from_slp1(slp1_key))
    return m


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--report", action="store_true")
    args = ap.parse_args()

    if not ROOTS.exists():
        print(f"ERROR: root inventory not found at {ROOTS}", file=sys.stderr)
        print("Make sure WhitneyRoots repo is a sibling of CommentaryStrategies.",
              file=sys.stderr)
        sys.exit(1)
    if not GITA_TM_SLP1.exists():
        print(f"ERROR: {GITA_TM_SLP1} missing — run crosswalk_gita_tm.py first.",
              file=sys.stderr)
        sys.exit(1)

    root_slp1_keys = load_roots()
    print(f"Root anchor inventory: {len(root_slp1_keys):,} SLP1 roots (WhitneyRoots/mw_roots.json)")
    matcher = build_matcher(root_slp1_keys)

    gita = json.loads(GITA_TM_SLP1.read_text(encoding="utf-8"))
    print(f"Gita-TM SLP1 crosswalk: {len(gita):,} keys")

    # (anchor_slp1, verse) -> evidence_count, tier
    pairs = defaultdict(lambda: {"count": 0, "tier": None})
    tier_counts = defaultdict(int)
    matched_terms = 0

    for gita_key, entry in gita.items():
        if gita_key.startswith("gita:"):
            continue  # unmatched by crosswalk_gita_tm.py — not a headword at all
        iast = from_slp1(gita_key)
        tier, anchors = matcher.match(iast, slp1_hint=gita_key)
        if not tier:
            continue
        matched_terms += 1
        for anchor in anchors:
            for gloss in entry.get("glosses", []):
                for verse in VERSE_RE.findall(gloss):
                    key = (anchor, verse)
                    rec = pairs[key]
                    rec["count"] += 1
                    # keep the highest-trust tier seen for this pair
                    if rec["tier"] is None or (
                        list(TIER_CONFIDENCE).index(tier)
                        < list(TIER_CONFIDENCE).index(rec["tier"])
                    ):
                        rec["tier"] = tier
            tier_counts[tier] += 1

    rows = []
    for (anchor, verse), rec in sorted(pairs.items()):
        tier = rec["tier"]
        rows.append({
            "anchor_type": "root",
            "anchor_id": f"root:{anchor}",
            "anchor_key_slp1": anchor,
            "target_locus": f"commentary:gita-tm:{verse}",
            "link_type": "commentary-citation",
            "source_dataset": SOURCE_DATASET,
            "match_method": tier,
            "confidence": TIER_CONFIDENCE[tier],
            "evidence_count": rec["count"],
            "date": DATE,
        })

    with open(OUT, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=TYPE_D_RECORD_FIELDS, delimiter="\t")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

    print(f"\nMatched gita-tm headwords -> root anchors: {matched_terms:,}")
    print(f"Emitted (root, verse) link rows: {len(rows):,}")
    print(f"Output: {OUT}")

    if args.report:
        print("\n-- Per-tier term-match counts (unique-match-only for relaxed/fuzzy) --")
        for tier in TIER_CONFIDENCE:
            if tier in tier_counts:
                print(f"  {tier:8s} {tier_counts[tier]:4d}")
        print("\n-- Sample rows --")
        for row in rows[:10]:
            print(f"  {row['anchor_id']:14s} -> {row['target_locus']:24s} "
                  f"({row['match_method']}, n={row['evidence_count']})")


if __name__ == "__main__":
    main()
