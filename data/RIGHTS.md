# Права на публикацию текстов примечаний (raw_text)

> Решение принято М. Гасунсом 2026-06-12 (сессия Claude Code; D4 в [ROADMAP_2026H2.md](../docs/ROADMAP_2026H2.md)).

## Решение

Тексты примечаний (`raw_text`) **всех пяти советских/российских изданий публикуются полнотекстово** — в репозитории и в Zenodo-релизе корпуса.

| Корпус | Издание | Статус публикации |
|---|---|---|
| Кальянов | Махабхарата, 1950–1996 | ✅ полный текст |
| Васильков / Невелева | Махабхарата, 1987–2005 | ✅ полный текст |
| Эрман | Бхишмапарва, 2009 | ✅ полный текст |
| Гринцер | Рамаяна (Ладомир) | ✅ полный текст |
| Сыркин | Упанишады | ✅ полный текст |
| Леонов / Костина | Рамаяна, кн. 5 (в работе) | по согласованию с авторами (соавторы проекта) |
| Топоров (Дхаммапада), Елизаренкова (Ригведа) | — | уточнить отдельно при включении в релиз данных |

## Следствия

- Zenodo-релиз (задача B6) — полнотекстовый, не metadata-only.
- TEI-экспорт (задача B3) включает полный `raw_text` в `<note>`.
- Лицензия данных указывается отдельно от лицензии кода ([LICENSE](../LICENSE)); для текстов примечаний — указание источника и издания обязательно в каждой записи (`cited` поля схемы).

---

## Vālmīki Rāmāyaṇa corpus (Gita Supersite) — ✅ RIGHTS CLEARED (2026-07-01)

Covers [`valmiki_shlokas/`](valmiki_shlokas/) (Sanskrit verse + modern English word‑by‑word glosses &
explanations) and [`valmiki_commentaries/`](valmiki_commentaries/) (seven traditional Sanskrit
commentaries). Full grant archived verbatim in [`valmiki_PERMISSION.md`](valmiki_PERMISSION.md).

| Field | Value |
|---|---|
| Grantor | **Sudalaimuthu Palaniappan**, editor of the Vālmīki Rāmāyaṇa section, Gita Supersite |
| Grantee | Mārcis Gasūns · Date: 1 July 2026 |
| Scope | Sanskrit text + 7 Sanskrit commentaries + modern English glosses/explanations |
| Terms | Non‑exclusive, worldwide, perpetual, royalty‑free; **attribution required** |
| Publication | ✅ open‑source repo + Zenodo, under an open license |
| **License** | **CC BY 4.0** (compilation/derived apparatus; underlying materials used by permission) |

**Required attribution (verbatim, in repo + README + Zenodo):**

> Vālmīki Rāmāyaṇa, as published on the Gita Supersite (https://valmiki.gitasupersite.in), used by permission of the editor, Sudalaimuthu Palaniappan.

Residual-risk note: editor-level grant (not a separate IIT Kanpur institutional instrument); relied upon
in good faith. Details in [`valmiki_PERMISSION.md`](valmiki_PERMISSION.md).

---

## GRETIL critical edition + valmikiramayan.net Southern text — ⛔ SUPERSEDED (2026-07-12), removed from current tree

Formerly covered `edition_comparison/other_kandas/` (Bāla/Ayodhyā/Araṇya/Kiṣkindhā critical↔southern
content-alignment against valmikiramayan.net, no permission on file, published on M.G.'s explicit
risk-acceptance). **Replaced same-day** once a properly-licensed alternative source was found already
sitting in this repo (`data/valmiki_shlokas/` — Gita Supersite, CC BY 4.0, see the section above) that
covers the same 4 kāṇḍas. The valmikiramayan.net-sourced files were deleted from the current tree in
this commit (still recoverable from git history if ever needed) — see
[`edition_comparison/gitasupersite_kandas/`](edition_comparison/gitasupersite_kandas/) for the current,
rights-clean version. GRETIL critical text itself (CC BY-NC-SA 4.0, Tokunaga/Smith/Neill) is unaffected
and still in use as the critical-edition side of the comparison — attribution still owed, not yet added
to README.

## GRETIL critical edition + Gita Supersite Southern text — ✅ both sides rights-clean (2026-07-12)

Covers [`edition_comparison/gitasupersite_kandas/`](edition_comparison/gitasupersite_kandas/) (Bāla/
Ayodhyā/Araṇya/Kiṣkindhā critical↔southern content-alignment, plus Yuddhakāṇḍa Leonov-source↔Gita
Supersite in the RussianRamayana repo). Critical side = GRETIL (CC BY-NC-SA 4.0, attribution owed,
not yet added to README). Southern side = Gita Supersite `data/valmiki_shlokas/` (CC BY 4.0, permission
already on file per the section above — `valmiki_PERMISSION.md`). No open rights question remains for
this material.
