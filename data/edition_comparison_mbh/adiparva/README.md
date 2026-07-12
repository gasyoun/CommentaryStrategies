# BORI/Poona критическое издание ↔ Нīлакантха-вульгата — Ādипарва (кн. 1)

_Created: 12-07-2026 · Last updated: 12-07-2026_

> Часть [H804](https://github.com/gasyoun/Uprava/blob/main/handoffs/H804-Sonnet_CommentaryStrategies_mbh-edition-apparatus-remaining-parvas_12.07.26.md)
> (продолжение [H784](https://github.com/gasyoun/Uprava/blob/main/handoffs/archive/H784-Sonnet_CommentaryStrategies_mahabharata_nilakantha_vs_critical_apparatus_12.07.26.md)/[H802](https://github.com/gasyoun/Uprava/blob/main/handoffs/archive/H802-Sonnet_CommentaryStrategies_mbh-edition-apparatus-virataparva_12.07.26.md)) —
> тот же пайплайн, без изменений в скриптах. Источники и метод —
> [`../vanaparva/README.md`](../vanaparva/README.md).

## Итог по книге

| | Критическое (BORI) | Вульгата (Нилакантха) | Δ |
|---|---:|---:|---:|
| **Адхьяй** | **225** | **234** | **+9** |
| **Шлок** | **7197** | **8623** (= перепись census) | **+1426** |

- Вульгата содержит **16 целых адхьяй без критического аналога** (14, 15, 22, 24, 52, 59, 98, 108, 112, 116, 129, 133, 139, 140, 149, 224) — не сверено построфно.
- Выравнивание: идентичных **123** · вариантных **5995** (вкл. 13 fuzzy-пар) ·
  «только в критическом» **1079** · транспозиций 0/0.
- Вульгатные шлоки без выравнивания = 2505: **1894 — истинное отсутствие**,
  **611 — переформулировка**.
- Крупнейшие вульгата-only пассажи (600 runs): 1.140.1–93 (93) · 1.223.12–83 (72) · 1.138.6–62 (57) · 1.1.56–109 (54) · 1.67.89–125 (37) · 1.129.1–36 (36).

## Вариантный аппарат (helayo-Gotoh)

[`apparatus_mbh-adiparva_variants.json`](apparatus_mbh-adiparva_variants.json) /
[`APPARATUS_MBH-ADIPARVA_VARIANTS.md`](APPARATUS_MBH-ADIPARVA_VARIANTS.md) —
**4564 чистых вариантных пары** (из 5995 difflib-«variant», 732 слишком
переформулированы → в слой отсутствий, 0 кириллических загрязнений) → **14651 позиционных
loci** по всем 225 адхьяям.

## Файлы

Та же четвёрка, что у Ванапарвы: `book_summary.json`, `concordance.json`,
`significant_absences.json` (gitignored), `critical_only_and_variants.json` (gitignored),
плюс апарат `apparatus_mbh-adiparva_variants.json`/`.md` (committed — короткие loci).

## Проверка против печатного аппарата (App. I)

[H810](https://github.com/gasyoun/Uprava/blob/main/handoffs/H810-Sonnet_CommentaryStrategies_mbh-apparatus-print-verification_12.07.26.md) — `structural_absence` сверен против реального критического аппарата BORI (App. I star-passages, bombay.indology.info/mahabharata/apps/), не реконструкции. **510/1894 флагов подтверждено** (sim >= 0.3, 4-gram char Jaccard; rate 0.269) — независимо засвидетельствовано в манускриптах, собранных редакторами BORI. Полная методика + интерпретация (почему НЕ все остальные — это ожидаемо, App. I не исчерпывает каждое вульгатное издание) — [`../PRINT_VERIFICATION_REPORT.md`](../PRINT_VERIFICATION_REPORT.md). Данные: `print_verification.json` (id/score/matched-supp-id — без текста).

_Dr. Mārcis Gasūns_
