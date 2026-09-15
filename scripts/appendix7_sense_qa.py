#!/usr/bin/env python3
"""H4709 — dcs-sintagmatic-appendix7 as collocate context for Sundara sense-note QA.

Joins every Sundarakaṇḍa lexical note (data/lexical/ch*.json, kept set) to the
DCS syntagmatic table (Приложение 7, kosha dataset `dcs-sintagmatic-appendix7`)
by lemma, emitting a per-note collocate-profile QA context file + coverage stats.

Match tiers (recorded per note, never silently merged):
  exact        — lemma_iast identical to a DCS lemma
  folded       — NFC + casefold + ṁ→ṃ + quote variants
  annotation   — parenthetical "(...)" qualifier stripped, then exact/folded
  hyphen-join  — hyphens/apostrophes removed, then exact/folded
  miss         — no DCS lemma; the note simply gets no collocate context

Usage:
  python3 scripts/appendix7_sense_qa.py [--csv PATH_TO_DCS_Sintagmatic.csv]

Stdlib only. Deterministic. Writes only under data/analysis/appendix7_sense_qa/.
"""
import argparse
import glob
import json
import os
import re
import sys
import unicodedata

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_CSV = os.path.join(
    os.path.dirname(REPO),
    "VisualDCS",
    "derived-data",
    "Lexical-Cores",
    "Prilozhenie-7.-«Sintagmaticheskaya-tablica-dlya-vseh-lemm-korpusa»v",
    "DCS_Sintagmatic.csv",
)
OUT_DIR = os.path.join(REPO, "data", "analysis", "appendix7_sense_qa")
TOP_N = 20  # collocates kept per note


def fold(s: str) -> str:
    s = unicodedata.normalize("NFC", s).lower()
    return s.replace("ṁ", "ṃ").replace("'", "’").replace("`", "’")


def load_appendix7(path: str):
    """lemma -> {'total': int, 'cooc': int, 'collocates': [[name, freq], ...]}"""
    table = {}
    with open(path, encoding="utf-8") as f:
        for lineno, line in enumerate(f, 1):
            line = line.rstrip("\n")
            if not line.strip():
                continue
            parts = line.split(";")
            if len(parts) < 4:
                raise ValueError(f"{path}:{lineno}: expected >=4 ;-fields, got {len(parts)}")
            lemma = parts[0].strip()
            total, cooc = int(parts[1]), int(parts[2])
            cols = []
            for cell in parts[3:]:
                cell = cell.strip()
                if not cell:
                    continue
                m = re.match(r"^(.+)\s+(\d+)$", cell)
                if not m:
                    raise ValueError(f"{path}:{lineno}: bad collocate cell {cell!r}")
                cols.append([m.group(1), int(m.group(2))])
            table[lemma] = {"total": total, "cooc": cooc, "collocates": cols}
    return table


def load_notes():
    notes = []
    for fp in sorted(glob.glob(os.path.join(REPO, "data", "lexical", "ch*.json"))):
        base = os.path.basename(fp)
        if ".rejected" in base or "qa_removed" in base:
            continue
        mch = re.search(r"ch(\d+)\.json", base)
        assert mch, f"unexpected filename: {base}"
        chapter = int(mch.group(1))
        with open(fp, encoding="utf-8") as f:
            data = json.load(f)
        for n in data:
            if "_meta" in n:
                continue
            notes.append(
                {
                    "chapter": chapter,
                    "shloka": n["shloka"],
                    "lemma_iast": n["lemma_iast"],
                    "note_ru_head": (n.get("note_ru") or "")[:180],
                    "judge_verdict": (n.get("judge") or {}).get("verdict", ""),
                    "review_required": bool(n.get("review_required")),
                }
            )
    return notes


