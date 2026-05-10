# ARCHITECTURE_TASKS.md — Инструкции для Gemini Flash

> Этот файл — пошаговый план выполнения каждой задачи из `docs/ARCHITECTURE.md §5`.
> Целевой агент: **Gemini Flash** (инструменты: bash, create_file, str_replace, view, web_fetch).
> Выполнять задачи в порядке разделов. Перед каждой задачей читать `.ai_state.md`.

---

## Как читать этот файл

- **PRECONDITION** — что должно быть выполнено до начала задачи
- **STEPS** — конкретные команды и содержимое файлов
- **VERIFY** — как проверить, что задача выполнена
- **UPDATE** — что обновить в `.ai_state.md` после

---

## 🔴 C3 — Создать `scripts/validate.py` (ДЕЛАТЬ ПЕРВЫМ)

**Почему первым:** самая быстрая задача, устраняет риск появления запрещённых строк в любом последующем артефакте.

**PRECONDITION:** ничего, выполняется независимо.

**STEPS:**

Создать файл `scripts/validate.py`:

```python
#!/usr/bin/env python3
"""
validate.py — CI validation for CommentaryStrategies.
Checks all text files for forbidden strings and structural rules.
Exit code 0 = pass, 1 = fail.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent

FORBIDDEN = [
    # (regex_pattern, human_readable_description)
    (r'М\.\s*:\s*Наука,\s*2022',          'Леонов 2022 том не существует'),
    (r'Парибо[каоу]',                      'Неверное склонение: должно быть «Парибка»'),
    (r'Goldman.*М\.\s*:\s*Наука',          'Смешение Goldman с русским изданием'),
    (r'М\.\s*:\s*Наука,\s*2022.*[Лл]еонов|[Лл]еонов.*М\.\s*:\s*Наука,\s*2022',
                                           'Леонов + 2022 в одной строке'),
]

EXTENSIONS = {'.html', '.md', '.txt', '.json', '.py'}

def check_file(path: Path) -> list[str]:
    errors = []
    try:
        text = path.read_text(encoding='utf-8', errors='replace')
    except Exception as e:
        return [f'{path}: read error: {e}']
    for pattern, desc in FORBIDDEN:
        for m in re.finditer(pattern, text):
            line_num = text[:m.start()].count('\n') + 1
            errors.append(f'{path}:{line_num}: [{desc}] → «{m.group()}»')
    return errors

def main():
    skip_dirs = {'.git', '__pycache__', 'archive', 'महाभारत_files',
                 'Рамаяна. Книга 5. Сундараканда_files'}
    all_errors = []
    checked = 0
    for path in ROOT.rglob('*'):
        if any(part in skip_dirs for part in path.parts):
            continue
        if path.suffix.lower() not in EXTENSIONS:
            continue
        if not path.is_file():
            continue
        errs = check_file(path)
        all_errors.extend(errs)
        checked += 1

    print(f'Checked {checked} files.')
    if all_errors:
        print(f'\n❌ {len(all_errors)} error(s) found:\n')
        for e in all_errors:
            print(' ', e)
        sys.exit(1)
    else:
        print('✅ All checks passed.')
        sys.exit(0)

if __name__ == '__main__':
    main()
```

Запустить немедленно:
```bash
cd /path/to/CommentaryStrategies
python scripts/validate.py
```

Если есть ошибки — исправить найденные строки в соответствующих файлах через `str_replace` и перезапустить до чистого прогона.

**VERIFY:** `python scripts/validate.py` завершается с кодом 0 и выводит `✅ All checks passed.`

**UPDATE `.ai_state.md`:**
```
- [x] C3: scripts/validate.py создан и прошёл чисто
```

---

## 🟡 S1 — Переименовать `README.md` → `PROMPT_TEMPLATE.md`, создать новый `README.md`

**PRECONDITION:** C3 выполнен (validate.py прошёл).

**STEPS:**

```bash
# Шаг 1: переименовать через git
git mv README.md PROMPT_TEMPLATE.md
```

Создать новый `README.md`:

