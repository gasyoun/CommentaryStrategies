# BORI/Poona критическое издание ↔ Нīлакантха-вульгата — Ванапарва (Āraṇyakaparvan, кн. 3)

_Created: 12-07-2026 · Last updated: 12-07-2026_

> Пилот [H784](https://github.com/gasyoun/Uprava/blob/main/handoffs/archive/H784-Sonnet_CommentaryStrategies_mahabharata_nilakantha_vs_critical_apparatus_12.07.26.md),
> зеркалирует пайплайн Сундараканды ([`data/edition_comparison/`](../../edition_comparison/README.md),
> [`docs/EDITION_APPARATUS_ROLLOUT.md`](../../../docs/EDITION_APPARATUS_ROLLOUT.md)) на Махабхарату.
> Построено [`scripts/compare_editions_mbh.py`](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/compare_editions_mbh.py)
> (обобщение `compare_editions.py`: pluggable critical/vulgate loaders + verse-id
> scheme) + [`scripts/build_edition_apparatus.py`](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/build_edition_apparatus.py)
> (тот же helayo-style Gotoh-выравниватель, параметризован CLI-флагами).
>
> **Источники (read-only, оба gitignored — права третьих лиц):**
> критическое = `mahabharata-nilakantha/bori-critical/MBh03.txt` (BORI/Poona,
> e-text Tokunaga/John Smith, ISO-15919; провенанс —
> [`BORI_CRITICAL_SOURCE.md`](../../../mahabharata-nilakantha/BORI_CRITICAL_SOURCE.md));
> вульгата = `mahabharata-nilakantha/nilakantha_vulgate_full.jsonl`, `parva_no==3`
> (скрейп sanatana.in; провенанс —
> [`NILAKANTHA_VULGATE_CENSUS.md`](../../../mahabharata-nilakantha/NILAKANTHA_VULGATE_CENSUS.md)).
> Почему Ванапарва: там же живёт уже профилированный корпус Нилакантхи
> (Nalopākhyāna/Rāmopākhyāna, [`NILAKANTHA_PROFILE.md`](../../../mahabharata-nilakantha/NILAKANTHA_PROFILE.md))
> — пилот на знакомом материале.

## Итог по книге

| | Критическое (BORI) | Вульгата (Нилакантха) | Δ |
|---|---:|---:|---:|
| **Адхьяй** | **299** | **315** | **+16** |
| **Шлок** | **10 316** | **11 859** (= перепись census) | **+1 543** |

- Вульгата содержит **25 целых адхьяй без критического аналога** (см. `book_summary.json` →
  `vulgate_extra_adhyayas`: 44,45,46,48,81,142,148,151,156,165,193–198,200,212,223,232,250,253,254,262,263).
  Как и в Рамаяне, часть — реальные интерполяции, часть может быть шумом сопоставления (нумерация
  сдвигается после первой структурной вставки) — не проверено построфно.
- Содержательное выравнивание (канонизация `sanskrit_util.nfold` + fuzzy-назначатель по Jaccard):
  идентичных **296** · вариантных **8520** (вкл. 21 fuzzy-пару, 89% с sim ≥ 0.8) · «только в
  критическом» **1500** · транспозиций 0/0.
- **Вульгатные шлоки без выравнивания = 3043**, по природе разные:
  - **2074 — истинное структурное отсутствие** (Jaccard к любой критич. шлоке < 0.25) → безопасные
    сноски «в критическом издании (BORI) отсутствует».
  - **969 — переформулировка** (Jaccard 0.25–0.5): шлока ЕСТЬ в критическом, но переписана —
    разночтение, не отсутствие.
- **Крупнейшие непрерывные вульгата-only пассажи** (кандидаты в сноски, `significant_absences.json`
  → `runs`): 3.200.1–129 (129 шлок) · 3.46.1–63 (63) · 3.142.1–63 (63) · 3.272.22–73 (52) ·
  3.263.1–49 (49) · 3.99.29–71 (43).

## Вариантный аппарат (helayo-Gotoh)

[`apparatus_mbh-vanaparva_variants.json`](apparatus_mbh-vanaparva_variants.json) /
[`APPARATUS_MBH-VANAPARVA_VARIANTS.md`](APPARATUS_MBH-VANAPARVA_VARIANTS.md) —
**6442 чистых вариантных пары** (из 8520 difflib-«variant», 930 переформулированы слишком
сильно → в слой отсутствий, 0 кириллических загрязнений — в отличие от южной Рамаяны, здесь
их не оказалось) → **18 699 позиционных loci** по всем 299 адхьяям. Нотация: `стих  lemma
(critical) ] variant (vulgate)`. Aligner — spike-grade (char-level + word-expansion);
akṣara-level апгрейд — отдельный [H776](https://github.com/gasyoun/Uprava/blob/main/handoffs/H776-Sonnet_CommentaryStrategies_helayo_aksara_apparatus_aligner_12.07.26.md).

## Файлы

- `book_summary.json` — счётчики, `per_adhyaya_aligned` (по содержанию, не по номеру),
  `vulgate_extra_adhyayas`, book totals.
- `concordance.json` — построчный кросс-волк крит.↔вульг. (`identical`/`variant`/`vulgate_only`/`critical_only`).
- `significant_absences.json` — вульгатные пассажи без критического аналога, `divergence`-тег
  (`structural_absence` vs `reworded`), сгруппированы в непрерывные `runs`.
- `critical_only_and_variants.json` — шлоки только в критическом + пары словесных вариантов
  (similarity-оценка) — вход для `build_edition_apparatus.py`.
- `apparatus_mbh-vanaparva_variants.json` / `.md` — позиционный вариантный аппарат.

## Оговорки

Надёжны: счёт адхьяй (299 vs 315), счёт шлок (10316 vs 11859 — вульгата сверена с независимым
census, совпадает), крупные непрерывные вульгата-only пассажи. Как и в Рамаяне, `critical_only`
(1500) не проверялось на остаточные артефакты глобального LCS-выравнивания (нечёткое назначение
уже частично включено, JACCARD_MIN=0.5/INTER_MIN=3 — 21 пара восстановлена). Whole-extra-adhyaya
список (25) не сверялся построфно с печатным изданием. Интерактивный HTML-отчёт (по образцу
`data/edition_comparison/report.html`) **не строился** в этом пилоте — вне минимального объёма
H784 («только comparator engineering»); JSON+MD были признаны достаточными.

## Дальше (не в этом пилоте)

- Масштабировать на оставшиеся 17 парв Махабхараты (тот же `compare_editions_mbh.py PARVA_NO`
  + `build_edition_apparatus.py --input .../critical_only_and_variants.json ...` — engineering
  готов, остаётся прогон + ревью по каждой парве).
- `build_edition_footnotes.py`-аналог для MBh (сноски-кандидаты из `structural_absence`,
  dedup — здесь нет аналога нот Леонова, дедуп не нужен).
- Human-review гейт перед публикацией любых производных, содержащих чтения BORI (см.
  `BORI_CRITICAL_SOURCE.md` — do-not-redistribute).

## Проверка против печатного аппарата (App. I)

[H810](https://github.com/gasyoun/Uprava/blob/main/handoffs/H810-Sonnet_CommentaryStrategies_mbh-apparatus-print-verification_12.07.26.md) — `structural_absence` сверен против реального критического аппарата BORI (App. I star-passages, bombay.indology.info/mahabharata/apps/), не реконструкции. **403/2074 флагов подтверждено** (sim >= 0.3, 4-gram char Jaccard; rate 0.194) — независимо засвидетельствовано в манускриптах, собранных редакторами BORI. Полная методика + интерпретация (почему НЕ все остальные — это ожидаемо, App. I не исчерпывает каждое вульгатное издание) — [`../PRINT_VERIFICATION_REPORT.md`](../PRINT_VERIFICATION_REPORT.md). Данные: `print_verification.json` (id/score/matched-supp-id — без текста).

_Dr. Mārcis Gasūns_
