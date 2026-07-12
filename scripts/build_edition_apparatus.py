#!/usr/bin/env python3
"""Book-wide Critical↔Southern VARIANT APPARATUS for the Sundarakāṇḍa.

Runs the helayo-style aligner (spike_helayo_align: Gotoh affine-gap +
consonant/vowel substitution matrix) over ALL committed variant pairs in
data/edition_comparison/critical_only_and_variants.json — every aligned verse
where the Baroda critical edition and the southern vulgate differ in wording —
and emits a positional apparatus: per verse, the competing readings (lemma ]
variant), in standard apparatus notation.

This is the concrete "collation engine + apparatus backbone" applied to the whole
book, not just the spike sargas. It covers the VARIANT-READING layer (1043 aligned
pairs); whole-passage differences (structural absences / critical-only) are a
separate footnote layer already produced by build_edition_footnotes.py.

Outputs (under data/analysis/helayo_spike/):
  apparatus_sundara_variants.json  — full machine-readable apparatus, all loci
  APPARATUS_SUNDARA_VARIANTS.md    — human-readable digest: per-sarga counts +
                                     the substantive (multi-akṣara) loci sample

Stdlib-only. Read-only inputs. Usage: python build_edition_apparatus.py
"""
import sys
import os
import json

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from spike_helayo_align import clean, gotoh, collapse_loci  # noqa: E402


def verse_key(vid):
    p = vid.split(".")
    return (int(p[1]), int(p[2]))


def substantive(c, s):
    """A locus worth an apparatus note: at least one side has ≥2 chars of real
    divergence (filters single-phoneme sandhi/orthographic flicker)."""
    return max(len(c), len(s)) >= 2


# clean-apparatus similarity gate: below this, difflib+alignment agree the verse is
# heavily REWORDED (many loci) — not a clean variant; itemising it just adds noise,
# it belongs to the absence/footnote layer. Threshold from the spike (0.9+ = clean
# single-word variants; ~0.64 = reworded).
CLEAN_SIM = 0.8

_CYRILLIC = set("абвгдежзийклмнопрстуфхцчшщъыьэюяёАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯЁ")


def has_cyrillic(text):
    return any(ch in _CYRILLIC for ch in (text or ""))


