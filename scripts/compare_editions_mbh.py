#!/usr/bin/env python3
"""Compare the BORI/Poona CRITICAL edition vs the Nīlakaṇṭha VULGATE for one
Mahābhārata parva — the MBh half of the edition-apparatus rollout
(docs/EDITION_APPARATUS_ROLLOUT.md), generalizing scripts/compare_editions.py
(built for Rāmāyaṇa Sundarakāṇḍa) to a pluggable (critical_loader,
vulgate_loader, verse_id_scheme) per H784.

Produces the same 4-file output shape as compare_editions.py so downstream
tooling (build_edition_apparatus.py, build_edition_footnotes.py) needs no
further changes: verse ids on BOTH sides are emitted as "parva.adhyaya.verse"
(3 dot-separated ints) — the same shape as Rāmāyaṇa's "5.sarga.verse", so
verse_key() in build_edition_apparatus.py parses MBh ids unchanged.

Sources (read-only):
  critical = mahabharata-nilakantha/bori-critical/MBh{parva:02d}.txt
             (BORI/Poona critical ed., John Smith/Tokunaga e-text, ISO-15919
             Roman; addressing PPAAASSSh — parva+adhyaya+śloka+half-letter).
             GITIGNORED, local-only — see BORI_CRITICAL_SOURCE.md.
  vulgate  = mahabharata-nilakantha/nilakantha_vulgate_full.jsonl
             (Nīlakaṇṭha-vulgate scrape; P/U/A/S addressing; mula_dev is
             Devanagari — transliterated to IAST via sa_align.deva_to_iast).
             GITIGNORED, local-only — see NILAKANTHA_VULGATE_CENSUS.md.

Deterministic, stdlib-only (difflib). Outputs under
data/edition_comparison_mbh/<parva_slug>/.
Usage: python scripts/compare_editions_mbh.py [PARVA_NO]   (default 3, vana)
"""
import sys
import os
import re
import json
import unicodedata
from difflib import SequenceMatcher
from collections import Counter, defaultdict

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
BORI_DIR = os.path.join(REPO, "mahabharata-nilakantha", "bori-critical")
VULGATE_PATH = os.path.join(REPO, "mahabharata-nilakantha", "nilakantha_vulgate_full.jsonl")

sys.path.insert(0, HERE)
from sa_align import canon as norm, deva_to_iast, backend as _align_backend  # noqa: E402

PARVA_NAMES = {
    1: "adiparva", 2: "sabhaparva", 3: "vanaparva", 4: "virataparva",
    5: "udyogaparva", 6: "bhishmaparva", 7: "dronaparva", 8: "karnaparva",
    9: "shalyaparva", 10: "sauptikaparva", 11: "striparva", 12: "shantiparva",
    13: "anushasanaparva", 14: "ashwamedhikaparva", 15: "ashramavasikaparva",
    16: "mausalaparva", 17: "mahaprasthanikaparva", 18: "swargarohanaparva",
}

# BORI line: 2-digit parva + 3-digit adhyaya + 3-digit sloka + optional
# half-verse letter (a/c, occasionally e for tristubh-length extra pada),
# then whitespace, then the reading. A bare 8-digit id (no letter) marks a
# speaker/uvaca tag line — folded into the same verse's text.
BORI_LINE_RE = re.compile(r"^(\d{2})(\d{3})(\d{3})([a-zA-Z]?)\s+(.+)$")


