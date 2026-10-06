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
| bhashya | 88,170 | 9,058 (10.3%) | 8,783 | 275 | 833 | 1,603 |
| vartika | 1,157 | 71 (6.1%) | 68 | 3 | 7 | 11 |
| **total** | **89,327** | **9,129** | **8,851** | **278** | **840** | **1,614** |

- κ sample n=300 (layer-proportional): **item κ 0.9732, 95% CI [0.9530, 0.9899], raw agreement 0.9733**; boundary κ **0.9808** over 3,153 decisions.
- Member-count distribution (bhashya, agreeing rows): 2-member 5,020 · 3: 2,278 · 4: 958 · 5: 424 · 6+: 103 — a long tail out to 10 members (max token length 123 code points).
- Top recurring candidates and the full per-sūtra table are in the data dir (`mbh_klammer_topcompounds.tsv`, `mbh_klammer_per_sutra.tsv`).

## Honest limitations (H5312 spirit — never soften)

1. **High κ is agreement between two mechanical passes sharing one vocabulary and one greedy family — it is NOT a correctness claim.** It says the segmentation is *deterministically reproducible*, which is the property the scale pass needs.
2. Spot-check (visible in the sample file): true compounds split correctly (दोषभाष्यम् → दोष | भाष्यम्; प्रत्ययलक्षणेन → प्रत्यय | लक्षणेन) coexist with **false positives**: sandhi-fused sequences (पुरुषस्येति = पुरुषस्य इति) and over-split simple words (निष्ठायां → निष्ठा | यां). Precision is unknown until the human lane lands.
3. Dual coverage ~8–9% of the bank: a ≤7-char simple-word vocabulary cannot segment member-internal sandhi. The bank itself (92,271 rows) is the complete candidate census; the dual subset is the machine-verifiable core.
4. Bracket-node labelling (the Klammerdiagramm tree proper) is **deferred to v2** — `tree: null, tree_status: "deferred_v2"`; no labelling is fabricated.

## Independent verifier round (cou-2, deepseek/deepseek-v4.1-flash)

A distinct-model static inspection returned **disagree** with two genuine defects, both fixed in the same PR:

1. **Tokenizer swallowed daṇḍa/digits** — the character class `[ऀ-ॿ]+` kept `। ॥ ०-९` inside tokens, inflating the census with punctuated duplicates (`प्राप्नोति` + `प्राप्नोति।` counted separately). Fixed: the class now excludes U+0964–U+0970; a regression test (`test_tokenize_danda_digits_are_separators_not_word_chars`) pins it. Census went 92,271 → **89,327**; the frequency table de-duplicated (प्राप्नोति now 2,468, merged).
2. **κ chance-term summed over an unordered set** — float summation order followed Python hash randomization, so the 4-dp κ could flip across processes and flake `--check`. Fixed: `sorted(cats)`. Also hardened the bhashya key parse (malformed keys now skip loudly) and renamed a misleading test.

The verifier also correctly noted the per-sūtra TSV is keyed by (sūtra × layer), so 921 vārttika records collapse to 516 distinct sūtras — 4,499 data rows, not 3,983+921. That is intended shape, now documented here.

## The human lane (next session's entry point)

`data/panini_klammer/second_annotator_sheet.html` — 60 stratified disagreement rows with both passes shown and an empty human column. Filling that column + an ingest with fail-closed guards (the H5312 `--ingest` pattern) is the natural v2 unit; it converts machine agreement into an interpretable human-κ. Residual: **@DO MG** — no human annotation exists yet; until then every precision claim about this dataset is INCONCLUSIVE.

## Checks

- `python3 scripts/mbh_klammer.py --selftest` → SELFTEST PASS
- `python3 scripts/mbh_klammer.py --check` → CHECK PASS (all six committed artifacts rebuild byte-identically)
- `python -m pytest tests/test_mbh_klammer.py` → green (hermetic; no network, no live data)
