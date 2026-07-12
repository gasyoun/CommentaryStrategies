# BORI/Poona критическое издание ↔ Нīлакантха-вульгата — Стрӣпарва (кн. 11)

_Created: 12-07-2026 · Last updated: 12-07-2026_

> Часть [H804](https://github.com/gasyoun/Uprava/blob/main/handoffs/H804-Sonnet_CommentaryStrategies_mbh-edition-apparatus-remaining-parvas_12.07.26.md)
> (продолжение [H784](https://github.com/gasyoun/Uprava/blob/main/handoffs/archive/H784-Sonnet_CommentaryStrategies_mahabharata_nilakantha_vs_critical_apparatus_12.07.26.md)/[H802](https://github.com/gasyoun/Uprava/blob/main/handoffs/archive/H802-Sonnet_CommentaryStrategies_mbh-edition-apparatus-virataparva_12.07.26.md)) —
> тот же пайплайн, без изменений в скриптах. Источники и метод —
> [`../vanaparva/README.md`](../vanaparva/README.md).

## Итог по книге

| | Критическое (BORI) | Вульгата (Нилакантха) | Δ |
|---|---:|---:|---:|
| **Адхьяй** | **27** | **27** | **+0** |
| **Шлок** | **730** | **825** (= перепись census) | **+95** |

- Вульгата содержит **1 целых адхьяй без критического аналога** (9) — не сверено построфно.
- Выравнивание: идентичных **26** · вариантных **631** (вкл. 0 fuzzy-пар) ·
  «только в критическом» **73** · транспозиций 0/0.
- Вульгатные шлоки без выравнивания = 168: **107 — истинное отсутствие**,
  **61 — переформулировка**.
- Крупнейшие вульгата-only пассажи (47 runs): 11.9.2–23 (22) · 11.20.21–34 (14) · 11.5.4–13 (10) · 11.27.21–30 (10) · 11.8.27–34 (8) · 11.27.4–10 (7).

## Вариантный аппарат (helayo-Gotoh)

[`apparatus_mbh-striparva_variants.json`](apparatus_mbh-striparva_variants.json) /
[`APPARATUS_MBH-STRIPARVA_VARIANTS.md`](APPARATUS_MBH-STRIPARVA_VARIANTS.md) —
**504 чистых вариантных пары** (из 631 difflib-«variant», 45 слишком
переформулированы → в слой отсутствий, 0 кириллических загрязнений) → **1427 позиционных
loci** по всем 27 адхьяям.

## Файлы

Та же четвёрка, что у Ванапарвы: `book_summary.json`, `concordance.json`,
`significant_absences.json` (gitignored), `critical_only_and_variants.json` (gitignored),
плюс апарат `apparatus_mbh-striparva_variants.json`/`.md` (committed — короткие loci).

## Проверка против печатного аппарата (App. I)

[H810](https://github.com/gasyoun/Uprava/blob/main/handoffs/H810-Sonnet_CommentaryStrategies_mbh-apparatus-print-verification_12.07.26.md) — `structural_absence` сверен против реального критического аппарата BORI (App. I star-passages, bombay.indology.info/mahabharata/apps/), не реконструкции. **35/107 флагов подтверждено** (sim >= 0.3, 4-gram char Jaccard; rate 0.327) — независимо засвидетельствовано в манускриптах, собранных редакторами BORI. Полная методика + интерпретация (почему НЕ все остальные — это ожидаемо, App. I не исчерпывает каждое вульгатное издание) — [`../PRINT_VERIFICATION_REPORT.md`](../PRINT_VERIFICATION_REPORT.md). Данные: `print_verification.json` (id/score/matched-supp-id — без текста).

_Dr. Mārcis Gasūns_
