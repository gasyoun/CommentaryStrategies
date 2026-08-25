"""Apply a Grintser style pass (H2833 conventions) to data/lexical/chN.json.

Generalisation of scripts/apply_grintser_pass_ch1.py (H2833, sarga 1 only).
Reads data/lexical/style_pass_<handoff>/chN_patch.json (key 'shloka|lemma_iast'
-> new note_ru), rewrites the matching cards' note_ru in place, and writes a
before/after ledger to data/lexical/style_pass_<handoff>/chN_audit.json.
Cards with judge verdict reject/park are never patched. Lemma / shloka fields
are never touched (the multiset of (shloka, lemma_iast) is asserted equal
before and after). Idempotent.

Run: python scripts/apply_grintser_pass.py --chapter 2 --handoff h3492
"""

import argparse
import json
import sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--chapter", type=int, required=True)
    ap.add_argument("--handoff", default="h3492")
    ap.add_argument("--date", default="25-08-2026")
    args = ap.parse_args()
    hid = args.handoff.lower()
    src = f"data/lexical/ch{args.chapter}.json"
    patch_path = f"data/lexical/style_pass_{hid}/ch{args.chapter}_patch.json"
    audit_path = f"data/lexical/style_pass_{hid}/ch{args.chapter}_audit.json"

    with open(src, encoding="utf-8") as f:
        cards = json.load(f)
    with open(patch_path, encoding="utf-8") as f:
        patch = json.load(f)["patches"]

    before_ids = Counter((c.get("shloka"), c.get("lemma_iast")) for c in cards if "_meta" not in c)

    ledger = []
    applied = skipped_verdict = unchanged = 0
    seen = set()
    for c in cards:
        if "_meta" in c:
            continue
        key = f"{c['shloka']}|{c['lemma_iast']}"
        if key not in patch:
            continue
        seen.add(key)
        verdict = (c.get("judge") or {}).get("verdict", "keep")
        if verdict in ("reject", "park"):
            skipped_verdict += 1
            continue
        new = patch[key]
        if c["note_ru"] == new:
            unchanged += 1
            continue
        ledger.append({"shloka": c["shloka"], "lemma_iast": c["lemma_iast"],
                       "verdict": verdict, "before": c["note_ru"], "after": new})
        c["note_ru"] = new
        c["style_pass"] = f"grintser-{hid.upper()}"
        applied += 1

    missing = set(patch) - seen
    if missing:
        print("ERROR: patch keys with no matching card:", sorted(missing))
        sys.exit(1)

    after_ids = Counter((c.get("shloka"), c.get("lemma_iast")) for c in cards if "_meta" not in c)
    assert before_ids == after_ids, "lemma/shloka multiset changed — refusing to write"

    for c in cards:
        if "_meta" in c:
            c["_meta"]["style_pass"] = (
                f"grintser-{hid.upper()} ({args.date}): note_ru приведены к конвенциям "
                "docs/LEXICAL_NOTE_STYLE_GRINTSER_2026.md; до/после — "
                f"style_pass_{hid}/ch{args.chapter}_audit.json"
            )
            break

    with open(src, "w", encoding="utf-8", newline="\n") as f:
        json.dump(cards, f, ensure_ascii=False, indent=2)
        f.write("\n")
    if ledger:
        with open(audit_path, "w", encoding="utf-8", newline="\n") as f:
            json.dump(ledger, f, ensure_ascii=False, indent=2)
            f.write("\n")
    print(f"ch{args.chapter}: applied={applied} unchanged={unchanged} skipped(reject/park)={skipped_verdict}")


if __name__ == "__main__":
    main()
