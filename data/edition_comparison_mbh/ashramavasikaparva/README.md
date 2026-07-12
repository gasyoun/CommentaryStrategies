# BORI/Poona критическое издание ↔ Нīлакантха-вульгата — Āшрамавāсикапарва (кн. 15)

_Created: 12-07-2026 · Last updated: 12-07-2026_

> Часть [H804](https://github.com/gasyoun/Uprava/blob/main/handoffs/H804-Sonnet_CommentaryStrategies_mbh-edition-apparatus-remaining-parvas_12.07.26.md)
> (продолжение [H784](https://github.com/gasyoun/Uprava/blob/main/handoffs/archive/H784-Sonnet_CommentaryStrategies_mahabharata_nilakantha_vs_critical_apparatus_12.07.26.md)/[H802](https://github.com/gasyoun/Uprava/blob/main/handoffs/archive/H802-Sonnet_CommentaryStrategies_mbh-edition-apparatus-virataparva_12.07.26.md)) —
> тот же пайплайн, без изменений в скриптах. Источники и метод —
> [`../vanaparva/README.md`](../vanaparva/README.md).

## Итог по книге

| | Критическое (BORI) | Вульгата (Нилакантха) | Δ |
|---|---:|---:|---:|
| **Адхьяй** | **47** | **39** | **-8** |
| **Шлок** | **1062** | **1088** (= перепись census) | **+26** |

- Вульгата содержит **0 целых адхьяй без критического аналога** — не сверено построфно.
- Выравнивание: идентичных **19** · вариантных **820** (вкл. 1 fuzzy-пар) ·
  «только в критическом» **223** · транспозиций 0/0.
- Вульгатные шлоки без выравнивания = 249: **124 — истинное отсутствие**,
  **125 — переформулировка**.
- Крупнейшие вульгата-only пассажи (37 runs): 15.10.22–52 (31) · 15.2.5–29 (25) · 15.3.5–28 (24) · 15.29.16–33 (18) · 15.36.35–48 (14) · 15.33.6–17 (12).

## Вариантный аппарат (helayo-Gotoh)

[`apparatus_mbh-ashramavasikaparva_variants.json`](apparatus_mbh-ashramavasikaparva_variants.json) /
[`APPARATUS_MBH-ASHRAMAVASIKAPARVA_VARIANTS.md`](APPARATUS_MBH-ASHRAMAVASIKAPARVA_VARIANTS.md) —
**674 чистых вариантных пары** (из 820 difflib-«variant», 73 слишком
переформулированы → в слой отсутствий, 0 кириллических загрязнений) → **2081 позиционных
loci** по всем 45 адхьяям.

## Файлы

Та же четвёрка, что у Ванапарвы: `book_summary.json`, `concordance.json`,
`significant_absences.json` (gitignored), `critical_only_and_variants.json` (gitignored),
плюс апарат `apparatus_mbh-ashramavasikaparva_variants.json`/`.md` (committed — короткие loci).

## Проверка против печатного аппарата (App. I)

[H810](https://github.com/gasyoun/Uprava/blob/main/handoffs/H810-Sonnet_CommentaryStrategies_mbh-apparatus-print-verification_12.07.26.md) — `structural_absence` сверен против реального критического аппарата BORI (App. I star-passages, bombay.indology.info/mahabharata/apps/), не реконструкции. **10/124 флагов подтверждено** (sim >= 0.3, 4-gram char Jaccard; rate 0.081) — независимо засвидетельствовано в манускриптах, собранных редакторами BORI. Полная методика + интерпретация (почему НЕ все остальные — это ожидаемо, App. I не исчерпывает каждое вульгатное издание) — [`../PRINT_VERIFICATION_REPORT.md`](../PRINT_VERIFICATION_REPORT.md). Данные: `print_verification.json` (id/score/matched-supp-id — без текста).

_Dr. Mārcis Gasūns_
