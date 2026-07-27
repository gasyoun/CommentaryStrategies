#!/usr/bin/env python3
"""H1685 step 7 — turn gate-cleared verdicts into decisions.json for the apply path.

Emits one decisions file per Phase-2 batch in exactly the shape
apply_phase2_decisions.py already consumes — `reviewer_decisions` keyed by
verse_id — plus a `gated_by` naming the AGENT that cast them, so the permanent
gate stamp cannot be mistaken for the human reviewer's.

Only `accept`, `edit` and `reject` cross over. `park` and `flag_anchor` are
deliberately omitted: a parked note keeps review_required, and a flagged anchor
must be repaired before anything is grafted (the apply script hard-errors on it,
which is the correct behaviour and is not bypassed here).

THE GATE IS ENFORCED HERE. Without --strata-open, this script writes nothing and
says so: verdicts may only be exported for strata whose measured Wilson lower
bound cleared the bar in spotcheck_precision.json. Passing --force-ungated is
possible but stamps `ungated: true` into the file and prints a warning, because
an unmeasured bulk apply is precisely the false-passing gate this pipeline
exists to avoid.

Usage:
  python scripts/h1685_export_decisions.py                     # reports, writes nothing
  python scripts/h1685_export_decisions.py --from-precision    # uses the measured gate
"""
import sys
import os
import json
import argparse
from collections import Counter, defaultdict

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
AD = os.path.join(REPO, "data", "analysis", "h1685_adjudication")
PRECISION = os.path.join(AD, "spotcheck_precision.json")

ADJUDICATOR = "Opus 5 1M (claude-opus-5[1m])"
GATED_BY = f"агент-адъюдикатор {ADJUDICATOR}, H1685 (ruling В2), Wilson-gated"
APPLYABLE = {"accept", "edit", "reject"}
# which stratum each ledger row belongs to — same predicates as the sheet
def stratum_of(r):
    if r.get("rule_id") == "FN-ABS-OK":
        return "A"
    if r.get("rule_id") == "FN-VAR-OK":
        return "B"
    if r.get("rule_id") == "NOTE-KEEP-CLEAN":
        return "C"
    if r.get("rule_id") == "FN-VAR-NULL":
        return "I"
    return {"accept": "D", "reject": "E", "edit": "F",
            "park": "G", "flag_anchor": "H"}.get(r["verdict"], "?")


def load(p):
    with open(p, encoding="utf-8") as fh:
        return json.load(fh)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--from-precision", action="store_true",
                    help="read the open strata from spotcheck_precision.json")
    ap.add_argument("--force-ungated", action="store_true")
    ap.add_argument("--date", default="")
    args = ap.parse_args()

    ledger = load(os.path.join(AD, "ledger_final.json"))["verdicts"]

    open_strata = set()
    if args.from_precision:
        if not os.path.exists(PRECISION):
            sys.exit(f"ERROR: {PRECISION} does not exist — the human spot-check "
                     f"has not been scored yet. Build the sheet, collect votes, "
                     f"run h1685_score_spotcheck.py, then re-run this.")
        open_strata = set(load(PRECISION)["_meta"]["strata_open"])
    elif args.force_ungated:
        open_strata = set("ABCDEFGHI")

    by_batch = defaultdict(dict)
    held = Counter()
    for r in ledger:
        if r["queue"] not in ("batch2", "batch3"):
            continue                       # lexical/footnotes have other paths
        if r["verdict"] not in APPLYABLE:
            held[f"{r['verdict']} (не переносится в apply)"] += 1
            continue
        s = stratum_of(r)
        if s not in open_strata:
            held[f"страта {s} закрыта"] += 1
            continue
        d = {"action": r["verdict"]}
        if r["verdict"] == "reject":
            d["reject_reason"] = r["reason"][:400]
        by_batch[r["queue"]][r["key"]] = d

    print(f"ledger: {len(ledger)} карт; открытых страт: "
          f"{sorted(open_strata) if open_strata else 'НЕТ — ворота закрыты'}")
    for k, v in sorted(held.items()):
        print(f"  удержано: {v:>4}  {k}")

    if not open_strata:
        print("\nНИЧЕГО НЕ ЗАПИСАНО. Вердикты существуют и лежат в ledger_final.json,\n"
              "но применение открывается только измеренной точностью адъюдикатора:\n"
              "  1. открыть commentarystrategies-h1685-adjudication-spotcheck_review.html\n"
              "  2. проголосовать 133 карты, скачать h1685_spotcheck_decisions.json\n"
              "  3. python scripts/h1685_score_spotcheck.py <файл> --bar <ставка>\n"
              "  4. python scripts/h1685_export_decisions.py --from-precision\n"
              "  5. python scripts/apply_phase2_decisions.py <decisions> --dry-run")
        return

    for batch, decisions in sorted(by_batch.items()):
        path = os.path.join(AD, f"h1685_{batch}_decisions.json")
        doc = {"sheet_id": f"commentarystrategies-sundarakanda-commentaries_{batch}",
               "handoff": "H1685",
               "reviewed_at": args.date,
               "gated_by": GATED_BY,
               "adjudicator": ADJUDICATOR,
               "ungated": bool(args.force_ungated),
               "reviewer_decisions": decisions}
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(doc, fh, ensure_ascii=False, indent=1)
        print(f"wrote {path}: {len(decisions)} decisions "
              f"{dict(Counter(d['action'] for d in decisions.values()))}")
    if args.force_ungated:
        sys.stderr.write("WARNING: --force-ungated — эти файлы помечены "
                         "ungated:true и НЕ должны применяться к книге\n")


if __name__ == "__main__":
    main()
