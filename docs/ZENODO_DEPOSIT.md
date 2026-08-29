# Zenodo-депозит и DOI — прогон для владельца (B6)

_Created: 29-08-2026 · Last updated: 29-08-2026_

> Пункт [ROADMAP_2026H2.md §B6](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/ROADMAP_2026H2.md):
> «Zenodo-релиз: DOI, версионирование (нужен человек — депозит)».
> Repo-side половина готова (см. «Статус» ниже); сам депозит — человеческий акт
> (Дорожка C): аккаунт zenodo.org от имени автора. Прогон ниже — ≈15 минут.

## Статус: что уже готово repo-side

| Артефакт | Состояние |
|---|---|
| [CITATION.cff](https://github.com/gasyoun/CommentaryStrategies/blob/main/CITATION.cff) | CFF 1.2.0, type dataset, версия 1.26.1, ORCID, лицензия Apache-2.0 |
| [.zenodo.json](https://github.com/gasyoun/CommentaryStrategies/blob/main/.zenodo.json) | метаданные депозита; версия синхронизирована с CITATION.cff (29-08-2026: устранён дрифт 1.2.0 → 1.26.1); нота о правах включает слой Vālmīki (CC BY 4.0) |
| `scripts/check_release_meta.py` | паритет-гейт «CITATION.cff ↔ .zenodo.json ↔ теги» — введён в CI (Corpus integrity), дрифт класса «cff-version вместо релиза» больше не воспроизводится |
| Релизы GitHub | конвенция уже живая: теги `vX.Y.Z` + [GitHub releases](https://github.com/gasyoun/CommentaryStrategies/releases) (последний — v1.26.1); Zenodo-версионирование садится на неё сверху, ничего менять не надо |
| Права | [data/RIGHTS.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/RIGHTS.md) — пять изданий полнотекстово с атрибуцией; [data/valmiki_PERMISSION.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/valmiki_PERMISSION.md) — грант Palaniappan (CC BY 4.0) |

## Прогон: GitHub–Zenodo интеграция (рекомендуемый путь)

Не ручной upload: после однократной связки каждый GitHub-релиз депозится
автоматически, получает собственный version DOI, а концепт-DOI остаётся
постоянным.

1. Войти на [zenodo.org](https://zenodo.org) через ORCID (`0000-0003-4513-884X`).
2. Профиль → **GitHub** → Connect → выбрать репозиторий `gasyoun/CommentaryStrategies` → включить.
3. Открыть существующий релиз **v1.26.1** и пересохранить (draft → publish) — Zenodo
   заберёт его первым депозитом и создаст концепт-DOI + version DOI. (Каждый
   последующий тег будет депозититься сам.)
4. На странице депозита сверить метаданные: подхватится `.zenodo.json`
   (title, creators, license, related_identifiers `isSupplementTo` репозиторий).
5. Записать оба DOI: концепт-DOI — в CITATION.cff и README (см. «После депозита»);
   version DOI — опционально туда же рядом.
6. Отметить остаток чекбокса B6 закрытым (вписать DOI в сам чекбокс).

## Concept DOI vs version DOI — что цитировать

Zenodo выдаёт на каждый релиз **version DOI** и один постоянный **concept DOI**
(указывает на «все версии»). Цитировать в статьях — **concept DOI**: он не меняется
при выходе v1.27+, а записей «как цитировать» не придётся править после каждого
релиза. Version DOI полезен, когда нужно сослаться на конкретный срез данных
(например, золотую выборку в состоянии на момент подачи статьи).

## Версионирование

- SemVer уже живёт в репо (см. шапку [CHANGELOG.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/CHANGELOG.md)):
  MINOR — новые слои, PATCH — фиксы, MAJOR — слом схемы. Zenodo-версии = теги
  `vX.Y.Z`, ничего дублировать не нужно.
- Рукописные поля версии в `.zenodo.json` и CITATION.cff держать равными тегу
  релиза — это гейтится `scripts/check_release_meta.py` в CI (в shallow-checkout
  теги невидимы, сверяются файлы между собой; локально — и последний тег).
- После первого депозита Zenodo **нельзя удалить** (только закрыть); правки
  метаданных — новую версию релиза, не пересоздание.

## Лицензии при депозите (не всё Apache-2.0)

Zenodo-депозит — это датасет, в нём три правовых слоя; поле `license` в
`.zenodo.json` остаётся Apache-2.0 (как в CITATION.cff), а расщепление живёт в
описании и в `notes`:

| Слой | Правовой режим |
|---|---|
| Код (`scripts/`, инфраструктура) | Apache-2.0 |
| Примечания пяти советских/российских изданий | полнотекстово, с обязательным указанием издания ([data/RIGHTS.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/RIGHTS.md)) |
| Слой Vālmīki (Gita Supersite: текст, 7 комментариев, англ. глоссы) | **CC BY 4.0**, атрибуция S. Palaniappan ([data/valmiki_PERMISSION.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/valmiki_PERMISSION.md)) |

## После депозита — вписать DOI (5 минут)

1. [CITATION.cff](https://github.com/gasyoun/CommentaryStrategies/blob/main/CITATION.cff):
   добавить `doi: <concept-doi>` и `identifier` блок с концепт-DOI.
2. [README.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/README.md)
   §«Как цитировать»: строка «DOI: …» вместо текущего указания «после депозита».
3. [docs/ROADMAP_2026H2.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/ROADMAP_2026H2.md)
   B6: вписать DOI в чекбокс Zenodo-релиза — пункт закрывается целиком.
4. `python scripts/check_release_meta.py` — гейт не должен заругаться
   (DOI-поля он не трогает, проверяется только версия и структура).

## Чего НЕ класть в депозит

- `tronsky-XXX/sources/kazansky_1987.pdf` (20 МБ, скан чужой статьи) — публикация
  релизным ассетом = правовое решение, не механический перенос (Дорожка C,
  отдельный пункт B6 в дорожной карте).
- Любые файлы `*_files/` (веб-дампы вынесены из git, H3558) и рукописные
  `*_commentary_analysis.html` — депозит берёт релиз GitHub как архив, этого
  достаточно.

---

_Dr. Mārcis Gasūns_
