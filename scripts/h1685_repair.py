#!/usr/bin/env python3
"""H1685 step 8 — repair the mechanically-fixable residue instead of parking it.

The adjudication left 87 cards diagnosed but unusable: 48 `flag_anchor` (the note
is filed at a śloka that does not contain its lemma) and 39 `edit` (a named,
fixable defect). Diagnosing them cost a strong model a full read each; leaving
them parked wastes that. A repaired card re-enters the SAME rule tier and the
SAME measured gate, so fixing one costs the human nothing extra.

Only DETERMINISTIC repairs are made here. Two classes:

  RE-ANCHOR   the lemma is searched across the whole southern Sundarakāṇḍa. A
              target is accepted only if it lies in the SAME sarga — a note
              filed at 5.49.7 may well belong to sarga 52, but moving it across
              sargas is a scholarly claim, not a repair, so cross-sarga hits are
              reported and left flagged.
  UNCORRUPT   a foreign-script or glued fragment spliced into the Russian text
              ('viमāna' for vimāna, 'экувেṇī' for eka-veṇī, 'марша&нīя' for
              marṣaṇīya, a stray 'dolce'/'version'). Each replacement is written
              out in full in repairs.json so it can be read before it is applied.

NOT repaired here, deliberately: unverifiable citations, wrong-commentator
attributions and register trims. Each has a prescription from the judge, but
applying it means rewriting an author's sentence — that is an editorial act, not
a mechanical one, and it stays with the human.

Writes data/analysis/h1685_adjudication/repairs.json (the proposal). With
--apply it edits the canonical records: batch{2,3}_candidates.json for the
commentary batches, and for the lexical layer ALL THREE of data/lexical/ch{N}.json,
its WS-3b park data/lexical/ch{N}.qa_removed.json (7 cards live only there, of
which 1 is repairable — omitting it made that repair a silent no-op) and the
book aggregate
data/sundara_commentary_to_add.json, which carry the same note and must not
drift apart. Every proposed repair must reach a real record: any that lands
nowhere is printed as a defect instead of being counted as done.

Usage:
  python scripts/h1685_repair.py                 # propose, write nothing
  python scripts/h1685_repair.py --apply
"""
import sys
import os
import re
import json
import argparse
from collections import Counter, defaultdict

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
DATA = os.path.join(REPO, "data")
AD = os.path.join(DATA, "analysis", "h1685_adjudication")
OUT = os.path.join(AD, "repairs.json")

sys.path.insert(0, HERE)
from sa_align import canon                                    # noqa: E402
from compare_editions import load_southern                    # noqa: E402
from h1685_evidence import lemma_alternatives, _match_in      # noqa: E402

# Exact, hand-verified text repairs. Key: (queue, card key) -> [(bad, good, why)]
TEXT_REPAIRS = {
    ("lexical", "V.4.27|vimāna"): [
        ("viमāna", "vimāna",
         "देवनагари म (ma) вклеена в IAST-слово; 2 вхождения")],
    ("lexical", "V.28.17|veṇīgrathana"): [
        ("экувেṇī", "eka-veṇī",
         "бенгальский знак гласной ে внутри слова; читается eka-veṇī")],
    ("lexical", "V.63.17|vyatikrama"): [
        ("марша&нīя", "marṣaṇīya",
         "склейка через & — предвосхищение marṣaṇīya из соседней заметки")],
    ("lexical", "V.55.7|svāmighātaka"): [
        (" dolce", "",
         "постороннее латинское слово, приклеенное к «предателем»")],
    ("batch3", "5.38.65"): [
        ("не выбирая version", "не выбирая версию",
         "латинский огрызок в русской фразе")],
}


STAMP = ("27-07-2026: {n} карт починено агентом-адъюдикатором "
         "Opus 5 1M (claude-opus-5[1m]) — см. h1685_adjudication/repairs.json")


def load(p):
    with open(p, encoding="utf-8") as fh:
        return json.load(fh)


def stamp_meta(doc, text):
    """Write provenance into _meta, whether the file is a dict or a list whose
    first element is the {"_meta": …} header (the lexical layer's shape)."""
    if isinstance(doc, dict):
        doc.setdefault("_meta", {})["h1685_repair"] = text
        return
    for el in doc:
        if isinstance(el, dict) and "_meta" in el:
            el["_meta"]["h1685_repair"] = text
            return
    doc.insert(0, {"_meta": {"h1685_repair": text}})


def dump(p, obj, dry):
    if dry:
        return
    with open(p, "w", encoding="utf-8") as fh:
        json.dump(obj, fh, ensure_ascii=False, indent=2)


def sarga_of(vid):
    m = re.match(r"(?:V\.|5\.)?(\d+)\.", vid or "")
    return int(m.group(1)) if m else None


