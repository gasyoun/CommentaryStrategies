#!/usr/bin/env python3
"""Fix the sarga-11 lexical-layer phantom anchors (H276 WS-3b).

Nine lexical notes were authored (hand-curated REGISTRY in lexical_pilot.py,
2026-06-27) against verse ids V.11.x whose actual content is the feast-hall /
seraglio scene of Rāvaṇa's palace — while the notes describe Sītā in the aśoka
grove. Verified against the vulgate corpus (SamudraManthanam) and the GRETIL
critical text: the lemmas do NOT occur in sarga 11; batch-3's sarga-11 drafter
first flagged this (its _meta caveat), and the H276 lexical judge pass
confirmed all nine as flag_anchor.

Resolution (each explicit, none silent):
  RE-ANCHOR (lemma occurs verbatim in a verse whose scene matches the note):
    V.11.9  kṣāma   -> V.17.30  (tāṃ kṣāmāṃ … maithilīm — Sītā emaciated)
    V.11.11 vivarṇa -> V.25.8   (vivarṇavadanābhavat — Sītā pale with fear)
  PARK to data/lexical/ch11.qa_removed.json (phantom anchor, no honest target;
  possible future targets recorded for the human gate):
    V.11.6  mālyahīna, V.11.7 dhūmajvāla (text has dhūma-jāla, 15.20/15.32 — a
    DIFFERENT word), V.11.12 rājīvanetri (text calls Sītā utpalapatrākṣī 13.16;
    rājīvalocana describes Rāma 26.39 — the note's claim is contradicted),
    V.11.16 śokaparipluta, V.11.21 duḥkha, V.11.23 nīlotpala, V.11.35 śokāgni.

Updates: data/lexical/ch11.json (+ch17/ch25 receive the re-anchored notes),
ch11.qa_removed.json, the book aggregate, and sundara_book_stats.json.
Re-anchored notes get judge.scores.anchoring=2 and a re-derived verdict, with
the H276 provenance appended; review_required stays true everywhere.

Run AFTER scripts/lexical_judge_merge.py. Idempotent-guarded: exits if the
phantom notes are already gone. Usage: python scripts/fix_ch11_lexical_anchors.py
"""
import sys
import os
import re
import json
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
DATA = os.path.join(REPO, "data")
LEX = os.path.join(DATA, "lexical")
BOOK = os.path.join(DATA, "sundara_commentary_to_add.json")
STATS = os.path.join(DATA, "sundara_book_stats.json")

REANCHOR = {  # (old shloka, lemma) -> (new shloka, evidence)
    ("V.11.9", "kṣāma"): ("V.17.30",
        "tāṃ kṣāmāṃ suvibhaktāṅgīṃ … maithilīm — лемма стоит в стихе, сцена "
        "(истощённая Сита в ашока-ване) совпадает с содержанием заметки"),
    ("V.11.11", "vivarṇa"): ("V.25.8",
        "rākṣasīnāṃ bhayatrastā vivarṇavadanābhavat — лемма стоит в стихе, "
        "сцена (побледневшая Сита) совпадает с содержанием заметки"),
}
PARK = {  # lemma -> reason (+ possible future target for the human gate)
    "mālyahīna": "лемма не встречается в вульгате Сундараканды; фантомный якорь",
    "dhūmajvāla": "в тексте стоит dhūma-jāla «сеть дыма» (15.20, 15.32), не "
                  "dhūma-jvāla «пламя дыма» — заметку можно вернуть только "
                  "переписав лемму и глоссу под dhūmajāla (гейт человека)",
    "rājīvanetri": "утверждение заметки противоречит тексту: глаза Ситы — "
                   "utpalapatrākṣī (13.16), а rājīvalocana описывает Раму "
                   "(26.39); сама заметка противопоставляет rājīva и utpala",
    "śokaparipluta": "лемма не встречается в вульгате (в 15.32 стоит "
                     "śokajālena); фантомный якорь",
    "duḥkha": "слово частотно, но в V.11.21 его нет; универсальная этимология "
              "духкхи без честной версовой привязки в этой сарге",
    "nīlotpala": "лемма не встречается в вульгате Сундараканды в применении к "
                 "глазам Ситы; фантомный якорь",
    "śokāgni": "лемма не встречается в вульгате Сундараканды; фантомный якорь",
}
PROV = {"fixed_by": "scripts/fix_ch11_lexical_anchors.py", "handoff": "H276",
        "date": "2026-07-07",
        "confirmed_by": "batch-3 sarga-11 drafter caveat + lexical judge pass "
                        "(flag_anchor) + corpus/GRETIL lemma search"}