```markdown
# CommentaryStrategies

Аналитический репозиторий для сравнительного изучения **комментаторских стратегий**
русских переводчиков санскритских текстов.

**Корпус:** 17 863+ примечаний · 6 переводчиков · Махабхарата, Рамаяна, Упанишады

## Быстрый старт

Открыть `index.html` в браузере — сводный анализ пяти переводчиков.

## Документация

| Файл | Назначение |
|------|-----------|
| `docs/GEMINI.md` | Контекст для AI-агентов (читать первым) |
| `docs/ROADMAP.md` | Пятифазный план развития |
| `docs/ARCHITECTURE.md` | Архитектурный обзор |
| `PROMPT_TEMPLATE.md` | Универсальный промт для LLM-анализа |

## Аналитические страницы

- `index.html` — сравнение 5 переводчиков (Кальянов, Васильков, Эрман, Гринцер, Сыркин)
- `leonov_kostina_commentary_analysis.html` — Леонов + Костина, Сундараканда
- `mahabharata_comparative_analysis.html` — сравнение трёх переводчиков Махабхараты
- `visualizations.html` — радар, пузырьки, тепловая карта

## Статья

`tronsky-XXX/10_article_v_tronsky_v15.md` — текущая версия статьи для
XXIX Тронских чтений (ИЛИ РАН, СПб.).
```

```bash
git add README.md PROMPT_TEMPLATE.md
git commit -m "docs: rename README to PROMPT_TEMPLATE, add project README"
```

**VERIFY:**
- `README.md` описывает проект, не содержит промт-шаблон
- `PROMPT_TEMPLATE.md` содержит исходный промт целиком
- `git log --oneline -1` показывает коммит

**UPDATE `.ai_state.md`:**
```
- [x] S1: README.md пересоздан, промт → PROMPT_TEMPLATE.md
```

---

## 🟡 S2 — Мета-инструкция доступна из корня (уже частично выполнено)

**PRECONDITION:** `docs/GEMINI.md` существует (создан ранее).

**STEPS:**

`docs/GEMINI.md` уже содержит сводку мета-инструкции из `tronsky-XXX/1_README.md`.
Добавить ссылку в новый `README.md`:

Проверить, что в README.md есть строка:
```
| `docs/GEMINI.md` | Контекст для AI-агентов (читать первым) |
```

Если нет — добавить через str_replace.

Дополнительно: добавить в `.ai_state.md` ссылку на `docs/GEMINI.md` в шапку:

```markdown
# Project Objective: [цель сессии]
> Agent context: docs/GEMINI.md | Full meta: tronsky-XXX/1_README.md
```

**VERIFY:** агент, получив только `README.md`, может найти `docs/GEMINI.md` за ≤ 2 шага.

**UPDATE `.ai_state.md`:** `- [x] S2: docs/GEMINI.md связан с README`

---

## 🟡 S3 — Один рабочий файл статьи, история в Git

**PRECONDITION:** C3 (validate.py) выполнен.

**STEPS:**

```bash
# Шаг 1: убедиться, что v15 — актуальная версия
ls -la tronsky-XXX/10_article_v_tronsky_v*.md
# Ожидаемый максимум: v15

# Шаг 2: переименовать рабочий файл
git mv tronsky-XXX/10_article_v_tronsky_v15.md tronsky-XXX/article_current.md

# Шаг 3: переместить все версии в archive/ (если ещё не там)
git mv tronsky-XXX/10_article_v_tronsky_v*.md tronsky-XXX/archive/ 2>/dev/null || true
git mv tronsky-XXX/3_gasuns_tronsky*.md tronsky-XXX/archive/ 2>/dev/null || true
# НЕ трогать: 1_README.md, erman_bhg-4.24.md, Kazanskiy-typology.md, policy.md
# НЕ трогать: К вопросу о термине adhyakṣa...

# Шаг 4: проверить структуру
ls tronsky-XXX/
# Должно остаться: 1_README.md, article_current.md, archive/, scripts/, + доп. файлы

# Шаг 5: обновить ссылку в docs/GEMINI.md
# str_replace: заменить все упоминания 'v15.md' на 'article_current.md'

# Шаг 6: коммит
git add -A
git commit -m "refactor: one working article file, versions to archive"
```

**VERIFY:**
- `tronsky-XXX/article_current.md` существует
- `ls tronsky-XXX/*.md` возвращает ≤ 5 файлов (не 15+)
- `docs/GEMINI.md` ссылается на `article_current.md`

**UPDATE `.ai_state.md`:** `- [x] S3: статья → article_current.md, архив убран в archive/`

