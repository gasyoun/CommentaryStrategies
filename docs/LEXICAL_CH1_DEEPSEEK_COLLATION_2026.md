# DeepSeek-сопоставление лексических примечаний песни 1 (H2833)

_Created: 16-08-2026 · Last updated: 16-08-2026_

Независимое второе прочтение всех лексических карточек песни 1 Сундараканды
после гринцеровской правки — исполнение требования пункта 19 бюллетеня
([votes/sarga.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/votes/sarga.md)):
«надо с deepseek досконально сопоставить все примечания».

- **Рецензент:** DeepSeek Flash (`deepseek-v4-flash` @ `https://api.deepseek.com`),
  thinking выключен, temperature 0. Скрипт:
  [scripts/deepseek_collate_lexical_ch1.py](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/deepseek_collate_lexical_ch1.py)
  (возобновляемый; ключ — repo `.env` / `../ORS-FAQ/.env`).
- **Материал:** все 58 карточек
  [data/lexical/ch1.json](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/lexical/ch1.json)
  после правки по
  [docs/LEXICAL_NOTE_STYLE_GRINTSER_2026.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/LEXICAL_NOTE_STYLE_GRINTSER_2026.md).
- **Сырые вердикты:**
  [data/lexical/style_pass_h2833/deepseek_collation.json](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/lexical/style_pass_h2833/deepseek_collation.json).
- **Правивший редактор:** Fable 5 (`claude-fable-5`), 16-08-2026.

## Итог

| Вердикт | Карточек |
|---|---|
| agree — примечание верно | 55 |
| minor — мелкие уточнения | 3 |
| major — фактическая ошибка | 0 |

Расхождения — список к разбору, не приговор (так предписывает H2833). Все три
разобраны ниже; все три признаны справедливыми и внесены в источники тем же
проходом.

## Разбор расхождений

1. **V.1.33 lāṅgūla** — «не исключительно обезьяний хвост; в Сундараканде
   бывает и о хвостах других обезьян». Справедливо: категоричное
   «исключительно» снято, формулировка смягчена до «в эпосе чаще всего —
   обезьяньего… в Сундараканде постоянно о хвосте Ханумана».
2. **V.1.53 khādyota** — «этимология дана упрощённо: не причастие "светящий
   в небе", а сложение kha + dyota с удлинением гласного на стыке».
   Справедливо: глосса заменена на «небесное сияние» с описанием сложения.
3. **V.1.62 parivesa** — «значение "ореол" в MW стоит под pariveṣa, не под
   parivesa/pariṣeṣa; словарные отсылки карточки неверны». Справедливо: лемма
   исправлена на pariveṣa с оговоркой о написании в тексте; ошибочные
   отсылки (в т.ч. на pariṣeṣa «remainder») сняты. Карточка живёт только в
   агрегате книги (в ch1.json она отклонена судьёй).

## Попутная находка: фиктивные отсылки к Гринцеру

Проверка отсылок «см. примеч. к <адрес> (Гринцер; …уточнить по примеч.)» по
дословному корпусу примечаний Гринцера
([SamudraManthanam/web/corpus_builder/jsonl](https://github.com/gasyoun/SamudraManthanam/tree/main/web/corpus_builder/jsonl))
дала: из восьми проверенных адресов **пять фиктивны или бьют мимо предмета**
(I.1.16, I.1.1, II.114.3 — примечания не существует; I.1.8, I.1.25, I.1.28 —
примечание о другом). Подтвердились и оставлены только III.48.10 (Амаравати),
II.40.24 (Меру), I.45.18 (Мандара). Все фиктивные отсылки сняты из
[data/sundara_commentary_to_add.json](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/sundara_commentary_to_add.json);
до/после — [data/analysis/grintser_pass_h2833_diff.html](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/analysis/grintser_pass_h2833_diff.html).
Урок для генераторов: отсылка к печатному примечанию вставляется только после
проверки по корпусу.

## Ограничение

Сверка с комментарием Голдменов не выполнена: она ждёт распознанного PDF —
[H2832 (Opus 5) — Goldman PDF OCR bake-off](https://github.com/gasyoun/Uprava/blob/main/handoffs/H2832-Opus_CommentaryStrategies_goldman-pdf-ocr-bakeoff_15.08.26.md)
на момент прохода не выполнен. H2833 прямо разрешает в этом случае
ограничиться конвенциями и сказать об этом явно.

_Dr. Mārcis Gasūns_
