# CommentaryStrategies

_Created: 24-04-2026 · Last updated: 14-08-2026_

Аналитический репозиторий для сравнительного изучения **комментаторских стратегий**
русских переводчиков санскритских текстов.

**Корпус:** 17 863+ примечаний · 7 переводчиков (6 основных + Топоров/Елизаренкова) · Махабхарата, Рамаяна, Упанишады

## Быстрый старт

Сводный анализ шести переводчиков: [`index.html`](https://gasyoun.github.io/CommentaryStrategies/).

Официальный интерфейс рецензирования Сундараканды для Е. Костиной:
[`data/apparatus/`](https://gasyoun.github.io/CommentaryStrategies/data/apparatus/) —
одна стартовая страница, все 68 песней, локальное возобновление и единый JSON.
Окончательная отправка всегда выполняется отдельно; локальное сохранение ее не запускает.

## Документация

| Файл | Назначение |
|------|-----------|
| [docs/GEMINI.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/GEMINI.md) | Контекст для AI-агентов (читать первым) |
| [docs/ROADMAP_2026H2.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/ROADMAP_2026H2.md) | Актуальный план (v2.0): DH-санация, праксис Сундараканды, греко-санскритское сравнение |
| [docs/ROADMAP.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/ROADMAP.md) | Прежний пятифазный план (v1.0, фазы 1–3 выполнены) |
| [docs/ARCHITECTURE.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/ARCHITECTURE.md) | Архитектурный обзор |
| [docs/TYPOLOGY_GREEK_SANSKRIT.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/TYPOLOGY_GREEK_SANSKRIT.md) | Сравнительная типология: схолии vs ṭīkā |
| [PROMPT_TEMPLATE.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/PROMPT_TEMPLATE.md) | Универсальный промт для LLM-анализа |

## Корпус и данные

Размеченная **золотая выборка**: 300 примечаний (по 50 от шести переводчиков),
размеченных по четырехосной сетке.

| Файл / директория | Содержание |
|---|---|
| [data/commentary_schema.json](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/commentary_schema.json) | JSON-схема разметки (4 оси + URN + IAST) |
| [data/*_markup_50.json](https://github.com/gasyoun/CommentaryStrategies/tree/main/data) | Золотая выборка, 6×50 примечаний с CTS-URN |
| [data/RIGHTS.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/RIGHTS.md) | Права: полнотекстовая публикация 5 изданий авторизована |
| [data/ramayana_epithets.json](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/ramayana_epithets.json) | Формульно-эпитетный слой Рамаяны (509 статей, кн. 1–2) |
| [tei/](https://github.com/gasyoun/CommentaryStrategies/tree/main/tei) | Экспорт корпуса в TEI P5 (6 файлов) |

**Оси разметки:** (1) тема примечания; (2) тип комментария по номенклатуре
Н. Н. Казанского (A/B/V/G); (3) пять *lakṣaṇa* (L1–L5); (4) категория термина по
модели А. В. Парибка (P/K/D). Адресация стихов — каноническими CTS-URN
(`urn:cts:sanskritLit:<work>:<passage>`).

## Параллельные корпусы (scraped) и PWG→EN Translation Memory

Дополнительные санскритские корпусы, скачанные с [Gita Supersite](https://www.gitasupersite.in),
для обогащения машинного перевода (PWG→EN harness) и диахронического анализа.

| Файл / директория | Содержание |
|---|---|
| [data/gita/](https://github.com/gasyoun/CommentaryStrategies/tree/main/data/gita) | 700 шлок BG × 27 полей (13 санскритских комментаторов + 14 переводчиков); 18 870 текстовых записей |
| [data/brahmasutra/](https://github.com/gasyoun/CommentaryStrategies/tree/main/data/brahmasutra) | 571 сутра + бхашья Шанкарачарьи (766 351 знак) |
| [data/yogasutra/](https://github.com/gasyoun/CommentaryStrategies/tree/main/data/yogasutra) | 195 сутр + бхашья Вьясы + вритти Бходжи (≈190 000 знаков) |
| [data/gita_tm.json](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/gita_tm.json) | 3 883 пар «санскритский термин → английская глосса» (Гамбирананда/Адидевананда) |
| [data/gita_tm_slp1.json](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/gita_tm_slp1.json) | Кроссвок Гита-TM → SLP1-ключи MW (2 173/2 926 терминов, 74 %) |
| [data/bs_term_map_slp1.json](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/bs_term_map_slp1.json) | Философские термины Брахмасутр с глоссами MW (826 терминов) |
| [data/ys_term_map_slp1.json](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/ys_term_map_slp1.json) | Философские термины Йогасутр с глоссами MW (582 термина) |
| [data/typed_link_commentary_citation.tsv](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/typed_link_commentary_citation.tsv) | Type-D-конкорданс `commentary-citation` (Q4.1 пилот, H541): корень → локус Гита-TM, где он цитируется (32 строки, 15 корней) |

Скрипты построения TM:

```sh
python scripts/build_gita_tm.py            # шаг 1: gita_tm.json
python scripts/crosswalk_gita_tm.py        # шаг 2: gita_tm_slp1.json
python scripts/build_sutra_tm.py           # шаги 3–4: bs/ys_term_map_slp1.json
python scripts/build_sutra_tm.py --corpus ys --report   # только Йогасутры
```

**Type-D `commentary-citation` конкорданс (Q4.1 пилот, H541, 11-07-2026):**
[`data/typed_link_commentary_citation.tsv`](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/typed_link_commentary_citation.tsv) —
первый датасет подтипа `commentary-citation` по
[`TYPED_LINK_ID_GRAMMAR.md`](https://github.com/gasyoun/Uprava/blob/main/TYPED_LINK_ID_GRAMMAR.md)
§4c: санскритские корни (`root:<SLP1>`), процитированные в аппарате Гита-TM
(`commentary:gita-tm:<глава.стих>`). Построен
[`scripts/build_root_gita_concordance.py`](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/build_root_gita_concordance.py)
(регенерируемый, не ручной): корневой якорный инвентарь — 704 SLP1-ключа из
[`WhitneyRoots/crosswalk/mw_roots.json`](https://github.com/gasyoun/WhitneyRoots/blob/main/crosswalk/mw_roots.json)
(sibling-репо, 750 MW-корней); сопоставление — общий `TieredMatcher` из
[`kosha/scripts/concordance_core.py`](https://github.com/gasyoun/kosha/blob/main/scripts/concordance_core.py)
против `data/gita_tm_slp1.json` (никакого повторного матчера, spec §6.3); локусы стихов
извлечены из встроенных меток `(BG <гл>.<стих> <код>)` в глоссах `gita_tm.json`. Пилот
даёт 32 строки / 15 корней, все на тире `exact` (0.7 % от 2 087 SLP1-ключей кроссвока —
честно и ожидаемо: голые формы корней редко совпадают с номинальными леммами кроссвока
дословно; `floor`/`relaxed`/`fuzzy` дали 0 совпадений в этом прогоне).
Провалидировано 0-ошибок против
[`kosha/scripts/typed_link_lint.py`](https://github.com/gasyoun/kosha/blob/main/scripts/typed_link_lint.py).
Зарегистрировано по-репозиторно (D2b) — **не** добавлено в
[`kosha/data/manifest/datasets.json`](https://github.com/gasyoun/kosha/blob/main/data/manifest/datasets.json)
до релиза Q2.1.

Все четыре TM-файла совместимы с `mw_en_tm.json` (187 506 записей) по ключам SLP1 и готовы
к подключению в `gen_opt_harness2 --lang en` как слой шастрического обогащения для
судьи-Opus.

## Аппарат Сундараканды (генерируемый комментарий к переводу М. В. Леонова)

Отдельный активный поток: корпусно-генерируемые русские примечания к Рамаяне V
(Леонов/Костина), добавляемые в параллельный Sa–Ru ридер. **897 примечаний яруса-2**
(на 11-07-2026, до гейтов М.Г.; + 1058 собственных примечаний яруса-1), покрывающих
все четыре типа комментария Казанского, плотность ≈24 % (гринцеровский
уровень). Все примечания яруса-2 — `review_required` (корпусное свидетельство — уровень шлоки).

Четыре типа комментария по номенклатуре Казанского:

| Тип Казанского | Слой |
|---|---|
| **А** филологический | лексико-этимологический ([data/lexical/](https://github.com/gasyoun/CommentaryStrategies/tree/main/data/lexical)) + базовый |
| **В** реалийный | реалии/мифология/география |
| **Б** текстологический | расхождения/опущения (полный слой диалога 5 комментаторов — Фаза 2, ждет Gemini-OCR) |
| **Г** историко-культурологический | вводные статьи ([data/hist_cultural/](https://github.com/gasyoun/CommentaryStrategies/tree/main/data/hist_cultural)) |

Пер-типовой ценз на этапе 788 примечаний: А 617 · В 122 · Б 38 · Г 11 (см.
[changelog.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/changelog.md)).
Текущий итог яруса-2 (897 на 11-07-2026) отражает последующие добавления
лексического слоя (тип А).

| Файл / директория | Содержание |
|---|---|
| [data/sundara_commentary_to_add.json](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/sundara_commentary_to_add.json) | Итоговый книжный аппарат яруса-2 (897 примечаний на 11-07-2026, гл. 1–68; зарегистрирован в [kosha-манифесте](https://github.com/gasyoun/kosha/blob/main/data/manifest/datasets.json) как `sundarakanda-two-tier-apparatus`, restricted) |
| [data/lexical/](https://github.com/gasyoun/CommentaryStrategies/tree/main/data/lexical), [data/hist_cultural/](https://github.com/gasyoun/CommentaryStrategies/tree/main/data/hist_cultural) | Пер-главные слои (+ `*.rejected.json` с причиной отклонения) |
| [SUNDARA_COMMENTARY_RATIONALE.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/SUNDARA_COMMENTARY_RATIONALE.md) | Решебник: почему ЭТИ примечания и почему не другие |
| [data/sundara_decision_ledger.json](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/sundara_decision_ledger.json) | Машиночитаемый журнал приема/отклонения |
| [docs/MANUAL.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/MANUAL.md) | Операторский справочник тома: два яруса, конвейер, листы гейтов, apply |
| [data/apparatus/](https://gasyoun.github.io/CommentaryStrategies/data/apparatus/) | Официальный Pages-портал: 68 бюллетеней Костиной, прогресс, восстановление и единый экспорт |
| [docs/LEONOV_SUNDARAKANDA_GUIDE.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/LEONOV_SUNDARAKANDA_GUIDE.md) · [docs/KOSTINA_SUNDARAKANDA_GUIDE.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/KOSTINA_SUNDARAKANDA_GUIDE.md) · [docs/GASUNS_SUNDARAKANDA_GUIDE.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/GASUNS_SUNDARAKANDA_GUIDE.md) | Три ролевых руководства «что делать именно тебе»: переводчик и литредактор — нетехнический регистр, оркестратор — ранбук критического пути |

## Воспроизводимость

Скрипты используют только стандартную библиотеку Python 3.10+ (третья сторона —
только `anthropic` для аннотационного пайплайна; см.
[requirements.txt](https://github.com/gasyoun/CommentaryStrategies/blob/main/requirements.txt)).

```sh
python scripts/profile_translator.py grintser vassilkov kalyanov  # профили по осям
python scripts/derive_urn.py                                      # CTS-URN из адресов
python scripts/export_tei.py                                      # JSON → TEI P5 (tei/)
python scripts/parse_formulas.py                                  # эпитетный слой
python scripts/build_pages.py                                     # data → pages/*.html

# PWG→EN Translation Memory (требует indic-transliteration и sibling SanskritLexicography/)
python scripts/build_gita_tm.py            # Гита TM (шаг 1)
python scripts/crosswalk_gita_tm.py        # SLP1 кроссвок (шаг 2)
python scripts/build_sutra_tm.py           # Брахмасутры + Йогасутры (шаги 3–4)
```

[pages/](https://github.com/gasyoun/CommentaryStrategies/tree/main/pages) — автогенерируемое табличное представление данных (НЕ заменяет
рукописные аналитические страницы, см. [pages/README.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/pages/README.md)).

## Как цитировать

См. [CITATION.cff](https://github.com/gasyoun/CommentaryStrategies/blob/main/CITATION.cff). Лицензия **кода** — Apache-2.0 ([LICENSE](https://github.com/gasyoun/CommentaryStrategies/blob/main/LICENSE));
условия использования **текстов примечаний** — отдельно, см. [data/RIGHTS.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/RIGHTS.md)
(полнотекстовая публикация авторизована, с обязательным указанием издания-источника).

### Корпус Вальмики (Gita Supersite) — CC BY 4.0, по разрешению

Санскритский текст, семь традиционных санскритских комментариев и современные английские
пословные глоссы Рамаяны в [data/valmiki_shlokas/](https://github.com/gasyoun/CommentaryStrategies/tree/main/data/valmiki_shlokas) и
[data/valmiki_commentaries/](https://github.com/gasyoun/CommentaryStrategies/tree/main/data/valmiki_commentaries) используются **по разрешению** редактора
раздела Вальмики Gita Supersite (см. [data/valmiki_PERMISSION.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/valmiki_PERMISSION.md),
[data/RIGHTS.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/RIGHTS.md)). Лицензия компиляции — **CC BY 4.0**. Обязательная атрибуция:

> Vālmīki Rāmāyaṇa, as published on the Gita Supersite (https://valmiki.gitasupersite.in), used by permission of the editor, Sudalaimuthu Palaniappan.

## Аналитические страницы

- [`index.html`](https://github.com/gasyoun/CommentaryStrategies/blob/main/index.html) — сравнение 6 переводчиков (Кальянов, Васильков, Эрман, Гринцер, Сыркин, Леонов)
- [`leonov_kostina_commentary_analysis.html`](https://github.com/gasyoun/CommentaryStrategies/blob/main/leonov_kostina_commentary_analysis.html) — Леонов + Костина, Сундараканда
- [`toporov_commentary_analysis.html`](https://github.com/gasyoun/CommentaryStrategies/blob/main/toporov_commentary_analysis.html) — В. Н. Топоров, «Текст и комментарий»
- [`elizarenkova_commentary_analysis.html`](https://github.com/gasyoun/CommentaryStrategies/blob/main/elizarenkova_commentary_analysis.html) — Т. Я. Елизаренкова, Ригведа
- [`mahabharata_comparative_analysis.html`](https://github.com/gasyoun/CommentaryStrategies/blob/main/mahabharata_comparative_analysis.html) — сравнение трех переводчиков Махабхараты
- [`visualizations.html`](https://github.com/gasyoun/CommentaryStrategies/blob/main/visualizations.html) — радар (6-way profile), пузырьки, тепловая карта

## Статьи

Публикационный конвейер репозитория (полный статус — в
[Uprava/ARTICLES.md](https://github.com/gasyoun/Uprava/blob/main/ARTICLES.md)):

- [`tronsky-XXX/article_current.md`](https://github.com/gasyoun/CommentaryStrategies/blob/main/tronsky-XXX/article_current.md) — статья для XXIX Тронских чтений (ИЛИ РАН), русские переводчики эпоса.
- [`articles/`](https://github.com/gasyoun/CommentaryStrategies/tree/main/articles) — статьи о концептуальной непереводимости, Бхагавадгите, комментарии Нилакантхи (RU/EN), «ложных друзьях».

_Dr. Mārcis Gasūns_
