# Changelog

All notable changes to CommentaryStrategies are documented here.

Versioning follows [Semantic Versioning](https://semver.org): MINOR for new
additive layers/features, PATCH for fixes, MAJOR reserved for breaking schema
changes. Each released version is git-tagged (`vX.Y.Z`) with a matching
[GitHub release](https://github.com/gasyoun/CommentaryStrategies/releases).
Work not yet on `main` stays under **[Unreleased]**.

## [Unreleased]

## [1.3.1] - 2026-07-02

### Changed

**Axis-4 semantics governance — [docs/AXIS4_KD_DECISION.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/AXIS4_KD_DECISION.md)** (Fable 5, `claude-fable-5`, delegated adjudication)
- Axis 4 is now documented as the project's **operational note-depth scale** (P gloss-identification /
  K system-placement / D discursive elaboration) — *derived from, but not identical to*, Paribok 2011,
  whose own П/К/Д (понятие / концепт / кодификатор) is a typology of **terms**, not notes. Data,
  letters, TEI and scripts are untouched; only attribution language changed.
- Divergent glosses aligned to the ruling: `CLAUDE.md`, `docs/ARCHITECTURE.md`, `docs/ROADMAP.md`,
  `docs/ROADMAP_2026H2.md`, `docs/TYPOLOGY_GREEK_SANSKRIT.md`, `prompts/classify_note.md`.

### Added

- **A21 hostile pre-send verdict (HOLD, 5/5→4/5)** appended to
  [articles/SUBMISSION_READINESS_A21.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/articles/SUBMISSION_READINESS_A21.md):
  Indologica Taurinensia defunct (last issue 45, 2019); Scrinium out of scope; Paribok attribution +
  defective «Парибок 2011» bibliography entry (externally: Зографский сборник вып. 1, ред.
  Васильков/Пахомов, ЛЕМА 2011).
- **A19 verification pass** appended to
  [articles/SUBMISSION_READINESS_A19.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/articles/SUBMISSION_READINESS_A19.md):
  report + cover letter verified accurate against the manuscript; deltas listed (+3 line drift,
  §2.2↔§2.3 «кодификатор» collision, Казанский 2025 venue/DOI fix, cover-letter «Мāрцис» typo).

## [1.3.0] - 2026-07-01

### Added

**Scraped corpora (`data/`)**
- **Bhagavad Gītā** — `scripts/scrape_gita.py` → `data/gita/chapter_{NN}/verse_{NNN}.json`
  (700 verses × 27 fields: 13 Sanskrit commentators + 14 Hindi/English translators; 18,870 field-texts).
- **Brahmasūtra** — `scripts/scrape_brahmasutra.py` → `data/brahmasutra/adhyaya_{A}/pada_{P}/sutra_{NNN}.json`
  (571 sūtras, Śaṅkarācārya bhāṣya, 766,351 chars).
- **Yogasūtra** — `scripts/scrape_yogasutra.py` → `data/yogasutra/chapter_{N}_{name}/sutra_{NNN}.json`
  (195 sūtras, Vyāsa bhāṣya + Bhoja vṛtti; 95,345 + 95,952 chars).
- **Rāmcaritmānas** — `scripts/scrape_manas.py` → `data/ramcharitmanas/` (7 kāṇḍas, 1,074 blocks).

**PWG→EN translation memory pipeline**
- **Step 1** — `scripts/build_gita_tm.py` → `data/gita_tm.json`: 3,883 Sanskrit term → English gloss
  pairs from Gambirananda (Śaṅkara word-by-word) + Rāmānuja Adidevananda; 2,926 unique terms.
  Top entries: jñānam×23, karmani×16, ātmanam×15, buddhiḥ×13, tapas×10.
- **Step 2** — `scripts/crosswalk_gita_tm.py` → `data/gita_tm_slp1.json`: 2,173/2,926 terms (74 %)
  crosswalked to SLP1 MW headwords via simplified reverse index on `mw_en_tm.json` (187,506 entries).
- **Steps 3–4** — `scripts/build_sutra_tm.py` → `data/bs_term_map_slp1.json` (826 terms from BS sūtras)
  + `data/ys_term_map_slp1.json` (582 terms from YS sūtras). Devanagari→SLP1 via `indic_transliteration`
  + greedy compound segmentation. Top YS: pariṇāma×9, saṃyama×9, samādhi×8, viṣaya×7, pratyaya×6,
  kaivalya×5, kleśa×4. Top BS: vyapadeśa×21, darśana×21, śabda×19, bheda×14.

**Analysis scripts**
- `scripts/analyze_bg_divergence.py` → `data/analysis/bg_divergence.{json,html}`:
  13-commentator CV analysis for 13 core terms; karma CV=2.66 (most contested), bhakti CV=1.56 (least).
- `scripts/analyze_sundara_coverage.py` → `data/analysis/sundara_coverage.{json,html}`:
  68-sarga × 4-commentary coverage matrix + Leonov density; 🟢20 / 🟡14 / 🔴11 / ⚪23.

**Phase-2 Sundarakāṇḍa commentator-note pipeline**
- `scripts/sundara_phase2_segmenter.py` — deterministic segmenter for traditional commentary
  (Tilaka/Bhūṣaṇa/Śiromaṇi) pilot (sargas 35/36/37); pratīka precision 0.43→0.90 after
  fuzzy-assigner (`p.1a`) + iti-stemming (`p.1b`).
- `data/leonov_kostina_apparatus.json` — Leonov/Kostina's own 1,058 notes digitized as
  Phase-2 deduplication baseline.
- Interactive review page + motivation labels (`why_proposed`); interactive HTML footnote
  gate for edition-difference notes.

**Critical vs southern edition comparison (Sundarakāṇḍa)**
- `scripts/compare_editions.py` + `data/edition_comparison/` — GRETIL/Baroda critical text
  vs Leonov southern recension; absent ślokas identified and surfaced with IAST text in
  review-gated footnote draft (`scripts/generate_edition_footnotes.py`).

**Rights clearance**
- `data/valmiki_PERMISSION.md` — written permission from Gita Supersite editor
  (Sudalaimuthu Palaniappan) for CC BY 4.0 use of Vālmīki text, commentaries, and EN glosses.

### Fixed
- **`mw_to_simple()` SLP1 encoding bug** (`scripts/crosswalk_gita_tm.py`,
  `scripts/build_sutra_tm.py`): `mw_en_tm.json` uses **standard SLP1** where `R=ṇ` (retroflex
  nasal), not `N=ṇ` as previously documented. The bug caused `guṇa` to map to `gUna`
  ("voided as ordure") instead of `guRa` ("quality, attribute"). Fixed by adding
  `R→n`, `E→ai`, `O→au`, `W→th`, `Q→dh` to the simplification function. Gita TM match rate:
  69 % → 74 %.

### Notes
- The four TM files (`gita_tm_slp1.json`, `bs_term_map_slp1.json`, `ys_term_map_slp1.json`)
  are ready for integration into the PWG→EN harness (`gen_opt_harness2 --lang en`) as a
  śāstric enrichment layer for the Opus judge pass.
- Phase-2 commentator-note pipeline (sargas 35/36/37 pilot) is Sonnet-4.6-drafted; human
  review via the interactive HTML gate precedes any commit to the apparatus.
- 🟡 sargas 22, 24, 26, 30, 34–37, 39, 51: untapped commentator coverage, queued for
  `extract_yellow_sargas.py` (not yet written).

## [1.2.0] - 2026-06-29

### Added
- **Г историко-культурологический layer** — 11 background intro-articles
  (`data/hist_cultural/ch{N}.json`, `subtype:"hist_cultural"`, `type:"Г"`), completing the
  4th Kazansky commentary level. Mostly Grintser cross-references (≈1 % yield = Leonov's own
  profile); `trikūṭa` the one new-in-Book-V article. (PR #38.)
- **Grintser cross-reference backfill** — 26 corpus-derived «См. примеч. к I.X.Y (Гринцер)»
  injected into В-realia notes confirmed in Grintser's Books I–II glossary and located in the
  Books I–III text (`scripts/backfill_grintser_crossrefs.py`, idempotent). All
  `review_required`, flagged `cross_ref_method:"corpus_first_appearance"`. (PR #38.)

### Changed
- `data/sundara_commentary_to_add.json` → **788 notes** (А 617 · В 122 · Б 38 · Г 11).
- Normalized 18 stray Latin type-codes (A/B) to Cyrillic (А/Б).
- `scripts/validate.py` exempts the rule-definition doc `CLAUDE.md` from its forbidden-string
  scan; report gained the required `<main class="container">` wrapper. (PR #37.)

### Fixed
- Removed the forbidden fabricated «Наука 2022» Leonov imprint (CLAUDE.md hard rule #1) from
  `scripts/sundara_ch1_enrich.py`, `data/sundara_ch1_corpus_relevance.json`, and the report. (PR #37.)

### Notes
- Phase 2 (the ≈38 % Б commentator-dialogue layer, toward Leonov's own ~36 % density) is gated on
  a Gemini-Pro OCR of the five Sanskrit commentaries — not yet available.
- `leonov_sundara_corpus_enriched.html` still shows pre-expansion counts (166); refresh pending.

## [1.1.0] - 2026-06-29

### Added
- **Lexical layer (А)** — 611 etymological/lexical gloss notes across all 68 chapters
  (`data/lexical/ch{N}.json`), relaxed rule + adversarial gate (~70 % reject). Raised the
  apparatus from ~5 % to **Grintser-level ~24 % density** (`data/sundara_commentary_to_add.json`
  166 → 777). Documented in [SUNDARA_COMMENTARY_RATIONALE.md](SUNDARA_COMMENTARY_RATIONALE.md),
  Режим 3. (PR #33.)

### Notes
- All generated Sundara notes carry `review_required: true` (verse-level corpus evidence is soft).

## [1.0.0] - 2026-06-13

### Added
- Added this changelog so repository-level changes have a stable home.
- Recorded the current repository purpose: Аналитический репозиторий для сравнительного изучения комментаторских стратегий русских переводчиков санскритских текстов.

### Recent Git History
- 2026-06-13 fix: post-merge consolidation — restore dropped CI corpus job + .gitattributes
- 2026-06-13 build(deps): bump actions/setup-python from 5 to 6 (#2)
- 2026-06-13 Merge pull request #3 from gasyoun/dependabot/github_actions/actions/checkout-6
- 2026-06-13 Merge pull request #4 from gasyoun/dependabot/github_actions/github/codeql-action-4
- 2026-06-13 Merge pull request #9 from gasyoun/synthesis-crosswalk
