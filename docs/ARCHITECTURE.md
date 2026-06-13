# CommentaryStrategies — Архитектура

> Версия: 2.0 · Дата: 2026-06-13 · Заменяет v1.0 (2026-05-10)
> Что изменилось: слой данных, генерация и DH-экспорт из «рекомендуемого будущего»
> стали действующей реальностью (см. [ROADMAP_2026H2.md](ROADMAP_2026H2.md), Workstream B).

---

## 1. Обзор

**CommentaryStrategies** — аналитический корпус и инструментарий для сравнительного
изучения комментаторских стратегий русских академических переводчиков санскритских
текстов (Махабхарата, Рамаяна, Упанишады).

Два уровня корпуса — не путать:

| Корпус | Объём | Где |
|---|---|---|
| **Аналитический** (весь материал) | 17 863+ примечаний, 7 переводчиков | рукописные `*_commentary_analysis.html` |
| **Размеченная золотая выборка** | 300 примечаний (6 × 50), 4 оси | [data/*_markup_50.json](../data/) |

Золотая выборка — это структурированное ядро (единый источник истины для машинной
обработки); рукописные страницы — развёрнутая аналитика поверх всего материала.

---

## 2. Структура репозитория

```
CommentaryStrategies/
├── index.html                          # сводный дашборд (рукописный)
├── *_commentary_analysis.html          # рукописные эссе по переводчикам (корень)
├── visualizations.html                 # Chart.js (radar / bubble / heatmap)
├── README.md / PROMPT_TEMPLATE.md      # обзор проекта / промт для LLM
├── CITATION.cff                        # как цитировать (CFF 1.2.0)
├── .ai_state.md                        # журнал состояния между сессиями агента
│
├── data/                               # ★ слой данных (источник истины)
│   ├── commentary_schema.json          #   JSON-схема разметки (4 оси + urn)
│   ├── {translator}_markup_50.json     #   золотая выборка, 6×50, с CTS-URN
│   ├── ramayana_epithets.json          #   формульно-эпитетный слой (C2)
│   └── RIGHTS.md                        #   права (полнотекстовая публикация)
├── tei/                                # ★ TEI P5 экспорт (генерируется)
│   └── {translator}.xml
├── pages/                              # ★ data-derived страницы (генерируются)
│   └── {translator}.html               #   НЕ заменяют рукописные эссе
├── scripts/                            # инструментарий (см. §5)
├── templates/translator_template.html  # шаблон для build_pages
├── css/commentary.css                  # общие стили
├── sources/                            # сырые примечания + рабочие листы
├── ramayana-leonov/                    # праксис Сундараканды (C0: профили, пилот)
├── mahabharata-nilakantha/             # парсер Нилакантхи v1.0 (11 КБ) + тексты
├── tronsky-XXX/                        # статья для Тронских чтений + архив
└── docs/                               # документация (этот файл, роадмапы, типология)
```

★ — появилось/наполнилось в цикле v2.0.

---

## 3. Модель данных: четырёхосная сетка

Каждое примечание получает координаты по 4 осям:

| Ось | Источник | Категории |
|-----|----------|-----------|
| 1. Тематика | 9 эмпирических рубрик | термин / миф / контекст / реалия / география / отсылка / текстология / философия / поэтика |
| 2. Тип комментария | Казанский 2025 | A филологический / B реалийный / V исторический / G культурологический |
| 3. Структура толкования | Лидова 2024 | L1–L5 *lakṣaṇa* по «Парашара-упапуране» |
| 4. Категориальная природа | Парибок 2011 | P понятие / K кодификатор / D концепт-расхождение (несоизмеримость) |

Реальная схема — [data/commentary_schema.json](../data/commentary_schema.json). Пример записи
(из [grintser_markup_50.json](../data/grintser_markup_50.json)):

```json
{
  "comment_id": "ram/grintser/c1",
  "urn": "urn:cts:sanskritLit:ramayana:1.1.1",
  "shloka_addr": "Rām. Bāla 1.1.1",
  "translator": "grintser",
  "raw_text": "«…Тёмнокожий (snigdha-varṇaḥ)…» Букв.: «цвета масла»…",
  "has_iast": true,
  "axis_1_topic": ["sanskrit_term"],
  "axis_2_kazansky": "A",
  "axis_3_lakshana": ["L2"],
  "axis_4_paribok": "P"
}
```

**Адресация стихов — каноническими CTS-URN** (`urn:cts:sanskritLit:<work>:<passage>`,
по образцу Perseus/SARIT): один work на эпос (ramayana / mahabharata / <упанишада>),
книга — первый элемент passage. Выводится из `shloka_addr` детерминированно
([derive_urn.py](../scripts/derive_urn.py)) с перекрёстной проверкой книга↔номер.

---

## 4. Поток данных (pipeline)

```
sources/{translator}_notes.json        (сырые примечания)
        │
        ▼  ручная / LLM-разметка по 4 осям
data/{translator}_markup_50.json       (золотая выборка)
        │
        ├─▶ derive_urn.py    → внедряет поле urn (CTS) + валидация
        │
        ├─▶ export_tei.py    → tei/{translator}.xml   (TEI P5, таксономии осей, @ana, @target=URN)
        ├─▶ build_pages.py   → pages/{translator}.html (табличный data-derived вид)
        └─▶ profile_translator.py → профили по осям (длины, IAST, темы) [stdout]

ramayana-leonov/ramayana-formulas_1-2.md
        └─▶ parse_formulas.py → data/ramayana_epithets.json   (формульный слой)

[LLM-пайплайн, gated на ANTHROPIC_API_KEY]
sources/*.json ─▶ annotate_batch.py ─▶ data/*.json ─▶ eval_pipeline.py (≥85% vs gold)
```

Принцип: **данные → артефакты**, не наоборот. `tei/` и `pages/` пересобираемы;
править нужно JSON, а не выход. Рукописные `*_commentary_analysis.html` — вне пайплайна
(содержательно богаче выборки; см. [pages/README.md](../pages/README.md)).

---

## 5. Инструментарий (scripts/)

| Скрипт | Назначение | Зависимости |
|---|---|---|
| [profile_translator.py](../scripts/profile_translator.py) | профили переводчиков по 4 осям (длины, IAST, темы, сравнение) | stdlib |
| [derive_urn.py](../scripts/derive_urn.py) | CTS-URN из `shloka_addr` + внедрение поля + валидация | stdlib |
| [export_tei.py](../scripts/export_tei.py) | JSON → TEI P5 (таксономии, `@ana`, `@target`) | stdlib |
| [parse_formulas.py](../scripts/parse_formulas.py) | эпитетный слой Рамаяны → JSON | stdlib |
| [build_pages.py](../scripts/build_pages.py) | data → `pages/*.html` (переиспользует profile_translator) | stdlib |
| [build_visualizations.py](../scripts/build_visualizations.py) | data → `visualizations.html` (Chart.js, 6-way) | stdlib |
| [extract_false_friends_profile.py](../scripts/extract_false_friends_profile.py) | профиль «ложных друзей» → `data/false_friends_profile.json` (Article 1) | stdlib |
| [profile_nilakantha.py](../scripts/profile_nilakantha.py) | структурный профиль ṭīkā Нилакантхи → `data/nilakantha_profile.json` (Article 4) | `indic-transliteration` |
| [taxonomy.py](../scripts/taxonomy.py) | единый источник кодов осей (читает схему); `assert_covers` | stdlib |
| [annotate_batch.py](../scripts/annotate_batch.py) | LLM-аннотация через Anthropic API (preflight, возобновляемая) | `anthropic` |
| [eval_pipeline.py](../scripts/eval_pipeline.py) | оценка точности vs золотая выборка (порог ≥85%) | stdlib |
| [validate.py](../scripts/validate.py) | схемная валидация корпуса + запрещённые формулы | stdlib |

Третья сторона ([requirements.txt](../requirements.txt)): `anthropic` (пайплайн),
`indic-transliteration` (profile_nilakantha); остальное — stdlib Python 3.10+. Все
data-derived артефакты пересобираемы и проверяются CI-джобом **Corpus integrity**
(.github/workflows/ci.yml): валидация + URN-кросс-чек + git diff после регенерации.

---

## 6. Технологический стек

| Слой | Технология |
|---|---|
| Данные | JSON (рабочий формат) + TEI P5 (экспорт) + CTS-URN (адресация) |
| Аналитика | Python (stdlib) ; Anthropic API для пайплайна |
| Страницы | HTML + [css/commentary.css](../css/commentary.css) ; шаблон [translator_template.html](../templates/translator_template.html) |
| Визуализации | Chart.js 4.4 (radar / bubble / stacked bar / heatmap) |
| Статья / DOCX | Markdown → DOCX (`tronsky-XXX/scripts/build_docx.py`) |

---

## 7. Ключевые архитектурные решения (v2.0)

| Решение | Обоснование |
|---|---|
| **CTS-URN, один work на эпос** | стандарт Perseus/SARIT; книга в passage, без дублирования (не `ramayana.sundara`) |
| **JSON-источник, TEI-экспорт** | LLM-пайплайн удобнее на JSON; TEI даёт DH-легитимность без переписывания |
| **`pages/` отдельно от рукописных** | генерация не затирает богатую ручную аналитику; два источника, две роли |
| **Полнотекстовая публикация** | авторизована для 5 изданий ([RIGHTS.md](../data/RIGHTS.md)); raw_text включается в TEI/релиз |

---

## 8. Известные пробелы

- **Ось 2 (Казанский):** ARCHITECTURE/схема называют B «реалийным», TEI-экспорт —
  «текстологическим». Расхождение именования требует научного решения (см.
  [Kazanskiy-typology.md](../tronsky-XXX/archive/Kazanskiy-typology.md)), не механической правки.
- **Межкодерская надёжность (B5):** нужен второй кодировщик + Cohen's κ.
- **Маппинг на ID samskrtam.ru:** для связи URN с параллельным корпусом нужны их ID.
- **CI:** пересборка `tei/`/`pages/` при изменении данных — пока вручную.
- **Веб-дампы в git:** `महाभारत_files/`, `Рамаяна…_files/` стоит вынести из дерева.
