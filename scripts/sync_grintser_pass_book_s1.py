"""Sync the H2833 Grintser style pass into the sarga-1 slice of the book aggregate.

data/sundara_commentary_to_add.json carries copies of the ch1 lexical cards
(and build_sarga_apparatus.py prefers them over data/lexical/ch1.json in its
dedup), so the pass must land here too:

1. subtype=lexical sarga-1 entries whose (shloka, lemma_iast) has a patch in
   data/lexical/style_pass_h2833/ch1_patch.json get the new note_ru;
2. two aggregate-only lexical entries (parivesa, tṛtīya) get their own
   convention texts (EXTRA below);
3. six phantom/mis-aimed «см. примеч. к <ref> (Гринцер…)» tails in base notes
   are dropped — the cited Grintser notes either do not exist in the corpus
   (I.1.16, I.1.1, II.114.3) or discuss a different subject (I.1.8, I.1.25,
   I.1.28); verified against SamudraManthanam comm segments 16-08-2026.

Ledger: data/lexical/style_pass_h2833/book_s1_audit.json. Idempotent.

Run: python scripts/sync_grintser_pass_book_s1.py
"""

import json
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

BOOK = "data/sundara_commentary_to_add.json"
PATCH = "data/lexical/style_pass_h2833/ch1_patch.json"
AUDIT = "data/lexical/style_pass_h2833/book_s1_audit.json"

EXTRA = {
    "V.1.62|parivesa": (
        "Ореол (pariveṣa; в тексте написание parivesa) — световое кольцо "
        "вокруг солнца или луны. Белозубый Хануман, окружённый кольцом "
        "хвоста, «подобен солнцу в ореоле» — точный атмосферный образ: "
        "сияющий диск в светлой кайме."
    ),
    "V.1.172|tṛtīya": (
        "Третье (tṛtīya) — «увидев это третье труднейшее дело Ханумана»: "
        "счёт подвигов — прыжок через океан, отказ от отдыха на Майнаке, "
        "победа над Сурасой хитростью. Число структурирует эпическую серию "
        "испытаний; такое подытоживание перечнем — обычная эпическая техника."
    ),
}

# exact dangling-ref sentences to drop from base notes (verified phantom/mis-aimed)
DROP_REFS = [
    " См. примеч. к I.1.16 (Гринцер; первое вхождение в кн. I–III, уточнить по примеч.).",
    " см. примеч. к I.1.1 (Гринцер).",
    " см. примеч. к I.1.25 (Гринцер).",
    " см. примеч. к I.1.8 (Гринцер).",
    " см. примеч. к I.1.28 (Гринцер).",
]


def main():
    with open(BOOK, encoding="utf-8") as f:
        book = json.load(f)
    notes = book["notes"] if isinstance(book, dict) and "notes" in book else book
    with open(PATCH, encoding="utf-8") as f:
        patch = dict(json.load(f)["patches"])
    patch.update(EXTRA)

    ledger = []
    n_lex = n_base = 0
    for n in notes:
        if not isinstance(n, dict) or "_meta" in n:
            continue
        if not re.match(r"^V\.1\.\d", str(n.get("shloka", ""))):
            continue
        before = n.get("note_ru") or ""
        after = before
        key = f"{n.get('shloka')}|{n.get('lemma_iast')}"
        if n.get("subtype") == "lexical" and key in patch:
            after = patch[key]
        else:
            for ref in DROP_REFS:
                after = after.replace(ref, "")
        if after != before:
            ledger.append({"shloka": n.get("shloka"), "lemma_iast": n.get("lemma_iast"),
                           "subtype": n.get("subtype"), "type": n.get("type"),
                           "before": before, "after": after})
            n["note_ru"] = after
            n["style_pass"] = "grintser-H2833"
            if n.get("subtype") == "lexical":
                n_lex += 1
            else:
                n_base += 1

    with open(BOOK, "w", encoding="utf-8") as f:
        json.dump(book, f, ensure_ascii=False, indent=1)
        f.write("\n")
    if ledger:
        with open(AUDIT, "w", encoding="utf-8") as f:
            json.dump(ledger, f, ensure_ascii=False, indent=1)
            f.write("\n")
    print(f"lexical synced={n_lex} base ref-fixes={n_base}")


if __name__ == "__main__":
    main()
