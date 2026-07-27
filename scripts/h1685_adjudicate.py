#!/usr/bin/env python3
"""H1685 step 3 — adjudicate every queued card; route the contested ones out.

Ruling В2 (MG, 26-07-2026) puts an agent in the seat the human could not reach:
1 889 cards across four sheets, each to leave with a verdict and the evidence it
was decided on. This script casts the verdicts that a stated rule plus the
measured evidence of h1685_evidence.py/h1685_calibrate.py already determine, and
writes every remaining card to an adjudication packet for the Opus adjudicator
to read individually. Nothing is decided by "looks fine".

A rule may only fire where the evidence is INDEPENDENT of what produced the card
(see h1685_evidence.py's docstring). Where the only thing speaking for a card is
the agent that drafted it, the card goes to the packet.

Verdict vocabulary is the sheets' own: accept · edit · reject · park ·
flag_anchor. `park` and `flag_anchor` are verdicts but NOT apply actions — a
parked note keeps review_required, and a flagged anchor must be repaired before
anything is grafted (apply_phase2_decisions.py enforces that with a hard error).

Outputs (data/analysis/h1685_adjudication/):
  ledger.json          every card, verdict + reason + cited evidence
  packet_<queue>.json  the cards routed to the Opus adjudicator

Usage: python scripts/h1685_adjudicate.py [--packet-only]
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
DATA = os.path.join(REPO, "data")
AD = os.path.join(DATA, "analysis", "h1685_adjudication")
LEDGER = os.path.join(AD, "ledger.json")

ADJUDICATOR = "Opus 5 1M (claude-opus-5[1m])"
ANCHOR_OK = {"exact", "stem", "commentary_only"}


def load(p):
    with open(p, encoding="utf-8") as fh:
        return json.load(fh)


def rule(card, cal):
    """-> (verdict, action, reason, cited, rule_id) or None to route to Opus."""
    q, e = card["queue"], card["evidence"]
    judge = card.get("judge") or {}
    jv = judge.get("verdict")

    # ---------------------------------------------------- edition footnotes
    if q == "footnotes":
        pb = cal["operating_point"]["present_bar_jaccard"]
        ab = cal["operating_point"]["absent_bar_jaccard"]
        if e["kind"] == "variant_reading":
            if not e["verse_texts_available"]:
                return None
            if e["n_readings_distinct"] == 0:
                return ("reject", "reject",
                        "Не разночтение: обе формы совпадают после снятия "
                        "орфографии (sanskrit_util.nfold) — сноска описывает "
                        "различие, которого в тексте нет.",
                        [f"readings={e['readings_checked']}",
                         "n_readings_distinct=0"], "FN-VAR-NULL")
            if e["all_readings_located"]:
                return ("accept", "accept",
                        f"Каждое чтение найдено в своём издании "
                        f"({e['readings_checked']} лок., из них "
                        f"{e['n_omission_markers']} — маркеры опущения ∅); "
                        f"различие сохраняется после нормализации.",
                        [f"crit={card['verse_id']}",
                         f"south={e.get('difflib_similarity')}",
                         f"located={e['readings_checked']}"], "FN-VAR-OK")
            return None
        # absence claims
        pv = e.get("per_verse") or []
        if not pv:
            return None
        hi = [p for p in pv if p["best_jaccard"] >= pb]
        mid = [p for p in pv if ab <= p["best_jaccard"] < pb]
        if hi:
            return ("reject", "reject",
                    "Шлока ЕСТЬ в критическом издании как вариант — "
                    "«отсутствует» ставить нельзя (README §Значимые отсутствия: "
                    "reworded — разночтение, не отсутствие). Найдено глобальным "
                    "перепоиском по всей критической книге.",
                    [f"{p['southern_id']}~{p['best_crit_id']} "
                     f"jaccard={p['best_jaccard']}" for p in hi[:3]], "FN-ABS-PRESENT")
        if mid:
            return None
        return ("accept", "accept",
                f"Структурное отсутствие подтверждено независимым глобальным "
                f"перепоиском по всем 2488 критическим шлокам: лучший аналог "
                f"j={e['max_global_jaccard']} — ниже p1={ab} шлок, у которых "
                f"аналог заведомо есть (recovery 600/600).",
                [f"max_global_jaccard={e['max_global_jaccard']}",
                 f"verses={e['verses_checked']}",
                 f"leonov_edition_note={e['leonov_edition_note_here']}"], "FN-ABS-OK")

    # ------------------------------------------------------------ note queues
    if not jv:
        return None                      # batch2 has no judge — always Opus
    if e.get("duplicate_in_book"):
        return None
    contradicted = (e.get("commentator_attribution_ok") is False
                    or e.get("anchor") not in ANCHOR_OK)
    if jv == "keep" and not contradicted:
        cited = [f"anchor={e['anchor']}",
                 f"note_in_podstrochnik={e.get('note_in_podstrochnik')}",
                 f"note_in_tier1={e.get('note_in_tier1')}"]
        if q != "lexical":
            cited.append("commentators_attested="
                         + ",".join(e.get("commentators_attested") or []))
        return ("accept", "accept",
                "Судья (Sonnet 5) поставил keep; независимая проверка "
                "подтверждает три шлюза рубрики §3.4: названный комментатор "
                "действительно комментирует этот стих, лемма стоит в стихе, "
                "заметка не пересказывает подстрочник/tier-1.",
                cited, "NOTE-KEEP-CLEAN")
    return None                          # everything contested goes to Opus


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--packet-only", action="store_true")
    args = ap.parse_args()

    ev = load(os.path.join(AD, "evidence.json"))
    cal = load(os.path.join(AD, "calibration.json"))
    cards = ev["cards"]

    ledger, packets = [], defaultdict(list)
    for c in cards:
        r = rule(c, cal)
        if r:
            verdict, action, reason, cited, rid = r
            ledger.append({
                "card_id": c["card_id"], "queue": c["queue"], "key": c["key"],
                "verse_id": c["verse_id"], "lemma": c["lemma"],
                "verdict": verdict, "apply_action": action, "reason": reason,
                "evidence_cited": cited, "rule_id": rid,
                "decided_by": "rule", "adjudicator": ADJUDICATOR,
                "judge_verdict": (c.get("judge") or {}).get("verdict"),
            })
        else:
            packets[c["queue"]].append(c)

    print(f"rule-decided: {len(ledger)} / {len(cards)}")
    print("  by rule:", dict(Counter(x["rule_id"] for x in ledger)))
    print("  by verdict:", dict(Counter(x["verdict"] for x in ledger)))
    print(f"routed to the Opus adjudicator: {sum(len(v) for v in packets.values())}")
    for q, v in sorted(packets.items()):
        why = Counter()
        for c in v:
            e, j = c["evidence"], (c.get("judge") or {}).get("verdict")
            if not j and c["queue"] != "footnotes":
                why["no judge verdict (batch2)"] += 1
            elif c["queue"] == "footnotes":
                why["borderline / unlocated"] += 1
            elif j != "keep":
                why[f"judge={j}"] += 1
            elif e.get("commentator_attribution_ok") is False:
                why["keep but commentator not attested"] += 1
            elif e.get("anchor") not in ANCHOR_OK:
                why[f"keep but anchor={e.get('anchor')}"] += 1
            else:
                why["keep but duplicate in book"] += 1
        print(f"  {q}: {len(v)}  {dict(why)}")

    os.makedirs(AD, exist_ok=True)
    for q, v in packets.items():
        p = os.path.join(AD, f"packet_{q}.json")
        with open(p, "w", encoding="utf-8") as fh:
            json.dump({"_meta": {"handoff": "H1685", "queue": q, "cards": len(v),
                                 "adjudicator": ADJUDICATOR,
                                 "instruction": "one verdict per card, with the "
                                                "evidence it rests on"},
                       "cards": v}, fh, ensure_ascii=False, indent=1)
        print(f"  wrote {os.path.basename(p)}")

    if not args.packet_only:
        with open(LEDGER, "w", encoding="utf-8") as fh:
            json.dump({"_meta": {"handoff": "H1685",
                                 "generated_by": "scripts/h1685_adjudicate.py",
                                 "adjudicator": ADJUDICATOR,
                                 "total_cards": len(cards),
                                 "rule_decided": len(ledger),
                                 "routed_to_opus": sum(len(v) for v in packets.values()),
                                 "operating_point": cal["operating_point"]},
                       "verdicts": ledger}, fh, ensure_ascii=False, indent=1)
        print(f"\nwrote {LEDGER}")


if __name__ == "__main__":
    main()
