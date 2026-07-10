# CommentaryStrategies

Аналитический репозиторий для сравнительного изучения **комментаторских стратегий**
русских переводчиков санскритских текстов.

**Корпус:** 17 863+ примечаний · 7 переводчиков (6 основных + Топоров/Елизаренкова) · Махабхарата, Рамаяна, Упанишады

## Быстрый старт

Открыть `index.html` в браузере — сводный анализ пяти переводчиков.

## Документация

| Файл | Назначение |
|------|-----------|
| [docs/GEMINI.md](docs/GEMINI.md) | Контекст для AI-агентов (читать первым) |
| [docs/ROADMAP_2026H2.md](docs/ROADMAP_2026H2.md) | Актуальный план (v2.0): DH-санация, праксис Сундараканды, греко-санскритское сравнение |
| [docs/ROADMAP.md](docs/ROADMAP.md) | Прежний пятифазный план (v1.0, фазы 1–3 выполнены) |
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | Архитектурный обзор |
| [docs/TYPOLOGY_GREEK_SANSKRIT.md](docs/TYPOLOGY_GREEK_SANSKRIT.md) | Сравнительная типология: схолии vs ṭīkā |
| [PROMPT_TEMPLATE.md](PROMPT_TEMPLATE.md) | Универсальный промт для LLM-анализа |

## Корпус и данные

Размеченная **золотая выборка**: 300 примечаний (по 50 от шести переводчиков),
размеченных по четырехосной сетке.

