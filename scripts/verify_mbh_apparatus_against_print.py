#!/usr/bin/env python3
"""H810 — independent verification of the H784/H802/H804 MBh edition-apparatus
review-gate flags (vulgate structural absences + whole extra adhyayas) against
the ACTUAL BORI critical-edition apparatus (App. I "star passages",
mahabharata-nilakantha/bori-apps/Supp{NN}.txt, fetched from
bombay.indology.info/mahabharata/apps/UR/ -- the same critical-edition project
that produced the base MBh{NN}.txt text).

Method: the anchor comments in Supp##.txt ("After 3.1.10, S ins.:") are
heavily-wrapped philological prose -- too fragile to parse reliably. Instead,
each star-passage's TEXT is grouped by its passage id (parvaNo*NNNN, ignoring
the _LL line suffix) into a candidate-interpolation pool, canon-normalized the
same way as compare_editions_mbh.py, and matched against every vulgate
structural_absence entry (+ a sample of each whole extra-adhyaya) by token
Jaccard -- the SAME similarity method already used for the fuzzy-pairing step
in the comparator, just applied to a third, independent witness pool.

A high-Jaccard match means: this "vulgate-only" passage the comparator
flagged corresponds to a manuscript reading the BORI editors themselves
collated and relegated to the apparatus -- independent confirmation it is a
real recension difference, not an alignment artifact. A miss does not mean
the flag is wrong (App. I is drawn from the manuscripts BORI collated, not
exhaustively every vulgate print edition) -- it means "not corroborated by
this particular independent source", which is reported as such.

Usage: python scripts/verify_mbh_apparatus_against_print.py [PARVA_NO ...]
       (default: all 18)
"""
import sys
import os
import re
import json
import difflib
import bisect
from collections import defaultdict

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
APPS_DIR = os.path.join(REPO, "mahabharata-nilakantha", "bori-apps")
sys.path.insert(0, HERE)
from sa_align import canon as norm  # noqa: E402

# Word-token Jaccard was tried first and badly penalized compound-spacing
# differences: the vulgate source is sandhi-fused Devanagari (no internal
# spaces in compounds), App. I is a scholarly Roman transcription that DOES
# space out compounds -- so e.g. "daivavrṛndaiḥ" (1 vulgate token)
# vs "deva vrṛndaiḥ" (2 App.I tokens) tanks word-Jaccard even for a
# near-identical reading. canon() already strips spaces along with
# diacritics/punctuation for character-level work, so a plain character
# SequenceMatcher ratio on the FULLY DESPACED canon string sidesteps
# tokenization entirely -- same family of method compare_editions_mbh.py
# itself uses for its primary (non-fuzzy) alignment.

PARVA_NAMES = {
    1: "adiparva", 2: "sabhaparva", 3: "vanaparva", 4: "virataparva",
    5: "udyogaparva", 6: "bhishmaparva", 7: "dronaparva", 8: "karnaparva",
    9: "shalyaparva", 10: "sauptikaparva", 11: "striparva", 12: "shantiparva",
    13: "anushasanaparva", 14: "ashwamedhikaparva", 15: "ashramavasikaparva",
    16: "mausalaparva", 17: "mahaprasthanikaparva", 18: "swargarohanaparva",
}

STAR_LINE_RE = re.compile(r"^(\d{2})\*(\d{4})_(\d{2})\s+(.+)$")


def load_supp_passages(parva_no):
    """-> list of (passage_id, text) for this parva's App. I star passages,
    text lines grouped by (parva, NNNN), ignoring the _LL line suffix."""
    path = os.path.join(APPS_DIR, f"Supp{parva_no:02d}.txt")
    groups = {}
    order = []
    for line in open(path, encoding="utf-8", errors="replace"):
        line = line.rstrip("\n")
        m = STAR_LINE_RE.match(line)
        if not m:
            continue
        pp, nnnn, _ll, body = m.groups()
        if int(pp) != parva_no:
            continue
        if nnnn not in groups:
            groups[nnnn] = []
            order.append(nnnn)
        groups[nnnn].append(body.strip())
    return [(nnnn, " ".join(groups[nnnn])) for nnnn in order]


