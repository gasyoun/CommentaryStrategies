# Nīlakaṇṭha-vulgate Mahābhārata — полный census скрейпа

_Created: 11-07-2026 · Last updated: 11-07-2026_

Полный скрейп корпуса Нилакантха-вульгаты (мула + ṭīkā *Bhāratabhāvadīpa*) с
[sanatana.in/mahabharata](https://sanatana.in/mahabharata/) (проект Sanatana Sampatti /
[srirangadigital.com](http://www.srirangadigital.com/)), выполнен
[`nilakantha_parser.py scrape`](https://github.com/gasyoun/CommentaryStrategies/blob/main/mahabharata-nilakantha/nilakantha_parser.py)
11-07-2026, Opus 4.8 (`claude-opus-4-8`). Эндпоинт `GET /mahabharata/listing/getParvaByPage/{parva}?page={N}`;
адресация P/U/A/S берётся из `id` каждого `div.shloka`. Текст (`nilakantha_vulgate_full.jsonl`,
58.9 MB) и кэш страниц — **gitignored** (права на сторонний текст; публикация гейтится
[`/publish-safety-check`](https://github.com/gasyoun/claude-config/blob/main/commands/publish-safety-check.md)).
Это только **numbers-only** census.

## Census по парванам

| # | Parva | Шлоки | С ṭīkā | % ṭīkā |
|---|---|---:|---:|---:|
| 1 | adiparva | 8 623 | 3 177 | 36.8 |
| 2 | sabhaparva | 2 713 | 1 107 | 40.8 |
| 3 | vanaparva | 11 859 | 3 592 | 30.3 |
| 4 | virataparva | 2 270 | 857 | 37.8 |
| 5 | udyogaparva | 6 613 | 2 391 | 36.2 |
| 6 | bhishmaparva | 5 868 | 1 393 | 23.7 |
| 7 | dronaparva | 9 641 | 1 249 | 13.0 |
| 8 | karnaparva | 5 012 | 736 | 14.7 |
| 9 | shalyaparva | 3 635 | 254 | 7.0 |
| 10 | sauptikaparva | 803 | 132 | 16.4 |
| 11 | striparva | 825 | 162 | 19.6 |
| 12 | shantiparva | 13 764 | 6 600 | 48.0 |
| 13 | anushasanaparva | 7 699 | 2 080 | 27.0 |
| 14 | ashwamedhikaparva | 2 845 | 732 | 25.7 |
| 15 | ashramavasikaparva | 1 088 | 149 | 13.7 |
| 16 | mausalaparva | 287 | 46 | 16.0 |
| 17 | mahaprasthanikaparva | 110 | 31 | 28.2 |
| 18 | swargarohanaparva | 316 | 6 | 1.9 |
| — | **ИТОГО** | **83 971** | **24 694** | **29.4** |

- Уникальных `id` = 83 971 (дедуп по P/U/A/S чистый, наложений страниц нет).
- Уникальных адхьяй (parva+adhyaya) = 2 110.
- Пустая мула = 231 запись (0.3 % — служебные div без стиха; отфильтровать при использовании).
- **Harivaṃśa НЕ включена** (придаток; доступна флагом `--harivamsha`).

## Что это разблокирует

Программа [проверки цитат PWG/MW](https://github.com/sanskrit-lexicon/csl-atlas/blob/main/docs/CITATION_VERIFICATION_ROADMAP_2026_2027.md)
считала MBH fitted-index census **BLOCKED**: «нет свободной bulk Nīlakaṇṭha-вульгаты». Этот
скрейп **опровергает** посылку — вульгата теперь есть локально, в правильной рецензии, с
машиночитаемой построфной адресацией по всем 18 парванам, включая Дрону (кн. 7 — пример
`MBH. 7,9283` из дорожной карты). Остаётся собственно fitted-index работа: сопоставить
непрерывную попарванную нумерацию PWG (`MBH. 7,<стих>`) с построфной P/U/A/S этого текста.

_Dr. Mārcis Gasūns_
