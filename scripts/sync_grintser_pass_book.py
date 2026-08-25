"""Sync a Grintser style pass into one sarga's slice of the book aggregate.

Generalisation of scripts/sync_grintser_pass_book_s1.py (H2833, sarga 1 only).
data/sundara_commentary_to_add.json carries copies of the data/lexical/chN.json
cards, and build_sarga_apparatus.py prefers them over chN.json in its dedup —
so a pass applied to chN.json alone never reaches data/apparatus/ or the print
master. This script lands the same chN_patch.json texts on the aggregate twins:
subtype=lexical entries of sarga N whose 'shloka|lemma_iast' has a patch get the
new note_ru (+ style_pass marker). reject/park twins are never touched.
Ledger: data/lexical/style_pass_<handoff>/book_sN_audit.json. Idempotent.

Run: python scripts/sync_grintser_pass_book.py --chapter 2 --handoff h3492
"""

import argparse
import json
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

BOOK = "data/sundara_commentary_to_add.json"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--chapter", type=int, required=True)
    ap.add_argument("--handoff", default="h3492")
    args = ap.parse_args()
    hid = args.handoff.lower()
    patch_path = f"data/lexical/style_pass_{hid}/ch{args.chapter}_patch.json"
    audit_path = f"data/lexical/style_pass_{hid}/book_s{args.chapter}_audit.json"

    with open(BOOK, encoding="utf-8") as f:
        book = json.load(f)
    notes = book["notes"] if isinstance(book, dict) and "notes" in book else book
    with open(patch_path, encoding="utf-8") as f:
        patch = json.load(f)["patches"]

    sarga_re = re.compile(rf"^V\.{args.chapter}\.\d")
    ledger = []
    synced = unchanged = skipped = 0
    for n in notes:
        if not isinstance(n, dict) or "_meta" in n:
            continue
        if n.get("subtype") != "lexical" or not sarga_re.match(str(n.get("shloka", ""))):
            continue
        key = f"{n.get('shloka')}|{n.get('lemma_iast')}"
        if key not in patch:
            continue
        verdict = (n.get("judge") or {}).get("verdict", "keep")
        if verdict in ("reject", "park"):
            skipped += 1
            continue
        before = n.get("note_ru") or ""
        after = patch[key]
        if before == after:
            unchanged += 1
            continue
        ledger.append({"shloka": n.get("shloka"), "lemma_iast": n.get("lemma_iast"),
                       "verdict": verdict, "before": before, "after": after})
        n["note_ru"] = after
        n["style_pass"] = f"grintser-{hid.upper()}"
        synced += 1

    with open(BOOK, "w", encoding="utf-8", newline="\n") as f:
        json.dump(book, f, ensure_ascii=False, indent=1)
        f.write("\n")
    if ledger:
        with open(audit_path, "w", encoding="utf-8", newline="\n") as f:
            json.dump(ledger, f, ensure_ascii=False, indent=1)
            f.write("\n")
    print(f"book sarga {args.chapter}: synced={synced} unchanged={unchanged} skipped(reject/park)={skipped}")


if __name__ == "__main__":
    main()
