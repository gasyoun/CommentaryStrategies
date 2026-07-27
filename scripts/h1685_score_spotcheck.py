#!/usr/bin/env python3
"""H1685 step 6 — score the blind spot-check and open (or refuse) the gate.

Takes the reviewer's h1685_spotcheck_decisions.json, compares each human verdict
with the adjudicator's hidden one, and reports per-stratum precision as a
**Wilson 95 % LOWER BOUND**, never a point estimate. A stratum at 3/3 = 1.000
has a lower bound near 0.44 and has proved nothing; that is the whole reason the
lower bound is the number that gates.

The gate: a stratum whose lower bound clears --bar may have its verdicts applied
under agent provenance. A stratum below the bar is NOT applied — its cards go to
the human in full, and this script prints exactly how many that is.

The bar is NOT this script's to choose. --bar defaults to the 0.80 the sheet was
sized against; the human sets the final figure, and its consequence in cards is
printed either way so the choice is made against a count, not a feeling.

Usage:
  python scripts/h1685_score_spotcheck.py <h1685_spotcheck_decisions.json> [--bar 0.8]
"""
import sys
import os
import json
import math
import argparse
from collections import defaultdict, Counter

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
AD = os.path.join(REPO, "data", "analysis", "h1685_adjudication")
OUT = os.path.join(AD, "spotcheck_precision.json")
Z = 1.96


def load(p):
    with open(p, encoding="utf-8") as fh:
        return json.load(fh)


def wilson_lb(k, n, z=Z):
    """Lower bound of the Wilson score interval — the number that gates."""
    if n == 0:
        return 0.0
    p = k / n
    denom = 1 + z * z / n
    centre = p + z * z / (2 * n)
    margin = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return round(max(0.0, (centre - margin) / denom), 3)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("decisions")
    ap.add_argument("--bar", type=float, default=0.80)
    args = ap.parse_args()

    ledger = {r["card_id"]: r for r in load(os.path.join(AD, "ledger_final.json"))["verdicts"]}
    doc = load(args.decisions)
    votes = doc["reviewer_decisions"]

    per = defaultdict(lambda: {"n": 0, "k": 0, "disagreements": []})
    for cid, v in votes.items():
        row = ledger.get(cid)
        if not row:
            sys.stderr.write(f"WARN: vote on an unknown card {cid}\n")
            continue
        s = v.get("stratum") or "?"
        per[s]["n"] += 1
        if v["action"] == row["verdict"]:
            per[s]["k"] += 1
        else:
            per[s]["disagreements"].append({
                "card_id": cid, "key": row["key"], "queue": row["queue"],
                "adjudicator": row["verdict"], "human": v["action"],
                "human_comment": v.get("comment", ""),
                "adjudicator_reason": row.get("reason", "")[:300]})

    pop = Counter()
    strata_of = {}
    for cid, row in ledger.items():
        pass
    # population per stratum comes from the sheet's own plan
    plan = {p["stratum"]: p for p in doc.get("meta", {}).get("plan", [])}

    print(f"{'str':<4}{'n':>4}{'верно':>7}{'точка':>8}{'Wilson LB':>11}"
          f"{'ворота':>9}{'население':>11}  описание")
    results, passed, blocked_cards = [], [], 0
    for s in sorted(per):
        d = per[s]
        lb = wilson_lb(d["k"], d["n"])
        point = round(d["k"] / d["n"], 3) if d["n"] else 0.0
        ok = lb >= args.bar
        popn = plan.get(s, {}).get("population", 0)
        if ok:
            passed.append(s)
        else:
            blocked_cards += popn
        print(f"{s:<4}{d['n']:>4}{d['k']:>7}{point:>8}{lb:>11}"
              f"{'ОТКРЫТЫ' if ok else 'ЗАКРЫТЫ':>9}{popn:>11}  "
              f"{plan.get(s, {}).get('title', '')[:38]}")
        results.append({"stratum": s, "n": d["n"], "correct": d["k"],
                        "point_estimate": point, "wilson_lower_bound": lb,
                        "population": popn, "gate_open": ok,
                        "disagreements": d["disagreements"]})

    total_n = sum(d["n"] for d in per.values())
    total_k = sum(d["k"] for d in per.values())
    agg_lb = wilson_lb(total_k, total_n)
    print(f"\nсовокупно: {total_k}/{total_n}, Wilson LB {agg_lb} — "
          f"НЕ основание для переноса на слабую страту (публикуется только "
          f"вместе с постратными)")
    print(f"страт открыто: {len(passed)}/{len(results)}; "
          f"карт остаётся человеку из закрытых страт: {blocked_cards}")

    dis = [d for r in results for d in r["disagreements"]]
    if dis:
        print(f"\nрасхождений: {len(dis)}")
        for d in dis[:15]:
            print(f"  {d['queue']:<10} {d['key']:<28} адъюдикатор={d['adjudicator']:<12}"
                  f" человек={d['human']:<12} {d['human_comment'][:60]}")

    out = {"_meta": {"handoff": "H1685", "bar": args.bar, "z": Z,
                     "generated_by": "scripts/h1685_score_spotcheck.py",
                     "reviewed_at": doc.get("reviewed_at"),
                     "aggregate": {"n": total_n, "correct": total_k,
                                   "wilson_lower_bound": agg_lb},
                     "strata_open": passed,
                     "cards_left_to_human": blocked_cards},
           "strata": results}
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
    print(f"\nwrote {OUT}")


if __name__ == "__main__":
    main()
