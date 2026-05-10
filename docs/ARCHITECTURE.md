# CommentaryStrategies — Architecture Review

> Версия: 1.0 · Дата: 2026-05-10

---

## 1. Обзор проекта

**CommentaryStrategies** — аналитический репозиторий для сравнительного изучения комментаторских стратегий русских переводчиков санскритских текстов. Корпус: 17 863+ примечаний · 6 переводчиков · 3 традиции (Махабхарата, Рамаяна, Упанишады).

---

## 2. Текущая структура

```
CommentaryStrategies/
├── index.html                          # Сводный анализ 5 переводчиков (68 KB)
├── kalyanov_commentary_analysis.html   # Кальянов (36 KB)
├── vassilkov_commentary_analysis.html  # Васильков (39 KB)
├── erman_commentary_analysis.html      # Эрман (37 KB)
├── grintser_commentary_analysis.html   # Гринцер (32 KB)
├── syrkin_commentary_analysis.html     # Сыркин (39 KB)
├── leonov_kostina_commentary_analysis.html  # Леонов + Костина (114 KB)
├── mahabharata_comparative_analysis.html    # Сравнение трёх (42 KB)
├── visualizations.html                 # Chart.js визуализации (8 KB)
├── .ai_state.md                        # AI state journal (каркас)
├── README.md                           # Промт-шаблон для LLM
├── mahabharata-nilakantha/             # Парсер + тексты Нилакантхи
├── ramayana-leonov/                    # Материалы Леонова
├── tronsky-XXX/                        # Статья для Тронских чтений
│   ├── 1_README.md                     # Мета-инструкция (33 KB)
│   ├── 10_article_v_tronsky_v15.md     # Текущая версия (67 KB)
│   ├── archive/                        # ~25 рабочих версий
│   └── scripts/                        # build_docx.py и утилиты
└── docs/                               # Документация
```

---

## 3. Аналитическое ядро: четырёхосная сетка

Каждое примечание получает координаты по 4 осям:

| Ось | Источник | Категории |
|-----|----------|-----------|
| 1. Тематика | 8 эмпирических рубрик | термин / миф / контекст / реалия / география / отсылка / текстология / философия |
| 2. Тип комментария | Казанский 2025 | A филологический / B реалийный / V исторический / G культурологический |
| 3. Структура толкования | Лидова 2024 | L1–L5 *lakṣaṇa* по «Парашара-упапуране» |
| 4. Категориальная природа | Парибок 2011 | П понятие / К концепт / Д кодификатор |

Предложенная JSON-схема:
```json
{
  "comment_id": "samskrtam.ru/05_ramayana-sundarakanda/leonov/comment_1_1a",
  "shloka_addr": "Rām. Sundara 1.1.a",
  "translator": "leonov",
  "axis_1_topic": ["sanskrit_term", "myth"],
  "axis_2_kazansky": "A",
  "axis_3_lakshana": ["L2", "L5"],
  "axis_4_paribok": "D",
  "cited_indian_commentators": ["tilaka", "bhushana"],
  "cited_western_sources": ["goldman_princeton"]
}
```

---

## 4. Технологический стек

| Компонент | Технология | Назначение |
|-----------|------------|-----------|
| HTML-отчёты | HTML + CSS (PT Serif / PT Sans, Playfair Display) | Аналитические страницы |
| Визуализации | Chart.js 4.4 | Radar, bubble, stacked bar, heatmap (SVG) |
| Парсер | Python (`nilakantha_parser.py`) | Извлечение комментариев |
| Сборка .docx | Python (`build_docx.py`) | Markdown → DOCX |
| Статья | Markdown (v6–v15) | Инкрементная работа |

---

## 5. Архитектурные проблемы

### 5.1 🔴 Критические

| # | Проблема | Рекомендация |
|---|---------|-------------|
| C1 | **Нет единой схемы данных.** Все HTML — ручная верстка, данные вшиты в разметку | Создать `data/` с JSON-файлами; HTML генерировать из данных |
| C2 | **Монолитные HTML.** CSS дублируется в 7 файлах | Вынести в `css/commentary.css` |
| C3 | **Нет валидации.** Запрещённые формулы могут просочиться | CI-скрипт `scripts/validate.py` |

### 5.2 🟡 Структурные

| # | Проблема | Рекомендация |
|---|---------|-------------|
| S1 | **README.md — промт, не описание проекта** | Новый README; промт → `PROMPT_TEMPLATE.md` |
| S2 | **Мета-инструкция погружена в `tronsky-XXX/`** | Сводка в `docs/GEMINI.md` |
| S3 | **Версионирование статьи — по файлам** | Одна рабочая версия; история — в Git |

### 5.3 🟢 Улучшения

| # | Проблема | Рекомендация |
|---|---------|-------------|
| I1 | **`visualizations.html` — данные захардкожены** | Генерировать из JSON |
| I2 | **Нет шаблона для новых переводчиков** | Создать `templates/translator_template.html` |
| I3 | **`.ai_state.md` — пуст** | Заполнить текущим состоянием |

---

## 6. Рекомендуемая целевая архитектура

```
CommentaryStrategies/
├── README.md                    # Обзор проекта (новый)
├── PROMPT_TEMPLATE.md           # Бывший README.md
├── .ai_state.md                 # Живой state для AI-агентов
├── data/                        # JSON-данные (НОВОЕ)
│   ├── schema.json
│   └── {translator}.json
├── css/commentary.css           # Общие стили (НОВОЕ)
├── js/charts.js                 # Общие скрипты (НОВОЕ)
├── pages/                       # HTML-страницы
├── scripts/                     # Утилиты + валидация
├── templates/                   # Шаблоны (НОВОЕ)
├── article/                     # Статья (из tronsky-XXX)
├── corpora/                     # Исходные тексты
└── docs/                        # Документация
```

> ⚠️ Миграция — постепенная, после подачи статьи.

---

## 7. Порядок действий

1. **Сейчас:** заполнить `.ai_state.md`, создать `docs/GEMINI.md`
2. **После подачи:** вынести CSS (C2)
3. **При расширении корпуса:** `data/` с JSON-схемой (C1)
4. **При CI:** `scripts/validate.py` (C3)
