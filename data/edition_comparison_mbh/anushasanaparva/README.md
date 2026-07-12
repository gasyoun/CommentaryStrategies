# BORI/Poona критическое издание ↔ Нīлакантха-вульгата — Анушāсанапарва (кн. 13)

_Created: 12-07-2026 · Last updated: 12-07-2026_

> Часть [H804](https://github.com/gasyoun/Uprava/blob/main/handoffs/H804-Sonnet_CommentaryStrategies_mbh-edition-apparatus-remaining-parvas_12.07.26.md)
> (продолжение [H784](https://github.com/gasyoun/Uprava/blob/main/handoffs/archive/H784-Sonnet_CommentaryStrategies_mahabharata_nilakantha_vs_critical_apparatus_12.07.26.md)/[H802](https://github.com/gasyoun/Uprava/blob/main/handoffs/archive/H802-Sonnet_CommentaryStrategies_mbh-edition-apparatus-virataparva_12.07.26.md)) —
> тот же пайплайн, без изменений в скриптах. Источники и метод —
> [`../vanaparva/README.md`](../vanaparva/README.md).

## Итог по книге

| | Критическое (BORI) | Вульгата (Нилакантха) | Δ |
|---|---:|---:|---:|
| **Адхьяй** | **154** | **168** | **+14** |
| **Шлок** | **6536** | **7469** (= перепись census) | **+933** |

- Вульгата содержит **22 целых адхьяй без критического аналога** (15, 32, 58, 109, 110, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 147, 148, 150) — не сверено построфно.
- Выравнивание: идентичных **160** · вариантных **5288** (вкл. 43 fuzzy-пар) ·
  «только в критическом» **1087** · транспозиций 1/1.
- Вульгатные шлоки без выравнивания = 2020: **1460 — истинное отсутствие**,
  **560 — переформулировка**.
- Крупнейшие вульгата-only пассажи (372 runs): 13.125.1–84 (84) · 13.150.1–82 (82) · 13.148.1–66 (66) · 13.147.1–62 (62) · 13.126.1–50 (50) · 13.40.9–53 (45).

## Вариантный аппарат (helayo-Gotoh)

[`apparatus_mbh-anushasanaparva_variants.json`](apparatus_mbh-anushasanaparva_variants.json) /
[`APPARATUS_MBH-ANUSHASANAPARVA_VARIANTS.md`](APPARATUS_MBH-ANUSHASANAPARVA_VARIANTS.md) —
**4158 чистых вариантных пары** (из 5288 difflib-«variant», 502 слишком
переформулированы → в слой отсутствий, 0 кириллических загрязнений) → **12730 позиционных
loci** по всем 154 адхьяям.

## Файлы

Та же четвёрка, что у Ванапарвы: `book_summary.json`, `concordance.json`,
`significant_absences.json` (gitignored), `critical_only_and_variants.json` (gitignored),
плюс апарат `apparatus_mbh-anushasanaparva_variants.json`/`.md` (committed — короткие loci).

## Проверка против печатного аппарата (App. I)

[H810](https://github.com/gasyoun/Uprava/blob/main/handoffs/H810-Sonnet_CommentaryStrategies_mbh-apparatus-print-verification_12.07.26.md) — `structural_absence` сверен против реального критического аппарата BORI (App. I star-passages, bombay.indology.info/mahabharata/apps/), не реконструкции. **141/1460 флагов подтверждено** (sim >= 0.3, 4-gram char Jaccard; rate 0.097) — независимо засвидетельствовано в манускриптах, собранных редакторами BORI. Полная методика + интерпретация (почему НЕ все остальные — это ожидаемо, App. I не исчерпывает каждое вульгатное издание) — [`../PRINT_VERIFICATION_REPORT.md`](../PRINT_VERIFICATION_REPORT.md). Данные: `print_verification.json` (id/score/matched-supp-id — без текста).

_Dr. Mārcis Gasūns_
