# H3492 — гринцеровский проход по лексическим примечаниям, песни 2–5

_Created: 25-08-2026 · Last updated: 25-08-2026_

Исполнитель: Fable 5 (`claude-fable-5`), 25-08-2026. Handoff:
[H3492](https://github.com/gasyoun/Uprava/blob/main/handoffs/H3492-Fable_CommentaryStrategies_sundara-lexical-grintser-pass-sargas-2-5_25.08.26.md).
Правила: [docs/LEXICAL_NOTE_STYLE_GRINTSER_2026.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/LEXICAL_NOTE_STYLE_GRINTSER_2026.md)
(H2833, 16-08-2026; песнь 1 уже приведена тем проходом).
Аудитор: [scripts/audit_lexical_grintser_conventions.py](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/audit_lexical_grintser_conventions.py).

## Что сделано

1. Обобщён применитель H2833 (был жёстко привязан к `ch1`):
   [scripts/apply_grintser_pass.py](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/apply_grintser_pass.py)
   `--chapter N --handoff h3492` — читает `chN_patch.json`, переписывает только
   `note_ru`, пишет до/после в `chN_audit.json`, ставит `style_pass: grintser-H3492`.
   Карточки с вердиктом `reject` / `park` не трогает; мультимножество
   `(shloka, lemma_iast)` проверяется до и после записи (assert).
2. Написаны 37 новых текстов примечаний — по одному на каждую карточку с
   вердиктом `keep` / `edit` / без вердикта в `ch2.json` … `ch5.json`:
   [ch2_patch.json](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/lexical/style_pass_h3492/ch2_patch.json) (14) ·
   [ch3_patch.json](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/lexical/style_pass_h3492/ch3_patch.json) (10) ·
   [ch4_patch.json](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/lexical/style_pass_h3492/ch4_patch.json) (7) ·
   [ch5_patch.json](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/lexical/style_pass_h3492/ch5_patch.json) (6).
   До/после каждой карточки: `ch{2,3,4,5}_audit.json` в этой же папке.
3. Правки только в источниках `data/lexical/ch2.json` … `ch5.json`;
   `data/apparatus/*` (производное), `*.rejected.json`, `*.qa_removed.json`
   не тронуты. Поля `lemma_iast` / `shloka` не менялись ни в одной карточке.

Стихи сверены по [SamudraManthanam/web/corpus_builder/jsonl/05_ramayana-sundarakanda.jsonl](https://github.com/gasyoun/SamudraManthanam/blob/main/web/corpus_builder/jsonl/05_ramayana-sundarakanda.jsonl);
отсылки к словарю Гринцера (Амаравати, Бхогавати, Вишвакарман, Кубера) — по
[slovar-grintsera-iz-ramayany-1-2.jsonl](https://github.com/gasyoun/SamudraManthanam/blob/main/web/corpus_builder/jsonl/slovar-grintsera-iz-ramayany-1-2.jsonl).
Внутренние отсылки «см. примеч. к V. 1. 36 / 1. 156 / 1. 213 / 2. 24 / 5. 8 / 5. 9»
проверены на существование целевой карточки.

## Аудит (`python scripts/audit_lexical_grintser_conventions.py --chapter N`)

| песнь | карточек | clean до | clean после | не clean после | причина |
|---|---|---|---|---|---|
| 1 | 58 | 51 | **51** | 7 | не трогалась (регрессионный контроль H2833) |
| 2 | 16 | 0 | **14** | 2 | `V.2.3 yojana`, `V.2.21 vaprā` — вердикт `reject` |
| 3 | 13 | 0 | **10** | 3 | `V.3.6 śātakumbha`, `V.3.16 vivasvant` — `reject`; `V.3.7 kiṅkiṇī` — `park` |
| 4 | 8 | 0 | **7** | 1 | `V.4.15 gulma` — `reject` |
| 5 | 7 | 0 | **6** | 1 | `V.5.9 tantrī` — `reject` |

Итог: **37 / 37** карточек, идущих в печать, чисты по всем одиннадцати
проверкам аудитора; все 7 остатков — карточки `reject` / `park`, которые по
правилу H2833 не редактируются (в печать не идут). Один раунд аудита из трёх
разрешённых.

Расхождение с текстом handoff-а: там песни 2–5 показаны как 9 / 4 / 4 / 4
карточки и песнь 1 как 59 — реальные числа аудитора на `origin/main` до
прохода: 16 / 13 / 8 / 7 и 58 (аудитор считает и `keep`, и `reject`/`park`;
`sundara_chN_commentary_to_add.json` лексических записей для песней 1–5 не
содержит). Регрессионная строка песни 1 — **58 карточек / 51 clean, файл не
менялся** (`git diff` пуст).

Дословный вывод аудитора после прохода:

```
ch1: Cards scanned: 58  clean: 51
ch2: Cards scanned: 16  clean: 14   (V.2.3 yojana [reject], V.2.21 vaprā [reject])
ch3: Cards scanned: 13  clean: 10   (V.3.6 śātakumbha [reject], V.3.7 kiṅkiṇī [park], V.3.16 vivasvant [reject])
ch4: Cards scanned: 8   clean: 7    (V.4.15 gulma [reject])
ch5: Cards scanned: 7   clean: 6    (V.5.9 tantrī [reject])
```

## Типичные правки (образцы до → после)

| карточка | до (дефекты аудитора) | после |
|---|---|---|
| V.2.5 `mahodadhi` | lemma×4, MW inline, «mahā + udadhi», «букв.» без двоеточия | «Океан (mahodadhi) — букв.: «великое вместилище вод», от udadhi «вместилище вод» (uda — «вода», корень dhā- «держать») с mahā- «великий». Одно из ряда эпических имён океана: samudra …» |
| V.2.24 `bhogavatī` | lemma×3, MW inline, «bhoga … + vatī «имеющая»» | «Бхогавати (bhogavatī) — букв.: «изобилующая извивами» или «изобилующая наслаждениями»: bhoga означает и «кольцо змеиного тела», и «наслаждение». … См. словарь Гринцера к кн. I–II (s.v. Бхогавати)» |
| V.3.1 `sattva` | lemma×6, MW inline, « = », «В подстрочнике …» | «Мощь (sattva) — букв.: «бытие, сущность», от sant «сущий»; далее — «внутренняя сила, стойкость духа». Здесь не гуна саттва … ср. триаду … в примеч. к V. 1. 36» |
| V.4.27 `vimāna` (вердикт `edit`) | lemma×5, MW inline, «vi- + māna», смешанный деванагари в лемме | «Вимана (vimāna) — букв.: «отмеренное [пространство]», от корня mā- «мерить» с vi-; небесная колесница богов … вимана Пушпака, отнятая у Куберы (см. примеч. к V. 2. 24)» |
| V.5.8 `pradoṣa` | lemma×7, MW inline | «Вечер (pradoṣa) — букв.: «начало ночи» … Стих построен на созвучии: три «изъяна» (doṣa) — тьма, ракшасы, любовные ссоры — и сам «вечер», в имени которого звучит то же doṣa» |

Систематически снято во всех 37 карточках: повтор цитатной формы (в том числе
в цитируемом стихе — стих теперь цитируется по-русски или фрагментом без
леммы), инлайн-словари (MW/Apte — остались только в поле `source`), суммы
морфем через « + », « = » как фигура, помета части речи в зачине
(`(savya, adj.)`), «В подстрочнике …», английские цитаты дефиниций.

## Замечания к содержанию, не решённые этим проходом

1. `V.3.5` `lemma_iast` = `bhujagācārita`, в стихе `bhujagācaritām`; `V.3.12`
   `lemma_iast` = `vasvokaṣārā`, в стихе `vasvokasārā`. Поля леммы не тронуты
   (условие handoff-а); в тексте примечания цитатная форма дана по стиху.
   Исправление лемм — отдельная правка данных, не стиля.
2. Сверка с комментарием Голдменов по-прежнему ждёт
   [H2832 (Opus 5) — Goldman PDF OCR bake-off](https://github.com/gasyoun/Uprava/blob/main/handoffs/H2832-Opus_CommentaryStrategies_goldman-pdf-ocr-bakeoff_15.08.26.md)
   — как и для песни 1.
3. Два `@DECIDE` песни 1 (nāga «слон/наг»; форма ссылки на Голдменов) не
   тронуты — они не блокируют песни 2–5.
4. `data/apparatus/` для песней 2–5 подхватит новые тексты при следующей
   пересборке (`scripts/build_sarga_apparatus.py`); в этом PR производное не
   пересобиралось.

## Как воспроизвести

```
python scripts/apply_grintser_pass.py --chapter 2 --handoff h3492   # …3, 4, 5; идемпотентно
python scripts/audit_lexical_grintser_conventions.py --chapter 2 --verbose
python scripts/validate.py && python scripts/translit_hygiene.py --check
```

_Dr. Mārcis Gasūns_