def iso15919_to_iast(text):
    """Normalize the BORI e-text's ISO-15919 Roman quirks to IAST for display
    (canon() strips diacritics anyway, so this only affects readability):
    anusvara ṁ -> ṃ; vocalic r/l as NFD base+combining-ring -> precomposed IAST.

    The vocalic-r/l step was previously a no-op despite this docstring's own
    claim: ISO-15919 spells vocalic r/l as base letter + COMBINING RING BELOW
    (U+0325), which has no Unicode canonical-equivalence to IAST's precomposed
    dot-below forms (ṛ U+1E5B / ḷ U+1E37), so plain NFC never unifies them.
    The vulgate side (Devanagari -> IAST via sa_align.deva_to_iast) emits the
    precomposed forms directly, so every ISO-15919 r̥/l̥ in the critical text
    silently mismatched the vulgate's ṛ/ḷ at comparison time -- found via H830
    (MBh apparatus regeneration): ~1000+ occurrences per parva, inflating the
    akṣara-level apparatus with spurious encoding-only loci. Long forms add a
    combining macron (U+0304) after the ring; replaced before the short forms
    so the macron isn't stranded."""
    t = unicodedata.normalize("NFC", text)
    t = t.replace("ṁ", "ṃ")   # ṁ (U+1E41) -> ṃ (U+1E43)
    t = t.replace("ṅ", "ṇ")   # ṅ-with-ring edge case, if any -> ṇ-family untouched
    t = t.replace("r̥̄", "ṝ")  # r̥̄ (long vocalic r) -> ṝ
    t = t.replace("l̥̄", "ḹ")  # l̥̄ (long vocalic l) -> ḹ
    t = t.replace("r̥", "ṛ")        # r̥ (short vocalic r) -> ṛ
    t = t.replace("l̥", "ḷ")        # l̥ (short vocalic l) -> ḷ
    return t


def load_critical(parva_no):
    """-> ordered list of (adhyaya, verse, text)."""
    path = os.path.join(BORI_DIR, f"MBh{parva_no:02d}.txt")
    halves = {}
    order = []
    for line in open(path, encoding="utf-8", errors="replace"):
        line = line.rstrip("\n")
        if not line or line.startswith("%"):
            continue
        m = BORI_LINE_RE.match(line)
        if not m:
            continue
        pp, aaa, sss, _pada, body = m.groups()
        if int(pp) != parva_no:
            continue
        key = (int(aaa), int(sss))
        if key not in halves:
            halves[key] = []
            order.append(key)
        halves[key].append(iso15919_to_iast(body.strip()))
    return [(a, v, " ".join(halves[(a, v)])) for a, v in order]


def load_vulgate(parva_no):
    """-> ordered list of (adhyaya, shloka, iast_text). Adhyaya numbers are
    continuous across upaparvas within a parva (verified empirically), so
    sorting by (adhyaya, shloka) alone reproduces reading order."""
    verses = []
    for line in open(VULGATE_PATH, encoding="utf-8"):
        line = line.strip()
        if not line:
            continue
        d = json.loads(line)
        if d.get("parva_no") != parva_no:
            continue
        a, s = d.get("adhyaya"), d.get("shloka")
        mula = d.get("mula_dev") or ""
        if a is None or s is None or not mula.strip():
            continue
        iast = deva_to_iast(mula.replace("\n", " "))
        verses.append((a, s, iast))
    verses.sort(key=lambda x: (x[0], x[1]))
    return verses


def per_chapter_counts(verses):
    return Counter(a for a, v, t in verses)


