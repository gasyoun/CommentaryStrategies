# Changelog

All notable changes to CommentaryStrategies are documented here.

Versioning follows [Semantic Versioning](https://semver.org): MINOR for new
additive layers/features, PATCH for fixes, MAJOR reserved for breaking schema
changes. Each released version is git-tagged (`vX.Y.Z`) with a matching
[GitHub release](https://github.com/gasyoun/CommentaryStrategies/releases).
Work not yet on `main` stays under **[Unreleased]**.

## [Unreleased]

## [1.15.0] - 2026-07-28

### Added

- **H1685 шаг 8: ремонт механически исправимого остатка адъюдикации —
  предложение на 29 карточек из 87** (Opus 5 1M `claude-opus-5[1m]`).
  [scripts/h1685_repair.py](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/h1685_repair.py)
  → [data/analysis/h1685_adjudication/repairs.json](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/analysis/h1685_adjudication/repairs.json).
  Перепривязка 24 из 48 битых якорей (только внутри той же сарги: 15 целей от
  поиска ±2, 9 — единственное книжное попадание леммы в своей сарге) +
  раскле́ивание 5 текстовых порч (`viमāna`, `экувেṇī`, `марша&нīя`, `dolce`,
  `version`). Отказано 58: 17 якорей уводят в другую саргу (научное
  утверждение, не ремонт), 7 неоднозначны внутри сарги, 34 `edit` — правка
  ссылок/атрибуций/регистра, то есть редакторский акт. `--apply` не запускался:
  ворота §8 закрыты до голосования человека. Раздел §9 отчёта
  [docs/SUNDARAKANDA_QUEUE_ADJUDICATION_H1685_2026.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/SUNDARAKANDA_QUEUE_ADJUDICATION_H1685_2026.md).

## [1.14.0] - 2026-07-27

### Added

- **H1685 (ruling В2): агентная адъюдикация всех воротных очередей Сундараканды —
  1889/1889 вердиктов с процитированными доказательствами**
  ([H1685](https://github.com/gasyoun/Uprava/blob/main/handoffs/H1685-Opus_CommentaryStrategies_sundarakanda-queues-b2-adjudication_26.07.26.md),
  Opus 5 1M `claude-opus-5[1m]`). Отчёт:
  [docs/SUNDARAKANDA_QUEUE_ADJUDICATION_H1685_2026.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/SUNDARAKANDA_QUEUE_ADJUDICATION_H1685_2026.md).
  Восемь скриптов `scripts/h1685_*.py` + `build_h1685_spotcheck_sheet.py`; данные в
  [data/analysis/h1685_adjudication/](https://github.com/gasyoun/CommentaryStrategies/tree/main/data/analysis/h1685_adjudication).
  Итог: accept 1733 · edit 39 · reject 43 · park 26 · flag_anchor 48. Из 838 карточек,
  уже имевших вердикт Sonnet 5, адъюдикатор согласился с 825 и пересмотрел 13.
  **Порог отсутствий измерен, а не назначен:** восстановление известных пар
  конкорданса 600/600, разделение полное (306 из 307 заявленных отсутствий ниже p1
  распределения заведомо присутствующих) — тем самым выполнен шаг «нечёткое
  глобальное назначение», помеченный в `data/edition_comparison/README.md` как не
  сделанный. Найдено: 31 выдуманная этимология/атрибуция в лексике (пять
  перепроверены прямо по `dic_mw.jsonl`: `vimada` — значение перевёрнуто, `vāyasa`,
  `karṇikāra`, `koka`, `śātakumbha`), 48 битых якорей (для 10 названа конкретная
  целевая шлока), карточка на несуществующем стихе 5.41.34 и два молчаливых
  столкновения ключей, которые дали бы «accept» без записи.
- **Слепой стратифицированный лист проверки адъюдикатора** —
  `commentarystrategies-h1685-adjudication-spotcheck_review.html`: 133 карточки
  вместо 1889 (−93 %), 9 страт риска, размер выборки выведен из условия
  «нижняя граница Уилсона 95 % при чистой страте = n/(n+z²) ≥ 0.80» ⇒ n = 16.
  Вердикты адъюдикатора и прежнего судьи на карточках скрыты намеренно.

### Changed

- **`apply_phase2_decisions.py` больше не штампует чужие вердикты именем
  человека-рецензента.** Если файл решений несёт `gated_by`, стамп берётся оттуда
  (для H1685 — `агент-адъюдикатор Opus 5 1M …, Wilson-gated`); без ключа поведение
  прежнее. Ложный провенанс в постоянной гейт-записи — это тот самый
  «reconstructed-as-recovered» мислейбл, который запрещён org-правилами.

### Fixed

- **Реестр листов занижал человеческую очередь по сноскам в двадцать раз:** 51
  против фактических 1013 карточек (лист склеивает `candidates` 51 +
  `single_verse_absences` 123 + `variant_reading_candidates` 839). Лексический лист
  наоборот завышен: «611+7» дважды считает 7 припаркованных WS-3b, в листе 611.
  Строки [REVIEW_SHEETS_INDEX.md](https://github.com/gasyoun/Uprava/blob/main/REVIEW_SHEETS_INDEX.md)
  исправлены; занижение заведено отдельным integrity-issue.

## [1.13.2] - 2026-07-26

### Changed

- **A21+A22: P/K/D convergence reframed, Paribok-taxonomy mislabel stripped
  ([H1378](https://github.com/gasyoun/Uprava/blob/main/handoffs/H1378-Fable_CommentaryStrategies_a21-a22-convergence-reframe-axis4-wording_20.07.26.md),
  Fable 5 `claude-fable-5`).** Both Nīlakaṇṭha manuscripts (RU v4 + EN translation v3, in
  lockstep) now carry the canonical `AXIS4_KD_DECISION.md` §2 provenance: the P/K/D scale
  is the project's operational note-depth scale, built on the model of Paribok's tripartite
  distinction of *terms* but not identical to it. The I–IV → P/K/D bridge is stated as a
  stipulative, definition-derived mapping; §4.1 discloses the Nīlakaṇṭha-side percentages
  as a re-expression of the type I–IV distribution (not independent coding); the abstract
  now leads with the selection-divergence result and demotes «Парибок описывает
  универсальные типы» to a hypothesis pending blind independent coding. Selection
  divergence / functional inversion untouched. Table 1/2 «Парибок» column headers renamed
  «Код P/K/D» / "P/K/D Code"; RU/EN table parity re-verified mechanically (30/30, 16/16).
  The defective «Парибок 2011» bibliography entry is deliberately NOT touched — it stays
  behind the §5 book-check gate. Readiness scores left at 4/5 (a human decides any move).

## [1.13.1] - 2026-07-24

### Changed

- **A19 manuscript: fold H1469 κ into §2.3 / §7.5** (agent follow-up). Measured human×LLM
  agreement (axis_2 κ=0.648, axis_4 κ=0.521, n=300) replaces the aspirational «≥85 %»
  validation sentence; §7.5 no longer claims IAA is unmeasured. Also: table captions
  renumbered 1→2→3 in document order; bibliography «Арааньяканда»→«Араньяканда»; cover
  letter «Мāрцис»→«Марцис»; §2.2 transliteration-convention sentence.

## [1.13.0] - 2026-07-24

### Added

- **H1469 — axis_2 / axis_4 blind second-annotator IAA (Cohen's κ) on the 300-note gold.**
  Pre-registered gate (`data/iaa/PRE_REGISTRATION_H1469.md`), Pass B = DeepSeek Chat
  (`deepseek-chat`) over all six `*_markup_50.json` samples via `annotate_batch.py`,
  stdlib scorer `scripts/compute_iaa_kappa.py` (bootstrap CI seed 20260724). Headline:
  axis_2 κ = **0.648** [0.571–0.719] agr 77.7 %; axis_4 κ = **0.521** [0.430–0.608]
  agr 77.0 %. Roadmap ≥0.7/≥85 % target not met — closed as honest finding (D2/H453);
  96–100 % of disagreements are protocol-ambiguity (V/G and P/K/D depth), not random
  coder error. Report: [`data/EVAL_RESULTS.md`](data/EVAL_RESULTS.md); A19 IRR @DO
  marked resolved in `articles/SUBMISSION_READINESS_A19.md`; B5 roadmap items ticked.

## [1.12.2] - 2026-07-21

### Fixed

- **One canonical 17 863 corpus-composition statement across the article series
  (H1377, C7 cross-paper numeric-drift repair).** The «17 863 примечаний» total was
  attributed to six translators in A19/A21/A22/A23 while A24 §1 correctly states five
  attributed sub-corpora (17 622) + 241 unattributed records, with Леонов (≈ 1 040)
  a separate ongoing source outside the total. Adopted A24 §1 as canonical in the new
  [docs/CORPUS_COMPOSITION_17863.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/CORPUS_COMPOSITION_17863.md)
  and repaired: A19 (RU abstract, EN Summary, §2.1 lead-in + table now summing to
  17 622 with Леонов below the total, §7 sample-vs-corpus sentence), A23 (§2.1, §2.3),
  A24's Приложение III caption (both the inline copy and the stale standalone
  [tronsky-XXX/Appendix_III.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/tronsky-XXX/Appendix_III.md),
  the latter also resynced to the post-Kostina-fold table values), the A21/A22 series
  footnote, M02's skeleton (now cites the canonical doc), and
  [articles/SUBMISSION_READINESS_A19.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/articles/SUBMISSION_READINESS_A19.md)'s
  false "internally consistent" certification. The 241-record reconciliation itself
  stays an open data task; the 300-note sample remains correctly 50 × six translators.

## [1.12.1] - 2026-07-14

### Fixed

- **Aligner bugs found while regenerating the MBh apparatus with the akṣara-level
  aligner (H830, [PR #101](https://github.com/gasyoun/CommentaryStrategies/pull/101)).**
  Two real bugs in the H776-shared aligner/loader code, both regression-verified
  against the already-published Sundarakāṇḍa apparatus with zero regressions:
  - `collapse_loci_aksara` (`scripts/spike_helayo_align.py`) fragmented one locus
    into two duplicate-pointing loci whenever the critical and vulgate witnesses
    disagreed on word-boundary placement for sandhi-joined compounds. Fixed by
    merging consecutive loci that share an identical non-empty string on one side.
  - `iso15919_to_iast` (`scripts/compare_editions_mbh.py`) never implemented the
    vocalic-r/l normalization its own docstring already promised — ISO-15919's
    combining-ring-below spelling has no Unicode canonical-equivalence to IAST's
    precomposed dot-below forms, so every `r̥`/`l̥` in the BORI critical text
    silently mismatched the vulgate's `ṛ`/`ḷ` (~1000+ occurrences/parva).

### Changed

- **MBh apparatus (all 18 parvas) regenerated with the H776 akṣara-level aligner
  (H830, [PR #101](https://github.com/gasyoun/CommentaryStrategies/pull/101)),
  superseding the char-level version built at H784/H802/H804.** Book-level totals
  unchanged (regression-verified exact match). Total apparatus loci 142,283 →
  298,930 — a real ~2.1x increase not fully explained by the two fixes above;
  flagged as an open question for a human ruling in the H830 handoff, not shipped
  as fully understood.

## [1.12.0] - 2026-07-12

### Added

- **Akṣara-level Gotoh aligner + footnote wiring (H776, [PR #98](https://github.com/gasyoun/CommentaryStrategies/pull/98)).**
  ADOPT ruling given directly by MG. `scripts/spike_helayo_align.py` gained `syllabify()`
  (maximal-onset IAST akṣara segmentation), `gotoh_aksara()`, `collapse_loci_aksara()`,
  `align_aksara()` — reuses the existing char-level `sub_score`/`_NEARMAP` as a nested
  per-syllable scoring engine, so the near-equivalence matrix applies inside a syllable too.
  Verified fix for the spike's two named problem cases (5.3.11, 5.3.19 — spurious/garbled
  adjacency loci from insertion/deletion next to a substitution); byte-identical on cases
  already clean at char level. Book-wide: 865→839 clean-variant verses, 2106→**1664**
  apparatus loci (21% fewer/cleaner). `scripts/build_edition_footnotes.py` gained a new
  `variant_reading` candidate kind (839 candidates with real competing readings — this layer
  existed but never reached the footnote review gate before); review HTML updated to render
  it. `compare_editions.py`'s book-level bucketing regression-verified untouched (git diff
  empty). Scoped to the Rāmāyaṇa Sundarakāṇḍa footnote pipeline; the MBh apparatus (18
  parvas, char-level) was not regenerated with the new aligner — follow-on, not this pass.

## [1.11.0] - 2026-07-12

### Added

- **MBh edition-apparatus review-gate verified against BORI App. I (H810, [PR #96](https://github.com/gasyoun/CommentaryStrategies/pull/96)).**
  Independent verification of the H784/H802/H804 `structural_absence`/`vulgate_extra_adhyayas`
  flags against the BORI critical edition's own apparatus criticus (App. I star-passages,
  bombay.indology.info/mahabharata/apps/) — the actual print apparatus in electronic form, not
  a reconstruction. New `scripts/verify_mbh_apparatus_against_print.py`: 4-gram character
  Jaccard on despaced canon strings + inverted index (word-token Jaccard and plain
  `SequenceMatcher.ratio` both tried first and rejected — see script docstring). Results:
  2969/14581 (20.4%) structural_absence flags confirmed (9.8% ≥0.5, 4.7% ≥0.7, 3.2% ≥0.9);
  233/5552 (4.2%) extra-adhyaya verses confirmed. ~20% is the expected, meaningful outcome —
  see `data/edition_comparison_mbh/PRINT_VERIFICATION_REPORT.md` for full interpretation.

## [1.10.0] - 2026-07-12

### Added

- **MBh edition-apparatus rollout complete — all 18 parvas (H804, [PR #92](https://github.com/gasyoun/CommentaryStrategies/pull/92)).**
  Completes the rollout begun at H784 (Vanaparva pilot) and continued at H802 (Virataparva):
  ran the same `compare_editions_mbh.py` + `build_edition_apparatus.py` pipeline for the
  remaining 16 parvas via a new batch driver, `scripts/run_all_mbh_parvas.py`. All 16 ran with
  zero errors; every parva's vulgate verse count matched
  [NILAKANTHA_VULGATE_CENSUS.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/mahabharata-nilakantha/NILAKANTHA_VULGATE_CENSUS.md)
  exactly except anushasanaparva and shantiparva, both fully explained by the census's own
  documented "231 empty-mula records" filter (230+1=231, exact accounting). 119,552 new
  apparatus loci; **142,283 total apparatus loci across the complete 18-parva Mahābhārata
  rollout**. Data: `data/edition_comparison_mbh/<parva>/`. Rights posture (bulk verbatim text
  gitignored/local-only per parva; only aggregates + short excerpted apparatus loci
  committed) held for all 16.

## [1.9.1] - 2026-07-12

### Added

- **MBh edition-apparatus rollout — Virataparva (parva 4, H802, [PR #88](https://github.com/gasyoun/CommentaryStrategies/pull/88)).**
  Continuation of H784: same `compare_editions_mbh.py` + `build_edition_apparatus.py`
  pipeline, no script changes. 1824 critical vs 2270 vulgate verses (vulgate count matches
  the independent census exactly). 48 identical / 1652 variant / 124 critical-only. 570
  vulgate-only (464 true structural absence / 106 reworded). Variant apparatus: 1285 clean
  pairs → 4032 loci across 67 adhyayas. Data: `data/edition_comparison_mbh/virataparva/`.
  Rights posture (bulk verbatim text gitignored/local-only, only aggregates + short loci
  committed) confirmed standing for the rest of the 18-parva rollout.

## [1.9.0] - 2026-07-12

### Added

- `mahabharata-nilakantha/nilakantha_parser.py`: новая подкоманда **`scrape`** — полный
  скрейпер корпуса Нилакантха-вульгаты (Bhāratabhāvadīpa) с [sanatana.in/mahabharata](https://sanatana.in/mahabharata/)
  по всем 18 парванам (эндпоинт `getParvaByPage`, адресация P/U/A/S из `id` div.shloka,
  мула + ṭīkā в Devanagari+IAST → JSONL, дисковый кэш, вежливый rate-limit). Старые функции
  `parse_nilakantha_commentary`/`devanagari_to_iast` и LMS-режим (подкоманда `lms`) сохранены.
  Кэш и полный JSONL gitignored (права на сторонний текст — публикация гейтится
  `/publish-safety-check`). Разблокирует MBH fitted-index адъюдикатор для проверки цитат PWG/MW.

- **MBh edition-apparatus comparator + Ванапарва-пилот (H784, [PR #84](https://github.com/gasyoun/CommentaryStrategies/pull/84)).**
  Новый `scripts/compare_editions_mbh.py` — обобщение `compare_editions.py` (Рамаяна
  Сундараканда) на Махабхарату: BORI-critical loader (ISO-15919 `MBh{NN}.txt`) + Нилакантха-
  вульгата loader, id-схема `parva.adhyāya.śloka` (та же форма, что у Рамаяны — `verse_key()`
  в `build_edition_apparatus.py` не потребовал изменений). `build_edition_apparatus.py`
  обобщён CLI-флагами (`--input/--outdir/--title/--work-label/--other-key/--chapter-label`);
  дефолты воспроизводят исходный Сундара-прогон байт-в-байт (865/2106/66, перепроверено).
  Пилот Ванапарва (parva 3): 10316 крит. vs 11859 вульг. (вульгата сверена с census — совпадает);
  296 идентичных · 8520 вариантных · 1500 только-крит.; вариантный аппарат — 6442 чистых пары →
  **18699 loci** по 299 адхьяям. Данные: `data/edition_comparison_mbh/vanaparva/`. Bulk
  verbatim-текст (`critical_only_and_variants.json`, `significant_absences.json`) остаётся
  gitignored/local-only (права BORI); коммитятся только агрегаты + короткие loci аппарата.
  Остаток 17 парв — тот же скрипт, инженерия готова.

## [1.8.5] - 2026-07-11

### Fixed

- README: счёт книжного аппарата обновлён 788 → **897 нот яруса-2** (+ 1058 яруса-1) с as-of-датой
  11-07-2026 и ссылкой на kosha-манифест — число 788 стояло без даты с эпохи Фазы-1 и вводило в
  заблуждение. Найдено прогоном /artifact-propagate по аппарату; эпистемический осадок аппарата
  зарегистрирован тем же прогоном ([SanskritLexicography PR #328](https://github.com/gasyoun/SanskritLexicography/pull/328):
  GAPS §12 стихи 2/28 · ASSUMPTIONS §7 финальность редакции · DEAD_ENDS §8 OCR-маршрут H370).

## [1.8.4] - 2026-07-11

### Added

- [docs/MANUAL.meta.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/MANUAL.meta.md) —
  метадок операторского справочника: провенанс ([PR #55](https://github.com/gasyoun/CommentaryStrategies/pull/55)),
  таблица ревизий, бэклог живых разделов §5/§8 ([PR #69](https://github.com/gasyoun/CommentaryStrategies/pull/69)).

### Changed

- **Сквозная разводка тройки ролевых руководств** (Fable 5 `claude-fable-5`, PRs
  [#66](https://github.com/gasyoun/CommentaryStrategies/pull/66)–[#74](https://github.com/gasyoun/CommentaryStrategies/pull/74)):
  ссылки + правила синхронизации добавлены во все точки входа — MANUAL §1/§8, README,
  CLAUDE.md (sync-правило для агентов), GEMINI.md (Quick orientation),
  COMMENTARY_ROADMAP (у статуса «на ратификацию»), PHASE2_METHOD, PHASE2_SUNDARA_HANDOFF
  (с precedence-note) и четыре остальных книжных дока единым блоком-указателем;
  попутно двум докам добавлены отсутствовавшие датированные заголовки.
  Вне репозитория (для истории): FEATURES_INDEX J14 освежён
  ([SanskritLexicography PR #325](https://github.com/gasyoun/SanskritLexicography/pull/325)),
  аппарат зарегистрирован в kosha-манифесте ([kosha PR #43](https://github.com/gasyoun/kosha/pull/43)).

## [1.8.3] - 2026-07-10

### Added

**H533 — operator runbook guide for M. Gasuns** (Fable 5 `claude-fable-5`)
- [docs/GASUNS_SUNDARAKANDA_GUIDE.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/GASUNS_SUNDARAKANDA_GUIDE.md) —
  третье ролевое руководство, завершающее тройку (Леонов H497, Костина H517), в
  операторском регистре: критический путь до сдачи ~07-08-2026 (блокеры → шаги),
  порядок голосования четырех листов «от короткого к длинному», параллельный запуск
  рулингов §8 с действующими дефолтами, правило эскалации молчунам, календарная
  прикидка, карта делегирования «только МГ / агентная сессия». Не дублирует
  [docs/MANUAL.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/MANUAL.md)
  (справочник) и [issue №56](https://github.com/gasyoun/CommentaryStrategies/issues/56)
  (чек-лист) — только последовательность и логика решений. Метадок:
  [docs/GASUNS_SUNDARAKANDA_GUIDE.meta.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/GASUNS_SUNDARAKANDA_GUIDE.meta.md).

## [1.8.2] - 2026-07-10

### Added

**H517 — non-technical onboarding guide for E. Kostina** (Fable 5 `claude-fable-5`)
- [docs/KOSTINA_SUNDARAKANDA_GUIDE.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/KOSTINA_SUNDARAKANDA_GUIDE.md) —
  руководство-близнец леоновского под роль первого комментатора / литредактора:
  ее четыре задачи из [issue №57](https://github.com/gasyoun/CommentaryStrategies/issues/57)
  пошагово (ратификация редполитики §3 · судьба ~427 помет `***[Е. Костина]***`,
  блокирующих верстку · статус «Анатолий» · сборочный гейт с Леоновым), общие
  механические разделы параллельны леоновским. Метадок:
  [docs/KOSTINA_SUNDARAKANDA_GUIDE.meta.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/KOSTINA_SUNDARAKANDA_GUIDE.meta.md).

### Changed

- [docs/LEONOV_SUNDARAKANDA_GUIDE.meta.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/LEONOV_SUNDARAKANDA_GUIDE.meta.md):
  бэклог №3 (вычитка Костиной) отменен решением МГ 10-07-2026 в пользу
  собственного руководства Костиной; введено парное правило — общие разделы двух
  руководств редактируются одним коммитом.

## [1.8.1] - 2026-07-10

### Added

**H497 — non-technical onboarding guide for M. Leonov** (Fable 5 `claude-fable-5`)
- [docs/LEONOV_SUNDARAKANDA_GUIDE.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/LEONOV_SUNDARAKANDA_GUIDE.md) —
  большое русское руководство «что, почему и как» для переводчика без технической
  подготовки: два яруса аппарата и двойной гейт по-человечески, его четыре задачи из
  [issue №58](https://github.com/gasyoun/CommentaryStrategies/issues/58) пошагово,
  механика скачивания и локального открытия интерактивных страниц/листов голосования
  (включая `decisions.json` = «переслать письмом, не открывать»), GitHub с нуля,
  словарик, раздел «что в репозитории Вам НЕ нужно» (научный этаж отфильтрован).
  Метадок: [docs/LEONOV_SUNDARAKANDA_GUIDE.meta.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/LEONOV_SUNDARAKANDA_GUIDE.meta.md).

### Fixed

- Имя переводчика: Максим (М.) Леонов — исправлены «А. Леонов» в
  [docs/MANUAL.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/MANUAL.md)
  и «Михаил» в
  [ramayana-leonov/C0_COVER_LETTER.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/ramayana-leonov/C0_COVER_LETTER.md);
  тексты issues №57/58 поправлены на GitHub.

## [1.8.0] - 2026-07-07

### Added

**H276 (session 1) — lexical-layer judge pass, batch-3 quality residues, batch-aware gate apply** (Fable 5 `claude-fable-5` orchestration, Sonnet 5 `claude-sonnet-5` ×15 judge/draft agents ≤3-wide)
- **Lexical judge pass over the full print-bound layer** (611 notes, 67 chapters): §3.4 rubric with
  `contrastive_value` → `lexical_value` (etymology/term/hapax = 2, transparent gloss = 0) and a
  deterministic lemma-in-verse `anchor_precheck` (315 exact / 185 stem / 111 absent) —
  [scripts/lexical_judge_prep.py](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/lexical_judge_prep.py),
  [JUDGE_BRIEF.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/analysis/lexical_judge/JUDGE_BRIEF.md),
  [scripts/lexical_judge_merge.py](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/lexical_judge_merge.py).
  Verdicts: **keep 492 / flag_anchor 45 / reject 32 / edit 23 / park 19**; ranked interactive gate
  sheet [commentarystrategies-sundarakanda-lexical_all68_review.html](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/analysis/lexical_judge/commentarystrategies-sundarakanda-lexical_all68_review.html)
  ([scripts/build_lexical_review_html.py](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/build_lexical_review_html.py));
  the judge ranks, the human gates — every note keeps `review_required`.
- **Sarga-11 phantom anchors resolved** ([scripts/fix_ch11_lexical_anchors.py](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/fix_ch11_lexical_anchors.py)):
  9 hand-curated lexical notes described Sītā-in-the-grove scenes under sarga-11 (feast-hall)
  verse ids; lemma search across the vulgate corpus + GRETIL critical text found 2 honest
  re-anchors (**kṣāma → V.17.30, vivarṇa → V.25.8**, corpus-evidenced) and 7 with no valid target,
  parked to [data/lexical/ch11.qa_removed.json](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/lexical/ch11.qa_removed.json)
  with reasons (incl. rājīvanetri, contradicted by the text: Sītā is utpalapatrākṣī 13.16). Book
  aggregate now 896 notes; merged density ceiling 46.0%.
- **Sarga-12 re-drafted under the quote-or-drop protocol**
  ([SARGA12_REDRAFT_BRIEF.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/analysis/phase2_batch3/SARGA12_REDRAFT_BRIEF.md)):
  the original 3 notes fabricated attributions (cited commentators absent from the verse bundle,
  0/3 judge faithfulness); the re-draft requires a verbatim Devanagari `source_quote` per cited
  commentator and cited ⊆ present. Re-judged **keep 1 / edit 2 / reject 0**; batch-3 aggregate
  re-merged (227 candidates: keep 210 / edit 8 / reject 7 / park 1 / flag_anchor 1) and the gate
  sheet rebuilt.
- **Gate apply extended batch-aware** ([scripts/apply_phase2_decisions.py](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/apply_phase2_decisions.py)):
  `--batch pilot|batch2|batch3|auto` (auto-detects by candidate-set containment), judge fields
  survive the graft, judge-flagged notes (`reject`/`park`/`flag_anchor`) get an explicit
  resolution table, accepting an unfixed `flag_anchor` note (5.21.19) is a hard error without
  `--allow-flagged-anchor`, `--dry-run` supported. Applies stay queued until M.G.'s decisions.json
  files arrive (batch-2 38 · batch-3 227 · footnotes 51 · lexical 611).

## [1.7.0] - 2026-07-07

### Added

**H268 — ЛП camera-ready build: alignment, judge, contrastive scale-out, print master** (Fable 5 `claude-fable-5` orchestration, Sonnet 5 `claude-sonnet-5` drafting/judging)
- **Content-anchor alignment** ([scripts/sa_align.py](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/sa_align.py) `containment` +
  [scripts/extract_yellow_sargas.py](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/extract_yellow_sargas.py)):
  second independent ṭīkā→verse signal for pronominal/paraphrase chunks; verified precision
  (pratīka ∪ content) **0.964** on the 10 gated sargas / **0.949** book-wide (strict pratīka
  metric kept unchanged at 0.888 for honesty); Tattvadīpikā added as 4th segmented commentator
  (sargas 1–6); `--outdir` per-sarga split mode.
- **LLM-as-judge rubric** ([docs/PHASE2_METHOD.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/PHASE2_METHOD.md) §3.4,
  STEP 2b): pointwise refute-framed 5-axis scoring (faithfulness veto · non-triviality ·
  contrastive value · register · anchoring), drafter ≠ judge; review sheet displays verdicts.
  Method provenance: [docs/ACL_METHODS_ADOPTED.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/ACL_METHODS_ADOPTED.md) (new).
- **Contrastive-first style contract** (§3.1 rewritten per H268 decision 3): preferred note form
  «в „Тилаке“ — X; в „Широмани“ — Y; перевод следует …»; single-commentator gloss demoted to fallback.
- **Batch-3 scale-out EXECUTED**: the remaining 58 sargas segmented
  ([data/analysis/phase2_batch3/](https://github.com/gasyoun/CommentaryStrategies/tree/main/data/analysis/phase2_batch3),
  2,734 verse bundles) and drafted by ≤3-wide Sonnet 5 agents under
  [DRAFTING_BRIEF.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/analysis/phase2_batch3/DRAFTING_BRIEF.md) /
  [JUDGE_BRIEF.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/analysis/phase2_batch3/JUDGE_BRIEF.md): **227 candidates
  from 2,734 verses (8.3% accept, 36 contrastive), judged keep 209 / edit 5 / park 1 / reject 11 /
  flag_anchor 1** (faithfulness veto caught real misattributions; one wrong-verse anchor caught);
  M.G. gate sheet
  [commentarystrategies-sundarakanda-commentaries_batch3_review.html](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/analysis/phase2_batch3/commentarystrategies-sundarakanda-commentaries_batch3_review.html);
  agent decision logs in [logs/](https://github.com/gasyoun/CommentaryStrategies/tree/main/data/analysis/phase2_batch3/logs); all notes `review_required`.
  Merged apparatus ceiling now **46.2%** of verses (target 37%); per-sarga apparatus pages rebuilt for all 68 sargas.
- **ЛП print master** ([scripts/build_book_apparatus.py](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/build_book_apparatus.py) →
  [data/book/](https://github.com/gasyoun/CommentaryStrategies/tree/main/data/book)): translation body (68 songs — complete, §8.3 answered) +
  merged status-slotted endnotes + Kostina editorial stratum (WS-E) + appendices skeleton, MD + DOCX;
  [BOOK_BUILD_REPORT.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/book/BOOK_BUILD_REPORT.md) + intro-article skeleton.
- **Density measurement** ([scripts/book_density_stats.py](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/book_density_stats.py)):
  Leonov reader tier-1 = 21.5% of verses (the ~36% benchmark conflated Kostina's 427 editorial-mark
  verses); merged tier-1∪tier-2 ceiling already **41.1%** vs the 37% target; residual gap 73 verses.

### Changed
- [docs/COMMENTARY_ROADMAP.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/COMMENTARY_ROADMAP.md) §6/§7/§9 —
  publisher resolved (**ЛП/Наука**), camera-ready target **~07-08-2026** (decision record:
  [docs/LP_APPARATUS_DESIGN.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/LP_APPARATUS_DESIGN.md), PR #51).

## [1.6.0] - 2026-07-04

### Added

**Agent decision logs preserved in-repo** (MG request 04-07-2026; Fable 5, `claude-fable-5`)
- [scripts/export_agent_logs.py](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/export_agent_logs.py) —
  copies each drafting agent's full Claude Code transcript (the verse-by-verse draft/reject
  reasoning) out of the ephemeral session cache into the repo, as raw `.jsonl` (harness
  `attachment` noise stripped) + a readable `*_reasoning.md` per sarga (assistant text +
  thinking + one-line tool summaries) + an orchestrator extract (assistant messages only —
  the raw main transcript embeds injected private context and is never committed).
- [data/analysis/phase2_batch2/logs/](https://github.com/gasyoun/CommentaryStrategies/tree/main/data/analysis/phase2_batch2/logs) —
  the H142 batch-2 logs: 7 Sonnet 5 (`claude-sonnet-5`) drafting transcripts (sargas
  22/24/26/30/34/39/51) + Fable 5 (`claude-fable-5`) orchestrator log + README.
  [docs/PHASE2_METHOD.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/PHASE2_METHOD.md) §8
  now mandates this export at every batch close-out.

## [1.5.0] - 2026-07-04

### Added

**H142 — Phase-2 pilot gate applied + scale to all 🟡 sargas** (orchestration Fable 5, `claude-fable-5`; drafting Sonnet 5, `claude-sonnet-5`)
- [scripts/apply_phase2_decisions.py](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/apply_phase2_decisions.py) —
  the PHASE2_METHOD §5 apply step: M.G.'s decisions.json (16/16 passed: 9 accept / 7 edit / 0 reject)
  grafted into [data/sundara_ch35/36/37_commentary_to_add.json](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/sundara_ch35_commentary_to_add.json)
  + book aggregate (903 notes) with `gate` stamps; reviewer edit-directives preserved in
  `gate.mg_comment`; stats rebuilt. `review_required` stays true until the Leonov/Kostina assembly gate.
- **Phase-2 batch 2** — sargas 22/24/26/30/34/39/51 drafted per ruling R2 (Sonnet agents, ≤3-wide):
  [data/analysis/phase2_batch2/](https://github.com/gasyoun/CommentaryStrategies/tree/main/data/analysis/phase2_batch2)
  38 candidates / 350 verses considered (10.9%), 312 per-verse rejects with reasons (§7 count
  reconciliation now exact), mandatory tier-1 dedup context in every prompt (41 rejects in the new
  `duplicate_of_tier1` bucket — the pilot's 9/16-collision defect fixed), MG-gate review page
  [review.html](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/analysis/phase2_batch2/review.html).
- Unified apparatus extended to all 10 🟡 sargas
  ([data/apparatus/](https://github.com/gasyoun/CommentaryStrategies/tree/main/data/apparatus)):
  phase2 layer shows MG gate status + `mg_comment`, gated notes are display-only; commentator-subtype
  notes excluded from the lexical layer (no double display).

### Changed

- [scripts/merge_phase2_pilot.py](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/merge_phase2_pilot.py) +
  [scripts/build_pilot_review_html.py](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/build_pilot_review_html.py)
  take a batch-dir argument (default `phase2_pilot`; per-batch localStorage keys, dynamic title).
- [scripts/sa_align.py](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/sa_align.py) `find_sibling()` —
  sibling repos (`sanskrit-util`, `SamudraManthanam`) located by walking up ancestors, fixing
  segmentation runs from nested git worktrees; pratīka precision 0.889 (981/1104) across 10 sargas.

## [1.4.0] - 2026-07-03

### Added

**H141 — unified per-sarga apparatus, pilot sargas 35/36/37** (Fable 5, `claude-fable-5`)
- [scripts/remap_archive_parallels.py](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/remap_archive_parallels.py) —
  deterministic critical (Baroda) → southern-vulgate remap of the 31 DCS archive parallels via the
  verse-level concordance ([data/edition_comparison/concordance.json](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/edition_comparison/concordance.json)):
  23 fully remapped, 1 partial, 7 kept with `edition:"critical"` (verses `critical_only` in the
  concordance — kept, never dropped). Output:
  [data/crosstext/archive_parallels_vulgate.json](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/crosstext/archive_parallels_vulgate.json).
- [scripts/build_sarga_apparatus.py](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/build_sarga_apparatus.py) —
  merges the FIVE note sources per verse (ярус 1 Leonov/Kostina · Фаза-1 lexical · Фаза-2 pilot ·
  edition footnotes · cross-text incl. remapped archive layer) into interactive per-sarga pages
  [data/apparatus/](https://github.com/gasyoun/CommentaryStrategies/tree/main/data/apparatus)`sarga_{NN}.html`
  + machine `sarga_{NN}.json`. Provenance + review-status badges, vote controls on non-tier-1 notes
  (localStorage, «Скачать decisions.json»), tier-1 collisions flagged; notes anchored inside merged
  verse bundles (e.g. `5.35.4347`) re-anchored, not dropped. Pilot totals: 71/34/38 notes for
  sargas 35/36/37; gate-pending layers marked «ожидает гейта М.Г.» until H142.

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
