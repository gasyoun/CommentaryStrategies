#!/usr/bin/env python3
"""Inter-reviewer agreement on the tier-2 assembly gate (Leonov vs Kostina).

Ruling R1 gives the final book assembly TWO gatekeepers. Once both have voted on
the same apparatus notes, the interesting question is no longer "was it gated"
but **did they agree, and where not** — the disagreements are the editorial
worklist, and κ says whether the two gates are measuring the same thing at all.

Reads data/apparatus/gate_ledger.json (schema v2 — one verdict per reviewer per
note; see scripts/gate_ledger.py) and reports, per reviewer pair:

  * overlap (notes both voted on) — κ is meaningless without it;
  * raw agreement, Cohen's κ, and a bootstrap 95% CI;
  * the accept/edit/reject confusion matrix;
  * every disagreeing note id, grouped by layer, as a human worklist.

κ machinery is imported from scripts/compute_iaa_kappa.py (H1469 — same
estimator, same 2 000-resample bootstrap, same seed) rather than reimplemented,
so the two IAA surfaces in this repo cannot drift apart.

Nothing is resolved or written back: choosing a winner is an editorial act.

Usage:
  python scripts/gate_reviewer_agreement.py
  python scripts/gate_reviewer_agreement.py --write   # + data/iaa/gate_agreement.json
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import gate_ledger                                        # noqa: E402
from compute_iaa_kappa import (SEED, N_BOOT, bootstrap_ci,  # noqa: E402
                               confusion)

ROOT = HERE.parent
LEDGER = ROOT / "data" / "apparatus" / "gate_ledger.json"
OUT = ROOT / "data" / "iaa" / "gate_agreement.json"

ACTIONS = ["accept", "edit", "reject"]


def collect(ledger: dict) -> tuple[dict, dict]:
    """note id -> {reviewer: action}, and note id -> layer."""
    per_note, layer = {}, {}
    for nid, entry in ledger.get("entries", {}).items():
        vs = entry.get("verdicts") or {}
        acts = {r: v for r, v in vs.items() if v.get("action")}
        if acts:
            per_note[nid] = acts
            layer[nid] = entry.get("layer") or nid.split(":")[0]
    return per_note, layer


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true",
                    help=f"also write {OUT.relative_to(ROOT)}")
    args = ap.parse_args()

    if not LEDGER.exists():
        sys.exit(f"ERROR: no gate ledger at {LEDGER} — nobody has gated anything yet")
    ledger = gate_ledger.load(str(LEDGER))
    per_note, layer = collect(ledger)
    reviewers = gate_ledger.reviewers(ledger)

    print("=" * 72)
    print("TIER-2 ASSEMBLY GATE — INTER-REVIEWER AGREEMENT (ruling R1)")
    print("=" * 72)
    print(f"  ledger entries       : {len(per_note)}")
    print(f"  reviewers on record  : {reviewers or '(none)'}")
    for r in reviewers:
        c = Counter(v.get("action") for acts in per_note.values()
                    for who, v in acts.items() if who == r)
        print(f"    {r}: {sum(c.values())} verdict(s) · {dict(c)}")

    if len(reviewers) < 2:
        print()
        print("  Only one reviewer has voted — κ needs two independent gates.")
        print("  Ruling R1 requires Leonov AND Kostina on the final assembly, so the")
        print("  gate is INCOMPLETE, not merely unmeasured. Next step: build the")
        print("  second gatekeeper's ballot —")
        print('    python scripts/build_sarga_apparatus.py <N> --reviewer "Костина"')
        return 0

    report = {"_meta": {"generated_by": "scripts/gate_reviewer_agreement.py",
                        "ledger": str(LEDGER.relative_to(ROOT)).replace("\\", "/"),
                        "kappa": {"estimator": "Cohen (scripts/compute_iaa_kappa.py)",
                                  "bootstrap": N_BOOT, "seed": SEED},
                        "reviewers": reviewers},
              "pairs": {}}

    for a, b in combinations(reviewers, 2):
        pairs = [(acts[a].get("action"), acts[b].get("action")) for acts in per_note.values()
                 if a in acts and b in acts]
        overlap = [nid for nid, acts in per_note.items() if a in acts and b in acts]
        print()
        print(f"  {a} vs {b}")
        if not pairs:
            print("    no shared notes — they voted on disjoint material, "
                  "so agreement is undefined (not 'perfect')")
            report["pairs"][f"{a}|{b}"] = {"overlap": 0}
            continue
        agree = sum(1 for x, y in pairs if x == y)
        k, lo, hi = bootstrap_ci(pairs, ACTIONS)
        print(f"    overlap           : {len(pairs)} note(s)")
        print(f"    raw agreement     : {agree}/{len(pairs)} = "
              f"{100.0 * agree / len(pairs):.1f}%")
        print(f"    Cohen's κ         : {k:.3f}  [95% CI {lo:.3f}, {hi:.3f}]"
              f"  (bootstrap {N_BOOT}, seed {SEED})")
        conf = confusion(pairs, ACTIONS)
        print(f"    confusion         : {json.dumps(conf, ensure_ascii=False)}")

        disagreements = defaultdict(list)
        for nid in sorted(overlap):
            av, bv = per_note[nid][a], per_note[nid][b]
            x, y = av.get("action"), bv.get("action")
            if gate_ledger.conflict({a: av, b: bv}):
                disagreements[layer[nid]].append((nid, x, y))
        total_dis = sum(len(v) for v in disagreements.values())
        if total_dis:
            print(f"    DISAGREEMENTS ({total_dis}) — editorial worklist, "
                  f"a human picks the winner:")
            for lay in sorted(disagreements):
                rows = disagreements[lay]
                print(f"      {lay} ({len(rows)}):")
                for nid, x, y in rows[:10]:
                    print(f"        {nid}: {a}={x} · {b}={y}")
                if len(rows) > 10:
                    print(f"        … +{len(rows) - 10} more")
        else:
            print("    no disagreements — every shared note has one agreed action")

        report["pairs"][f"{a}|{b}"] = {
            "overlap": len(pairs), "raw_agreement": agree,
            "kappa": None if k != k else round(k, 4),
            "ci95": [None if lo != lo else round(lo, 4),
                     None if hi != hi else round(hi, 4)],
            "confusion": conf,
            "disagreements": {lay: [{"id": n, a: x, b: y} for n, x, y in rows]
                              for lay, rows in sorted(disagreements.items())},
        }

    # notes still short of a full two-reviewer gate
    singles = [n for n, acts in per_note.items() if len(acts) < 2]
    print()
    print(f"  notes with only ONE reviewer: {len(singles)} / {len(per_note)}"
          " — the assembly gate is complete only when both have voted")
    report["_meta"]["single_reviewer_notes"] = len(singles)

    if args.write:
        OUT.parent.mkdir(parents=True, exist_ok=True)
        OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2),
                       encoding="utf-8")
        print(f"  wrote {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
