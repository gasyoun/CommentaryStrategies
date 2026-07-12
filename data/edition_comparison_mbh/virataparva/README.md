# BORI/Poona критическое издание ↔ Нīлакантха-вульгата — Вирāтапарва (кн. 4)

_Created: 12-07-2026 · Last updated: 12-07-2026_

> [H802](https://github.com/gasyoun/Uprava/blob/main/handoffs/archive/H802-Sonnet_CommentaryStrategies_mbh-edition-apparatus-virataparva_12.07.26.md),
> продолжение [H784](https://github.com/gasyoun/Uprava/blob/main/handoffs/archive/H784-Sonnet_CommentaryStrategies_mahabharata_nilakantha_vs_critical_apparatus_12.07.26.md)
> (пилот Ванапарва) — второй парван по тому же пайплайну, без изменений в скриптах.
> Источники и метод те же, что в [`../vanaparva/README.md`](../vanaparva/README.md).

## Итог по книге

| | Критическое (BORI) | Вульгата (Нилакантха) | Δ |
|---|---:|---:|---:|
| **Адхьяй** | **67** | **72** | **+5** |
| **Шлок** | **1 824** | **2 270** (= перепись census) | **+446** |

- Вульгата содержит **5 целых адхьяй без критического аналога** (6, 34, 40, 41, 42) — не
  сверено построфно.
- Выравнивание: идентичных **48** · вариантных **1652** (вкл. 3 fuzzy-пары, ~78% с sim ≥ 0.8) ·
  «только в критическом» **124** · транспозиций 0/0.
- Вульгатные шлоки без выравнивания = 570: **464 — истинное отсутствие**, **106 — переформулировка**.
- Крупнейшие вульгата-only пассажи: 4.55.3–39 (37) · 4.6.1–35 (35) · 4.14.12–31 (20) ·
  4.22.50–64 (15) · 4.61.3–17 (15) · 4.57.1–14 (14).

## Вариантный аппарат (helayo-Gotoh)

[`apparatus_mbh-virataparva_variants.json`](apparatus_mbh-virataparva_variants.json) /
[`APPARATUS_MBH-VIRATAPARVA_VARIANTS.md`](APPARATUS_MBH-VIRATAPARVA_VARIANTS.md) —
**1285 чистых вариантных пары** (из 1652 difflib-«variant», 183 переформулированы слишком
сильно → в слой отсутствий, 0 кириллических загрязнений) → **4032 позиционных loci** по всем
67 адхьяям.

## Файлы

Та же четвёрка, что у Ванапарвы: `book_summary.json`, `concordance.json`,
`significant_absences.json` (gitignored — bulk verbatim текст), `critical_only_and_variants.json`
(gitignored), плюс апарат `apparatus_mbh-virataparva_variants.json`/`.md` (committed — короткие
loci, не полные шлоки).

## Дальше

Оставшиеся 16 парв — тот же `compare_editions_mbh.py PARVA_NO` + `build_edition_apparatus.py`
прогон, движок не меняется.

_Dr. Mārcis Gasūns_
