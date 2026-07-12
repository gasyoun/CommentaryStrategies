#!/usr/bin/env python3
"""Book-wide Critical↔vulgate VARIANT APPARATUS — generalized (H784) from the
Sundarakāṇḍa reference build to any 2-witness edition-comparison output.

Runs the helayo-style aligner (spike_helayo_align: Gotoh affine-gap +
consonant/vowel substitution matrix) over ALL committed variant pairs in a
compare_editions*.py `critical_only_and_variants.json` — every aligned verse
where the critical edition and the vulgate differ in wording — and emits a
positional apparatus: per verse, the competing readings (lemma ] variant), in
standard apparatus notation.

This is the concrete "collation engine + apparatus backbone" applied to the
whole book, not just spike sargas. It covers the VARIANT-READING layer;
whole-passage differences (structural absences / critical-only) are a
separate footnote layer already produced by build_edition_footnotes.py.

Verse ids on both witnesses are "work.chapter.verse" (3 dot-separated ints,
e.g. Rāmāyaṇa "5.35.12" or Mahābhārata "3.7.42") — verse_key() below parses
that shape regardless of which text it names; no per-work change needed.

CLI (all optional; defaults reproduce the original Sundarakāṇḍa run exactly):
  --input PATH     critical_only_and_variants.json (default: Sundara's)
  --outdir DIR     output directory (default: data/analysis/helayo_spike)
  --title STR      report title (default: Sundarakāṇḍa's)
  --other-key STR  the non-"critical" witness key in the input JSON/output
                   ("southern" for Rāmāyaṇa, "vulgate" for Mahābhārata)

Stdlib-only. Read-only inputs. Usage: python build_edition_apparatus.py [opts]
"""
import sys
import os
import json
import argparse

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_DEFAULT = os.path.dirname(HERE)
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


def parse_args():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input", default=None,
                   help="critical_only_and_variants.json (default: Sundarakanda's)")
    p.add_argument("--outdir", default=None,
                   help="output directory (default: data/analysis/helayo_spike)")
    p.add_argument("--title", default="Sundarakāṇḍa — Critical (Baroda) ↔ Southern vulgate variant apparatus",
                   help="report title")
    p.add_argument("--work-label", default="Sundara",
                   help="short work label used in output filenames, e.g. 'Sundara' or 'MBh-Vanaparva'")
    p.add_argument("--other-key", default="southern",
                   help="the non-'critical' witness key in the input/output JSON "
                        "('southern' for Ramayana, 'vulgate' for Mahabharata)")
    p.add_argument("--chapter-label", default="sarga",
                   help="chapter unit name for reporting, e.g. 'sarga' or 'adhyaya'")
    return p.parse_args()


