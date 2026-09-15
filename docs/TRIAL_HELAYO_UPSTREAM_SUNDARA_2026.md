_Created: 15-09-2026 · Last updated: 15-09-2026_

# Trial: upstream `helayo` binary on a Sundarakāṇḍa Sa-Sa witness sample (H4742)

**Gap closed.** The 12-07-2026 spike ([`SPIKE_HELAYO_VS_DIFFLIB_SUNDARA.md`](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/SPIKE_HELAYO_VS_DIFFLIB_SUNDARA.md)) reimplemented helayo's *method* in Python and explicitly did **not** run the upstream Haskell binary. H4742 (sibling census A6) trialled the **real upstream tool** on our texts for the first time.

## Setup

- **Tool:** `helayo` prebuilt macOS binary from [chchch/sanskrit-alignment](https://github.com/chchch/sanskrit-alignment) `helayo/dist/macOS-latest/` (x86_64, runs under Rosetta), with upstream [`substitution_matrix.csv`](https://github.com/chchch/sanskrit-alignment/tree/master/helayo) and its documented CLI: `./helayo -x substitution_matrix.csv -l aksara in.fas > out.xml`. Upstream commit `ed643c3b68578b080050b5859db32883cdd1c77b`. Binary NOT committed (foreign executable); re-fetch per provenance above.
- **Witnesses (2):** Baroda critical vs southern vulgate verse pairs from [`data/edition_comparison/critical_only_and_variants.json`](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/edition_comparison/critical_only_and_variants.json).
- **Sample (deterministic, seed 42):** all 19 spike pairs (critical sargas 3 + 6, for continuity) + 11 seeded extras stratified over difflib-similarity quartiles = **30 verse pairs**, spread over sargas 1–56.
- **Harness-side normalisation:** helayo's own normaliser does not strip IAST daṇḍas (।॥) or verse digits, and only our southern witness carries them — the trial strips them pre-FASTT (same `clean()` as the spike). Without this, daṇḍas attach to word-final southern readings and spawn false loci (first run: 158 loci, 41 orthographic-only; after cleaning: **108**, of which **2** orth-only).
- **Trial script:** [`scripts/trial_helayo_upstream.py`](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/trial_helayo_upstream.py) (stdlib-only; writes FASTT + TEI XML + `trial_results.json` under [`data/analysis/helayo_upstream_trial/`](https://github.com/gasyoun/CommentaryStrategies/tree/main/data/analysis/helayo_upstream_trial)).

## Results (30 verses × 2 lemma modes)

| Check | aksara | character |
|---|---|---|
| Round-trip canary (de-gapped columns ≡ input, per witness) | 30/30 PASS | 30/30 PASS |
| Apparatus loci (word-grouped variant lemmata) | 108 | 116 |
| … substantive | 60 | 57 |
| … ins/del (one witness shorter) | 46 | 57 |
| … orthographic-only | 2 | 2 |

**Quality assessed on all 30 verses:**

1. **Known variant loci reproduce exactly.** The spike's showcase readings come back as single crisp loci from the untouched upstream binary: `supuṣṭabalasaṃguptāṃ | supuṣṭabalasampuṣṭāṃ` (5.3.4), `vaidūryatalasopānaiḥ | vaidūryakṛtasopānaiḥ` (5.3.10), `ketumālasya | kapimukhyasya` (5.3.16), `koṣṭhā- | goṣṭhā-` (5.3.18). The Python re-implementation was faithful.
2. **Column alignment is sound everywhere.** The canary (every character of every witness recoverable from the alignment) passes 60/60 in both modes — no lost or duplicated text even on the most diverged pairs (sim 0.50).
3. **Mode difference is marginal.** aksara vs character produce nearly the same locus sets (108 vs 116, same known loci); aksara fragments less and is the upstream-recommended mode. Center-Star MSA stays latent with 2 witnesses (reduces to pairwise), as predicted.
4. **Known failure mode confined to reworded verses.** At difflib sim ≲ 0.7 (e.g. 5.51.34~5.53.38) the underlying columns remain correct but *word-grouped* reading pairs fragment (`utpa | katham`, `pātātha | asmadvi`) because word boundaries/order genuinely differ — word-level loci are trustworthy at high sim and must be human-read on reworded verses. Matches the spike's «makes the reworded verdict transparent» caveat, now measured.
5. **Upstream's default matrix is weaker than our spike matrix.** It grades only vowel/vowel vs cons/cons vs cross mismatches (−1/−1/−1.25) with no near-equivalence folding (ā~a, ś~ṣ…), so orthographic alternations surface as variant columns until word-grouping absorbs them (residual orth-only: 2). Our spike matrix remains the better cost model.

## Verdict

Upstream helayo **runs correctly on our Sundara witnesses and reproduces the spike's apparatus loci** — the candidate backbone is validated as an external tool, *consume-don't-rebuild* holds. The adopt decision (aksara aligner → `build_edition_footnotes.py`, TEI apparatus export) stays with **[H776](https://github.com/gasyoun/Uprava/blob/main/handoffs/H776-Sonnet_CommentaryStrategies_helayo_aksara_apparatus_aligner_12.07.26.md)** — human ruling, unchanged by this trial except upward: the "never actually ran it" risk is now retired.

## Delivery (five fields)

- **Changed:** new trial script + trial artifacts (30 FASTT (reused across modes), 30×2 TEI XML, `trial_results.json`) + this report + CHANGELOG entry.
- **Unchanged:** spike script/docs, edition-comparison data, `compare_editions.py`/`sa_align.py`/`build_edition_footnotes.py` — nothing downstream was rewired (that is H776's call).
- **Checks:** `python3 scripts/trial_helayo_upstream.py --helayo <bin> --matrix <csv>` → `CANARY: 60/60 round-trips PASS, 0 FAIL`; JSON aggregate in `trial_results.json`.
- **Risks:** word-grouped loci unreliable at sim ≲ 0.7 (human-read those); upstream binary is a foreign x86_64 executable — provenance pinned to upstream commit `ed643c3`, never committed here.
- **Inspect:** `data/analysis/helayo_upstream_trial/trial_results.json` (`verses[].modes.aksara.loci_detail`), then any `*.aksara.xml` in the matrix-editor.

_Гасунс_