# Calibrated by spot-check (not guessed): manually inspected matches at 0.35-0.45,
# 0.55-0.65 and 0.95-1.0 n-gram-Jaccard bands on Vanaparva were ALL genuine same-
# passage matches -- low scores in the 0.3-0.5 range are usually partial matches
# where the vulgate structural_absence query bundles more verse content (e.g. a
# speaker tag, or an adjacent pada) than the specific App. I passage covers, which
# a symmetric Jaccard penalizes even though the shared portion matches verbatim.
# SIM_CONFIRM is the primary "confirmed" cutoff; TIERS are reported for transparency
# rather than presenting one binary number.
SIM_CONFIRM = 0.3
TIERS = [0.3, 0.5, 0.7, 0.9]


def nospace(s):
    return s.replace(" ", "")


NGRAM = 4


def ngrams(s):
    if len(s) < NGRAM:
        return {s} if s else set()
    return {s[i:i + NGRAM] for i in range(len(s) - NGRAM + 1)}


class NgramIndex:
    """Inverted index (n-gram -> candidate indices) over a candidate pool.
    Sanskrit verses cluster tightly in length, so length-bucketing barely
    shrinks the candidate set (tried first, too slow); n-gram Jaccard is a
    pure set-intersection op (no O(n*m) DP like SequenceMatcher.ratio) and
    the inverted index means a query only ever touches candidates that
    share at least one n-gram with it, which for despaced Sanskrit text is
    a small fraction of the pool unless the texts are genuinely similar."""
    def __init__(self, strs):
        self.strs = strs
        self.grams = [ngrams(s) for s in strs]
        self.inverted = defaultdict(set)
        for i, gs in enumerate(self.grams):
            for g in gs:
                self.inverted[g].add(i)

    def candidate_indices(self, query_grams):
        cands = set()
        for g in query_grams:
            cands |= self.inverted.get(g, set())
        return cands


def best_match(query_str, pool_index):
    """N-gram Jaccard on fully despaced canon strings, via an inverted index
    so only candidates sharing at least one n-gram are ever scored -- the
    compound word-boundary differences between the vulgate source and
    App. I's transcription don't matter once spaces are stripped."""
    if not query_str:
        return None, 0.0
    qg = ngrams(query_str)
    if not qg:
        return None, 0.0
    best_i, best_j = None, 0.0
    for i in pool_index.candidate_indices(qg):
        cg = pool_index.grams[i]
        if not cg:
            continue
        inter = len(qg & cg)
        if inter == 0:
            continue
        j = inter / len(qg | cg)
        if j > best_j:
            best_i, best_j = i, j
    return best_i, best_j


def verify_parva(parva_no):
    slug = PARVA_NAMES[parva_no]
    outdir = os.path.join(REPO, "data", "edition_comparison_mbh", slug)
    sa = json.load(open(os.path.join(outdir, "significant_absences.json"), encoding="utf-8"))
    bs = json.load(open(os.path.join(outdir, "book_summary.json"), encoding="utf-8"))

    supp = load_supp_passages(parva_no)
    supp_ids = [pid for pid, _ in supp]
    supp_strs = [nospace(norm(t)) for _, t in supp]
    pool_index = NgramIndex(supp_strs)

    # ---- structural_absence verses: individually matched ----
    struct_abs = sa["structural_absence"]
    results = []
    for r in struct_abs:
        qs = nospace(norm(r["text"]))
        if not qs:
            results.append({"vulgate": r["vulgate"], "best_sim": 0.0, "matched_supp": None})
            continue
        bi, bj = best_match(qs, pool_index)
        results.append({"vulgate": r["vulgate"], "best_sim": round(bj, 2),
                        "matched_supp": supp_ids[bi] if bi is not None else None})
    confirmed = [r for r in results if r["best_sim"] >= SIM_CONFIRM]

    # ---- whole extra adhyayas: sample-verified (all verses checked, report % confirmed) ----
    extra_adhy = bs["book_totals"]["vulgate_extra_adhyayas"]
    extra_adhy_stats = {}
    if extra_adhy:
        vulg_path = os.path.join(REPO, "mahabharata-nilakantha", "nilakantha_vulgate_full.jsonl")
        from sa_align import deva_to_iast
        adhy_set = set(extra_adhy)
        verses_by_adhy = defaultdict(list)
        for line in open(vulg_path, encoding="utf-8"):
            line = line.strip()
            if not line:
                continue
            d = json.loads(line)
            if d.get("parva_no") != parva_no:
                continue
            a = d.get("adhyaya")
            if a not in adhy_set:
                continue
            mula = d.get("mula_dev") or ""
            if not mula.strip():
                continue
            verses_by_adhy[a].append(deva_to_iast(mula.replace("\n", " ")))
        for a in sorted(adhy_set):
            vv = verses_by_adhy.get(a, [])
            n_conf = 0
            for t in vv:
                qs = nospace(norm(t))
                if not qs:
                    continue
                _, bj = best_match(qs, pool_index)
                if bj >= SIM_CONFIRM:
                    n_conf += 1
            extra_adhy_stats[a] = {"verses": len(vv), "confirmed": n_conf}

    tier_counts = {t: sum(1 for r in results if r["best_sim"] >= t) for t in TIERS}

    return {
        "parva": parva_no, "slug": slug,
        "supp_passages": len(supp),
        "structural_absence_total": len(struct_abs),
        "structural_absence_confirmed": len(confirmed),
        "structural_absence_confirm_rate": round(len(confirmed) / len(struct_abs), 3) if struct_abs else None,
        "tier_counts": tier_counts,
        "extra_adhyayas": extra_adhy_stats,
        "results": results,
    }