def load(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def dump(path, obj):
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(obj, fh, ensure_ascii=False, indent=2)


def rederive_verdict(scores):
    if scores.get("faithfulness", 0) < 2:
        return "reject"
    if scores.get("anchoring", 0) == 0:
        return "flag_anchor"
    if scores.get("non_triviality", 0) < 1:
        return "park"
    if scores.get("lexical_value", 0) == 0 and scores.get("non_triviality", 0) < 2:
        return "park"
    if scores.get("register", 0) < 2:
        return "edit"
    return "keep"


def main():
    ch11 = load(os.path.join(LEX, "ch11.json"))
    lemmas = {n.get("lemma_iast") for n in ch11 if "_meta" not in n}
    targets = set(PARK) | {lem for _, lem in REANCHOR}
    if not (targets & lemmas):
        sys.exit("Nothing to do: phantom notes already resolved (idempotent guard).")

    parked, moved = [], []
    keep_ch11 = [ch11[0]]
    for n in ch11[1:]:
        lem = n.get("lemma_iast")
        key = (n.get("shloka"), lem)
        if key in REANCHOR:
            new_shloka, evidence = REANCHOR[key]
            n["reanchored"] = {**PROV, "from": key[0], "to": new_shloka,
                               "evidence": evidence}
            n["shloka"] = new_shloka
            if isinstance(n.get("judge"), dict):
                n["judge"]["scores"]["anchoring"] = 2
                n["judge"]["verdict"] = rederive_verdict(n["judge"]["scores"])
                n["judge"]["reason"] += (" | H276 WS-3b: переякорено "
                                         f"{key[0]}→{new_shloka}; {evidence}")
            moved.append(n)
        elif lem in PARK:
            n["qa_removed"] = {**PROV, "reason": PARK[lem],
                               "original_shloka": n.get("shloka")}
            parked.append(n)
        else:
            keep_ch11.append(n)
    keep_ch11[0]["_meta"]["notes_count"] = len(keep_ch11) - 1
    keep_ch11[0]["_meta"]["anchor_fix"] = (
        "07-07-2026 (H276 WS-3b): 9 фантомных якорей разрешено — 2 переякорено "
        "(kṣāma→V.17.30, vivarṇa→V.25.8), 7 запарковано в ch11.qa_removed.json")
    dump(os.path.join(LEX, "ch11.json"), keep_ch11)
    print(f"ch11.json: {len(keep_ch11)-1} notes remain "
          f"(-{len(parked)} parked, -{len(moved)} re-anchored away)")

    # parked -> ch11.qa_removed.json (append if the file ever re-runs partially)
    qa_path = os.path.join(LEX, "ch11.qa_removed.json")
    qa = load(qa_path) if os.path.exists(qa_path) else [
        {"_meta": {"description": "Отклонённые заметки QA-прохода, гл. 11",
                   "chapter": 11, "layer": "lexical"}}]
    qa.extend(parked)
    qa[0]["_meta"]["qa_pruned"] = "2026-07-07"
    qa[0]["_meta"]["removed_count"] = len(qa) - 1
    qa[0]["_meta"]["qa_pass"] = "H276 WS-3b (phantom verse anchors)"
    dump(qa_path, qa)
    print(f"ch11.qa_removed.json: {len(parked)} parked")

    # re-anchored -> their new chapters' lexical files
    for n in moved:
        ch = int(n["shloka"].split(".")[1])
        path = os.path.join(LEX, f"ch{ch}.json")
        doc = load(path)
        if any(m.get("lemma_iast") == n["lemma_iast"] and
               m.get("shloka") == n["shloka"] for m in doc if "_meta" not in m):
            sys.exit(f"ERROR: {n['shloka']} {n['lemma_iast']} already in ch{ch}")
        doc.append(n)
        doc[0]["_meta"]["notes_count"] = len(doc) - 1
        dump(path, doc)
        print(f"ch{ch}.json: +1 re-anchored ({n['lemma_iast']} @ {n['shloka']})")

    # ---- book aggregate ----
    book = load(BOOK)
    new_book, removed_book = [], 0
    reanchor_by_lemma = {lem: REANCHOR[(old, lem)][0] for old, lem in REANCHOR}
    for n in book:
        if "_meta" not in n and n.get("subtype") == "lexical" \
                and str(n.get("shloka", "")).startswith("V.11."):
            lem = n.get("lemma_iast")
            if lem in PARK:
                removed_book += 1
                continue
            if (n.get("shloka"), lem) in REANCHOR:
                upd = next(m for m in moved if m["lemma_iast"] == lem)
                n = upd
        new_book.append(n)
    notes = [n for n in new_book if "_meta" not in n]
    bm = new_book[0]["_meta"]
    bm["total_notes"] = len(notes)
    verses_noted = {n["shloka"] for n in notes}
    bm["verses_with_note"] = len(verses_noted)
    bm["verses_without_note"] = bm["total_verses"] - len(verses_noted)
    bm["by_type"] = dict(Counter(n.get("type") for n in notes if n.get("type")))
    bm["by_trigger"] = dict(Counter(n.get("trigger") for n in notes if n.get("trigger")))
    bm["anchor_fix"] = keep_ch11[0]["_meta"]["anchor_fix"]
    dump(BOOK, new_book)
    print(f"book: -{removed_book} parked, {len(moved)} re-anchored "
          f"(total {len(notes)})")

    # ---- stats ----
    stats = load(STATS)
    per_chapter_notes = Counter()
    noted = {}
    for n in notes:
        m = re.match(r"^V\.(\d+)\.(\d+)", str(n.get("shloka", "")))
        if m:
            per_chapter_notes[m.group(1)] += 1
            noted.setdefault(m.group(1), set()).add(m.group(2))
    stats["total_notes"] = len(notes)
    stats["verses_with_note"] = sum(len(v) for v in noted.values())
    stats["verses_without_note"] = stats["total_verses"] - stats["verses_with_note"]
    stats["by_subtype"] = dict(Counter(n.get("subtype", "base") for n in notes))
    for c, st in stats["per_chapter"].items():
        st["notes"] = per_chapter_notes.get(c, 0)
        st["verses_noted"] = len(noted.get(c, set()))
        st["verses_unnoted"] = st["verses"] - st["verses_noted"]
    stats["_meta"]["generated"] = "2026-07-07"
    stats["_meta"]["source"] = ("sundara_commentary_to_add.json "
                                "(fix_ch11_lexical_anchors.py rebuild)")
    dump(STATS, stats)
    print(f"stats: total_notes={stats['total_notes']}")


if __name__ == "__main__":
    main()