---

## 🟢 I3 — Обновить `.ai_state.md` (выполнять после каждой сессии)

**PRECONDITION:** любая другая задача завершена.

**STEPS:**

`.ai_state.md` должен всегда содержать актуальное состояние. Шаблон:

```markdown
# Project Objective: [описание цели текущей сессии]
> Agent context: docs/GEMINI.md | Full meta: tronsky-XXX/1_README.md

## ➡️ Next Steps (Queue)
- [ ] [следующая задача с номером из ARCHITECTURE_TASKS.md]

## 🚧 Current Work-In-Progress (WIP)
- [ ] [текущая задача]

## 🧠 Dev Notes & Hypotheses
- YYYY-MM-DD: [что сделано, что обнаружено]

## ✅ Completed (Recent only)
- [x] [задача] — [дата]
```

**Правило:** после каждого коммита — обновить `.ai_state.md` и сделать отдельный коммит:
```bash
git add .ai_state.md
git commit -m "state: update after [task]"
```

---

## 🟢 I2 — Создать `templates/translator_template.html`

**PRECONDITION:** S1 выполнен.

**STEPS:**

Создать директорию и шаблон:

```bash
mkdir -p templates
```

Создать `templates/translator_template.html` — минимальный HTML с переменными-заглушками:

```html
<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Логика комментирования {{TRANSLATOR_NAME}} · CommentaryStrategies</title>
<!-- STYLE: скопировать из css/commentary.css после выполнения C2 -->
<!-- ВРЕМЕННО: скопировать <style> из kalyanov_commentary_analysis.html -->
<style>
  /* {{TRANSLATOR_COLOR_VAR}}: #{{TRANSLATOR_HEX}} */
  /* Заменить все var(--k) на var(--{{TRANSLATOR_KEY}}) */
</style>
</head>
<body>

<!-- ШАПКА -->
<nav><!-- ссылка на index.html --></nav>
<header class="page-header">
  <div class="page-label">{{CORPUS_LABEL}}</div>
  <h1>Логика комментирования {{TRANSLATOR_NAME_GEN}}</h1>
  <div class="page-meta">{{CORPUS_DETAIL}} · {{TOTAL_NOTES}} примечаний</div>
</header>

<!-- СТАТИСТИКА (раздел 1) -->
<!-- {{РАЗДЕЛ_1_БАЗОВЫЕ_ПАРАМЕТРЫ}} -->

<!-- ПЛОТНОСТЬ (раздел 2) -->
<!-- {{РАЗДЕЛ_2_ПЛОТНОСТЬ}} -->

<!-- ДЛИНА (раздел 3) -->
<!-- {{РАЗДЕЛ_3_ДЛИНА}} -->

<!-- IAST (раздел 4) -->
<!-- {{РАЗДЕЛ_4_IAST}} -->

<!-- КАТЕГОРИИ (раздел 5) -->
<!-- {{РАЗДЕЛ_5_КАТЕГОРИИ}} -->

<!-- ФОРМУЛЫ (раздел 6) -->
<!-- {{РАЗДЕЛ_6_ФОРМУЛЫ}} -->

<!-- СНОСКА -->
<div class="footnote">
  CommentaryStrategies · <a href="index.html">← Все переводчики</a>
</div>

</body>
</html>
```

Создать `templates/NEW_TRANSLATOR_CHECKLIST.md`:

```markdown
# Чеклист добавления нового переводчика

1. [ ] Скопировать `templates/translator_template.html` → `{name}_commentary_analysis.html`
2. [ ] Заменить все `{{PLACEHOLDER}}` на реальные данные
3. [ ] Добавить CSS-переменную цвета в `:root` (новый `--{key}: #hex`)
4. [ ] Добавить запись в навигацию `index.html`
5. [ ] Добавить запись в таблицу переводчиков в `docs/GEMINI.md`
6. [ ] Добавить запись в `data/{translator}.json` (после выполнения C1)
7. [ ] Запустить `python scripts/validate.py`
8. [ ] Обновить `.ai_state.md`
```

**VERIFY:** `ls templates/` показывает 2 файла.

---

## 🔴 C2 — Вынести общие CSS в `css/commentary.css`

**PRECONDITION:** I2 выполнен (templates готов). Делать ПОСЛЕ подачи статьи.

**STEPS:**

```bash
mkdir -p css js
```

**Шаг 1:** Извлечь общие стили.

Открыть `kalyanov_commentary_analysis.html`. Скопировать содержимое `<style>...</style>` в `css/commentary.css`. Это базовый файл.

Затем просмотреть каждый из 7 HTML-файлов и добавить в `css/commentary.css` только те стили, которых ещё нет. Итоговый `css/commentary.css` должен содержать весь общий CSS, параметризованный через CSS-переменные:

```css
/* css/commentary.css — общие стили CommentaryStrategies */

