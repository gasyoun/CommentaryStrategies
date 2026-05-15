# sources/ — Input format for annotation pipeline

Each translator gets one file: `{translator}_notes.json`

## Format

JSON array of note objects. The only required field is `raw_text`.

```json
[
  {
    "raw_text": "Дхарма (dharma) — закон, долг, добродетель. Одно из четырех стремлений человека."
  },
  {
    "raw_text": "Курукшетра — священная равнина в Северной Индии, место битвы Пандавов и Кауравов.",
    "shloka_addr": "BhG 1.1",
    "editor": ""
  }
]
```

### Optional fields (carried through to output)

| Field | Description |
|---|---|
| `shloka_addr` | Canonical passage address, e.g. `"BhG 1.1"`, `"MBh 1.1.1"` |
| `editor` | For Leonov corpus: `"kostina"` |
| `comment_id` | If pre-assigned; otherwise generated as `{translator}/comment_{NNNN}` |

## Year 1 target files

| File | Translator | Notes est. | Status |
|---|---|---|---|
| `sementsov_notes.json` | Семенцов 1985/1999 | ~200 | pending |
| `burba_notes.json` | Бурба 2009 | ~350 | pending |
| `petrov_notes.json` | Петров 1788 | ~50 | pending |
| `smirnov_notes.json` | Смирнов 1956 | ~400 | pending |
| `blinderman_notes.json` | Блиндерман | ~200 | pending |

## Generating sources files

From a plain-text OCR with numbered footnotes, you can extract notes with:

```python
import re, json

text = open("translation.txt", encoding="utf-8").read()

# Pattern: footnote number followed by text, ending at next number or end-of-file
# Adjust regex to match your footnote format
notes = re.findall(r'^\d+\.\s+(.+?)(?=^\d+\.|\Z)', text, re.MULTILINE | re.DOTALL)
output = [{"raw_text": n.strip()} for n in notes if n.strip()]
json.dump(output, open("translator_notes.json", "w", encoding="utf-8"),
          ensure_ascii=False, indent=2)
```

Common footnote formats to handle:
- `1. Note text here` (numbered with period)
- `[1] Note text here` (bracketed)
- `* Note text here` (asterisk, for short texts like Petrov 1788)
- Superscript in Word/PDF exports — strip the number, keep the text
