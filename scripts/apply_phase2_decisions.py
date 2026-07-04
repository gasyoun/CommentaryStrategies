#!/usr/bin/env python3
"""Apply M.G.'s Phase-2 gate decisions (decisions.json from review.html) — H142 step 1.

Deterministic, stdlib-only. For every reviewer decision:
  accept / edit -> graft the (possibly edited) note into the per-chapter file
                   data/sundara_ch{N}_commentary_to_add.json with a `gate` stamp,
                   append it to the book aggregate data/sundara_commentary_to_add.json,
                   and stamp the candidate in pilot_candidates.json;
  reject        -> log to data/analysis/phase2_pilot/pilot_gate_rejected.json with reason.

In an `edit` decision the reviewer's textarea may carry trailing meta-directives
(e.g. «Нужно объединить с комментарием Костиной») after the note text proper.
The note text is the FIRST line/paragraph; every subsequent non-empty line goes
to `gate.mg_comment` verbatim — reviewer directives are audit trail, not note text.

Finally regenerates data/sundara_book_stats.json from the merged book file
(same counters as scripts/rebuild_crosstext.py; per-chapter verse totals are
taken from the existing stats file — they never change here).

Usage: python scripts/apply_phase2_decisions.py <decisions.json>
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
PILOT_DIR = os.path.join(DATA, "analysis", "phase2_pilot")
CAND = os.path.join(PILOT_DIR, "pilot_candidates.json")
BOOK = os.path.join(DATA, "sundara_commentary_to_add.json")
STATS = os.path.join(DATA, "sundara_book_stats.json")
GATE_REJECTED = os.path.join(PILOT_DIR, "pilot_gate_rejected.json")

GATED_BY = "М.Г. (review.html → decisions.json)"


def split_edit(text):
    """First line/paragraph = note text; the rest = reviewer meta-comment."""
    parts = [p.strip() for p in text.split("\n") if p.strip()]
    if not parts:
        return "", ""
    return parts[0], " ".join(parts[1:])


def load(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def dump(path, obj):
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(obj, fh, ensure_ascii=False, indent=2)


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: python scripts/apply_phase2_decisions.py <decisions.json>")
    decisions_doc = load(sys.argv[1])
    decisions = decisions_doc["reviewer_decisions"]
    gated_date = (decisions_doc.get("reviewed_at") or "")[:10]

    cand = load(CAND)
    by_vid = {n["verse_id"]: n for n in cand["notes"]}

    unknown = sorted(set(decisions) - set(by_vid))
    if unknown:
        sys.exit(f"ERROR: decisions for unknown candidates: {unknown}")
    undecided = sorted(set(by_vid) - set(decisions))
    if undecided:
        sys.stderr.write(f"WARN: candidates without a decision (left review_required): {undecided}\n")

    accepted, rejected = [], []
    for vid in sorted(decisions, key=lambda v: [int(x) for x in v.split(".")]):
        d = decisions[vid]
        note = by_vid[vid]
        action = d["action"]
        if action == "reject":
            rejected.append({
                "verse_id": vid,
                "lemma_iast": note.get("lemma_iast"),
                "note_ru": note.get("note_ru"),
                "reject_reason": d.get("reject_reason", ""),
                "gated_by": GATED_BY, "gated_date": gated_date,
            })
            note["gate"] = {"action": "reject", "gated_by": GATED_BY,
                           "gated_date": gated_date,
                           "reject_reason": d.get("reject_reason", "")}
            continue
        text, mg_comment = split_edit(d.get("edited_note") or note["note_ru"])
        silently_edited = (action == "accept" and text != note["note_ru"])
        gate = {"action": action, "gated_by": GATED_BY, "gated_date": gated_date}
        if mg_comment:
            gate["mg_comment"] = mg_comment
        if silently_edited:
            gate["text_changed_on_accept"] = True
        m = re.match(r"5\.(\d+)\.(\d+)$", vid)
        if not m:
            sys.exit(f"ERROR: non-single-verse id cannot be grafted: {vid}")
        chapter = int(m.group(1))
        final = {
            "shloka": f"V.{chapter}.{int(m.group(2))}",
            "lemma_iast": note.get("lemma_iast"),
            "note_ru": text,
            "type": note.get("kazansky_type"),
            "trigger": "commentator",
            "priority": "high",
            "subtype": "commentator",
            "source": "Phase-2: комментаторский диалог (Tilaka/Bhūṣaṇa/Śiromaṇi; Gita Supersite, CC BY 4.0)",
            "source_commentary": note.get("source_commentary", []),
            "why_proposed": note.get("why_proposed"),
            # M.G. gated the pilot (ruling R1); Leonov/Kostina still gate the
            # final book assembly — hence review_required stays true.
            "review_required": True,
            "gate": gate,
            "provenance": {**note.get("provenance", {}),
                           "applied_by": "scripts/apply_phase2_decisions.py"},
        }
        accepted.append((chapter, final))
        note["gate"] = gate

    # ---- per-chapter files ----
    per_ch = Counter(ch for ch, _ in accepted)
    for ch in sorted(per_ch):
        path = os.path.join(DATA, f"sundara_ch{ch}_commentary_to_add.json")
        doc = load(path)
        existing = {(n.get("shloka"), n.get("lemma_iast")) for n in doc if "_meta" not in n}
        added = 0
        for c, n in accepted:
            if c != ch:
                continue
            key = (n["shloka"], n["lemma_iast"])
            if key in existing:
                sys.stderr.write(f"WARN: {key} already in ch{ch} file; skipped\n")
                continue
            doc.append(n)
            added += 1
        meta = doc[0]["_meta"]
        meta["notes_count"] = len(doc) - 1
        meta["phase2_gate"] = (f"{gated_date}: +{added} комментаторских примечаний "
                               f"(гейт М.Г., пилот Фазы-2)")
        dump(path, doc)
        print(f"ch{ch}: +{added} notes -> {os.path.basename(path)}")

    # ---- book aggregate ----
    book = load(BOOK)
    existing = {(n.get("shloka"), n.get("lemma_iast")) for n in book if "_meta" not in n}
    added_book = 0
    for _, n in accepted:
        if (n["shloka"], n["lemma_iast"]) in existing:
            continue
        book.append(n)
        added_book += 1
    notes = [n for n in book if "_meta" not in n]
    bm = book[0]["_meta"]
    bm["total_notes"] = len(notes)
    verses_noted = {n["shloka"] for n in notes}
    bm["verses_with_note"] = len(verses_noted)
    bm["verses_without_note"] = bm["total_verses"] - len(verses_noted)
    bm["by_type"] = dict(Counter(n.get("type") for n in notes if n.get("type")))
    bm["by_trigger"] = dict(Counter(n.get("trigger") for n in notes if n.get("trigger")))
    bm["phase2_gate"] = (f"{gated_date}: +{added_book} примечаний Фазы-2 "
                         f"(комментаторский слой, гейт М.Г.)")
    dump(BOOK, book)
    print(f"book: +{added_book} notes -> {os.path.basename(BOOK)} (total {len(notes)})")

    # ---- stats (recomputed from the merged book; verse totals kept) ----
    stats = load(STATS)
    per_chapter_notes = Counter()
    noted_verses = {}
    for n in notes:
        m = re.match(r"^V\.(\d+)\.(\d+)", str(n.get("shloka", "")))
        if m:
            per_chapter_notes[m.group(1)] += 1
            noted_verses.setdefault(m.group(1), set()).add(m.group(2))
    stats["total_notes"] = len(notes)
    stats["verses_with_note"] = sum(len(v) for v in noted_verses.values())
    stats["verses_without_note"] = stats["total_verses"] - stats["verses_with_note"]
    stats["by_type"] = dict(Counter(n.get("type") for n in notes if n.get("type")))
    stats["by_trigger"] = dict(Counter(n.get("trigger") for n in notes if n.get("trigger")))
    stats["by_subtype"] = dict(Counter(n.get("subtype", "base") for n in notes))
    stats["by_priority"] = dict(Counter(n.get("priority") for n in notes if n.get("priority")))
    for c, st in stats["per_chapter"].items():
        st["notes"] = per_chapter_notes.get(c, 0)
        st["verses_noted"] = len(noted_verses.get(c, set()))
        st["verses_unnoted"] = st["verses"] - st["verses_noted"]
    stats["_meta"]["generated"] = gated_date
    stats["_meta"]["source"] = ("sundara_commentary_to_add.json "
                                "(apply_phase2_decisions.py rebuild)")
    dump(STATS, stats)
    print(f"stats: total_notes={stats['total_notes']} -> {os.path.basename(STATS)}")

    # ---- rejected log + stamped candidates ----
    if rejected:
        dump(GATE_REJECTED, {"_meta": {"generated_by": "scripts/apply_phase2_decisions.py",
                                       "gated_by": GATED_BY, "gated_date": gated_date},
                             "rejected": rejected})
        print(f"rejected: {len(rejected)} -> {os.path.basename(GATE_REJECTED)}")
    cand["_meta"]["status"] = (f"GATED {gated_date} by М.Г.: "
                               f"{sum(1 for _, _n in accepted if True)} accepted/edited, "
                               f"{len(rejected)} rejected; accepted notes grafted into "
                               f"per-chapter files by apply_phase2_decisions.py")
    dump(CAND, cand)
    acts = Counter(d["action"] for d in decisions.values())
    print(f"decisions applied: {dict(acts)}")


if __name__ == "__main__":
    main()