/* Переменные переводчиков переопределяются в каждом HTML */
:root {
  --text: #1c1c1c;
  --text-secondary: #555;
  --bg: #ffffff;
  --bg-alt: #f5f5f5;
  --border: #ddd;

  /* Кальянов */
  --k: #2a5a8b;   --k-l: #e8f0f9;
  /* Васильков */
  --v: #3a6b35;   --v-l: #eaf2e8;
  /* Эрман */
  --e: #5a2d82;   --e-l: #f2ecf9;
  /* Гринцер */
  --g: #8b4513;   --g-l: #f9f0e8;
  /* Сыркин */
  --s: #7a3b00;   --s-l: #faf0e6;
  /* Леонов */
  --leonov: #7c4b2a;
}

/* ... весь общий CSS ... */
```

**Шаг 2:** В каждом HTML-файле заменить блок `<style>...</style>` на:

```html
<link rel="stylesheet" href="css/commentary.css">
```

(для файлов в корне — `href="css/commentary.css"`)

Делать по одному файлу, после каждого открывать в браузере и визуально проверять.

**Шаг 3:**

```bash
git add css/ *.html
git commit -m "refactor(C2): extract shared CSS to css/commentary.css"
```

**VERIFY:**
- Все 7 HTML открываются в браузере без визуальных отличий от оригинала
- `grep -l '<style>' *.html` возвращает пустой список
- `python scripts/validate.py` проходит

---

## 🔴 C1 — Создать `data/` с JSON и `data/schema.json`

**PRECONDITION:** C2, C3 выполнены. Делать при расширении корпуса (Phase 3).

**STEPS:**

```bash
mkdir -p data
```

**Шаг 1:** Создать `data/schema.json`:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "CommentaryStrategiesAnnotation",
  "description": "Схема разметки одного примечания по 4 осям",
  "type": "object",
  "required": ["comment_id", "translator", "axis_1_topic", "axis_2_kazansky"],
  "properties": {
    "comment_id":    { "type": "string", "description": "Уникальный ID: {source}/{translator}/comment_{shloka}" },
    "shloka_addr":   { "type": "string", "description": "Канонический адрес шлоки, напр. Rām. Sundara 1.1.a" },
    "translator":    { "type": "string", "enum": ["kalyanov","vasilkov","erman","grintser","syrkin","leonov"] },
    "editor":        { "type": "string", "description": "Редактор (для Леонова: kostina)" },
    "raw_text":      { "type": "string", "description": "Исходный текст примечания" },
    "char_count":    { "type": "integer" },
    "has_iast":      { "type": "boolean" },
    "axis_1_topic":  {
      "type": "array",
      "items": { "type": "string", "enum": [
        "sanskrit_term","myth","context","realia","geography","reference","textology","philosophy"
      ]}
    },
    "axis_2_kazansky": { "type": "string", "enum": ["A","B","V","G"] },
    "axis_3_lakshana": {
      "type": "array",
      "items": { "type": "string", "enum": ["L1","L2","L3","L4","L5"] }
    },
    "axis_4_paribok": { "type": "string", "enum": ["P","K","D"] },
    "cited_indian_commentators": { "type": "array", "items": { "type": "string" } },
    "cited_western_sources": { "type": "array", "items": { "type": "string" } }
  }
}
```

**Шаг 2:** Создать `data/README.md`:

```markdown
# data/

JSON-файлы с размеченными примечаниями (микроразметка по 4 осям).

## Схема
Все файлы валидируются против `schema.json`.

## Файлы
- `schema.json` — JSON Schema (draft-07)
- `kalyanov.json` — Кальянов, 7424 прим. (создать в Phase 2)
- `vasilkov.json` — Васильков (создать в Phase 2)
- `erman.json` — Эрман
- `grintser.json` — Гринцер
- `syrkin.json` — Сыркин
- `leonov.json` — Леонов

## Формат каждого файла
Массив объектов по схеме `schema.json`:
```json
[
  { "comment_id": "...", "translator": "kalyanov", ... },
  ...
]
```

## Валидация
```bash
python scripts/validate_schema.py data/kalyanov.json
```
```

