# Приложение IV. Формальная схема (JSON Schema) для разметки комментария

Для обеспечения воспроизводимости исследования и возможности автоматической обработки корпуса была разработана JSON-схема разметки, фиксирующая аналитические параметры каждого примечания по четырем осям.

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "CommentaryStrategiesAnnotation",
  "description": "Схема разметки одного примечания по 4 осям",
  "type": "object",
  "required": ["comment_id", "translator", "axis_1_topic", "axis_2_kazansky"],
  "properties": {
    "comment_id":    { "type": "string", "description": "ID: {source}/{translator}/comment_{shloka}" },
    "shloka_addr":   { "type": "string", "description": "Адрес шлоки, напр. Rām. Sundara 1.1.a" },
    "translator":    { "type": "string", "enum": ["kalyanov","vasilkov","erman","grintser","syrkin","leonov"] },
    "raw_text":      { "type": "string", "description": "Исходный текст примечания" },
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
    "axis_4_paribok": { "type": "string", "enum": ["P","C","K"] },
    "cited_indian_commentators": { "type": "array", "items": { "type": "string" } }
  }
}
```

## Соответствие осей
1.  **axis_1_topic**: Тематическая рубрика (8 категорий).
2.  **axis_2_kazansky**: Тип по Казанскому (A — филол., B — реальн., V — истор., G — культур.).
3.  **axis_3_lakshana**: Функции *vyākhyāna* (L1 — padaccheda, L2 — padārthokti, L3 — vigraha, L4 — vākyayojanā, L5 — ākṣepasamādhāna).
4.  **axis_4_paribok**: Категориальный статус (P — понятие, C — концепт, K — кодификатор).
