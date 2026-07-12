# BORI/Poona критическое издание ↔ Нīлакантха-вульгата — Дроṇапарва (кн. 7)

_Created: 12-07-2026 · Last updated: 12-07-2026_

> Часть [H804](https://github.com/gasyoun/Uprava/blob/main/handoffs/H804-Sonnet_CommentaryStrategies_mbh-edition-apparatus-remaining-parvas_12.07.26.md)
> (продолжение [H784](https://github.com/gasyoun/Uprava/blob/main/handoffs/H784-Sonnet_CommentaryStrategies_mahabharata_nilakantha_vs_critical_apparatus_12.07.26.md)/[H802](https://github.com/gasyoun/Uprava/blob/main/handoffs/H802-Sonnet_CommentaryStrategies_mbh-edition-apparatus-virataparva_12.07.26.md)) —
> тот же пайплайн, без изменений в скриптах. Источники и метод —
> [`../vanaparva/README.md`](../vanaparva/README.md).

## Итог по книге

| | Критическое (BORI) | Вульгата (Нилакантха) | Δ |
|---|---:|---:|---:|
| **Адхьяй** | **173** | **202** | **+29** |
| **Шлок** | **8152** | **9641** (= перепись census) | **+1489** |

- Вульгата содержит **30 целых адхьяй без критического аналога** (6, 50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 76, 81, 88, 126, 189, 191, 192, 194) — не сверено построфно.
- Выравнивание: идентичных **215** · вариантных **5920** (вкл. 21 fuzzy-пар) ·
  «только в критическом» **2017** · транспозиций 0/0.
- Вульгатные шлоки без выравнивания = 3506: **2249 — истинное отсутствие**,
  **1257 — переформулировка**.
- Крупнейшие вульгата-only пассажи (529 runs): 7.54.1–58 (58) · 7.32.25–74 (50) · 7.55.1–50 (50) · 7.200.86–132 (47) · 7.52.1–45 (45) · 7.112.17–57 (41).

## Вариантный аппарат (helayo-Gotoh)

[`apparatus_mbh-dronaparva_variants.json`](apparatus_mbh-dronaparva_variants.json) /
[`APPARATUS_MBH-DRONAPARVA_VARIANTS.md`](APPARATUS_MBH-DRONAPARVA_VARIANTS.md) —
**4565 чистых вариантных пары** (из 5920 difflib-«variant», 580 слишком
переформулированы → в слой отсутствий, 0 кириллических загрязнений) → **12875 позиционных
loci** по всем 173 адхьяям.

## Файлы

Та же четвёрка, что у Ванапарвы: `book_summary.json`, `concordance.json`,
`significant_absences.json` (gitignored), `critical_only_and_variants.json` (gitignored),
плюс апарат `apparatus_mbh-dronaparva_variants.json`/`.md` (committed — короткие loci).

## Проверка против печатного аппарата (App. I)

[H810](https://github.com/gasyoun/Uprava/blob/main/handoffs/H810-Sonnet_CommentaryStrategies_mbh-apparatus-print-verification_12.07.26.md) — `structural_absence` сверен против реального критического аппарата BORI (App. I star-passages, bombay.indology.info/mahabharata/apps/), не реконструкции. **410/2249 флагов подтверждено** (sim >= 0.3, 4-gram char Jaccard; rate 0.182) — независимо засвидетельствовано в манускриптах, собранных редакторами BORI. Полная методика + интерпретация (почему НЕ все остальные — это ожидаемо, App. I не исчерпывает каждое вульгатное издание) — [`../PRINT_VERIFICATION_REPORT.md`](../PRINT_VERIFICATION_REPORT.md). Данные: `print_verification.json` (id/score/matched-supp-id — без текста).

_Dr. Mārcis Gasūns_
