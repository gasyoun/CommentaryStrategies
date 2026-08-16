"""Apply the H2833 Grintser style pass to data/lexical/ch1.json.

Reads data/lexical/ch1.grintser_pass_patch.json (key 'shloka|lemma_iast' →
new note_ru), rewrites the matching cards' note_ru in place, and writes a
before/after ledger to data/lexical/ch1.grintser_pass.audit.json. Cards with
judge verdict reject/park are never patched. Idempotent.

Run: python scripts/apply_grintser_pass_ch1.py
"""

import json
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

SRC = "data/lexical/ch1.json"
PATCH = "data/lexical/style_pass_h2833/ch1_patch.json"
AUDIT = "data/lexical/style_pass_h2833/ch1_audit.json"


def main():
    with open(SRC, encoding="utf-8") as f:
        cards = json.load(f)
    with open(PATCH, encoding="utf-8") as f:
        patch = json.load(f)["patches"]

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
        c["style_pass"] = "grintser-H2833"
        applied += 1

    missing = set(patch) - seen
    if missing:
        print("ERROR: patch keys with no matching card:", sorted(missing))
        sys.exit(1)

    for c in cards:
        if "_meta" in c:
            c["_meta"]["style_pass"] = (
                "grintser-H2833 (16-08-2026): note_ru приведены к конвенциям "
                "docs/LEXICAL_NOTE_STYLE_GRINTSER_2026.md; до/после — "
                "ch1.grintser_pass.audit.json"
            )
            break

    with open(SRC, "w", encoding="utf-8") as f:
        json.dump(cards, f, ensure_ascii=False, indent=1)
        f.write("\n")
    if ledger:
        with open(AUDIT, "w", encoding="utf-8") as f:
            json.dump(ledger, f, ensure_ascii=False, indent=1)
            f.write("\n")
    print(f"applied={applied} unchanged={unchanged} skipped(reject/park)={skipped_verdict}")


if __name__ == "__main__":
    main()
