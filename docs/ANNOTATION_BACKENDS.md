# Аннотационный пайплайн — бэкенды LLM

`scripts/annotate_batch.py` классифицирует примечания по 4-осной сетке через
*выбираемый* бэкенд. Антропик больше не обязателен: бэкенд по умолчанию —
**`openai`**, который работает с **любым OpenAI-совместимым** эндпойнтом
(`/v1/chat/completions`). Это покрывает OpenAI, OpenRouter, Google Gemini,
YandexGPT и локальные серверы — без правки кода, только через переменные окружения.

Провайдер-специфична ровно одна функция (`OpenAIBackend.complete`); схема, валидация
(`normalise`), возобновляемость и инкрементальное сохранение — общие для всех бэкендов.

---

## Переменные окружения (бэкенд `openai`)

| Переменная | Назначение | Обязательна |
|---|---|---|
| `LLM_API_KEY` | Ключ провайдера (запасной вариант — `OPENAI_API_KEY`) | да |
| `LLM_BASE_URL` | Эндпойнт; не задавать для api.openai.com, задать для остальных | для не-OpenAI |
| `LLM_MODEL` | Идентификатор модели по умолчанию (перекрывается `--model`) | желательно |
| `LLM_BACKEND` | `openai` (по умолчанию) или `anthropic` | нет |

Приоритет модели: `--model` > `$LLM_MODEL` > дефолт бэкенда (`openai`: `gpt-4o-mini`).

---

## Рецепты по провайдерам

Команды для Windows PowerShell (`$env:VAR = "..."`). В bash — `export VAR=...`.

### OpenAI

```powershell
$env:LLM_API_KEY = "sk-..."
$env:LLM_MODEL   = "gpt-4o-mini"        # или gpt-4o для качества
python scripts/annotate_batch.py kalyanov --limit 5
```

### OpenRouter (один ключ → много моделей)

```powershell
$env:LLM_API_KEY  = "sk-or-..."
$env:LLM_BASE_URL = "https://openrouter.ai/api/v1"
$env:LLM_MODEL    = "google/gemini-2.0-flash-001"   # или anthropic/..., openai/..., meta-llama/...
python scripts/annotate_batch.py kalyanov --limit 5
```

### Google Gemini (OpenAI-совместимый режим)

```powershell
$env:LLM_API_KEY  = "AI..."
$env:LLM_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
$env:LLM_MODEL    = "gemini-2.0-flash"
# Бесплатный тариф — низкий RPM: поднимите паузу между вызовами
python scripts/annotate_batch.py kalyanov --limit 5 --sleep 4
```

### YandexGPT (OpenAI-совместимый режим)

```powershell
$env:LLM_API_KEY  = "<API-ключ сервисного аккаунта>"
$env:LLM_BASE_URL = "https://llm.api.cloud.yandex.net/v1"
$env:LLM_MODEL    = "gpt://<folder-id>/yandexgpt/latest"
python scripts/annotate_batch.py kalyanov --limit 5
```

### Локальная модель (Ollama / vLLM / LM Studio)

```powershell
$env:LLM_API_KEY  = "ollama"            # любая непустая строка
$env:LLM_BASE_URL = "http://localhost:11434/v1"
$env:LLM_MODEL    = "qwen2.5:14b-instruct"
python scripts/annotate_batch.py kalyanov --limit 5
```
> Качество на тонкой 4-осной задаче (рус./санскрит) у малых локальных моделей может
> не дотянуть до порога ≥85 % — измеряйте через `eval_pipeline.py` (см. ниже).

### Anthropic (если ключ всё-таки есть)

```powershell
$env:ANTHROPIC_API_KEY = "sk-ant-..."
python scripts/annotate_batch.py kalyanov --backend anthropic
```

### GigaChat (Sber) — нужен отдельный шим

GigaChat предоставляет OpenAI-совместимый эндпойнт, но авторизуется **не статичным
ключом**, а OAuth-токеном (POST `Authorization key` → access token, TTL ~30 мин,
российский корневой сертификат). Прямой `LLM_API_KEY` не подойдет. Если выбираете
GigaChat — нужен небольшой обмен токена перед запуском (добавляется по запросу).

---

## Полный прогон и проверка точности

```powershell
# 1. Аннотировать 50 примечаний (золотая выборка)
python scripts/annotate_batch.py kalyanov --limit 50

# 2. Сравнить с человеческой разметкой data/kalyanov_markup_50.json
python scripts/eval_pipeline.py kalyanov --verbose
```

`eval_pipeline.py` печатает точность по `axis_2_kazansky` и `axis_4_paribok` против
ручной золотой выборки (n=50, сопоставление по позиции). **Порог качества данных
для Article 1 — ≥85 % по обеим осям.** Если ниже — поднимайте модель (например,
`gpt-4o`, `gemini-2.5-pro`) или возвращайтесь к ручной разметке.

Выбор провайдера/модели — не только цена, но и валидность H1–H4: модель, не
дающая ≥85 %, не годится для количественных утверждений статьи. Сначала измерьте
на одном переводчике (kalyanov), затем масштабируйте.

---

## Офлайн-проверка (без ключа)

```powershell
python scripts/annotate_batch.py kalyanov --dry-run
```
Загружает источник и печатает, что было бы сделано, не обращаясь к API. Удобно
проверить, что входные файлы и окружение на месте, до траты токенов.
