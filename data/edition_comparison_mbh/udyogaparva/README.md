# BORI/Poona критическое издание ↔ Нīлакантха-вульгата — Удьйогапарва (кн. 5)

_Created: 12-07-2026 · Last updated: 12-07-2026_

> Часть [H804](https://github.com/gasyoun/Uprava/blob/main/handoffs/H804-Sonnet_CommentaryStrategies_mbh-edition-apparatus-remaining-parvas_12.07.26.md)
> (продолжение [H784](https://github.com/gasyoun/Uprava/blob/main/handoffs/H784-Sonnet_CommentaryStrategies_mahabharata_nilakantha_vs_critical_apparatus_12.07.26.md)/[H802](https://github.com/gasyoun/Uprava/blob/main/handoffs/H802-Sonnet_CommentaryStrategies_mbh-edition-apparatus-virataparva_12.07.26.md)) —
> тот же пайплайн, без изменений в скриптах. Источники и метод —
> [`../vanaparva/README.md`](../vanaparva/README.md).

## Итог по книге

| | Критическое (BORI) | Вульгата (Нилакантха) | Δ |
|---|---:|---:|---:|
| **Адхьяй** | **197** | **196** | **-1** |
| **Шлок** | **6063** | **6613** (= перепись census) | **+550** |

- Вульгата содержит **24 целых адхьяй без критического аналога** (45, 63, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 152, 169) — не сверено построфно.
- Выравнивание: идентичных **228** · вариантных **4907** (вкл. 285 fuzzy-пар) ·
  «только в критическом» **901** · транспозиций 26/27.
- Вульгатные шлоки без выравнивания = 1452: **743 — истинное отсутствие**,
  **709 — переформулировка**.
- Крупнейшие вульгата-only пассажи (438 runs): 5.160.2–80 (79) · 5.162.7–56 (50) · 5.160.94–125 (32) · 5.163.24–53 (30) · 5.39.34–59 (26) · 5.63.2–24 (23).

## Вариантный аппарат (helayo-Gotoh)

[`apparatus_mbh-udyogaparva_variants.json`](apparatus_mbh-udyogaparva_variants.json) /
[`APPARATUS_MBH-UDYOGAPARVA_VARIANTS.md`](APPARATUS_MBH-UDYOGAPARVA_VARIANTS.md) —
**3613 чистых вариантных пары** (из 4907 difflib-«variant», 641 слишком
переформулированы → в слой отсутствий, 0 кириллических загрязнений) → **11540 позиционных
loci** по всем 188 адхьяям.

## Файлы

Та же четвёрка, что у Ванапарвы: `book_summary.json`, `concordance.json`,
`significant_absences.json` (gitignored), `critical_only_and_variants.json` (gitignored),
плюс апарат `apparatus_mbh-udyogaparva_variants.json`/`.md` (committed — короткие loci).

## Проверка против печатного аппарата (App. I)

[H810](https://github.com/gasyoun/Uprava/blob/main/handoffs/H810-Sonnet_CommentaryStrategies_mbh-apparatus-print-verification_12.07.26.md) — `structural_absence` сверен против реального критического аппарата BORI (App. I star-passages, bombay.indology.info/mahabharata/apps/), не реконструкции. **169/743 флагов подтверждено** (sim >= 0.3, 4-gram char Jaccard; rate 0.227) — независимо засвидетельствовано в манускриптах, собранных редакторами BORI. Полная методика + интерпретация (почему НЕ все остальные — это ожидаемо, App. I не исчерпывает каждое вульгатное издание) — [`../PRINT_VERIFICATION_REPORT.md`](../PRINT_VERIFICATION_REPORT.md). Данные: `print_verification.json` (id/score/matched-supp-id — без текста).

_Dr. Mārcis Gasūns_
