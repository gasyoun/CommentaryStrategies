#!/usr/bin/env python3
"""Apply M.G.'s Phase-2 gate decisions (decisions.json from a review sheet).

H142 step 1 (pilot); extended for batch-2/batch-3 by H276 WS-1.

Deterministic, stdlib-only. For every reviewer decision:
  accept / edit -> graft the (possibly edited) note into the per-chapter file
                   data/sundara_ch{N}_commentary_to_add.json with a `gate` stamp,
                   append it to the book aggregate data/sundara_commentary_to_add.json,
                   and stamp the candidate in the batch's candidates file;
  reject        -> log to data/analysis/<batch>/<prefix>_gate_rejected.json with reason.

Batch selection (`--batch pilot|batch2|batch3`, default `auto`): auto-detection
requires every decision verse_id to belong to exactly one batch's candidate set.

Judge fields (batch-3 carries a §3.4 `judge` object per note) SURVIVE the graft
verbatim. Candidates whose judge verdict is `reject` / `park` / `flag_anchor`
require EXPLICIT resolution: the run prints a resolution table for all of them,
and an `accept`/`edit` decision on a `flag_anchor` note is a hard error unless
--allow-flagged-anchor is given (the verse anchor must be fixed first — see the
judge's reason).

In an `edit` decision the reviewer's textarea may carry trailing meta-directives
(e.g. «Нужно объединить с комментарием Костиной») after the note text proper.
The note text is the FIRST line/paragraph; every subsequent non-empty line goes
to `gate.mg_comment` verbatim — reviewer directives are audit trail, not note text.

Finally regenerates data/sundara_book_stats.json from the merged book file
(per-chapter verse totals are taken from the existing stats file — they never
change here). With --dry-run nothing is written; the full summary still prints.

After a real (non-dry) apply, rebuild the downstream artifacts:
  python scripts/build_sarga_apparatus.py      # per-sarga interactive apparatus
  python scripts/build_book_apparatus.py       # ЛП print master (MD+DOCX)
  python scripts/book_density_stats.py         # density JSON

Usage: python scripts/apply_phase2_decisions.py <decisions.json>
           [--batch pilot|batch2|batch3|auto] [--dry-run] [--allow-flagged-anchor]
"""
import sys
import os
import re
import json
import argparse
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
DATA = os.path.join(REPO, "data")
BOOK = os.path.join(DATA, "sundara_commentary_to_add.json")
STATS = os.path.join(DATA, "sundara_book_stats.json")

BATCHES = {
    "pilot": {"dir": os.path.join(DATA, "analysis", "phase2_pilot"),
              "candidates": "pilot_candidates.json",
              "rejected": "pilot_gate_rejected.json",
              "label": "пилот Фазы-2"},
    "batch2": {"dir": os.path.join(DATA, "analysis", "phase2_batch2"),
               "candidates": "batch2_candidates.json",
               "rejected": "batch2_gate_rejected.json",
               "label": "партия 2 Фазы-2"},
    "batch3": {"dir": os.path.join(DATA, "analysis", "phase2_batch3"),
               "candidates": "batch3_candidates.json",
               "rejected": "batch3_gate_rejected.json",
               "label": "партия 3 Фазы-2"},
}

GATED_BY = "М.Г. (review.html → decisions.json)"
JUDGE_FLAGGED = {"reject", "park", "flag_anchor"}


def split_edit(text):
    """First line/paragraph = note text; the rest = reviewer meta-comment."""
    parts = [p.strip() for p in text.split("\n") if p.strip()]
    if not parts:
        return "", ""
    return parts[0], " ".join(parts[1:])