def main():
    repo = os.environ.get("CS_REPO",
                          r"C:/Users/user/Documents/GitHub/CommentaryStrategies")
    cvp = os.path.join(repo, "data", "edition_comparison",
                       "critical_only_and_variants.json")
    cv = json.load(open(cvp, encoding="utf-8"))
    pairs = [v for v in cv["variants"]
             if "critical_text" in v and "southern_text" in v]
    pairs.sort(key=lambda v: verse_key(v["critical"]))

    entries = []
    reworded = []          # sim < CLEAN_SIM — routed to the absence/footnote layer
    contaminated = []      # source verses with Cyrillic contamination (data bug)
    from collections import Counter, defaultdict
    per_sarga = defaultdict(lambda: {"verses": 0, "loci": 0})
    loci_hist = Counter()
    total_loci = 0
    for v in pairs:
        ct, st = clean(v["critical_text"]), clean(v["southern_text"])
        if has_cyrillic(ct) or has_cyrillic(st):
            contaminated.append({"critical": v["critical"], "southern": v["southern"],
                                 "critical_text": ct, "southern_text": st})
            continue
        sim = v.get("similarity") or 0.0
        if sim < CLEAN_SIM:
            reworded.append({"critical": v["critical"], "southern": v["southern"],
                             "difflib_similarity": sim})
            continue
        _, aa, bb = gotoh(ct, st)
        loci = collapse_loci(aa, bb, ct, st)
        app = [{"crit": c or "∅", "south": s or "∅"}
               for c, s in loci if substantive(c, s)]
        if not app:
            continue                       # difflib flagged variant; matrix says none
        sg = verse_key(v["critical"])[0]
        per_sarga[sg]["verses"] += 1
        per_sarga[sg]["loci"] += len(app)
        loci_hist[len(app)] += 1
        total_loci += len(app)
        entries.append({
            "critical": v["critical"], "southern": v["southern"],
            "difflib_similarity": v.get("similarity"),
            "kind": v.get("kind", "lcs-variant"),
            "n_loci": len(app), "apparatus": app,
        })

    out = {
        "_meta": {
            "title": "Sundarakāṇḍa — Critical (Baroda) ↔ Southern vulgate variant apparatus",
            "generated_by": "build_edition_apparatus.py (helayo-style Gotoh aligner)",
            "layer": "variant readings on aligned verses (NOT whole-passage absences)",
            "aligner": "char-level Gotoh affine-gap + consonant/vowel/modifier "
                       "substitution matrix; loci word-expanded",
            "witnesses": 2,
            "note": "2-witness collation; Center-Star MSA advantage latent until a "
                    "3rd witness (Gita Press) is digitised. Reworded southern-only "
                    "verses (435) not included — their critical counterpart text is "
                    "absent from the committed data.",
        },
        "totals": {
            "clean_variant_verses": len(entries),
            "apparatus_loci": total_loci,
            "sargas": len(per_sarga),
            "loci_per_verse_hist": dict(sorted(loci_hist.items())),
            "reworded_verses_routed_to_footnote_layer": len(reworded),
            "cyrillic_contaminated_verses": len(contaminated),
            "input_variant_pairs": len(pairs),
            "clean_sim_gate": CLEAN_SIM,
        },
        "per_sarga": {str(k): per_sarga[k] for k in sorted(per_sarga)},
        "entries": entries,
        "reworded": reworded,
        "cyrillic_contaminated": contaminated,
    }
    outdir = os.path.join(repo, "data", "analysis", "helayo_spike")
    os.makedirs(outdir, exist_ok=True)
    jpath = os.path.join(outdir, "apparatus_sundara_variants.json")
    json.dump(out, open(jpath, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    # ---- human-readable markdown digest ----
    md = []
    md.append("_Created: 12-07-2026 · Last updated: 12-07-2026_\n")
    md.append("# Sundarakāṇḍa — Critical↔Southern variant apparatus (helayo-method)\n")
    md.append(f"Book-wide collation of the **{len(entries)} clean-variant verse pairs** "
              f"between the Baroda critical edition and the southern vulgate (the text "
              f"M. Leonov translates), across **{len(per_sarga)} sargas** — **{total_loci} "
              f"apparatus loci**. Gated from {len(pairs)} difflib-'variant' pairs: "
              f"{len(reworded)} heavily-reworded (sim < {CLEAN_SIM}) routed to the "
              f"footnote/absence layer, {len(contaminated)} quarantined for Cyrillic "
              "source contamination (see below). Generated by the helayo-style Gotoh "
              "aligner (`scripts/build_edition_apparatus.py`), full data in "
              "`apparatus_sundara_variants.json`.\n")
    md.append("Notation: `verse  lemma (critical) ] variant (southern)`. VARIANT layer "
              "only; whole-passage absences are in `build_edition_footnotes.py`. 2 "
              "witnesses — Center-Star MSA latent until Gita Press is the 3rd. Aligner is "
              "spike-grade (char-level + word-expansion); an akṣara-level rebuild (H776) "
              "would refine loci further.\n")
    if contaminated:
        md.append(f"⚠️ **Data bug surfaced by the aligner:** {len(contaminated)} southern "
                  "verses carry Cyrillic characters mis-encoded as Sanskrit (e.g. "
                  "`saṃcukoсa` with a Cyrillic `с`) — a corpus-source defect worth fixing "
                  "upstream in `SamudraManthanam`. Listed in the JSON `cyrillic_contaminated`.\n")
    md.append("## Per-sarga variant-locus counts\n")
    md.append("| sarga | clean-variant verses | apparatus loci |")
    md.append("|---:|---:|---:|")
    for k in sorted(per_sarga):
        r = per_sarga[k]
        md.append(f"| {k} | {r['verses']} | {r['loci']} |")
    md.append(f"| **book** | **{len(entries)}** | **{total_loci}** |\n")
    md.append("## Apparatus — sample (first 45 loci)\n")
    md.append("| verse | critical | ] | southern |")
    md.append("|---|---|:-:|---|")
    shown = 0
    for e in entries:
        for a in e["apparatus"]:
            if shown < 45:
                md.append(f"| {e['critical']} | {a['crit']} | ] | {a['south']} |")
                shown += 1
    md.append("\n_Dr. Mārcis Gasūns_")
    mpath = os.path.join(outdir, "APPARATUS_SUNDARA_VARIANTS.md")
    open(mpath, "w", encoding="utf-8").write("\n".join(md) + "\n")

    print(f"clean-variant verses: {len(entries)} | apparatus loci: {total_loci} | "
          f"sargas: {len(per_sarga)} | reworded routed: {len(reworded)} | "
          f"cyrillic-quarantined: {len(contaminated)} (of {len(pairs)} input pairs)")
    print("loci/verse hist:", dict(sorted(loci_hist.items())))
    print("wrote", os.path.relpath(jpath, repo))
    print("wrote", os.path.relpath(mpath, repo))


if __name__ == "__main__":
    main()