| Файл / директория | Содержание |
|---|---|
| [data/commentary_schema.json](data/commentary_schema.json) | JSON-схема разметки (4 оси + URN + IAST) |
| [data/*_markup_50.json](data/) | Золотая выборка, 6×50 примечаний с CTS-URN |
| [data/RIGHTS.md](data/RIGHTS.md) | Права: полнотекстовая публикация 5 изданий авторизована |
| [data/ramayana_epithets.json](data/ramayana_epithets.json) | Формульно-эпитетный слой Рамаяны (509 статей, кн. 1–2) |
| [tei/](tei/) | Экспорт корпуса в TEI P5 (6 файлов) |

**Оси разметки:** (1) тема примечания; (2) тип комментария по номенклатуре
Н. Н. Казанского (A/B/V/G); (3) пять *lakṣaṇa* (L1–L5); (4) категория термина по
модели А. В. Парибка (P/K/D). Адресация стихов — каноническими CTS-URN
(`urn:cts:sanskritLit:<work>:<passage>`).

## Параллельные корпусы (scraped) и PWG→EN Translation Memory

Дополнительные санскритские корпусы, скачанные с [Gita Supersite](https://www.gitasupersite.in),
для обогащения машинного перевода (PWG→EN harness) и диахронического анализа.

| Файл / директория | Содержание |
|---|---|
| [data/gita/](data/gita/) | 700 шлок BG × 27 полей (13 санскритских комментаторов + 14 переводчиков); 18 870 текстовых записей |
| [data/brahmasutra/](data/brahmasutra/) | 571 сутра + бхашья Шанкарачарьи (766 351 знак) |
| [data/yogasutra/](data/yogasutra/) | 195 сутр + бхашья Вьясы + вритти Бходжи (≈190 000 знаков) |
| [data/gita_tm.json](data/gita_tm.json) | 3 883 пар «санскритский термин → английская глосса» (Гамбирананда/Адидевананда) |
| [data/gita_tm_slp1.json](data/gita_tm_slp1.json) | Кроссвок Гита-TM → SLP1-ключи MW (2 173/2 926 терминов, 74 %) |
| [data/bs_term_map_slp1.json](data/bs_term_map_slp1.json) | Философские термины Брахмасутр с глоссами MW (826 терминов) |
| [data/ys_term_map_slp1.json](data/ys_term_map_slp1.json) | Философские термины Йогасутр с глоссами MW (582 термина) |

Скрипты построения TM:

```sh
python scripts/build_gita_tm.py            # шаг 1: gita_tm.json
python scripts/crosswalk_gita_tm.py        # шаг 2: gita_tm_slp1.json
python scripts/build_sutra_tm.py           # шаги 3–4: bs/ys_term_map_slp1.json
python scripts/build_sutra_tm.py --corpus ys --report   # только Йогасутры
```

Все четыре TM-файла совместимы с `mw_en_tm.json` (187 506 записей) по ключам SLP1 и готовы
к подключению в `gen_opt_harness2 --lang en` как слой шастрического обогащения для
судьи-Opus.

## Аппарат Сундараканды (генерируемый комментарий к переводу М. В. Леонова)

Отдельный активный поток: корпусно-генерируемые русские примечания к Рамаяне V
(Леонов/Костина), добавляемые в параллельный Sa–Ru ридер. **897 примечаний яруса-2**
(на 11-07-2026, до гейтов М.Г.; + 1058 собственных примечаний яруса-1), покрывающих
все четыре типа комментария Казанского, плотность ≈24 % (грин­церовский
уровень). Все примечания яруса-2 — `review_required` (корпусное свидетельство — уровень шлоки).

| Тип Казанского | Слой | Кол-во |
|---|---|---|
| **А** филологический | лексико-этимологический (`data/lexical/`) + базовый | 617 |
| **В** реалийный | реалии/мифология/география | 122 |
| **Б** текстологический | расхождения/опущения (полный слой диалога 5 комментаторов — Фаза 2, ждет Gemini-OCR) | 38 |
| **Г** историко-культурологический | вводные статьи (`data/hist_cultural/`) | 11 |

| Файл / директория | Содержание |
|---|---|
| [data/sundara_commentary_to_add.json](data/sundara_commentary_to_add.json) | Итоговый книжный аппарат яруса-2 (897 примечаний на 11-07-2026, гл. 1–68; зарегистрирован в [kosha-манифесте](https://github.com/gasyoun/kosha/blob/main/data/manifest/datasets.json) как `sundarakanda-two-tier-apparatus`, restricted) |
| [data/lexical/](data/lexical/), [data/hist_cultural/](data/hist_cultural/) | Пер-главные слои (+ `*.rejected.json` с причиной отклонения) |
| [SUNDARA_COMMENTARY_RATIONALE.md](SUNDARA_COMMENTARY_RATIONALE.md) | Решебник: почему ЭТИ примечания и почему не другие |
| [data/sundara_decision_ledger.json](data/sundara_decision_ledger.json) | Машиночитаемый журнал приема/отклонения |
| [docs/MANUAL.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/MANUAL.md) | Операторский справочник тома: два яруса, конвейер, листы гейтов, apply |
| [docs/LEONOV_SUNDARAKANDA_GUIDE.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/LEONOV_SUNDARAKANDA_GUIDE.md) · [docs/KOSTINA_SUNDARAKANDA_GUIDE.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/KOSTINA_SUNDARAKANDA_GUIDE.md) · [docs/GASUNS_SUNDARAKANDA_GUIDE.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/GASUNS_SUNDARAKANDA_GUIDE.md) | Три ролевых руководства «что делать именно тебе»: переводчик и литредактор — нетехнический регистр, оркестратор — ранбук критического пути |

## Воспроизводимость

Скрипты используют только стандартную библиотеку Python 3.10+ (третья сторона —
только `anthropic` для аннотационного пайплайна; см. [requirements.txt](requirements.txt)).

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

[pages/](pages/) — автогенерируемое табличное представление данных (НЕ заменяет
рукописные аналитические страницы, см. [pages/README.md](pages/README.md)).

## Как цитировать

См. [CITATION.cff](CITATION.cff). Лицензия **кода** — Apache-2.0 ([LICENSE](LICENSE));
условия использования **текстов примечаний** — отдельно, см. [data/RIGHTS.md](data/RIGHTS.md)
(полнотекстовая публикация авторизована, с обязательным указанием издания-источника).

### Корпус Вальмики (Gita Supersite) — CC BY 4.0, по разрешению

Санскритский текст, семь традиционных санскритских комментариев и современные английские
пословные глоссы Рамаяны в [data/valmiki_shlokas/](data/valmiki_shlokas/) и
[data/valmiki_commentaries/](data/valmiki_commentaries/) используются **по разрешению** редактора
раздела Вальмики Gita Supersite (см. [data/valmiki_PERMISSION.md](data/valmiki_PERMISSION.md),
[data/RIGHTS.md](data/RIGHTS.md)). Лицензия компиляции — **CC BY 4.0**. Обязательная атрибуция:

> Vālmīki Rāmāyaṇa, as published on the Gita Supersite (https://valmiki.gitasupersite.in), used by permission of the editor, Sudalaimuthu Palaniappan.

## Аналитические страницы

- `index.html` — сравнение 6 переводчиков (Кальянов, Васильков, Эрман, Гринцер, Сыркин, Леонов)
- `leonov_kostina_commentary_analysis.html` — Леонов + Костина, Сундараканда
- `toporov_commentary_analysis.html` — В. Н. Топоров, «Текст и комментарий»
- `elizarenkova_commentary_analysis.html` — Т. Я. Елизаренкова, Ригведа
- `mahabharata_comparative_analysis.html` — сравнение трех переводчиков Махабхараты
- `visualizations.html` — радар (6-way profile), пузырьки, тепловая карта

## Статья

`tronsky-XXX/article_current.md` — финальная версия статьи (v16+) для
XXIX Тронских чтений (ИЛИ РАН, СПб., 2025).
