# Руководство: как сейчас устроен CommentaryStrategies (том «Сундараканда» для ЛП)

_Created: 07-07-2026 · Last updated: 07-07-2026_

Это операторское руководство для трёх участников тома — переводчика (А. Леонов),
первого комментатора и литературного редактора (Е. Костина), второго комментатора и
оркестратора (М. Гасунс) — и для будущих агентных сессий. Научная сторона репозитория
(статьи о стратегиях комментирования, золотая выборка 300 примечаний) описана в
[README.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/README.md) и
[docs/ARCHITECTURE.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/ARCHITECTURE.md);
здесь — только производственный конвейер книги.

## 1. Что мы делаем

Готовится camera-ready том **«Рамаяна. Книга V. Сундараканда»** для серии
«Литературные памятники» (Наука); целевой срок ~07-08-2026. Четыре решения М.Г.
зафиксированы в [docs/LP_APPARATUS_DESIGN.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/LP_APPARATUS_DESIGN.md):
полный том · плотность аппарата по Леонову (~37%) · максимум контрастивного слоя
«в Тилаке X / в Широмани Y» · ACL/DH-методы для контроля качества.

## 2. Роли и кто что гейтит

| Участник | Роль | Что гейтит |
|---|---|---|
| А. Леонов | переводчик | финальность перевода (все 68 песней), версия подстрочника, итоговая сборка яруса-2 |
| Е. Костина | 1-й комментатор, лит. редактор | редполитика примечаний (§3 [COMMENTARY_ROADMAP](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/COMMENTARY_ROADMAP.md)), судьба её редакторских помет, итоговая сборка яруса-2 |
| М. Гасунс | 2-й комментатор, оркестратор | четыре браузерных листа (черновики яруса-2, рулинг R1), рулинги §8 (шаблон ЛП, бюджет страниц) |

Принцип двойных ворот: **машина предлагает и ранжирует — М.Г. гейтит черновики —
Леонов/Костина гейтят сборку**. Ни одно машинное примечание не попадает в печать,
минуя оба человеческих гейта; ничего не удаляется автоматически, каждое примечание
несёт `review_required: true` до финальной сборки.

## 3. Два яруса аппарата (модель II)

- **Ярус 1 — собственный аппарат Леонова/Костиной**: 1 058 примечаний (Леонов 616,
  Костина 442), оцифрованы из перевода в
  [data/leonov_own_notes.json](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/leonov_own_notes.json).
  Печатный минимум; машина его не трогает, только дедуплицируется об него.
- **Ярус 2 — дополнительный аппарат** (всё `review_required`), четыре слоя:
  1. **комментаторский диалог** (Phase-2): русские ноты по санскритским комментариям
     Тилаки/Бхушаны/Широмани/Таттвадипики (Gita Supersite, CC BY 4.0), контраст-первый
     формат; пилот 16 нот применён, партия-2 (38) и партия-3 (227) ждут гейта;
  2. **лексико-этимологический слой**: 604 глоссы (термины, этимологии, хапаксы) +
     7 запаркованных; отсужен целиком 07-07-2026;
  3. **межтекстовый слой** (cross_text): 170 параллелей (Ману, Махабхарата, Гита,
     Калидаса и др.);
  4. **сноски о расхождениях изданий**: 51 пассаж южной вульгаты, отсутствующий в
     критическом издании Бароды (+ Phase-1 базовые ноты, 95).

## 4. Конвейер (как примечание попадает в книгу)

```
санскр. комментарии + корпус → сегментация по стихам (extract_yellow_sargas.py)
  → черновики агентов (Sonnet 5, контракт §3.1, dedup об ярус-1)
  → LLM-судья (рубрика §3.4: достоверность-вето · нетривиальность · контрастивность/
    лексическая ценность · регистр · якорь; drafter ≠ judge)
  → браузерный лист → голос М.Г. → *_decisions.json
  → apply_phase2_decisions.py (графт в data/sundara_ch{N}_commentary_to_add.json + книгу)
  → пересборка: аппарат (build_sarga_apparatus.py) · печатный мастер
    (build_book_apparatus.py, MD+DOCX) · плотность (book_density_stats.py)
  → сборочный гейт Леонова/Костиной → печать
```

Канонический метод-мануал конвейера:
[docs/PHASE2_METHOD.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/PHASE2_METHOD.md).

## 5. Четыре браузерных листа (текущие гейты М.Г.)

