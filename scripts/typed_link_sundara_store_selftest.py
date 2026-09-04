#!/usr/bin/env python3
"""Selftest for the H3346 Type-D concordance store merge (H4087).

Guards the invariants a silent store-write bug could break:

  1. the confirmed tier exists and matches the vote (258 approved, 0 rejected
     -- vote h3346_typed_store, MG ruling 'approve (a)', 04-09-2026);
  2. TSV and JSONL confirmed tiers carry the same row set (`_row_key`);
  3. every confirmed row's ids still match the linkid grammar shape
     (root:<SLP1> / commentary:sundara-lexical:V.<sarga>.<verse>) -- a
     regression here would mean the promotion step corrupted a row;
  4. the store-write invariant the H3346 dedup pass proved holds after
     promotion too: 0 root-overlap rows made it into the confirmed tier
     (156 unique-vs-1058 + 102 verse-overlap == 258, root-overlap == 0);
  5. the decisions.json this promotion was built from carries no open votes
     (apply_decisions() already refuses that, but the store selftest checks
     the artifact independently of the script that produced it).

Run: python scripts/typed_link_sundara_store_selftest.py
"""
import csv
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)

PROPOSED_JSONL = os.path.join(REPO, "data", "typed_link_sundara_concordance.jsonl")
CONFIRMED_TSV = os.path.join(REPO, "data",
                              "typed_link_sundara_concordance.confirmed.tsv")
CONFIRMED_JSONL = os.path.join(REPO, "data",
                                "typed_link_sundara_concordance.confirmed.jsonl")
DECISIONS = os.path.join(
    REPO, "data", "analysis", "typed_link_sundara",
    "commentarystrategies-sundarakanda-typed-link-q41_decisions.json")

ANCHOR_RE = re.compile(r"^root:[A-Za-z]+$")
LOCUS_RE = re.compile(r"^commentary:sundara-lexical:V\.\d+\.\d+[ab]?$")

FAILED = []


def check(label, cond, detail=""):
    print(f"  {'ok  ' if cond else 'FAIL'} {label}" + (f" — {detail}" if detail else ""))
    if not cond:
        FAILED.append(label)


def load_jsonl(path):
    with open(path, encoding="utf-8") as fh:
        return [json.loads(line) for line in fh if line.strip()]


def main():
    check("decisions.json exists", os.path.exists(DECISIONS), DECISIONS)
    check("confirmed TSV exists", os.path.exists(CONFIRMED_TSV), CONFIRMED_TSV)
    check("confirmed JSONL exists", os.path.exists(CONFIRMED_JSONL), CONFIRMED_JSONL)
    if FAILED:
        print(f"\n{len(FAILED)} check(s) failed — cannot continue.")
        sys.exit(1)

    decisions = json.load(open(DECISIONS, encoding="utf-8"))
    votes = decisions.get("reviewer_decisions", {})
    check("decisions.json carries votes (human gate was not bypassed)",
          len(votes) > 0, f"{len(votes)} votes")
    open_votes = [k for k, v in votes.items() if v.get("action") not in
                  ("approve", "reject")]
    check("no open votes remain in decisions.json", not open_votes,
          f"{len(open_votes)} open")
    rejects = [k for k, v in votes.items() if v.get("action") == "reject"]

    proposed = load_jsonl(PROPOSED_JSONL)
    confirmed_jsonl = load_jsonl(CONFIRMED_JSONL)
    check("proposed dataset is 258 rows (H3346 shipped shape)",
          len(proposed) == 258, f"{len(proposed)} rows")
    check("confirmed JSONL row count == approved votes",
          len(confirmed_jsonl) == len(votes) - len(rejects),
          f"{len(confirmed_jsonl)} confirmed vs "
          f"{len(votes) - len(rejects)} approved")

    with open(CONFIRMED_TSV, encoding="utf-8", newline="") as fh:
        confirmed_tsv = list(csv.DictReader(fh, delimiter="\t"))
    check("TSV and JSONL confirmed tiers carry the same row count",
          len(confirmed_tsv) == len(confirmed_jsonl),
          f"tsv={len(confirmed_tsv)} jsonl={len(confirmed_jsonl)}")

    tsv_keys = {f'{r["anchor_id"]}|{r["target_locus"]}' for r in confirmed_tsv}
    jsonl_keys = {r["_row_key"] for r in confirmed_jsonl}
    check("TSV and JSONL confirmed tiers carry the identical row set",
          tsv_keys == jsonl_keys,
          f"{len(tsv_keys ^ jsonl_keys)} rows differ" if tsv_keys != jsonl_keys
          else "")

    bad_anchor = [r["anchor_id"] for r in confirmed_jsonl
                  if not ANCHOR_RE.match(r["anchor_id"])]
    check("every confirmed anchor_id matches root:<SLP1>", not bad_anchor,
          f"{len(bad_anchor)} malformed, e.g. {bad_anchor[:3]}")
    bad_locus = [r["target_locus"] for r in confirmed_jsonl
                 if not LOCUS_RE.match(r["target_locus"])]
    check("every confirmed target_locus matches the Sundara lexical grammar",
          not bad_locus, f"{len(bad_locus)} malformed, e.g. {bad_locus[:3]}")

    root_overlap = [r["_row_key"] for r in confirmed_jsonl
                    if r.get("_dedup_status") == "root-overlap"]
    check("no root-overlap-vs-1058 row was promoted into the confirmed store",
          not root_overlap, f"{len(root_overlap)} promoted anyway")

    known = {r["_row_key"]: r for r in proposed}
    unknown_votes = set(votes) - set(known)
    check("every voted row_key exists in the proposed dataset",
          not unknown_votes, f"{len(unknown_votes)} unknown, e.g. "
          f"{sorted(unknown_votes)[:3]}")

    print()
    if FAILED:
        print(f"{len(FAILED)} check(s) FAILED:")
        for label in FAILED:
            print(f"  - {label}")
        sys.exit(1)
    print(f"ALL CHECKS PASSED — {len(confirmed_jsonl)} Type-D concordance rows "
          f"in the confirmed store, {len(rejects)} rejected.")


if __name__ == "__main__":
    main()
