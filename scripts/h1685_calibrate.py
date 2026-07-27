#!/usr/bin/env python3
"""H1685 step 2 — calibrate the absence discriminator on labelled pairs.

The footnote queue asks a human to ratify 174 «отсутствует в критическом
издании (Барода)» claims. h1685_evidence.py re-searches the WHOLE critical book
for each claimed-absent southern shloka; this script decides what score is
allowed to count as "found", instead of inventing a threshold.

Two measurements, both on data whose answer is already known:

1. RECOVERY — for southern shlokas the concordance maps to a critical shloka
   (`identical` 1065 + `variant` 1021), does the global searcher return THAT
   critical id? If it cannot re-find known counterparts it has no standing to
   pronounce on absences, and this whole line of evidence is void.

2. SEPARATION — the distribution of best-global-Jaccard for those known-present
   shlokas versus for the claimed absences. The operating point is read off the
   positives' lower tail: a claimed absence scoring where genuine counterparts
   score is not an absence, it is an alignment artifact — precisely the failure
   data/edition_comparison/README.md § Оговорки predicts ("глобальное LCS-
   выравнивание оставляет несопоставленными шлоки, у которых в южном есть
   вариантный аналог") and marks as not yet addressed.

Writes data/analysis/h1685_adjudication/calibration.json.

Usage: python scripts/h1685_calibrate.py [--sample N]
"""
import sys
import os
import re
import json
import time
import random
import argparse
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
DATA = os.path.join(REPO, "data")
OUTDIR = os.path.join(DATA, "analysis", "h1685_adjudication")
OUT = os.path.join(OUTDIR, "calibration.json")
SEED = 1685

sys.path.insert(0, HERE)
from h1685_evidence import build_global_matcher, load  # noqa: E402
from compare_editions import load_critical, load_southern  # noqa: E402


def pct(sorted_vals, p):
    if not sorted_vals:
        return 0.0
    i = min(len(sorted_vals) - 1, max(0, int(round(p / 100 * (len(sorted_vals) - 1)))))
    return round(sorted_vals[i], 3)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sample", type=int, default=600,
                    help="labelled positives to test (0 = all)")
    args = ap.parse_args()
    t0 = time.time()
    os.makedirs(OUTDIR, exist_ok=True)

    crit = load_critical()
    south = load_southern()
    south_by_id = {f"5.{s}.{v}": t for s, v, t in south}
    best_match = build_global_matcher(crit)

    conc = load(os.path.join(DATA, "edition_comparison", "concordance.json"))["concordance"]
    positives = [r for r in conc if r["status"] in ("identical", "variant")
                 and r.get("southern") in south_by_id]
    rng = random.Random(SEED)
    sample = positives if not args.sample or args.sample >= len(positives) \
        else rng.sample(positives, args.sample)
    print(f"labelled positives: {len(positives)} | testing {len(sample)} (seed {SEED})")

    recovered, jac_pos, by_status = 0, [], Counter()
    misses = []
    for r in sample:
        sid, expect = r["southern"], r["critical"]
        got, jac, dl, top3 = best_match(south_by_id[sid])
        jac_pos.append(jac)
        hit = (got == expect) or any(t["crit_id"] == expect for t in top3)
        recovered += bool(hit)
        by_status[(r["status"], "hit" if hit else "miss")] += 1
        if not hit and len(misses) < 15:
            misses.append({"southern": sid, "expected_crit": expect,
                           "got": got, "jaccard": jac, "top3": top3})
    rec_rate = recovered / len(sample) if sample else 0.0
    jac_pos.sort()

    ev = load(os.path.join(OUTDIR, "evidence.json"))
    abs_cards = [c for c in ev["cards"] if c["queue"] == "footnotes"
                 and c["evidence"]["kind"] != "variant_reading"]
    jac_claim = sorted(p["best_jaccard"] for c in abs_cards
                       for p in c["evidence"]["per_verse"])

    print(f"\n1. RECOVERY  known counterpart re-found in top-3: "
          f"{recovered}/{len(sample)} = {rec_rate:.1%}")
    for (st, res), n in sorted(by_status.items()):
        print(f"     {st:<10} {res:<5} {n}")
    print(f"\n2. SEPARATION  best-global-Jaccard percentiles")
    print(f"     {'':<22}{'p1':>7}{'p5':>7}{'p10':>7}{'p25':>7}{'p50':>7}{'p75':>7}{'p90':>7}")
    print(f"     {'known-present (n=' + str(len(jac_pos)) + ')':<22}"
          + "".join(f"{pct(jac_pos, p):>7}" for p in (1, 5, 10, 25, 50, 75, 90)))
    print(f"     {'claimed-absent (n=' + str(len(jac_claim)) + ')':<22}"
          + "".join(f"{pct(jac_claim, p):>7}" for p in (1, 5, 10, 25, 50, 75, 90)))

    present_bar = pct(jac_pos, 5)     # a real counterpart scores at least this
    absent_bar = pct(jac_pos, 1)
    n_above = sum(1 for j in jac_claim if j >= present_bar)
    n_mid = sum(1 for j in jac_claim if absent_bar <= j < present_bar)
    n_below = sum(1 for j in jac_claim if j < absent_bar)
    print(f"\n   operating point: PRESENT if >= p5 of positives = {present_bar}; "
          f"ABSENT if < p1 = {absent_bar}")
    print(f"   claimed-absent verses: present {n_above} | borderline {n_mid} | "
          f"absent {n_below}  (of {len(jac_claim)})")

    if misses:
        print("\n   recovery misses (searcher failed to re-find a known pair):")
        for m in misses[:8]:
            print(f"     {m['southern']} -> expected {m['expected_crit']}, "
                  f"got {m['got']} (jac {m['jaccard']})")

    doc = {
        "_meta": {
            "handoff": "H1685",
            "generated_by": "scripts/h1685_calibrate.py",
            "seed": SEED,
            "runtime_s": round(time.time() - t0, 1),
        },
        "recovery": {
            "labelled_positives_total": len(positives),
            "tested": len(sample),
            "recovered_top3": recovered,
            "recovery_rate": round(rec_rate, 4),
            "by_status": {f"{k[0]}_{k[1]}": v for k, v in by_status.items()},
            "misses_sample": misses,
            "interpretation": ("if this is low the global searcher cannot re-find "
                               "counterparts it is known to have, and no absence "
                               "verdict may rest on it"),
        },
        "separation": {
            "known_present_percentiles": {f"p{p}": pct(jac_pos, p)
                                          for p in (1, 5, 10, 25, 50, 75, 90)},
            "claimed_absent_percentiles": {f"p{p}": pct(jac_claim, p)
                                           for p in (1, 5, 10, 25, 50, 75, 90)},
            "n_known_present": len(jac_pos),
            "n_claimed_absent_verses": len(jac_claim),
        },
        "operating_point": {
            "present_bar_jaccard": present_bar,
            "absent_bar_jaccard": absent_bar,
            "basis": "p5 / p1 of the best-global-Jaccard of shlokas the "
                     "concordance already maps to a critical counterpart",
            "claimed_absent_present": n_above,
            "claimed_absent_borderline": n_mid,
            "claimed_absent_absent": n_below,
        },
    }
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, ensure_ascii=False, indent=1)
    print(f"\nwrote {OUT} ({doc['_meta']['runtime_s']}s)")


if __name__ == "__main__":
    main()
