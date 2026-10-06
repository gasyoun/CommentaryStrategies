# MBh Klammeranalyse v1 — full-corpus scale pass (H6055)

_Created: 06-10-2026 · Gasūns · tier: GLM 5.3 (`opencode/zai-coding-plan/glm-5.3`)_
_Data: [`data/panini_klammer/`](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/panini_klammer/) · Parity gate: `python3 scripts/mbh_klammer.py --check` → CHECK PASS_

## What was asked

Rulings [GRILL_RESEARCH_WIDENING §H](https://github.com/gasyoun/Uprava/blob/main/reports/GRILL_RESEARCH_WIDENING_04-10-2026.md) (04-10-2026): **H1** — first full Klammeranalyse pass on **Patañjali's Mahābhāṣya** (not Kāśikā, not a pilot slice); **H2** — one full commentary; **H11** — JSON schema, not TEI; **H12** — κ gate with a second annotator per the H5312/H5313 protocol shape. H6055 mission: scale + layer-stratification of commentary strategies + double-annotation κ control.

## What was built

`scripts/mbh_klammer.py` (stdlib, deterministic, self-caching, `--check` parity gate) + seven derived artifacts under `data/panini_klammer/` (README documents schema, pre-registered parameters, rights). Source = ashtadhyayi-com/data `bhashya.txt` (3,983 sūtras) + `vartika.txt` (921 records) — **no license upstream**, so the mirror is gitignored and only derived measurements are committed (license-gated-ingest discipline).

Double annotation = two independent mechanical passes over a shared corpus-induced vocabulary: A = greedy longest-match left-to-right, B = right-to-left. κ = Cohen's κ on the canonical segmentation label, 2,000-resample bootstrap CI, plus a boundary-level κ over every interior code-point position (house reference implementation mirrored from csl-observatory `compute_component_kappa.py`).

## Measured (full corpus, seed 20261006)

| layer | candidates | dually segmented | exact agree | disagreements | A-only | B-only |
|---|---|---|---|---|---|---|
| bhashya | 91,114 | 7,688 (8.4%) | 7,527 | 161 | 769 | 1,255 |
| vartika | 1,157 | 63 (5.4%) | 61 | 2 | 6 | 6 |
| **total** | **92,271** | **7,751** | **7,588** | **163** | **775** | **1,261** |

- κ sample n=300 (layer-proportional): **item κ 0.9833, 95% CI [0.9664, 0.9966], raw agreement 0.9833**; boundary κ **0.9867** over 3,235 decisions.
- Member-count distribution (bhashya, A-pass segmentations): 2-member 5,180 · 3: 2,182 · 4: 775 · 5: 255 · 6+: 65 — a long tail out to 8 members (max token length 123 code points).
- Top recurring candidates and the full per-sūtra table are in the data dir (`mbh_klammer_topcompounds.tsv`, `mbh_klammer_per_sutra.tsv`).

## Honest limitations (H5312 spirit — never soften)

1. **High κ is agreement between two mechanical passes sharing one vocabulary and one greedy family — it is NOT a correctness claim.** It says the segmentation is *deterministically reproducible*, which is the property the scale pass needs.
2. Spot-check (visible in the sample file): true compounds split correctly (दोषभाष्यम् → दोष | भाष्यम्; प्रत्ययलक्षणेन → प्रत्यय | लक्षणेन) coexist with **false positives**: sandhi-fused sequences (पुरुषस्येति = पुरुषस्य इति) and over-split simple words (निष्ठायां → निष्ठा | यां). Precision is unknown until the human lane lands.
3. Dual coverage ~8–9% of the bank: a ≤7-char simple-word vocabulary cannot segment member-internal sandhi. The bank itself (92,271 rows) is the complete candidate census; the dual subset is the machine-verifiable core.
4. Bracket-node labelling (the Klammerdiagramm tree proper) is **deferred to v2** — `tree: null, tree_status: "deferred_v2"`; no labelling is fabricated.

## The human lane (next session's entry point)

`data/panini_klammer/second_annotator_sheet.html` — 60 stratified disagreement rows with both passes shown and an empty human column. Filling that column + an ingest with fail-closed guards (the H5312 `--ingest` pattern) is the natural v2 unit; it converts machine agreement into an interpretable human-κ. Residual: **@DO MG** — no human annotation exists yet; until then every precision claim about this dataset is INCONCLUSIVE.

## Checks

- `python3 scripts/mbh_klammer.py --selftest` → SELFTEST PASS
- `python3 scripts/mbh_klammer.py --check` → CHECK PASS (all six committed artifacts rebuild byte-identically)
- `python -m pytest tests/test_mbh_klammer.py` → green (hermetic; no network, no live data)
