# BORI/Poona критическое издание ↔ Нīлакантха-вульгата — Сваргарохаṇапарва (кн. 18)

_Created: 12-07-2026 · Last updated: 12-07-2026_

> Часть [H804](https://github.com/gasyoun/Uprava/blob/main/handoffs/H804-Sonnet_CommentaryStrategies_mbh-edition-apparatus-remaining-parvas_12.07.26.md)
> (продолжение [H784](https://github.com/gasyoun/Uprava/blob/main/handoffs/H784-Sonnet_CommentaryStrategies_mahabharata_nilakantha_vs_critical_apparatus_12.07.26.md)/[H802](https://github.com/gasyoun/Uprava/blob/main/handoffs/H802-Sonnet_CommentaryStrategies_mbh-edition-apparatus-virataparva_12.07.26.md)) —
> тот же пайплайн, без изменений в скриптах. Источники и метод —
> [`../vanaparva/README.md`](../vanaparva/README.md).

## Итог по книге

| | Критическое (BORI) | Вульгата (Нилакантха) | Δ |
|---|---:|---:|---:|
| **Адхьяй** | **5** | **7** | **+2** |
| **Шлок** | **194** | **316** (= перепись census) | **+122** |

- Вульгата содержит **2 целых адхьяй без критического аналога** (6, 7) — не сверено построфно.
- Выравнивание: идентичных **6** · вариантных **173** (вкл. 2 fuzzy-пар) ·
  «только в критическом» **15** · транспозиций 0/0.
- Вульгатные шлоки без выравнивания = 137: **125 — истинное отсутствие**,
  **12 — переформулировка**.
- Крупнейшие вульгата-only пассажи (20 runs): 18.6.1–87 (87) · 18.5.11–21 (11) · 18.7.2–11 (10) · 18.5.44–49 (6) · 18.5.61–66 (6) · 18.4.4–5 (2).

## Вариантный аппарат (helayo-Gotoh)

[`apparatus_mbh-swargarohanaparva_variants.json`](apparatus_mbh-swargarohanaparva_variants.json) /
[`APPARATUS_MBH-SWARGAROHANAPARVA_VARIANTS.md`](APPARATUS_MBH-SWARGAROHANAPARVA_VARIANTS.md) —
**129 чистых вариантных пары** (из 173 difflib-«variant», 16 слишком
переформулированы → в слой отсутствий, 0 кириллических загрязнений) → **344 позиционных
loci** по всем 5 адхьяям.

## Файлы

Та же четвёрка, что у Ванапарвы: `book_summary.json`, `concordance.json`,
`significant_absences.json` (gitignored), `critical_only_and_variants.json` (gitignored),
плюс апарат `apparatus_mbh-swargarohanaparva_variants.json`/`.md` (committed — короткие loci).

## Проверка против печатного аппарата (App. I)

[H810](https://github.com/gasyoun/Uprava/blob/main/handoffs/H810-Sonnet_CommentaryStrategies_mbh-apparatus-print-verification_12.07.26.md) — `structural_absence` сверен против реального критического аппарата BORI (App. I star-passages, bombay.indology.info/mahabharata/apps/), не реконструкции. **21/125 флагов подтверждено** (sim >= 0.3, 4-gram char Jaccard; rate 0.168) — независимо засвидетельствовано в манускриптах, собранных редакторами BORI. Полная методика + интерпретация (почему НЕ все остальные — это ожидаемо, App. I не исчерпывает каждое вульгатное издание) — [`../PRINT_VERIFICATION_REPORT.md`](../PRINT_VERIFICATION_REPORT.md). Данные: `print_verification.json` (id/score/matched-supp-id — без текста).

_Dr. Mārcis Gasūns_
