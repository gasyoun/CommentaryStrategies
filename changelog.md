# Changelog

All notable changes to CommentaryStrategies are documented here.

Versioning follows [Semantic Versioning](https://semver.org): MINOR for new
additive layers/features, PATCH for fixes, MAJOR reserved for breaking schema
changes. Each released version is git-tagged (`vX.Y.Z`) with a matching
[GitHub release](https://github.com/gasyoun/CommentaryStrategies/releases).
Work not yet on `main` stays under **[Unreleased]**.

## [Unreleased]

_Nothing pending beyond the released versions below._

## [1.2.0] - 2026-06-29 — Sundarakāṇḍa: all four Kazansky levels + Grintser cross-refs

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

## [1.1.0] - 2026-06-29 — Sundarakāṇḍa lexical/etymological layer

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