**Шаг 3:** Создать `scripts/validate_schema.py`:

```python
#!/usr/bin/env python3
"""Validate a data JSON file against data/schema.json."""
import json, sys
from pathlib import Path

try:
    import jsonschema
except ImportError:
    print("Install jsonschema: pip install jsonschema")
    sys.exit(1)

ROOT = Path(__file__).parent.parent
SCHEMA = json.loads((ROOT / "data" / "schema.json").read_text())

def main():
    if len(sys.argv) < 2:
        print("Usage: validate_schema.py data/kalyanov.json")
        sys.exit(1)
    path = Path(sys.argv[1])
    data = json.loads(path.read_text())
    errors = []
    for i, item in enumerate(data):
        v = jsonschema.Draft7Validator(SCHEMA)
        for e in v.iter_errors(item):
            errors.append(f"  item[{i}]: {e.message}")
    if errors:
        print(f"❌ {len(errors)} schema error(s) in {path}:")
        print("\n".join(errors))
        sys.exit(1)
    print(f"✅ {len(data)} items valid in {path}")

if __name__ == "__main__":
    main()
```

```bash
git add data/ scripts/validate_schema.py
git commit -m "feat(C1): add data/ schema and validate_schema.py"
```

**VERIFY:**
- `python scripts/validate_schema.py data/schema.json` — корректно обрабатывает схему
- `ls data/` показывает schema.json + README.md

---

## 🟢 I1 — `visualizations.html` из JSON (после C1)

**PRECONDITION:** C1 выполнен, `data/*.json` заполнены.

**STEPS:**

Создать `scripts/generate_viz.py`:

```python
#!/usr/bin/env python3
"""
generate_viz.py — regenerates visualizations.html from data/*.json.
Run after updating any translator JSON file.
"""
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA_DIR = ROOT / "data"
TRANSLATORS = ["kalyanov", "vasilkov", "erman", "grintser", "syrkin", "leonov"]

def load_stats(name):
    path = DATA_DIR / f"{name}.json"
    if not path.exists():
        return None
    data = json.loads(path.read_text())
    total = len(data)
    iast_pct = round(sum(1 for d in data if d.get("has_iast")) / total * 100, 1) if total else 0
    avg_len = round(sum(d.get("char_count", 0) for d in data) / total) if total else 0
    return {"name": name, "total": total, "iast_pct": iast_pct, "avg_len": avg_len}

stats = [s for s in (load_stats(t) for t in TRANSLATORS) if s]
# Inject stats into visualizations.html template
# (str_replace the JS data block)
print("Stats computed:", stats)
print("TODO: inject into visualizations.html via str_replace")
```

> **Примечание для агента:** полную реализацию генератора писать только когда `data/*.json` содержат реальные данные. Сейчас — зафиксировать скрипт-заготовку.

```bash
git add scripts/generate_viz.py
git commit -m "feat(I1): add generate_viz.py skeleton"
```

---

## Порядок выполнения (сводка)

```
СЕЙЧАС (не требует подачи статьи):
  C3 → S1 → S2 → S3 → I3 → I2

ПОСЛЕ ПОДАЧИ СТАТЬИ:
  C2

ПРИ РАСШИРЕНИИ КОРПУСА (Phase 3 ROADMAP):
  C1 → I1
```

---

## Чеклист для `.ai_state.md`

Скопировать в `.ai_state.md` после начала работы:

```markdown
## 🏗️ Architecture Tasks Progress
- [ ] C3 — scripts/validate.py
- [ ] S1 — README.md переписан
- [ ] S2 — docs/GEMINI.md связан с README
- [ ] S3 — article_current.md, архив убран
- [ ] I3 — .ai_state.md обновлён (постоянная задача)
- [ ] I2 — templates/translator_template.html
- [ ] C2 — css/commentary.css (после статьи)
- [ ] C1 — data/schema.json (при расширении)
- [ ] I1 — generate_viz.py (после C1)
```