Каждый лист — самодостаточный HTML: открыть двойным кликом, по каждой карточке
✅ принять / ✏️ править / ❌ отклонить, выбор хранится в браузере (localStorage),
кнопка «⬇ Скачать» отдаёт файл с **самоописывающим именем** — его не спутать в Downloads:

| Лист | Карточек | Скачивается как |
|---|---|---|
| [партия-2](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/analysis/phase2_batch2/commentarystrategies-sundarakanda-commentaries_batch2_review.html) | 38 | `commentarystrategies-sundarakanda-commentaries_batch2_decisions.json` |
| [партия-3](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/analysis/phase2_batch3/commentarystrategies-sundarakanda-commentaries_batch3_review.html) | 227 | `commentarystrategies-sundarakanda-commentaries_batch3_decisions.json` |
| [лексический слой](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/analysis/lexical_judge/commentarystrategies-sundarakanda-lexical_all68_review.html) | 604+7 | `commentarystrategies-sundarakanda-lexical_all68_decisions.json` |
| [сноски изданий](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/edition_footnotes/commentarystrategies-edition-footnotes_v1_review.html) | 51 | `commentarystrategies-edition-footnotes_v1_decisions.json` |

На карточках виден вердикт судьи (лексический лист отсортирован «проблемные выше»);
судья только ранжирует — решает человек.

## 6. Применение решений

```sh
python scripts/apply_phase2_decisions.py <путь к *_decisions.json>   # партия определяется автоматически
python scripts/apply_phase2_decisions.py <файл> --dry-run            # репетиция без записи
```

Судейские поля переживают графт; примечания с вердиктами `reject`/`park`/`flag_anchor`
требуют явного решения (таблица в выводе); принять непочиненный `flag_anchor`
(сейчас один: 5.21.19 → вероятно, стих 18) скрипт откажется без `--allow-flagged-anchor`.
После применения — пересборка тремя командами из §4.

## 7. Типовые сценарии (use cases)

1. **Леонов: посмотреть песнь N со всем аппаратом.** Открыть
   [data/apparatus/](https://github.com/gasyoun/CommentaryStrategies/tree/main/data/apparatus)`sarga_NN.html`
   — стихи (IAST + подстрочник), все пять слоёв примечаний с бейджами провенанса и
   статуса гейта.
2. **Костина: проверить формат примечаний.** Редполитика — §3
   [COMMENTARY_ROADMAP](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/COMMENTARY_ROADMAP.md);
   стилевой контракт машинных нот — §3.1
   [PHASE2_METHOD](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/PHASE2_METHOD.md).
3. **Гасунс: проголосовать лист.** Открыть лист из §5 → голосовать (можно частями,
   выбор сохраняется) → «⬇ Скачать» → запустить apply из §6 (или отдать файл агентной
   сессии — стартовая строка в
   [H276](https://github.com/gasyoun/Uprava/blob/main/handoffs/H276-Fable_CommentaryStrategies_sundara_gates_apply_final_assembly_07.07.26.md)).
4. **Посмотреть, как будет выглядеть книга.** Печатный мастер:
   [data/book/sundarakanda_print_master.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/book/sundarakanda_print_master.md)
   (+ DOCX рядом); сводка сборки —
   [data/book/BOOK_BUILD_REPORT.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/book/BOOK_BUILD_REPORT.md).
5. **Проверить плотность аппарата** (цель ~37% по Леонову): merged-потолок сейчас 46.0% —
   [data/analysis/book_density_stats.json](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/analysis/book_density_stats.json);
   запас на отсев при голосовании заложен.
6. **Агентная сессия: продолжить работу.** Прочитать
   [.ai_state.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/.ai_state.md) (живое
   состояние) и [PHASE2_METHOD](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/PHASE2_METHOD.md);
   после любой правки данных — `python scripts/validate.py`.

## 8. Что сейчас блокирует печать (07-07-2026)

1. Четыре листа §5 не проголосованы (М.Г.).
2. Сборочный гейт Леонова/Костиной не назначен (механизм + срок) — самое длинное звено.
3. Рулинги §8: шаблон/формат ЛП, судьба помет Костиной (~427), бюджет страниц.
4. Мелочь: недостающие стихи песней 2 (55/58) и 28 (19/20); якорь 5.21.19.

Персональные списки задач — в трёх issue: по одному для Гасунса, Костиной и Леонова
(см. [issues](https://github.com/gasyoun/CommentaryStrategies/issues)).

_Dr. Mārcis Gasūns_
