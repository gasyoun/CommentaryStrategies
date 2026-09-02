# C3 — пилот: 20 строф Sundara 1 (модель II, born-structured)

_Created: 02-09-2026 · Last updated: 02-09-2026_

> Шаг C3 дорожной карты ([docs/ROADMAP_2026H2.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/ROADMAP_2026H2.md), Workstream C).
> Расширяет [C0.2](https://github.com/gasyoun/CommentaryStrategies/blob/main/ramayana-leonov/C0_SPECIMENS_SUNDARA1.md) (10 строф, три слепых аппарата) до 20 строф
> в уже **решённой** модели II (двухъярусный гибрид, D2, М.Г. 2026-07-01) — и, впервые,
> собирает разметку сразу в JSON-схему ([data/commentary_schema.json](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/commentary_schema.json)),
> а не задним числом переносит из markdown.

## Что в файле

[data/sundara1_pilot_c3_20.json](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/sundara1_pilot_c3_20.json) — 20 записей (Sundara 1.1–1.20),
каждая:

- `sanskrit_iast` / `translation_ru` — стих и перевод М. Леонова (из параллельного корпуса samskrtam.ru);
- `tier1_print_gloss` — ярус 1 (печать): для строф 1,3,6,7,8,10 — дословно унаследовано из
  C0.2 (аппарат II уже прошёл калибровку); для строф 16,18,19,20 — новый краткий глосс,
  сжатый из того же яруса 2, без нового филологического утверждения; для 2,4,5,9,11–15,17
  ярус 1 оставлен пустым — как и в C0.2, часть строф печатного глосса не получает;
- `tier2_digital_note` — ярус 2 (цифровой): существующий, выверенный аппарат Леонова/Костиной
  (`data/leonov_own_notes.json`) — для 14 из 20 строф (нет заметки у 4, 11, 13, 14, 15, 17 —
  сами эти строфы Леонов/Костина пока не прокомментировали, это не пробел разметки);
- `govindaraja_bhusana_raw` / `tilaka_raw` / `siromani_raw` / `tattvadipika_raw` —
  **параллельный слой**: подлинный санскритский текст четырёх традиционных комментариев
  (Говиндараджи-«Бхушана», «Тилака», «Широмани», «Таттвадипика») к тем же 20 строфам,
  сегментированный уже существующим калиброванным парсером
  [`scripts/extract_yellow_sargas.py`](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/extract_yellow_sargas.py) (H268 WS-C2:
  pratīka + якорь по содержанию, точность 0.887/0.931 верифицированная — см. `_meta` файла).
  Перевод этого слоя на русский НЕ сделан здесь: это и есть задача tertium comparationis
  для рецензентов, не механический шаг.
- `axis_2_kazansky` — первый проход по 4-осной схеме (только там, где есть ярус-2 заметка);
  помечен `needs_review: true` — не ратифицирован.

## Что НЕ сделано (осознанно, а не по пропуску)

- **Перевод/интерпретация традиционных комментариев на русский** — это и есть содержательная
  работа рецензентов (Говиндараджа/Тилака как *независимая* проверка апарата Леонова, а не
  то, что Леонов уже процитировал из них).
- **Ратификация `axis_2_kazansky`** и любых других осей — первый проход, гейт на review.

## Гейт

**`{gate: human:leonov,kostina}`** — roadmap-пункт «Ревью Леонова/Костиной → итерация guidelines»
(строка 127) требует их прочтения и решения; ни один тир этого не заменяет.

_Dr. Mārcis Gasūns_