def main():
    parva_no = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    slug = PARVA_NAMES[parva_no]
    outdir = os.path.join(REPO, "data", "edition_comparison_mbh", slug)
    os.makedirs(outdir, exist_ok=True)

    crit = load_critical(parva_no)
    vulg = load_vulgate(parva_no)

    cc, vc = per_chapter_counts(crit), per_chapter_counts(vulg)
    all_adhy = sorted(set(cc) | set(vc))
    per_adhyaya = [{
        "adhyaya": a,
        "critical_verses": cc.get(a, 0),
        "vulgate_verses": vc.get(a, 0),
        "delta_vulgate_minus_critical": vc.get(a, 0) - cc.get(a, 0),
        "only_in_one_edition": (cc.get(a, 0) == 0) or (vc.get(a, 0) == 0),
    } for a in all_adhy]

    # ---- content alignment at BOOK level (robust to adhyaya renumbering) ----
    cn = [norm(t) for _, _, t in crit]
    vn = [norm(t) for _, _, t in vulg]
    sm = SequenceMatcher(a=cn, b=vn, autojunk=False)

    concordance = []
    vulgate_only = []
    crit_only = []
    variants = []
    identical = 0

    def cid(i):
        a, v, t = crit[i]
        return {"critical": f"{parva_no}.{a}.{v}", "text": t}

    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1):
                identical += 1
                concordance.append({"status": "identical",
                                    "critical": f"{parva_no}.{crit[i1+k][0]}.{crit[i1+k][1]}",
                                    "vulgate": f"{parva_no}.{vulg[j1+k][0]}.{vulg[j1+k][1]}"})
        elif tag == "insert":
            for j in range(j1, j2):
                a, v, t = vulg[j]
                vulgate_only.append({"vulgate": f"{parva_no}.{a}.{v}", "text": t})
                concordance.append({"status": "vulgate_only", "vulgate": f"{parva_no}.{a}.{v}"})
        elif tag == "delete":
            for i in range(i1, i2):
                a, v, t = crit[i]
                crit_only.append({"critical": f"{parva_no}.{a}.{v}", "text": t})
                concordance.append({"status": "critical_only", "critical": f"{parva_no}.{a}.{v}"})
        elif tag == "replace":
            ci, vj = list(range(i1, i2)), list(range(j1, j2))
            used_v = set()
            sm2 = SequenceMatcher(autojunk=False)
            for i in ci:
                sm2.set_seq2(cn[i])
                best, bestr = None, 0.0
                for j in vj:
                    if j in used_v:
                        continue
                    sm2.set_seq1(vn[j])
                    floor = max(bestr, 0.6)
                    if sm2.real_quick_ratio() < floor or sm2.quick_ratio() < floor:
                        continue
                    r = sm2.ratio()
                    if r > bestr:
                        best, bestr = j, r
                if best is not None and bestr >= 0.6:
                    used_v.add(best)
                    a2, v2, t2 = vulg[best]
                    variants.append({"critical": f"{parva_no}.{crit[i][0]}.{crit[i][1]}",
                                     "vulgate": f"{parva_no}.{a2}.{v2}",
                                     "similarity": round(bestr, 2),
                                     "critical_text": crit[i][2], "vulgate_text": t2})
                    concordance.append({"status": "variant",
                                        "critical": f"{parva_no}.{crit[i][0]}.{crit[i][1]}",
                                        "vulgate": f"{parva_no}.{a2}.{v2}",
                                        "similarity": round(bestr, 2)})
                else:
                    crit_only.append(cid(i))
                    concordance.append({"status": "critical_only",
                                        "critical": f"{parva_no}.{crit[i][0]}.{crit[i][1]}"})
            for j in vj:
                if j not in used_v:
                    a, v, t = vulg[j]
                    vulgate_only.append({"vulgate": f"{parva_no}.{a}.{v}", "text": t})
                    concordance.append({"status": "vulgate_only", "vulgate": f"{parva_no}.{a}.{v}"})

    # ---- reclassify TRANSPOSITIONS (moved, not absent) ----
    c_canons, v_canons = set(cn), set(vn)
    transposed_vulgate = [r for r in vulgate_only if norm(r["text"]) in c_canons]
    vulgate_only = [r for r in vulgate_only if norm(r["text"]) not in c_canons]
    transposed_critical = [r for r in crit_only if norm(r["text"]) in v_canons]
    crit_only = [r for r in crit_only if norm(r["text"]) not in v_canons]

    # ---- fuzzy global assignment: pair mutually-unmatched verses by token
    #      Jaccard (recovers near-variant counterparts the book-level LCS
    #      orphaned; the rest are true absences) ----
    co_sets = [set(norm(r["text"]).split()) for r in crit_only]
    vo_sets = [set(norm(r["text"]).split()) for r in vulgate_only]
    JACCARD_MIN, INTER_MIN = 0.5, 3
    fuzzy_pairs = []
    used_v = set()
    keep_crit = []
    for i, cr in enumerate(crit_only):
        a = co_sets[i]
        best, bestr = None, 0.0
        if a:
            for j, b in enumerate(vo_sets):
                if j in used_v or not b:
                    continue
                inter = len(a & b)
                if inter < INTER_MIN:
                    continue
                jac = inter / len(a | b)
                if jac > bestr:
                    best, bestr = j, jac
        if best is not None and bestr >= JACCARD_MIN:
            used_v.add(best)
            fuzzy_pairs.append({"critical": cr["critical"], "vulgate": vulgate_only[best]["vulgate"],
                                "similarity": round(bestr, 2), "kind": "fuzzy_variant",
                                "critical_text": cr["text"], "vulgate_text": vulgate_only[best]["text"]})
        else:
            keep_crit.append(cr)
    crit_only = keep_crit
    vulgate_only = [r for j, r in enumerate(vulgate_only) if j not in used_v]
    variants = variants + fuzzy_pairs

    # ---- partition vulgate-only: TRUE structural absence vs REWORDED ----
    crit_sets = [set(c.split()) for c in cn]
    for r in vulgate_only:
        a = set(norm(r["text"]).split())
        best = 0.0
        for b in crit_sets:
            if not b:
                continue
            inter = len(a & b)
            if inter < 2:
                continue
            j = inter / len(a | b)
            if j > best:
                best = j
        r["best_crit_jaccard"] = round(best, 2)
        r["divergence"] = "structural_absence" if best < 0.25 else "reworded"
    structural_absence = [r for r in vulgate_only if r["divergence"] == "structural_absence"]
    reworded_vulgate = [r for r in vulgate_only if r["divergence"] == "reworded"]

    # group vulgate-only into contiguous runs (footnote candidates)
    vo_sorted = sorted(vulgate_only, key=lambda r: tuple(int(x) for x in r["vulgate"].split(".")[1:]))
    runs = []
    for r in vo_sorted:
        a, v = (int(x) for x in r["vulgate"].split(".")[1:])
        if runs and runs[-1]["adhyaya"] == a and v == runs[-1]["_last"] + 1:
            runs[-1]["verses"].append(v)
            runs[-1]["_last"] = v
        else:
            runs.append({"adhyaya": a, "verses": [v], "_last": v})
    for run in runs:
        run["range"] = f"{parva_no}.{run['adhyaya']}.{run['verses'][0]}" + (
            f"–{run['verses'][-1]}" if len(run["verses"]) > 1 else "")
        run["count"] = len(run["verses"])
        del run["_last"]

    # ---- derive ADHYAYA correspondence from verse alignment ----
    votes = defaultdict(Counter)
    for row in concordance:
        if row["status"] in ("identical", "variant") and "critical" in row and "vulgate" in row:
            ca = int(row["critical"].split(".")[1])
            va = int(row["vulgate"].split(".")[1])
            votes[ca][va] += 1
    crit_to_vulg = {ca: c.most_common(1)[0][0] for ca, c in votes.items()}
    mapped_vulg = set(crit_to_vulg.values())
    per_adhyaya_aligned = []
    for a in sorted(cc):
        ja = crit_to_vulg.get(a)
        per_adhyaya_aligned.append({
            "critical_adhyaya": a, "critical_verses": cc.get(a, 0),
            "vulgate_adhyaya": ja, "vulgate_verses": vc.get(ja, 0) if ja else 0,
            "delta_vulgate_minus_critical": (vc.get(ja, 0) if ja else 0) - cc.get(a, 0),
        })
    vulgate_extra_adhyayas = sorted(set(vc) - mapped_vulg)

    summary = {
        "_meta": {
            "generated_by": "scripts/compare_editions_mbh.py",
            "critical": f"BORI/Poona critical edition (MBh{parva_no:02d}.txt, John Smith/Tokunaga e-text)",
            "vulgate": "Nilakantha vulgate (sanatana.in scrape, mula only)",
            "parva": slug, "parva_no": parva_no,
            "method": "content alignment of canonicalized IAST verses (difflib), book-level",
            "canon_backend": _align_backend(),
            "canon": "sanskrit_util.nfold (diacritics/length stripped, nasals folded->n)",
        },
        "book_totals": {
            "critical_verses": len(crit),
            "vulgate_verses": len(vulg),
            "delta_vulgate_minus_critical": len(vulg) - len(crit),
            "critical_adhyayas": len(cc),
            "vulgate_adhyayas": len(vc),
            "identical_verses": identical,
            "variant_verses": len(variants),
            "fuzzy_paired_verses": len(fuzzy_pairs),
            "vulgate_only_verses": len(vulgate_only),
            "vulgate_structural_absence": len(structural_absence),
            "vulgate_reworded": len(reworded_vulgate),
            "critical_only_verses": len(crit_only),
            "transposed_vulgate_verses": len(transposed_vulgate),
            "transposed_critical_verses": len(transposed_critical),
            "vulgate_only_runs": len(runs),
            "vulgate_extra_adhyayas": vulgate_extra_adhyayas,
        },
        "per_adhyaya_aligned": per_adhyaya_aligned,
        "vulgate_extra_adhyayas": vulgate_extra_adhyayas,
        "per_adhyaya_by_number_RAW": per_adhyaya,
        "_caveat": "Use per_adhyaya_aligned (adhyayas matched by verse content). "
                   "per_adhyaya_by_number_RAW compares by adhyaya NUMBER and is misleading "
                   "once numbering diverges. identical/variant/only counts are content-based; "
                   "near-identical verses with minor orthographic/sandhi differences inflate "
                   "'variant' and 'only' buckets — the reliable absence signal is the large "
                   "contiguous vulgate_only runs.",
    }

    json.dump(summary, open(os.path.join(outdir, "book_summary.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    json.dump({"_meta": summary["_meta"], "concordance": concordance},
              open(os.path.join(outdir, "concordance.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    json.dump({"_meta": {"note": "Vulgate verses/passages not aligned to critical. Each carries "
                                 "`divergence`: 'structural_absence' (best token-Jaccard vs any "
                                 "critical verse < 0.25 -- genuinely absent) or 'reworded' "
                                 "(0.25-0.5 -- same verse present but heavily reworded, a variant "
                                 "reading, NOT an absence). Prefer structural_absence + whole extra "
                                 "adhyayas for footnotes.",
                         "structural_absence_verses": len(structural_absence),
                         "reworded_verses": len(reworded_vulgate)},
               "runs": runs,
               "structural_absence": structural_absence,
               "reworded": reworded_vulgate},
              open(os.path.join(outdir, "significant_absences.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    json.dump({"_meta": {"note": "Critical verses truly absent in vulgate (canon nowhere in "
                                 "vulgate) + word-variant pairs + transpositions (same canon, "
                                 "different position)."},
               "critical_only": crit_only, "variants": variants,
               "transposed_vulgate": transposed_vulgate,
               "transposed_critical": transposed_critical},
              open(os.path.join(outdir, "critical_only_and_variants.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)

    bt = summary["book_totals"]
    print(f"=== {slug} (parva {parva_no}) ===")
    print("BOOK:", json.dumps(bt, ensure_ascii=False))
    print(f"adhyayas: critical {bt['critical_adhyayas']} vs vulgate {bt['vulgate_adhyayas']}")
    print(f"vulgate EXTRA adhyayas (no critical counterpart): {vulgate_extra_adhyayas}")
    print(f"vulgate-only runs (footnote candidates): {len(runs)}; "
          f"largest: " + ", ".join(f"{r['range']}({r['count']})" for r in sorted(runs, key=lambda x: -x['count'])[:5]))
    print(f"wrote 4 files -> {outdir}")


if __name__ == "__main__":
    main()
