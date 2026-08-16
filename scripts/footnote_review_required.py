#!/usr/bin/env python3
"""Step-0 predicate for edition-footnote cards (H2809).

A new card is ``review_required`` only when a *named* predicate says the
claim is not mechanically checkable (or it overlaps a Leonov/Kostina
edition note — the assembly gate stays gated). Default is false.

Independent of the generator's own Jaccard (VOTING_QUEUE_BURDEN_REDUCTION
METHOD §4): a check that re-reads the source that produced the card
proves nothing.

Named outcomes
--------------
ASSEMBLY-GATE   leonov_edition_note_here — stay review_required
VAR-OK          both sides located and distinct after nfold
VAR-NULL        both sides located; not distinct after nfold (not a variant)
VAR-NO-TEXT     verse texts missing
VAR-UNLOCATED   a reading is not in its edition's verse
ABS-OK          independent global Jaccard below the absent bar
ABS-PRESENT     independent global Jaccard at/above the present bar
ABS-BORDERLINE  independent Jaccard in (absent_bar, present_bar)
ABS-NO-EVIDENCE no independent per-verse search (generator Jaccard is not one)

Usage:
  python scripts/footnote_review_required.py --frozen-sample
  python scripts/footnote_review_required.py --selftest
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
EVIDENCE = os.path.join(
    REPO, "data", "analysis", "h1685_adjudication", "evidence.json"
)
CALIBRATION = os.path.join(
    REPO, "data", "analysis", "h1685_adjudication", "calibration.json"
)
CANDIDATES = os.path.join(REPO, "data", "edition_footnotes", "candidates.json")

sys.path.insert(0, HERE)
from sa_align import canon  # noqa: E402

# Apparatus "omitted here" marker — not a string to locate (H1685).
EMPTY_READING = frozenset({"∅", "", "-", "—"})

ABSENCE_KINDS = frozenset({"verse_range", "single", "sarga_absence"})
DEFAULT_BARS = {"present_bar_jaccard": 0.4, "absent_bar_jaccard": 0.267}

# Frozen H1685 class sizes (own-data 26-07-2026; re-counted from evidence.json).
FROZEN_VARIANT_N = 839
FROZEN_FN_N = 1013


def variant_locate(readings, crit_text, south_text, other_key="southern"):
    """Independent locate of each apparatus pair in its edition verse."""
    cv = canon(crit_text or "")
    sv = canon(south_text or "")
    checks = []
    for r in readings or []:
        raw_c = (r.get("crit") or "").strip()
        raw_s = (r.get(other_key) or r.get("southern") or "").strip()
        c_empty, s_empty = raw_c in EMPTY_READING, raw_s in EMPTY_READING
        c_r, s_r = canon(raw_c), canon(raw_s)
        c_ok = True if c_empty else (bool(c_r) and c_r in cv)
        s_ok = True if s_empty else (bool(s_r) and s_r in sv)
        checks.append({
            "crit": raw_c,
            other_key: raw_s,
            "omission": c_empty or s_empty,
            "crit_located": c_ok,
            "southern_located": s_ok,
            "distinct_after_fold": c_r != s_r,
        })
    return {
        "verse_texts_available": bool(cv) and bool(sv),
        "readings_checked": len(checks),
        "reading_checks": checks,
        "n_omission_markers": sum(1 for c in checks if c["omission"]),
        "all_readings_located": (
            all(c["crit_located"] and c["southern_located"] for c in checks)
            if checks else False
        ),
        "n_readings_unlocated": sum(
            1 for c in checks if not (c["crit_located"] and c["southern_located"])
        ),
        "n_readings_distinct": sum(1 for c in checks if c["distinct_after_fold"]),
    }


def _bars(cal=None):
    if cal and "operating_point" in cal:
        op = cal["operating_point"]
        return {
            "present_bar_jaccard": op["present_bar_jaccard"],
            "absent_bar_jaccard": op["absent_bar_jaccard"],
        }
    return dict(DEFAULT_BARS)


def review_required_for(kind, evidence, *, leonov_edition_note=False, bars=None):
    """Return (review_required, reason_code).

    Default is False. True only when the named predicate marks the claim
    uncheckable or the assembly-gate overlap is set.
    """
    if leonov_edition_note:
        return True, "ASSEMBLY-GATE"
    ev = evidence or {}
    bars = bars or DEFAULT_BARS
    if kind == "variant_reading":
        if not ev.get("verse_texts_available"):
            return True, "VAR-NO-TEXT"
        if not ev.get("all_readings_located"):
            return True, "VAR-UNLOCATED"
        if ev.get("n_readings_distinct", 0) == 0:
            return False, "VAR-NULL"
        return False, "VAR-OK"
    if kind in ABSENCE_KINDS:
        pv = ev.get("per_verse") or []
        if not pv:
            return True, "ABS-NO-EVIDENCE"
        pb = bars["present_bar_jaccard"]
        ab = bars["absent_bar_jaccard"]
        mx = max(p.get("best_jaccard", 0.0) for p in pv)
        if mx >= pb:
            return False, "ABS-PRESENT"
        if mx >= ab:
            return True, "ABS-BORDERLINE"
        return False, "ABS-OK"
    return True, "UNKNOWN-KIND"


def review_required_for_candidate(rec, *, variant_ev=None, absence_ev=None, bars=None):
    """Apply the predicate to a generator candidate record."""
    kind = rec.get("kind")
    leo = bool(rec.get("leonov_edition_note_here"))
    if kind == "variant_reading":
        return review_required_for(
            kind, variant_ev or {}, leonov_edition_note=leo, bars=bars
        )
    return review_required_for(
        kind, absence_ev, leonov_edition_note=leo, bars=bars
    )


def load_footnote_evidence_index(path=EVIDENCE):
    """Map (kind, verse_id) → H1685 independent evidence. Empty if the file is missing."""
    if not os.path.exists(path):
        return {}
    doc = json.load(open(path, encoding="utf-8"))
    out = {}
    for card in doc.get("cards") or []:
        if card.get("queue") != "footnotes":
            continue
        ev = card.get("evidence") or {}
        kind = ev.get("kind")
        vid = card.get("verse_id")
        if kind and vid:
            out[(kind, vid)] = ev
    return out


def classify_evidence_card(card, bars=None):
    ev = card.get("evidence") or {}
    return review_required_for(
        ev.get("kind"),
        ev,
        leonov_edition_note=bool(ev.get("leonov_edition_note_here")),
        bars=bars,
    )


def frozen_sample_table(evidence_path=EVIDENCE, calibration_path=CALIBRATION,
                        candidates_path=CANDIDATES):
    """Before/after ``review_required`` on the H1685 1013-card frozen sample."""
    ev_doc = json.load(open(evidence_path, encoding="utf-8"))
    cal = json.load(open(calibration_path, encoding="utf-8"))
    bars = _bars(cal)
    fn = [c for c in ev_doc["cards"] if c.get("queue") == "footnotes"]
    cand_meta = {}
    if os.path.exists(candidates_path):
        cand_meta = json.load(open(candidates_path, encoding="utf-8")).get("_meta", {})

    before_true = 0
    after_true = 0
    reasons = Counter()
    by_kind = Counter()
    after_true_by_kind = Counter()
    before_true_by_kind = Counter()
    for card in fn:
        kind = (card.get("evidence") or {}).get("kind") or "?"
        by_kind[kind] += 1
        before_true += 1
        before_true_by_kind[kind] += 1
        req, reason = classify_evidence_card(card, bars=bars)
        reasons[reason] += 1
        if req:
            after_true += 1
            after_true_by_kind[kind] += 1

    sample_date = (ev_doc.get("_meta") or {}).get("handoff", "H1685")
    return {
        "sample": {
            "source": os.path.relpath(evidence_path, REPO).replace("\\", "/"),
            "handoff": sample_date,
            "candidates_meta_date_note": (
                "data/edition_footnotes/candidates.json (generator dump that "
                "H1685's 1013-card sheet was built from; _meta.all_review_required "
                f"= {cand_meta.get('all_review_required')})"
            ),
            "n_footnote_cards": len(fn),
            "n_variants": by_kind.get("variant_reading", 0),
            "bars": bars,
        },
        "before": {
            "review_required_true": before_true,
            "review_required_false": 0,
            "by_kind": dict(before_true_by_kind),
        },
        "after": {
            "review_required_true": after_true,
            "review_required_false": len(fn) - after_true,
            "by_kind_true": dict(after_true_by_kind),
            "by_reason": dict(reasons),
        },
    }


def _print_table(rep):
    s, b, a = rep["sample"], rep["before"], rep["after"]
    print(f"sample: {s['source']}  ({s['handoff']})")
    print(f"  {s['candidates_meta_date_note']}")
    print(f"  cards: {s['n_footnote_cards']}  variants: {s['n_variants']}")
    print(f"  bars: present>={s['bars']['present_bar_jaccard']}  "
          f"absent<{s['bars']['absent_bar_jaccard']}")
    print()
    print(f"{'class':<22} {'before rr':>10} {'after rr':>10}")
    print(f"{'-'*22} {'-'*10} {'-'*10}")
    print(f"{'all footnotes':<22} {b['review_required_true']:>10} "
          f"{a['review_required_true']:>10}")
    print(f"{'  variant_reading':<22} {b['by_kind'].get('variant_reading', 0):>10} "
          f"{a['by_kind_true'].get('variant_reading', 0):>10}")
    for k in ("verse_range", "single", "sarga_absence"):
        if k in b["by_kind"]:
            print(f"{'  ' + k:<22} {b['by_kind'][k]:>10} "
                  f"{a['by_kind_true'].get(k, 0):>10}")
    print()
    print("after by reason (named predicate):")
    for reason, n in sorted(a["by_reason"].items(), key=lambda kv: (-kv[1], kv[0])):
        flag = "review_required" if reason in (
            "ASSEMBLY-GATE", "VAR-NO-TEXT", "VAR-UNLOCATED",
            "ABS-BORDERLINE", "ABS-NO-EVIDENCE", "UNKNOWN-KIND",
        ) else "not required"
        print(f"  {reason:<18} {n:>5}  {flag}")
    dropped = b["review_required_true"] - a["review_required_true"]
    print()
    print(f"cards that would no longer be created: {dropped} "
          f"({100 * dropped / b['review_required_true']:.1f}%)")


def _selftest():
    """Tiny synthetic cases — no corpus, no frozen file."""
    ok_ev = {
        "verse_texts_available": True,
        "all_readings_located": True,
        "n_readings_distinct": 1,
    }
    null_ev = {
        "verse_texts_available": True,
        "all_readings_located": True,
        "n_readings_distinct": 0,
    }
    missing = {
        "verse_texts_available": False,
        "all_readings_located": False,
        "n_readings_distinct": 1,
    }
    assert review_required_for("variant_reading", ok_ev) == (False, "VAR-OK")
    assert review_required_for("variant_reading", null_ev) == (False, "VAR-NULL")
    assert review_required_for("variant_reading", missing) == (True, "VAR-NO-TEXT")
    assert review_required_for(
        "variant_reading", ok_ev, leonov_edition_note=True
    ) == (True, "ASSEMBLY-GATE")
    lo = {"per_verse": [{"best_jaccard": 0.11}]}
    mid = {"per_verse": [{"best_jaccard": 0.30}]}
    hi = {"per_verse": [{"best_jaccard": 0.50}]}
    assert review_required_for("single", lo) == (False, "ABS-OK")
    assert review_required_for("single", mid) == (True, "ABS-BORDERLINE")
    assert review_required_for("single", hi) == (False, "ABS-PRESENT")
    assert review_required_for("single", {}) == (True, "ABS-NO-EVIDENCE")
    loc = variant_locate(
        [{"crit": "rāma", "southern": "rāmaḥ"}],
        "rāmo vanam gacchati",
        "rāmaḥ vanam gacchati",
    )
    assert loc["verse_texts_available"]
    print("selftest: PASS (9 asserts)")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n", 1)[0])
    ap.add_argument("--frozen-sample", action="store_true",
                    help="print before/after table on H1685 evidence.json")
    ap.add_argument("--json", action="store_true",
                    help="with --frozen-sample, emit JSON")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args(argv)
    if args.selftest:
        _selftest()
        return 0
    if args.frozen_sample:
        rep = frozen_sample_table()
        if args.json:
            json.dump(rep, sys.stdout, ensure_ascii=False, indent=2)
            sys.stdout.write("\n")
        else:
            _print_table(rep)
        n_var = rep["sample"]["n_variants"]
        if n_var != FROZEN_VARIANT_N or rep["sample"]["n_footnote_cards"] != FROZEN_FN_N:
            sys.stderr.write(
                f"WARN: frozen class drifted (variants={n_var}, "
                f"fn={rep['sample']['n_footnote_cards']})\n"
            )
            return 2
        return 0
    ap.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
