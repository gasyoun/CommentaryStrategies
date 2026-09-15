# Appendix-7 collocate profiles as QA context for Sundara sense-note review — H4709

_Created: 15-09-2026 · Last updated: 15-09-2026 (OxAlpha `zai-coding-plan/glm-5.3-flash`, H4709)_

**Dataset consumed:** kosha [`dcs-sintagmatic-appendix7`](https://github.com/gasyoun/kosha/blob/main/data/manifest/datasets.json) — "DCS syntagmatic table — all corpus lemmas (Приложение 7)", CC BY-SA 4.0, 82,799 rows, canonical copy `VisualDCS/derived-data/Lexical-Cores/Prilozhenie-7.…/DCS_Sintagmatic.csv` (semicolon-CSV: `lemma; total; co-occur; collocate freq; …`). This closes its **Census A3 leg 2** (leg 1 = H4708, SanskritLexicography wordportrait collocates) — the dataset's `awaiting-consumer` status ends here for CommentaryStrategies.

**What was built (Census A3, leg 2):** every kept Sundarakaṇḍa lexical note (`data/lexical/ch*.json`, 68 sargas) is joined by `lemma_iast` to its DCS collocate profile, so a reviewer checking a `note_ru` sense claim can read, next to the note, how that headword is actually attested across DCS: total occurrences, co-occurrence volume, and the ranked collocate list.

## Artifacts

| Artifact | Path |
|---|---|
| QA context file (685 notes, per-note profile) | [`data/analysis/appendix7_sense_qa/sundara_sense_qa_context.json`](../data/analysis/appendix7_sense_qa/sundara_sense_qa_context.json) |
| Coverage stats | [`data/analysis/appendix7_sense_qa/coverage_stats.json`](../data/analysis/appendix7_sense_qa/coverage_stats.json) |
| Join script (deterministic, stdlib-only, re-runnable) | [`scripts/appendix7_sense_qa.py`](../scripts/appendix7_sense_qa.py) |
| This report | `reports/APPENDIX7_SUNDARA_SENSE_QA_2026-09-15.md` |

Regenerate: `python3 scripts/appendix7_sense_qa.py` (default CSV path = sibling VisualDCS clone; `--csv` overrides).

## Coverage (honest tiers, no silent merging)

| Match tier | Notes | Share |
|---|---|---|
| exact (raw lemma_iast = DCS lemma string) | 410 | 59.9% |
| folded (NFC + ṁ→ṃ + quote variants via fold index) | 28 | 4.1% |
| annotation (strip "(…)" qualifier) | 10 | 1.5% |
| hyphen-join | 1 | 0.1% |
| **covered total** | **449** | **65.5%** |
| miss (no DCS lemma) | 236 | 34.5% |

- 685 notes total, 636 unique lemmas; **all 68 sargas have ≥1 matched note** (min ch18/ch23/ch29/ch47: 1 each; max ch1: 50).
- The 236 misses are dominated by Epic hapax/epithet compounds absent from DCS lemmatization (`agra-mahiṣī`, `akliṣṭacāritrā`, `śatrukārśana`, …) — genuinely not in the 79,985-lemma table, recorded as `match_tier: "miss"` with an empty profile, never dropped and never fuzzy-matched.

## Verification — 10-note stratified sample (hand-inspected)

Stratified: one matched note per sarga across ch1→ch56 (`total_occ ≥ 5` for informative profiles), deterministic order. Each: does the DCS collocate field corroborate the `note_ru` sense claim?

| # | Note | DCS lemma (total) | Collocates cited (selected from the committed top-20 profile; values verbatim) | Verdict |
|---|---|---|---|---|
| 1 | V.1.100 kākutstha — "патроним Рамы" | kākutstha (272) | rāma 7 · lakṣmaṇa 6 · viśvāmitra 4 · rājan 4 | **CONFIRMED-CONTEXT** — patronymic-of-Rāma usage field |
| 2 | V.7.1 vaidūrya — "кошачий глаз, не изумруд" | vaidūrya (15) | sphaṭika · vajra · vidruma · vimala | **CONFIRMED-CONTEXT (weak n)** — gem-cluster, generic precious-materials register |
| 3 | V.13.1 prākāra — "крепостная стена" | prākāra (177) | toraṇa 22 · parikhā 14 · vapra 7 · gopura 5 · laṅkā 5 | **CONFIRMED-CONTEXT (strong)** — full fortification frame incl. Laṅkā |
| 4 | V.19.11 prajñā — "знание, мудрость" | prajñā (179) | āgam 25 · citta 17 · vid · jñā | **CONFIRMED-CONTEXT** — wisdom field; āgam-heavy (DCS register caveat below) |
| 5 | V.25.12 akāla — "не-время, неподходящий момент" | akāla (217) | kāla 24 · mṛtyu 18 · maraṇa 10 · bhojana | **CONFIRMED-CONTEXT (strong)** — akāla-mṛtyu idiom visible |
| 6 | V.32.14 vācaspati — "ведийское имя Брихаспати" | vācaspati (50) | namas 4 · vāc · deva · āṅgirasa | **CONFIRMED-CONTEXT** — veneration + Āṅgirasa (Bṛhaspati's clan) |
| 7 | V.38.21 paryāya — "чередование, очерёдность" | paryāya (321) | aneka 23 · kāla 20 · śabda 14 · bodhisattva 6 | **CONFIRMED-CONTEXT** + caveat: Buddhist collocates (see limitations) |
| 8 | V.44.1 mahādaṁṣṭra — "бахуврихи: великий + клык" | mahādaṁṣṭra (8) | mahādanta 2 · mahājihva 2 · karāla | **CONFIRMED-CONTEXT** — rākṣasa-epithet series |
| 9 | V.50.19 āgneya — "огненный, относящийся к Агни" | āgneya (36) | mahāpurāṇa 22 · rāmāyaṇa 7 · agni | **CONFIRMED-CONTEXT with caveat** — sense holds, but profile polluted by work-title lemmas (below) |
| 10 | V.56.20 rohiṇī — "любимая жена Луны" | rohiṇī (276) | śaśin 8 · candra 8 · soma 7 · devakī 5 · graha | **CONFIRMED-CONTEXT (strong)** — lunar-wife/nakṣatra frame direct |

**Canary (own-data, no-signal behaviour):** V.14.3 `aśoka` (tree, Saraca asoca, "без-скорби") — an **exact-tier** match whose DCS profile carries total=2 (collocate: aravinda), i.e. honest **NO-SIGNAL** at this n; the note must stand on MW/Apte, and the context file says so by carrying `total=2` instead of inventing support. Tier-labelled, no fabricated evidence.

**Paired-family verifier (DeepSeek, 15-09-2026):** numerics confirmed (tier sum 685, coverage arithmetic, all 10 sample dcs_total values, read-only guarantee); its three report defects were fixed in this revision — (1) `exact` tier now means raw-string identity only (fold-index hits labelled `folded`; counts corrected 433/5 → 410/28, covered 449 and 65.5% unchanged), (2) canary re-labelled exact/no-signal, (3) collocate column re-framed as selected-from-profile. The join spot-check DeepSeek was sandbox-blocked from was completed by the executor against the raw CSV: kākutstha 272/rāma 7, prākāra 177/toraṇa 22, rohiṇī 276/śaśin 8 — all match.

**Sample verdict: 10/10 usable QA context, 0 contradictions with `note_ru`; strongest where the note claims a semantic field (prākāra, akāla, rohiṇī, mahādaṁṣṭra).**

## Findings & limitations (encoded in the context file `_meta`)

1. **DCS is pan-Indian, not Rāmāyaṇa-specific** — Buddhist/purāṇic registers contribute collocates (bodhisattva under paryāya; āgam dominating prajñā). The profile is corpus-usage context, not Sundara-register evidence; the reviewer weighs it accordingly.
2. **Work-title lemmas pollute some profiles** (āgneya ← mahāpurāṇa 22): DCS treats text titles as lemmas, so "of-Agni" section attributions in Purāṇas surface as collocates. A future refinement may down-rank title lemmas; not done in leg 2 (scope: context delivery, not filtering policy).
3. **Hapax epithets have no profile** (34.5% miss) — by design honest; these are exactly the notes where lexicon-first QA stays mandatory.
4. The join is **tier-labelled per note** (`exact/folded/annotation/hyphen-join/miss`), so any downstream consumer can filter to exact-only if it needs zero normalization risk.

## Delivery (five fields)

- **Changed:** new analysis layer `data/analysis/appendix7_sense_qa/` (context JSON 685 notes + coverage stats); new join script `scripts/appendix7_sense_qa.py`; this report; `changelog_queue/H4709-appendix7-sundara-sense-qa-context.md`. Edge registered upstream: Uprava `interlinks_edges.tsv` (+ PROJECT_INTERLINKS prose), kosha `datasets.json` consumer flip for `dcs-sintagmatic-appendix7`.
- **Unchanged:** every file under `data/lexical/` (read-only consumer — the QA layer adds context, never edits notes); lexical schema; all other datasets/edges.
- **Checks:** `python3 scripts/appendix7_sense_qa.py` → `coverage_pct: 65.5` over 685 notes, all 68 chapters, exit 0 (PASS). 10-note sample hand-verified (table above, 10/10 usable). Reproducibility: re-run is deterministic (sorted inputs, no randomness).
- **Risks:** consumers may over-read DCS profiles as Ramāyaṇa-register evidence (mitigated: `_meta` + §Findings 1–2); title-lemma pollution (mitigated: documented, filter left to a future leg); 34.5% no-profile notes could be mistaken for data loss (mitigated: explicit `match_tier: miss` + coverage report).
- **Inspect:** [`data/analysis/appendix7_sense_qa/sundara_sense_qa_context.json`](../data/analysis/appendix7_sense_qa/sundara_sense_qa_context.json) `_meta`, then the §Verification table, then `coverage_stats.json`.

## Evidence required (handoff contract)

- [x] QA context file — `data/analysis/appendix7_sense_qa/sundara_sense_qa_context.json` (685 notes)
- [x] Report with 10-note sample — this file
- [x] Own-data canary — V.14.3 `aśoka` exact-tier NO-SIGNAL row (above)
- [x] Paired-family verifier — DeepSeek static verification + fixes landed; raw-CSV join spot-check 3/3
- [x] Edge registered — Uprava `interlinks_edges.tsv` row `CommentaryStrategies → VisualDCS` (consumes, 15-09-2026) + kosha consumer flip

_Гасунс_
