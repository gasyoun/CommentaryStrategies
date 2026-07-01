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
размеченных по четырёхосной сетке.

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

## Аппарат Сундараканды (генерируемый комментарий к переводу М. В. Леонова)

Отдельный активный поток: корпусно-генерируемые русские примечания к Рамаяне V
(Леонов/Костина), добавляемые в параллельный Sa–Ru ридер. **788 примечаний**,
покрывающих все четыре типа комментария Казанского, плотность ≈24 % (грин­церовский
уровень). Все примечания — `review_required` (корпусное свидетельство — уровень шлоки).

| Тип Казанского | Слой | Кол-во |
|---|---|---|
| **А** филологический | лексико-этимологический (`data/lexical/`) + базовый | 617 |
| **В** реалийный | реалии/мифология/география | 122 |
| **Б** текстологический | расхождения/опущения (полный слой диалога 5 комментаторов — Фаза 2, ждёт Gemini-OCR) | 38 |
| **Г** историко-культурологический | вводные статьи (`data/hist_cultural/`) | 11 |

| Файл / директория | Содержание |
|---|---|
| [data/sundara_commentary_to_add.json](data/sundara_commentary_to_add.json) | Итоговый книжный аппарат (788 примечаний, гл. 1–68) |
| [data/lexical/](data/lexical/), [data/hist_cultural/](data/hist_cultural/) | Пер-главные слои (+ `*.rejected.json` с причиной отклонения) |
| [SUNDARA_COMMENTARY_RATIONALE.md](SUNDARA_COMMENTARY_RATIONALE.md) | Решебник: почему ЭТИ примечания и почему не другие |
| [data/sundara_decision_ledger.json](data/sundara_decision_ledger.json) | Машиночитаемый журнал приёма/отклонения |

## Воспроизводимость

Скрипты используют только стандартную библиотеку Python 3.10+ (третья сторона —
только `anthropic` для аннотационного пайплайна; см. [requirements.txt](requirements.txt)).

```sh
python scripts/profile_translator.py grintser vassilkov kalyanov  # профили по осям
python scripts/derive_urn.py                                      # CTS-URN из адресов
python scripts/export_tei.py                                      # JSON → TEI P5 (tei/)
python scripts/parse_formulas.py                                  # эпитетный слой
python scripts/build_pages.py                                     # data → pages/*.html
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
- `mahabharata_comparative_analysis.html` — сравнение трёх переводчиков Махабхараты
- `visualizations.html` — радар (6-way profile), пузырьки, тепловая карта

## Статья

`tronsky-XXX/article_current.md` — финальная версия статьи (v16+) для
XXIX Тронских чтений (ИЛИ РАН, СПб., 2025).
