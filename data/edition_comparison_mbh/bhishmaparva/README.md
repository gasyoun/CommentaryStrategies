# BORI/Poona критическое издание ↔ Нīлакантха-вульгата — Бхӣшмапарва (кн. 6)

_Created: 12-07-2026 · Last updated: 12-07-2026_

> Часть [H804](https://github.com/gasyoun/Uprava/blob/main/handoffs/H804-Sonnet_CommentaryStrategies_mbh-edition-apparatus-remaining-parvas_12.07.26.md)
> (продолжение [H784](https://github.com/gasyoun/Uprava/blob/main/handoffs/archive/H784-Sonnet_CommentaryStrategies_mahabharata_nilakantha_vs_critical_apparatus_12.07.26.md)/[H802](https://github.com/gasyoun/Uprava/blob/main/handoffs/archive/H802-Sonnet_CommentaryStrategies_mbh-edition-apparatus-virataparva_12.07.26.md)) —
> тот же пайплайн, без изменений в скриптах. Источники и метод —
> [`../vanaparva/README.md`](../vanaparva/README.md).

## Итог по книге

| | Критическое (BORI) | Вульгата (Нилакантха) | Δ |
|---|---:|---:|---:|
| **Адхьяй** | **117** | **122** | **+5** |
| **Шлок** | **5406** | **5868** (= перепись census) | **+462** |

- Вульгата содержит **7 целых адхьяй без критического аналога** (15, 23, 24, 48, 49, 99, 117) — не сверено построфно.
- Выравнивание: идентичных **208** · вариантных **4302** (вкл. 17 fuzzy-пар) ·
  «только в критическом» **896** · транспозиций 0/0.
- Вульгатные шлоки без выравнивания = 1358: **750 — истинное отсутствие**,
  **608 — переформулировка**.
- Крупнейшие вульгата-only пассажи (270 runs): 6.48.1–121 (121) · 6.9.32–69 (38) · 6.23.1–28 (28) · 6.49.1–28 (28) · 6.52.42–68 (27) · 6.47.44–67 (24).

## Вариантный аппарат (helayo-Gotoh)

[`apparatus_mbh-bhishmaparva_variants.json`](apparatus_mbh-bhishmaparva_variants.json) /
[`APPARATUS_MBH-BHISHMAPARVA_VARIANTS.md`](APPARATUS_MBH-BHISHMAPARVA_VARIANTS.md) —
**3154 чистых вариантных пары** (из 4302 difflib-«variant», 460 слишком
переформулированы → в слой отсутствий, 0 кириллических загрязнений) → **8945 позиционных
loci** по всем 117 адхьяям.

## Файлы

Та же четвёрка, что у Ванапарвы: `book_summary.json`, `concordance.json`,
`significant_absences.json` (gitignored), `critical_only_and_variants.json` (gitignored),
плюс апарат `apparatus_mbh-bhishmaparva_variants.json`/`.md` (committed — короткие loci).

## Проверка против печатного аппарата (App. I)

[H810](https://github.com/gasyoun/Uprava/blob/main/handoffs/H810-Sonnet_CommentaryStrategies_mbh-apparatus-print-verification_12.07.26.md) — `structural_absence` сверен против реального критического аппарата BORI (App. I star-passages, bombay.indology.info/mahabharata/apps/), не реконструкции. **66/750 флагов подтверждено** (sim >= 0.3, 4-gram char Jaccard; rate 0.088) — независимо засвидетельствовано в манускриптах, собранных редакторами BORI. Полная методика + интерпретация (почему НЕ все остальные — это ожидаемо, App. I не исчерпывает каждое вульгатное издание) — [`../PRINT_VERIFICATION_REPORT.md`](../PRINT_VERIFICATION_REPORT.md). Данные: `print_verification.json` (id/score/matched-supp-id — без текста).

_Dr. Mārcis Gasūns_
