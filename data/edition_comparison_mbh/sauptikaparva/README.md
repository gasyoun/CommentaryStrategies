# BORI/Poona критическое издание ↔ Нīлакантха-вульгата — Саупатикапарва (кн. 10)

_Created: 12-07-2026 · Last updated: 12-07-2026_

> Часть [H804](https://github.com/gasyoun/Uprava/blob/main/handoffs/H804-Sonnet_CommentaryStrategies_mbh-edition-apparatus-remaining-parvas_12.07.26.md)
> (продолжение [H784](https://github.com/gasyoun/Uprava/blob/main/handoffs/H784-Sonnet_CommentaryStrategies_mahabharata_nilakantha_vs_critical_apparatus_12.07.26.md)/[H802](https://github.com/gasyoun/Uprava/blob/main/handoffs/H802-Sonnet_CommentaryStrategies_mbh-edition-apparatus-virataparva_12.07.26.md)) —
> тот же пайплайн, без изменений в скриптах. Источники и метод —
> [`../vanaparva/README.md`](../vanaparva/README.md).

## Итог по книге

| | Критическое (BORI) | Вульгата (Нилакантха) | Δ |
|---|---:|---:|---:|
| **Адхьяй** | **18** | **18** | **+0** |
| **Шлок** | **772** | **803** (= перепись census) | **+31** |

- Вульгата содержит **0 целых адхьяй без критического аналога** — не сверено построфно.
- Выравнивание: идентичных **24** · вариантных **562** (вкл. 0 fuzzy-пар) ·
  «только в критическом» **186** · транспозиций 0/0.
- Вульгатные шлоки без выравнивания = 217: **122 — истинное отсутствие**,
  **95 — переформулировка**.
- Крупнейшие вульгата-only пассажи (36 runs): 10.8.91–124 (34) · 10.6.12–33 (22) · 10.7.31–49 (19) · 10.9.30–46 (17) · 10.8.23–38 (16) · 10.2.20–34 (15).

## Вариантный аппарат (helayo-Gotoh)

[`apparatus_mbh-sauptikaparva_variants.json`](apparatus_mbh-sauptikaparva_variants.json) /
[`APPARATUS_MBH-SAUPTIKAPARVA_VARIANTS.md`](APPARATUS_MBH-SAUPTIKAPARVA_VARIANTS.md) —
**454 чистых вариантных пары** (из 562 difflib-«variant», 46 слишком
переформулированы → в слой отсутствий, 0 кириллических загрязнений) → **1295 позиционных
loci** по всем 18 адхьяям.

## Файлы

Та же четвёрка, что у Ванапарвы: `book_summary.json`, `concordance.json`,
`significant_absences.json` (gitignored), `critical_only_and_variants.json` (gitignored),
плюс апарат `apparatus_mbh-sauptikaparva_variants.json`/`.md` (committed — короткие loci).

## Проверка против печатного аппарата (App. I)

[H810](https://github.com/gasyoun/Uprava/blob/main/handoffs/H810-Sonnet_CommentaryStrategies_mbh-apparatus-print-verification_12.07.26.md) — `structural_absence` сверен против реального критического аппарата BORI (App. I star-passages, bombay.indology.info/mahabharata/apps/), не реконструкции. **16/122 флагов подтверждено** (sim >= 0.3, 4-gram char Jaccard; rate 0.131) — независимо засвидетельствовано в манускриптах, собранных редакторами BORI. Полная методика + интерпретация (почему НЕ все остальные — это ожидаемо, App. I не исчерпывает каждое вульгатное издание) — [`../PRINT_VERIFICATION_REPORT.md`](../PRINT_VERIFICATION_REPORT.md). Данные: `print_verification.json` (id/score/matched-supp-id — без текста).

_Dr. Mārcis Gasūns_