def load(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def dump(path, obj, dry):
    if dry:
        return
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(obj, fh, ensure_ascii=False, indent=2)


def detect_batch(decision_vids):
    """The single batch whose candidate set contains every decided verse_id."""
    hits = {}
    for name, cfg in BATCHES.items():
        path = os.path.join(cfg["dir"], cfg["candidates"])
        if not os.path.exists(path):
            continue
        vids = {n["verse_id"] for n in load(path)["notes"]}
        if set(decision_vids) <= vids:
            hits[name] = len(vids)
    if len(hits) == 1:
        return next(iter(hits))
    if not hits:
        sys.exit("ERROR: decisions match no batch's candidate set in full — "
                 "pass --batch explicitly or fix the decisions file")
    sys.exit(f"ERROR: decisions are ambiguous across batches {sorted(hits)} — "
             f"pass --batch explicitly")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("decisions")
    ap.add_argument("--batch", choices=[*BATCHES, "auto"], default="auto")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--allow-flagged-anchor", action="store_true",
                    help="permit accepting a note the judge marked flag_anchor "
                         "(only after the verse anchor was actually fixed)")
    args = ap.parse_args()
    dry = args.dry_run

    decisions_doc = load(args.decisions)
    decisions = decisions_doc["reviewer_decisions"]
    gated_date = (decisions_doc.get("reviewed_at") or "")[:10]

    batch = args.batch if args.batch != "auto" else detect_batch(decisions)
    cfg = BATCHES[batch]
    cand_path = os.path.join(cfg["dir"], cfg["candidates"])
    rej_path = os.path.join(cfg["dir"], cfg["rejected"])
    print(f"batch: {batch} ({cand_path})" + (" [DRY RUN]" if dry else ""))

    cand = load(cand_path)
    by_vid = {n["verse_id"]: n for n in cand["notes"]}

    unknown = sorted(set(decisions) - set(by_vid))
    if unknown:
        sys.exit(f"ERROR: decisions for unknown candidates: {unknown}")
    undecided = sorted(set(by_vid) - set(decisions))
    if undecided:
        sys.stderr.write(f"WARN: {len(undecided)} candidates without a decision "
                         f"(left review_required): {undecided}\n")

    # ---- explicit resolution of judge-flagged candidates (H276 WS-1) ----
    flagged = [(vid, n["judge"]["verdict"]) for vid, n in sorted(by_vid.items())
               if isinstance(n.get("judge"), dict)
               and n["judge"].get("verdict") in JUDGE_FLAGGED]
    if flagged:
        print(f"judge-flagged candidates requiring explicit resolution "
              f"({len(flagged)}):")
        hard_errors = []
        for vid, verdict in flagged:
            d = decisions.get(vid)
            action = d["action"] if d else "— UNRESOLVED (no reviewer decision)"
            print(f"  {vid}: judge={verdict} -> reviewer={action}")
            if d and verdict == "flag_anchor" and d["action"] in ("accept", "edit") \
                    and not args.allow_flagged_anchor:
                hard_errors.append(vid)
        if hard_errors:
            sys.exit(f"ERROR: accepting flag_anchor notes {hard_errors} without "
                     f"--allow-flagged-anchor — fix the verse anchor first "
                     f"(see judge.reason), then re-run with the flag")

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
                "judge": note.get("judge"),
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
            # M.G. gated the batch (ruling R1); Leonov/Kostina still gate the
            # final book assembly — hence review_required stays true.
            "review_required": True,
            "gate": gate,
            "provenance": {**note.get("provenance", {}),
                           "batch": batch,
                           "applied_by": "scripts/apply_phase2_decisions.py"},
        }
        # §3.4 judge verdicts survive the graft verbatim (H276 WS-1)
        if note.get("judge"):
            final["judge"] = note["judge"]
        if "contrastive" in note:
            final["contrastive"] = note["contrastive"]
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
                               f"(гейт М.Г., {cfg['label']})")
        dump(path, doc, dry)
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
                         f"({cfg['label']}, гейт М.Г.)")
    dump(BOOK, book, dry)
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
    dump(STATS, stats, dry)
    print(f"stats: total_notes={stats['total_notes']} -> {os.path.basename(STATS)}")

    # ---- rejected log + stamped candidates ----
    if rejected:
        dump(rej_path, {"_meta": {"generated_by": "scripts/apply_phase2_decisions.py",
                                  "batch": batch,
                                  "gated_by": GATED_BY, "gated_date": gated_date},
                        "rejected": rejected}, dry)
        print(f"rejected: {len(rejected)} -> {os.path.basename(rej_path)}")
    cand["_meta"]["status"] = (f"GATED {gated_date} by М.Г.: "
                               f"{len(accepted)} accepted/edited, "
                               f"{len(rejected)} rejected; accepted notes grafted into "
                               f"per-chapter files by apply_phase2_decisions.py")
    dump(cand_path, cand, dry)
    acts = Counter(d["action"] for d in decisions.values())
    print(f"decisions applied: {dict(acts)}")
    if not dry:
        print("REBUILD NOW: python scripts/build_sarga_apparatus.py && "
              "python scripts/build_book_apparatus.py && "
              "python scripts/book_density_stats.py")


if __name__ == "__main__":
    main()
