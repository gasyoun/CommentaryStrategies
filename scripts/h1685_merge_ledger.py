#!/usr/bin/env python3
"""H1685 step 4 — merge the rule tier and the Opus tier into one ledger.

Produces ledger_final.json: one row per queued card, 1 889 of them, each with a
verdict, who cast it, and the evidence it rests on. This is the file the
Definition of Done is measured against — «934/934 agent verdicts» in the
handoff, 1 889/1 889 as the sheets actually stand (see the count correction in
the report).

Fails loudly on any card that ends up with zero verdicts or two.

Inputs. `ledger.json` (the rule tier) and `packet_*.json` are step-3 outputs of
scripts/h1685_adjudicate.py and are deliberately NOT committed — .gitignore
lines 30-31 exclude both. They have therefore never existed in this repo's
history (H4370 checked `git log --all --diff-filter=A`: the only ledger.json
ever committed under that path is H4368's test fixture). Nothing was lost; the
step-3 intermediate is simply regenerated rather than stored, and the surviving
record of the rule tier is ledger_final.json itself, whose 1 649 `tier: "rule"`
rows carry their rule_id, reason and cited evidence. So a fresh checkout must
re-run step 3 before this step, and the absence of ledger.json is an explicit
refusal below, not a FileNotFoundError traceback.

Usage: python scripts/h1685_adjudicate.py  &&  python scripts/h1685_merge_ledger.py
"""
import sys
import os
import json
from collections import Counter, defaultdict

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
AD = os.path.join(REPO, "data", "analysis", "h1685_adjudication")
OUT = os.path.join(AD, "ledger_final.json")

ADJUDICATOR = "Opus 5 1M (claude-opus-5[1m])"
# verdict -> what apply_phase2_decisions.py is allowed to do with it
APPLY_ACTION = {"accept": "accept", "edit": "edit", "reject": "reject",
                "park": None, "flag_anchor": None}


def load(p):
    with open(p, encoding="utf-8") as fh:
        return json.load(fh)


def main():
    ev = load(os.path.join(AD, "evidence.json"))
    cards = {c["card_id"]: c for c in ev["cards"]}

    rule_path = os.path.join(AD, "ledger.json")
    if not os.path.exists(rule_path):
        sys.exit(
            f"ERROR: missing {rule_path}\n"
            "       The rule tier is a step-3 intermediate, gitignored by "
            "design (.gitignore lines 30-31) and never committed, so a fresh\n"
            "       checkout does not have it. Regenerate it first:\n"
            "           python scripts/h1685_adjudicate.py\n"
            "       The already-merged rule-tier verdicts survive in "
            "ledger_final.json as the rows with tier == \"rule\"; do not "
            "reconstruct them by hand.")
    rule = load(rule_path)["verdicts"]

    rows = {}
    for r in rule:
        rows[r["card_id"]] = {**r, "tier": "rule"}

    # ---- Opus tier: keyed per queue by the packet's own `key` field ----
    opus_files = {q: os.path.join(AD, f"opus_verdicts_{q}.json")
                  for q in ("batch2", "batch3", "lexical", "footnotes")}
    by_queue_key = defaultdict(dict)
    for cid, c in cards.items():
        by_queue_key[c["queue"]][c["key"]] = cid

    dupes, orphans = [], []
    for q, path in opus_files.items():
        if not os.path.exists(path):
            sys.exit(f"ERROR: missing {path}")
        for v in load(path)["verdicts"]:
            cid = by_queue_key[q].get(v["key"])
            if not cid:
                orphans.append((q, v["key"]))
                continue
            if cid in rows:
                dupes.append(cid)
                continue
            c = cards[cid]
            rows[cid] = {
                "card_id": cid, "queue": q, "key": v["key"],
                "verse_id": c["verse_id"], "lemma": c["lemma"],
                "verdict": v["verdict"],
                "apply_action": APPLY_ACTION[v["verdict"]],
                "reason": v.get("reason", ""),
                "evidence_cited": (v.get("evidence_cited") if isinstance(
                    v.get("evidence_cited"), list) else [v.get("evidence_cited", "")]),
                "rule_id": None,
                "decided_by": "opus",
                "adjudicator": ADJUDICATOR,
                "judge_verdict": v.get("judge_verdict") or (c.get("judge") or {}).get("verdict"),
                "disposition": v.get("disposition"),
                "tier": "opus",
            }

    if orphans:
        sys.exit(f"ERROR: {len(orphans)} Opus verdicts match no card: {orphans[:5]}")
    if dupes:
        sys.exit(f"ERROR: {len(dupes)} cards decided twice: {dupes[:5]}")
    missing = sorted(set(cards) - set(rows))
    if missing:
        sys.exit(f"ERROR: {len(missing)} cards with NO verdict: {missing[:5]}")

    ledger = [rows[cid] for cid in cards]
    by_queue = defaultdict(Counter)
    for r in ledger:
        by_queue[r["queue"]][r["verdict"]] += 1

    overturned = [r for r in ledger if r.get("disposition") == "OVERTURNED"]
    judged = [r for r in ledger if r.get("judge_verdict")]
    agree = sum(1 for r in judged
                if (r["judge_verdict"] == "keep" and r["verdict"] == "accept")
                or r["judge_verdict"] == r["verdict"])

    doc = {
        "_meta": {
            "handoff": "H1685",
            "generated_by": "scripts/h1685_merge_ledger.py",
            "adjudicator": ADJUDICATOR,
            "total_cards": len(ledger),
            "by_tier": dict(Counter(r["tier"] for r in ledger)),
            "by_verdict": dict(Counter(r["verdict"] for r in ledger)),
            "by_queue": {q: dict(c) for q, c in by_queue.items()},
            "cards_with_a_prior_judge_verdict": len(judged),
            "adjudicator_agrees_with_judge": agree,
            "adjudicator_overturns": len(overturned),
            "overturned_cards": [
                {"card_id": r["card_id"], "judge": r["judge_verdict"],
                 "adjudicator": r["verdict"]} for r in overturned],
        },
        "verdicts": ledger,
    }
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, ensure_ascii=False, indent=1)

    print(f"wrote {OUT}")
    print(f"cards: {len(ledger)}  tiers: {doc['_meta']['by_tier']}")
    print(f"verdicts: {doc['_meta']['by_verdict']}")
    for q, c in sorted(by_queue.items()):
        print(f"  {q:<10} {dict(c)}")
    print(f"\nof {len(judged)} cards that already had a Sonnet judge verdict, "
          f"the adjudicator agreed with {agree} and overturned {len(overturned)}")


if __name__ == "__main__":
    main()
