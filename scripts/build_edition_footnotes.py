#!/usr/bin/env python3
"""Generate footnote candidates for critical↔southern edition differences.

Deterministic (no LLM — these are structural statements). Two candidate
kinds, both `review_required`:

1. **Absence footnotes** («в критическом издании (Барода) отсутствует») from
   genuine structural absences (significant_absences.json → divergence ==
   'structural_absence'), grouped into contiguous passages, deduped against
   Leonov/Kostina's own notes.
2. **Variant-reading footnotes** (H776) — the counterpart for verses that DO
   have a critical-edition match but read differently: the actual competing
   readings from the akṣara-level apparatus
   (data/analysis/helayo_spike/apparatus_sundara_variants.json → entries),
   one candidate per verse carrying its `apparatus` loci (`crit`]`south`
   pairs), not just a generic "reworded" label. Before H776 this layer was
   computed (by build_edition_apparatus.py) but never reached the footnote
   review gate at all -- variant verses had no footnote-candidate path.

Format is per COMMENTARY_ROADMAP §3 and is [to ratify].

Usage: python scripts/build_edition_footnotes.py
Output: data/edition_footnotes/candidates.json + footnotes_review.html
"""
import sys
import os
import json

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
CD = os.path.join(REPO, "data", "edition_comparison")
OUTDIR = os.path.join(REPO, "data", "edition_footnotes")
APPARATUS_PATH = os.path.join(REPO, "data", "analysis", "helayo_spike", "apparatus_sundara_variants.json")

MIN_RUN = 2          # [to ratify] min passage length for a standalone footnote
WHOLE_FRAC = 0.8     # a run covering >= this fraction of a sarga = whole-sarga absence
EDITION_KW = ["критическ", "южн", "издани", "выпал", "отсутств", "редакц", "рецензи", "вульгат", "рукопис"]


def build_variant_reading_candidates(leo_any, leo_edition):
    """H776: one candidate per clean-variant verse in the akṣara-level
    apparatus, carrying the actual competing readings (not just a
    'reworded' label). Source: build_edition_apparatus.py's output --
    read-only here, this generator never re-runs the aligner."""
    if not os.path.exists(APPARATUS_PATH):
        return []
    ap = json.load(open(APPARATUS_PATH, encoding="utf-8"))
    other_key = ap["_meta"].get("other_key", "southern")
    out = []
    for e in ap["entries"]:
        vid = e["critical"]
        south_id = e[other_key]
        s = vparts(vid)[0]
        readings = [{"crit": a["crit"], other_key: a[other_key]} for a in e["apparatus"]]
        note = "; ".join(f"{r['crit']} ] {r[other_key]}" for r in readings)
        rec = {
            "anchor": vid, "kind": "variant_reading", "sarga": s,
            "range": vid, "southern_id": south_id, "count": len(readings),
            "note_ru": f"Разночтение: {note}",
            "readings": readings,
            "difflib_similarity": e.get("difflib_similarity"),
            "confidence": f"aksara-level Gotoh, {len(readings)} loci (H776)",
            "leonov_note_here": [south_id] if south_id in leo_any else None,
            "leonov_edition_note_here": [south_id] if south_id in leo_edition else None,
            "review_required": True,
            "source": "helayo_spike/apparatus_sundara_variants.entries",
            "provenance": {"generator": "scripts/build_edition_footnotes.py",
                          "aligner": "scripts/build_edition_apparatus.py (H776 aksara-level)",
                          "deterministic": True},
        }
        out.append(rec)
    return out


def vparts(vid):
    p = vid.split(".")
    return int(p[1]), int(p[2])