def find_lemma(lemma, south_by_id, sarga):
    """Every śloka whose text contains the lemma; same-sarga hits first."""
    alts = lemma_alternatives(lemma)
    same, other = [], []
    for vid, txt in south_by_id.items():
        cv = canon(txt)
        cvt = set(cv.split())
        for a in alts:
            state, _ = _match_in(a, cv, cvt)
            if state:
                (same if sarga_of(vid) == sarga else other).append((vid, state, a))
                break
    return same, other


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    dry = not args.apply

    ledger = load(os.path.join(AD, "ledger_final.json"))["verdicts"]
    ev = {c["card_id"]: c for c in load(os.path.join(AD, "evidence.json"))["cards"]}
    south_by_id = {f"5.{s}.{v}": t for s, v, t in load_southern()}

    repairs, unresolved = [], []

    # ---------------------------------------------------------- re-anchoring
    for r in [x for x in ledger if x["verdict"] == "flag_anchor"]:
        c = ev[r["card_id"]]
        detail = c["evidence"].get("anchor_detail") or ""
        m = re.search(r"stands in (5\.\d+\.\d+)", detail)
        target, how = (m.group(1), "named by the ±2 re-search") if m else (None, None)
        cross = []
        if not target:
            same, other = find_lemma(c["lemma"], south_by_id, sarga_of(c["verse_id"]))
            if len(same) == 1:
                target, how = same[0][0], "unique hit in the same sarga (book-wide search)"
            elif len(same) > 1:
                exact = [h for h in same if h[1] == "exact"]
                if len(exact) == 1:
                    target, how = exact[0][0], "unique EXACT hit in the same sarga"
                else:
                    cross = [h[0] for h in same[:5]]
                    why_not = "ambiguous: several ślokas in this sarga carry the lemma"
            else:
                cross = [h[0] for h in other[:5]]
                why_not = ("the lemma occurs only in OTHER sargas — moving it there "
                           "is a scholarly claim, not a repair")
        rec = {"card_id": r["card_id"], "queue": r["queue"], "key": r["key"],
               "kind": "re-anchor", "lemma": c["lemma"],
               "from": c["verse_id"], "to": target, "how": how,
               "candidates": cross,
               "why_not_repaired": None if target else (
                   why_not if cross else "the lemma occurs nowhere in the kāṇḍa"),
               "parked_ws3b": bool(c["evidence"].get("parked_ws3b"))}
        (repairs if target else unresolved).append(rec)

    # ------------------------------------------------------------- text fixes
    for r in ledger:
        fixes = TEXT_REPAIRS.get((r["queue"], r["key"]))
        if not fixes:
            continue
        note = ev[r["card_id"]]["note_ru"]
        applied = []
        for bad, good, why in fixes:
            if bad not in note:
                sys.stderr.write(f"WARN: {r['key']}: {bad!r} not present — skipped\n")
                continue
            applied.append({"bad": bad, "good": good, "why": why,
                            "occurrences": note.count(bad),
                            "context": note[max(0, note.find(bad) - 60):
                                            note.find(bad) + len(bad) + 60]})
        if applied:
            repairs.append({"card_id": r["card_id"], "queue": r["queue"],
                            "key": r["key"], "kind": "uncorrupt",
                            "verdict_was": r["verdict"], "fixes": applied})

    # ------------------------------------------------------------------ apply
    touched = Counter()
    landed = defaultdict(list)          # card_id -> files the repair reached
    if args.apply:
        # batch candidates
        for batch in ("batch2", "batch3"):
            p = os.path.join(DATA, "analysis", f"phase2_{batch}", f"{batch}_candidates.json")
            doc = load(p)
            by_vid = defaultdict(list)
            for n in doc["notes"]:
                by_vid[n["verse_id"]].append(n)
            n_ch = 0
            for rep in repairs:
                if rep["queue"] != batch:
                    continue
                hits = by_vid.get(rep["key"], [])
                if len(hits) > 1:
                    # a bare verse_id is the card key here, so a duplicated
                    # verse_id makes the target ambiguous — narrow by lemma
                    # rather than guessing (the silent-collision failure the
                    # adjudication itself caught in apply_phase2_decisions.py)
                    hits = [n for n in hits if n.get("lemma_iast") == rep["lemma"]]
                if len(hits) != 1:
                    sys.stderr.write(f"WARN: {batch} {rep['key']}: "
                                     f"{len(hits)} matching notes — not applied\n")
                    continue
                note = hits[0]
                if rep["kind"] == "re-anchor":
                    note["h1685_reanchored_from"] = note["verse_id"]
                    note["verse_id"] = rep["to"]
                else:
                    for f in rep["fixes"]:
                        note["note_ru"] = note["note_ru"].replace(f["bad"], f["good"])
                n_ch += 1
                landed[rep["card_id"]].append(os.path.basename(p))
            if n_ch:
                doc["_meta"]["h1685_repair"] = STAMP.format(n=n_ch)
                dump(p, doc, dry)
                touched[os.path.basename(p)] = n_ch

        # lexical: chapter file, its WS-3b park, and the book aggregate, kept in
        # step. A card parked by H276 WS-3b lives ONLY in ch{N}.qa_removed.json —
        # 7 such cards, 1 of them repairable (V.11.12|rājīvanetri), and omitting
        # that file made its repair a silent no-op.
        book_p = os.path.join(DATA, "sundara_commentary_to_add.json")
        docs = {book_p: load(book_p)}                       # path -> loaded doc
        for rep in [x for x in repairs if x["queue"] == "lexical"]:
            shloka, lemma = rep["key"].split("|", 1)
            ch = sarga_of(shloka)
            paths = [os.path.join(DATA, "lexical", f"ch{ch}.json"),
                     os.path.join(DATA, "lexical", f"ch{ch}.qa_removed.json"),
                     book_p]
            for path in paths:
                if path not in docs:
                    if not os.path.exists(path):
                        continue
                    docs[path] = load(path)
                doc = docs[path]
                items = doc if isinstance(doc, list) else doc.get("notes", [])
                for n in items:
                    if not isinstance(n, dict):
                        continue
                    if n.get("shloka") != shloka or n.get("lemma_iast") != lemma:
                        continue
                    if rep["kind"] == "re-anchor":
                        n["h1685_reanchored_from"] = n["shloka"]
                        n["shloka"] = "V." + rep["to"][2:]
                    else:
                        for f in rep["fixes"]:
                            n["note_ru"] = n["note_ru"].replace(f["bad"], f["good"])
                    touched[os.path.basename(path)] += 1
                    landed[rep["card_id"]].append(os.path.basename(path))
        for path, doc in docs.items():
            n_here = touched.get(os.path.basename(path), 0)
            if not n_here:
                continue
            stamp_meta(doc, STAMP.format(n=n_here))
            dump(path, doc, dry)

        # every proposed repair must have reached a real record; a repair that
        # lands nowhere is the failure mode this pass exists to end, so it is
        # reported as a defect rather than counted as done
        missed = [r for r in repairs if not landed.get(r["card_id"])]
        if missed:
            print(f"\nNOT APPLIED — no canonical record found ({len(missed)}):")
            for r in missed:
                print(f"  {r['queue']:<8} {r['key']}")

    # ----------------------------------------------------------------- report
    by_kind = Counter(r["kind"] for r in repairs)
    print(f"repairs proposed: {len(repairs)}  {dict(by_kind)}"
          + ("  [APPLIED]" if args.apply else "  [proposal only — rerun with --apply]"))
    print(f"still unresolved: {len(unresolved)} flag_anchor cards\n")

    # the splits, computed — prose about this pass quotes THESE, never a count
    # made by eye off the listing below (16/8 and 18/6 were first published as
    # 15/9 and 17/7 that way)
    by_how = Counter(r["how"] for r in repairs if r["kind"] == "re-anchor")
    by_why = Counter(r["why_not_repaired"] for r in unresolved)
    print("splits — re-anchor by provenance:")
    for k, v in by_how.most_common():
        print(f"  {v:>3}  {k}")
    print("splits — refusal by reason:")
    for k, v in by_why.most_common():
        print(f"  {v:>3}  {k}")
    print()

    print("re-anchors:")
    for r in [x for x in repairs if x["kind"] == "re-anchor"]:
        print(f"  {r['queue']:<8} {r['key']:<28} {r['from']} -> {r['to']}   ({r['how']})")
    print("\ntext repairs:")
    for r in [x for x in repairs if x["kind"] == "uncorrupt"]:
        for f in r["fixes"]:
            print(f"  {r['queue']:<8} {r['key']:<28} {f['bad']!r} -> {f['good']!r} "
                  f"×{f['occurrences']}")
    if unresolved:
        print("\nleft flagged (no same-sarga home for the lemma):")
        for r in unresolved[:40]:
            alt = ("; кандидаты: " + ", ".join(r["candidates"])) if r["candidates"] else ""
            print(f"  {r['queue']:<8} {r['key']:<28} @{r['from']}{alt}\n"
                  f"           └─ {r['why_not_repaired']}")
    if touched:
        print("\nfiles written:", dict(touched))

    doc = {"_meta": {"handoff": "H1685", "generated_by": "scripts/h1685_repair.py",
                     "adjudicator": "Opus 5 1M (claude-opus-5[1m])",
                     "applied": bool(args.apply),
                     "proposed": len(repairs), "unresolved": len(unresolved),
                     "by_kind": dict(by_kind),
                     "splits": {"re_anchor_by_provenance": dict(by_how),
                                "refusal_by_reason": dict(by_why)},
                     "policy": ("re-anchor only within the same sarga; text repairs "
                                "only for foreign-script/glued corruption; citations, "
                                "attributions and register left to the human")},
           "repairs": repairs, "unresolved": unresolved}
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, ensure_ascii=False, indent=1)
    print(f"\nwrote {OUT}")


if __name__ == "__main__":
    main()