def match(lemma: str, table, folded_idx, joined_idx):
    """Return (tier, dcs_lemma) or (None-tier, None).

    Tier truthfulness (H4709 verifier fix): `exact` is returned ONLY for a raw
    string identity with a DCS lemma; any hit via the fold index is `folded`,
    even when reached from the exact branch of the note's own spelling.
    """
    if lemma in table:
        return "exact", lemma
    f = fold(lemma)
    hit = folded_idx.get(f)
    if hit is not None:
        return "folded", hit
    stripped = re.sub(r"\s*\([^)]*\)\s*", "", lemma).strip()
    if stripped and stripped != lemma:
        if stripped in table:
            return "annotation", stripped
        hit = folded_idx.get(fold(stripped))
        if hit is not None:
            return "annotation", hit
    f2 = fold(lemma).replace("-", "").replace("’", "")
    if f2 in joined_idx:
        return "hyphen-join", joined_idx[f2]
    return "miss", None


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--csv", default=DEFAULT_CSV, help="path to DCS_Sintagmatic.csv")
    args = ap.parse_args()
    if not os.path.exists(args.csv):
        sys.exit(f"appendix7 CSV not found: {args.csv}")

    table = load_appendix7(args.csv)
    folded_idx = {}
    for l in table:
        folded_idx.setdefault(fold(l), l)
    joined_idx = {}
    for l in table:
        joined_idx.setdefault(fold(l).replace("-", "").replace("’", ""), l)

    notes = load_notes()
    records, tier_counts, covered_by_ch = [], {}, {}
    for n in notes:
        tier, dcs_lemma = match(n["lemma_iast"], table, folded_idx, joined_idx)
        tier_counts[tier] = tier_counts.get(tier, 0) + 1
        rec = dict(n)
        if dcs_lemma is not None:
            prof = table[dcs_lemma]
            rec.update(
                {
                    "match_tier": tier,
                    "dcs_lemma": dcs_lemma,
                    "dcs_total_occ": prof["total"],
                    "dcs_cooc": prof["cooc"],
                    "collocates_top": prof["collocates"][:TOP_N],
                }
            )
            covered_by_ch.setdefault(n["chapter"], 0)
            covered_by_ch[n["chapter"]] += 1
        else:
            rec.update({"match_tier": "miss", "dcs_lemma": None,
                        "dcs_total_occ": None, "dcs_cooc": None,
                        "collocates_top": []})
        records.append(rec)

    os.makedirs(OUT_DIR, exist_ok=True)
    out_doc = {
        "_meta": {
            "generated": "2026-09-15",
            "handoff": "H4709",
            "purpose": "QA context for Sundara lexical-note sense review: per-note DCS "
                       "collocate profile (kosha dataset dcs-sintagmatic-appendix7, CC BY-SA 4.0, "
                       "source VisualDCS derived-data/.../DCS_Sintagmatic.csv). A reviewer checking "
                       "note_ru sense claims reads dcs_total_occ/dcs_cooc/collocates_top as corpus-"
                       "usage context for the headword.",
            "source_csv_registered": "kosha data/manifest/datasets.json#dcs-sintagmatic-appendix7",
            "notes_total": len(records),
            "match_tiers": tier_counts,
            "top_n_collocates": TOP_N,
            "regen": "python3 scripts/appendix7_sense_qa.py",
        },
        "notes": records,
    }
    with open(os.path.join(OUT_DIR, "sundara_sense_qa_context.json"), "w", encoding="utf-8") as f:
        json.dump(out_doc, f, ensure_ascii=False, indent=1)

    cov = {
        "notes_total": len(records),
        "unique_lemmas": len({n["lemma_iast"] for n in notes}),
        "covered_notes": tier_counts.get("exact", 0) + tier_counts.get("folded", 0)
                         + tier_counts.get("annotation", 0) + tier_counts.get("hyphen-join", 0),
        "match_tiers": tier_counts,
        "chapters_with_any_match": len(covered_by_ch),
        "per_chapter_covered": dict(sorted(covered_by_ch.items())),
    }
    cov["coverage_pct"] = round(100.0 * cov["covered_notes"] / cov["notes_total"], 1)
    with open(os.path.join(OUT_DIR, "coverage_stats.json"), "w", encoding="utf-8") as f:
        json.dump(cov, f, ensure_ascii=False, indent=1)

    print(json.dumps(cov, ensure_ascii=False, indent=1))
    print(f"wrote {OUT_DIR}/sundara_sense_qa_context.json ({len(records)} notes)")


if __name__ == "__main__":
    main()