def main():
    sa = json.load(open(os.path.join(CD, "significant_absences.json"), encoding="utf-8"))
    bs = json.load(open(os.path.join(CD, "book_summary.json"), encoding="utf-8"))
    structural = sa.get("structural_absence", [])

    # southern verse totals per sarga (raw by-number table has southern_verses)
    south_total = {r["sarga"]: r["southern_verses"] for r in bs.get("per_sarga_by_number_RAW", [])}

    # Leonov/Kostina own notes: which verses they annotate, and which carry an edition remark
    leo_any, leo_edition = set(), set()
    lp = os.path.join(REPO, "data", "leonov_own_notes.json")
    if os.path.exists(lp):
        for n in json.load(open(lp, encoding="utf-8"))["notes"]:
            leo_any.add(n["verse_id"])
            if any(k in n.get("raw_text", "").lower() for k in EDITION_KW):
                leo_edition.add(n["verse_id"])

    # contiguous runs of structural-absence verses within a sarga
    verses = sorted({vparts(r["southern"]) for r in structural})
    runs = []
    for s, v in verses:
        if runs and runs[-1]["sarga"] == s and v == runs[-1]["verses"][-1] + 1:
            runs[-1]["verses"].append(v)
        else:
            runs.append({"sarga": s, "verses": [v]})

    text_by_id = {r["southern"]: r.get("text", "") for r in structural}   # IAST of each absent verse

    candidates, singletons = [], []
    for run in runs:
        s, vs = run["sarga"], run["verses"]
        n = len(vs)
        rng = f"5.{s}.{vs[0]}" + (f"–{vs[-1]}" if n > 1 else "")
        ids = [f"5.{s}.{v}" for v in vs]
        leo_here = [i for i in ids if i in leo_any]
        leo_ed = [i for i in ids if i in leo_edition]
        whole = south_total.get(s) and n >= WHOLE_FRAC * south_total[s]
        if whole:
            kind = "sarga_absence"
            note = (f"Песнь [южн. {s}] (стихи {vs[0]}–{vs[-1]}, {n} шлок) целиком отсутствует "
                    f"в критическом издании (Барода).")
        elif n >= MIN_RUN:
            kind = "verse_range"
            note = f"Шлоки {rng} ({n} шлок) отсутствуют в критическом издании (Барода)."
        else:
            kind = "single"
            note = f"Шлока {rng} отсутствует в критическом издании (Барода)."
        rec = {
            "anchor": ids[0], "kind": kind, "sarga": s, "range": rng,
            "verses": vs, "count": n, "note_ru": note,
            "verses_iast": [{"verse_id": i, "iast": text_by_id.get(i, "")} for i in ids],
            "confidence": "structural_absence (best_crit_jaccard < 0.25)",
            "leonov_note_here": leo_here or None,
            "leonov_edition_note_here": leo_ed or None,
            "review_required": True,
            "source": "edition_comparison/structural_absence",
            "provenance": {"generator": "scripts/build_edition_footnotes.py", "deterministic": True},
        }
        (singletons if kind == "single" else candidates).append(rec)

    variant_candidates = build_variant_reading_candidates(leo_any, leo_edition)

    os.makedirs(OUTDIR, exist_ok=True)
    payload = {
        "_meta": {
            "generated_by": "scripts/build_edition_footnotes.py",
            "basis": "structural_absence verses (южные шлоки без критич. аналога, Jaccard<0.25) "
                     "+ variant readings from the akṣara-level apparatus (H776)",
            "format": "COMMENTARY_ROADMAP §3 — [на ратификацию]",
            "thresholds": {"min_run_for_footnote": MIN_RUN, "whole_sarga_fraction": WHOLE_FRAC},
            "footnote_candidates": len(candidates),
            "single_verse_absences": len(singletons),
            "variant_reading_candidates": len(variant_candidates),
            "sarga_absences": sum(1 for c in candidates if c["kind"] == "sarga_absence"),
            "with_leonov_note_on_verse": sum(1 for c in candidates if c["leonov_note_here"]),
            "with_leonov_edition_note": sum(1 for c in candidates if c["leonov_edition_note_here"]),
            "all_review_required": True,
            "rights_note": "coordinates are corpus-derived — verify against the print critical apparatus",
        },
        "candidates": candidates,
        "single_verse_absences": singletons,
        "variant_reading_candidates": variant_candidates,
    }
    json.dump(payload, open(os.path.join(OUTDIR, "candidates.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)

    # Human gate is the interactive footnotes_review.html — build it now (no
    # markdown checkbox sheet; see CLAUDE.md "Human review / gating artifacts").
    try:
        sys.path.insert(0, HERE)
        import build_footnotes_review_html as _r
        _r.main()
    except Exception as e:      # keep candidate generation independent of the viewer
        sys.stderr.write(f"WARN: could not build footnotes_review.html: {e}\n")

    m = payload["_meta"]
    print(f"footnote candidates: {m['footnote_candidates']} passages "
          f"({m['sarga_absences']} whole-sarga) + {m['single_verse_absences']} singletons")
    print(f"variant-reading candidates (H776): {m['variant_reading_candidates']}")
    print(f"dedup: {m['with_leonov_edition_note']} overlap a Leonov EDITION note; "
          f"{m['with_leonov_note_on_verse']} have any Leonov note on the verse")
    print(f"wrote candidates.json -> {OUTDIR}")


if __name__ == "__main__":
    main()