def main():
    parvas = [int(a) for a in sys.argv[1:]] or list(range(1, 19))
    outdir = os.path.join(REPO, "data", "edition_comparison_mbh")
    all_stats = []
    for n in parvas:
        print(f"\n===== parva {n} ({PARVA_NAMES[n]}) =====", flush=True)
        stats = verify_parva(n)
        all_stats.append(stats)
        slug = stats["slug"]
        json.dump({"_meta": {
                       "note": "Independent verification of structural_absence flags against "
                               "the BORI critical edition's own App. I star-passage apparatus "
                               "(bombay.indology.info Supp##.txt). 4-gram character Jaccard on "
                               "fully despaced canon strings (robust to compound word-boundary "
                               "differences between the vulgate source and App. I's transcription; "
                               "calibrated by manual spot-check, not guessed -- see script "
                               "docstring). best_sim >= 0.3 counts as 'confirmed by App. I'; tier "
                               "breakdown at 0.3/0.5/0.7/0.9 reported for transparency instead of "
                               "one binary cutoff. A miss does NOT mean the flag is wrong -- App. I "
                               "reflects the manuscripts BORI collated, not exhaustively every "
                               "vulgate print edition.",
                       "sim_confirm_threshold": SIM_CONFIRM, "tiers": TIERS,
                       "method": "4-gram character Jaccard, despaced canon, inverted-index candidate lookup",
                       "supp_source": "https://bombay.indology.info/mahabharata/apps/UR/",
                   },
                   "structural_absence_total": stats["structural_absence_total"],
                   "structural_absence_confirmed": stats["structural_absence_confirmed"],
                   "structural_absence_confirm_rate": stats["structural_absence_confirm_rate"],
                   "tier_counts": stats["tier_counts"],
                   "extra_adhyayas": stats["extra_adhyayas"],
                   "per_verse": stats["results"]},
                  open(os.path.join(outdir, slug, "print_verification.json"), "w", encoding="utf-8"),
                  ensure_ascii=False, indent=2)
        print(f"structural_absence: {stats['structural_absence_confirmed']}/{stats['structural_absence_total']} "
              f"confirmed ({stats['structural_absence_confirm_rate']}) | tiers: {stats['tier_counts']}")
        if stats["extra_adhyayas"]:
            tot_v = sum(v["verses"] for v in stats["extra_adhyayas"].values())
            tot_c = sum(v["confirmed"] for v in stats["extra_adhyayas"].values())
            print(f"extra_adhyayas: {tot_c}/{tot_v} verses confirmed across "
                  f"{len(stats['extra_adhyayas'])} adhyayas")

    print("\n\n===== VERIFICATION SUMMARY =====")
    tot_abs = sum(s["structural_absence_total"] for s in all_stats)
    tot_conf = sum(s["structural_absence_confirmed"] for s in all_stats)
    tot_tiers = {t: sum(s["tier_counts"][t] for s in all_stats) for t in TIERS}
    for s in all_stats:
        print(f"parva {s['parva']:2d} {s['slug']:22s} "
              f"struct_abs={s['structural_absence_total']:5d} confirmed={s['structural_absence_confirmed']:5d} "
              f"rate={s['structural_absence_confirm_rate']}")
    print(f"\nTOTAL: {tot_conf}/{tot_abs} structural-absence flags confirmed by App. I "
          f"({round(tot_conf/tot_abs, 3) if tot_abs else 'n/a'})")
    print("Tier breakdown (>= threshold):",
          {t: f"{tot_tiers[t]} ({round(tot_tiers[t]/tot_abs, 3)})" for t in TIERS} if tot_abs else "n/a")


if __name__ == "__main__":
    main()
