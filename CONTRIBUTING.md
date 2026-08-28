# Contributing to CommentaryStrategies — для индологов

_Created: 28-08-2026 · Last updated: 28-08-2026_

> Part of the [Sanskrit Lexicon](https://github.com/sanskrit-lexicon) project. Inherits the [org-wide contribution standard](https://github.com/sanskrit-lexicon/COLOGNE/blob/main/CONTRIBUTING.md).

Этот файл — как индологу (переводчику, комментатору, редактору) добавить материал
в аналитический корпус: нового переводчика, разметку примечаний по четырём осям,
и как пройти валидацию до PR. Общая архитектура — [docs/ARCHITECTURE.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/ARCHITECTURE.md);
производственный конвейер тома «Сундараканда» — [docs/MANUAL.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/MANUAL.md).

## 1. Что здесь лежит

Корпус двух уровней (не путать):

| Уровень | Объём | Где |
|---|---|---|
| Рукописные аналитические эссе | 17 863+ примечаний, 7 переводчиков | `*_commentary_analysis.html` в корне |
| Размеченная золотая выборка | 300 примечаний (6 переводчиков × 50), 4 оси | `data/*_markup_50.json` |

Золотая выборка — единый источник истины для машинной обработки (профилирование,
TEI-экспорт, сравнение переводчиков). Всё машинное строится поверх неё.

## 2. Добавить нового переводчика (путь A)

Порядок шагов — как это сделано для `erman`, `grintser`, `kalyanov`, `vassilkov`,
`syrkin`, `leonov` (примеры: [data/erman_markup_50.json](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/erman_markup_50.json)):

1. **Оцифруйте полный корпус примечаний** переводчика → `data/<translator>_full.json`
   (структура — по образцу существующих `*_full.json`: комментарий + адрес шлоки).
2. **Отберите 50 репрезентативных примечаний** (золотая выборка: разные книги,
   разные типы — словарные, реалии, текстология, философия) → `data/<translator>_markup_50.json`.
3. **Разметьте каждое по четырём осям** (см. §3) — формат и обязательные поля
   задаёт [data/commentary_schema.json](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/commentary_schema.json).
4. **Добавьте переводчика в enum схемы**: `translator` в
   `data/commentary_schema.json` — без этого разметка не пройдёт валидацию.
5. **Прогоните профилировщик**: `python scripts/profile_translator.py <translator>`
   — он считает распределения по осям, длины, долю IAST. Это и есть проверка,
   что разметка машинно читаема и статистически осмысленна.
6. **Сгенерируйте страницу**: `python scripts/build_pages.py` (шаблон —
   `templates/translator_template.html`); при желании — TEI-выгрузка
   `python scripts/export_tei.py`.
7. **Напишите рукописное эссе** `<translator>_commentary_analysis.html` (корень) —
   это содержательная часть, схема её не заменяет.

## 3. Разметить примечание по четырём осям (путь B)

Одна запись JSON на одно примечание. Обязательные поля: `comment_id`,
`translator`, `axis_1_topic`, `axis_2_kazansky`; рекомендуемые: `urn`,
`shloka_addr`, `raw_text`, `has_iast`, `axis_3_lakshana`, `axis_4_paribok`,
`cited_indian_commentators`, `cited_western_sources`.

| Поле | Значения | Суть |
|---|---|---|
| `comment_id` | `{source}/{translator}/comment_{shloka}` | уникальный ID записи |
| `shloka_addr` | `Rām. Sundara 5.1.1`, `MBh. Bhīṣma 6.1.3` | человекочитаемый адрес |
| `urn` | `urn:cts:sanskritLit:ramayana:5.1.1` | канонический CTS-URN; выводится из адреса скриптом `python scripts/derive_urn.py` |
| **Ось 1** `axis_1_topic` | `sanskrit_term, myth, context, realia, geography, reference, textology, philosophy, poetics` | темы; можно 2–3 на запись |
| **Ось 2** `axis_2_kazansky` | `A, B, V, G` | тип комментария (текстологическая номенклатура Казанского) |
| **Ось 3** `axis_3_lakshana` | `L1…L5` | лингвистическая характеристика примечания |
| **Ось 4** `axis_4_paribok` | `P, K, D` | глубина комментаторского хода: P — глосса-идентификация, K — системное позиционирование, D — дискурсивное развертывание |

Канонические ловушки оси 2 (частые ошибки):

- **A** — филологический/словарный: примечание о самой санскритской словоформе
  («буквально…», морфология, этимология, передача эпитета).
- **B** — текстологический: метатекст о состоянии источника или акте перевода
  (опущение, разночтение рукописей, «поздняя вставка»).
- **V** — историко-культурный/реальный: божество, демон, царь, каста, река,
  оружие, воинский строй, сцена сюжета. **Реалии идут только сюда, никогда в B.**
- **G** — культурологический/интерпретационный: абстрактные понятия (дхарма,
  мокша, юга) и интерпретативные ходы, кросс-традиционные сопоставления.

Ось 2: каноничный маппинг — золотая выборка `data/*_markup_50.json` и
`scripts/export_tei.py`; обоснование — `tronsky-XXX/archive/Kazanskiy-typology.md`.
Ось 4: канон `P/K/D`, значения `C` нет — решение зафиксировано в
[docs/AXIS4_KD_DECISION.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/AXIS4_KD_DECISION.md).

`has_iast: true` — если в `raw_text` есть санскрит в IAST; `editor` — только для
Леонова (`kostina`).

## 4. Валидация (до PR)

Локально, из корня репозитория:

```sh
python scripts/validate.py
```

Проверяет: запрещённые формулы (фактические ошибки, известные по истории
проекта — например, склонение «Парибка», а не «Парибок»; несуществующий том
Леонова с фиктивным годом 2022) и структурные правила аналитических HTML-страниц
(дизайн-система: `css/commentary.css`, breadcrumb, `<main class="container">`).

CI (`.github/workflows/ci.yml`) гоняет тот же `scripts/validate.py` на каждый PR —
зелёный PR = те же проверки прошли в облаке.

## 5. Права и что нельзя коммитить

- Полнотексты переводов в репозиторий не попадают: права — InC, корпус хранит
  только библиографические описания и разметку примечаний. Реестр —
  [data/RIGHTS.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/RIGHTS.md).
- Сканы PDF (защищённые издания) — отдельный правовой акт, не коммитим.
- Код — Apache 2.0 ([LICENSE](https://github.com/gasyoun/CommentaryStrategies/blob/main/LICENSE));
  разметка и документация — открытые данные.

## 6. Механика PR

1. Fork → feature-branch → PR (как в [org-стандарте](https://github.com/sanskrit-lexicon/COLOGNE/blob/main/CONTRIBUTING.md)).
2. PR должен держать `scripts/validate.py` и CI зелёными.
3. Нетехнический регистр работы над томом — [docs/MANUAL.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/MANUAL.md)
   и ролевые руководства (`docs/LEONOV_SUNDARAKANDA_GUIDE.md`, `docs/KOSTINA_SUNDARAKANDA_GUIDE.md`).

_Dr. Mārcis Gasūns_