def main():
    args = parse_args()
    repo = os.environ.get("CS_REPO", REPO_DEFAULT)
    ok = args.other_key
    cvp = args.input or os.path.join(repo, "data", "edition_comparison",
                                     "critical_only_and_variants.json")
    cv = json.load(open(cvp, encoding="utf-8"))
    pairs = [v for v in cv["variants"]
             if "critical_text" in v and f"{ok}_text" in v]
    pairs.sort(key=lambda v: verse_key(v["critical"]))

    entries = []
    reworded = []          # sim < CLEAN_SIM — routed to the absence/footnote layer
    contaminated = []      # source verses with Cyrillic contamination (data bug)
    from collections import Counter, defaultdict
    per_sarga = defaultdict(lambda: {"verses": 0, "loci": 0})
    loci_hist = Counter()
    total_loci = 0
    for v in pairs:
        ct, st = clean(v["critical_text"]), clean(v[f"{ok}_text"])
        if has_cyrillic(ct) or has_cyrillic(st):
            contaminated.append({"critical": v["critical"], ok: v[ok],
                                 "critical_text": ct, f"{ok}_text": st})
            continue
        sim = v.get("similarity") or 0.0
        if sim < CLEAN_SIM:
            reworded.append({"critical": v["critical"], ok: v[ok],
                             "difflib_similarity": sim})
            continue
        _, aa, bb = gotoh(ct, st)
        loci = collapse_loci(aa, bb, ct, st)
        app = [{"crit": c or "∅", ok: s or "∅"}
               for c, s in loci if substantive(c, s)]
        if not app:
            continue                       # difflib flagged variant; matrix says none
        sg = verse_key(v["critical"])[0]
        per_sarga[sg]["verses"] += 1
        per_sarga[sg]["loci"] += len(app)
        loci_hist[len(app)] += 1
        total_loci += len(app)
        entries.append({
            "critical": v["critical"], ok: v[ok],
            "difflib_similarity": v.get("similarity"),
            "kind": v.get("kind", "lcs-variant"),
            "n_loci": len(app), "apparatus": app,
        })

    out = {
        "_meta": {
            "title": args.title,
            "generated_by": "build_edition_apparatus.py (helayo-style Gotoh aligner)",
            "layer": "variant readings on aligned verses (NOT whole-passage absences)",
            "aligner": "char-level Gotoh affine-gap + consonant/vowel/modifier "
                       "substitution matrix; loci word-expanded",
            "witnesses": 2,
            "other_key": ok,
            "note": "2-witness collation; Center-Star MSA advantage latent until a "
                    "3rd witness is digitised. Reworded/absent-counterpart pairs are "
                    "NOT included here — their critical counterpart text is absent "
                    "from the committed data (see the significant_absences layer).",
        },
        "totals": {
            "clean_variant_verses": len(entries),
            "apparatus_loci": total_loci,
            "chapters": len(per_sarga),
            "loci_per_verse_hist": dict(sorted(loci_hist.items())),
            "reworded_verses_routed_to_footnote_layer": len(reworded),
            "cyrillic_contaminated_verses": len(contaminated),
            "input_variant_pairs": len(pairs),
            "clean_sim_gate": CLEAN_SIM,
        },
        "per_chapter": {str(k): per_sarga[k] for k in sorted(per_sarga)},
        "entries": entries,
        "reworded": reworded,
        "cyrillic_contaminated": contaminated,
    }
    outdir = args.outdir or os.path.join(repo, "data", "analysis", "helayo_spike")
    os.makedirs(outdir, exist_ok=True)
    jpath = os.path.join(outdir, f"apparatus_{args.work_label.lower()}_variants.json")
    json.dump(out, open(jpath, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    # ---- human-readable markdown digest ----
    md = []
    md.append("_Created: 12-07-2026 · Last updated: 12-07-2026_\n")
    md.append(f"# {args.title} (helayo-method)\n")
    md.append(f"Book-wide collation of the **{len(entries)} clean-variant verse pairs**, "
              f"across **{len(per_sarga)} {args.chapter_label}s** — **{total_loci} "
              f"apparatus loci**. Gated from {len(pairs)} difflib-'variant' pairs: "
              f"{len(reworded)} heavily-reworded (sim < {CLEAN_SIM}) routed to the "
              f"footnote/absence layer, {len(contaminated)} quarantined for Cyrillic "
              "source contamination (see below). Generated by the helayo-style Gotoh "
              f"aligner (`scripts/build_edition_apparatus.py`), full data in "
              f"`{os.path.basename(jpath)}`.\n")
    md.append(f"Notation: `verse  lemma (critical) ] variant ({ok})`. VARIANT layer "
              "only; whole-passage absences are in `build_edition_footnotes.py` "
              "(Rāmāyaṇa) / `significant_absences.json` (this comparator). 2 "
              "witnesses — Center-Star MSA latent until a 3rd is digitised. Aligner is "
              "spike-grade (char-level + word-expansion); an akṣara-level rebuild (H776) "
              "would refine loci further.\n")
    if contaminated:
        md.append(f"⚠️ **Data bug surfaced by the aligner:** {len(contaminated)} {ok} "
                  "verses carry Cyrillic characters mis-encoded as Sanskrit (e.g. "
                  "`saṃcukoсa` with a Cyrillic `с`) — a corpus-source defect. "
                  "Listed in the JSON `cyrillic_contaminated`.\n")
    md.append(f"## Per-{args.chapter_label} variant-locus counts\n")
    md.append(f"| {args.chapter_label} | clean-variant verses | apparatus loci |")
    md.append("|---:|---:|---:|")
    for k in sorted(per_sarga):
        r = per_sarga[k]
        md.append(f"| {k} | {r['verses']} | {r['loci']} |")
    md.append(f"| **book** | **{len(entries)}** | **{total_loci}** |\n")
    md.append("## Apparatus — sample (first 45 loci)\n")
    md.append(f"| verse | critical | ] | {ok} |")
    md.append("|---|---|:-:|---|")
    shown = 0
    for e in entries:
        for a in e["apparatus"]:
            if shown < 45:
                md.append(f"| {e['critical']} | {a['crit']} | ] | {a[ok]} |")
                shown += 1
    md.append("\n_Dr. Mārcis Gasūns_")
    mpath = os.path.join(outdir, f"APPARATUS_{args.work_label.upper()}_VARIANTS.md")
    open(mpath, "w", encoding="utf-8").write("\n".join(md) + "\n")

    print(f"clean-variant verses: {len(entries)} | apparatus loci: {total_loci} | "
          f"{args.chapter_label}s: {len(per_sarga)} | reworded routed: {len(reworded)} | "
          f"cyrillic-quarantined: {len(contaminated)} (of {len(pairs)} input pairs)")
    print("loci/verse hist:", dict(sorted(loci_hist.items())))
    print("wrote", os.path.relpath(jpath, repo))
    print("wrote", os.path.relpath(mpath, repo))


if __name__ == "__main__":
    main()
