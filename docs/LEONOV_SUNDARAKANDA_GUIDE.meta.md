# Метадок: LEONOV_SUNDARAKANDA_GUIDE.md

_Created: 10-07-2026 · Last updated: 12-07-2026 (в интро добавлен указатель на отдельную линию — среду автосносок книг 5–7)_

Метадок для [docs/LEONOV_SUNDARAKANDA_GUIDE.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/LEONOV_SUNDARAKANDA_GUIDE.md).

## Назначение и аудитория

Единственный документ проекта, написанный целиком для М. Леонова —
переводчика Сундараканды, человека без технической подготовки (браузер и
почта, без git/терминала). Закрывает четыре зафиксированных затыка: общая
картина проекта, конкретные шаги руками, механика листов голосования /
`decisions.json`, GitHub с нуля. Дополняет, а не заменяет
[docs/MANUAL.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/MANUAL.md)
(регламент для всех троих участников) и
[issue №58](https://github.com/gasyoun/CommentaryStrategies/issues/58)
(его чек-лист): MANUAL говорит «что положено», это руководство — «как это
сделать, если ты не программист».

## Происхождение

Написано 10-07-2026, Fable 5 (`claude-fable-5`), handoff
[H497](https://github.com/gasyoun/Uprava/blob/main/handoffs/archive/H497-Fable_CommentaryStrategies_leonov_sundarakanda_guide_10.07.26.md),
по запросу МГ («Леонов не понимает, что пошагово делать»). Фактура — из
[docs/MANUAL.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/MANUAL.md),
[docs/COMMENTARY_ROADMAP.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/COMMENTARY_ROADMAP.md),
[data/book/BOOK_BUILD_REPORT.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/book/BOOK_BUILD_REPORT.md)
и [issue №58](https://github.com/gasyoun/CommentaryStrategies/issues/58).

## Бэклог улучшений (ранжирован)

1. **Скриншоты** — раздел 5.1 (кнопка «Download raw file») и 5.2 (карточки
   голосования) заметно выиграют от 3–4 картинок; текстовое описание —
   временная замена. Статус: открыто.
2. **Актуализация после решения по сборочному гейту** — когда Леонов
   выберет формат (экран vs распечатка), раздел 4.3 переписать из
   «договоритесь» в конкретную инструкцию выбранного формата. Статус:
   заблокировано ответом Леонова.
3. ~~**Проверка читателем** — попросить Костину прочитать руководство до
   отправки Леонову.~~ Отменено МГ 10-07-2026: вместо вычитки решено
   написать Костиной собственное руководство-близнец —
   [docs/KOSTINA_SUNDARAKANDA_GUIDE.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/KOSTINA_SUNDARAKANDA_GUIDE.md)
   (H517); руководство Леонову уже отправлено (комментарий в
   [issue №58](https://github.com/gasyoun/CommentaryStrategies/issues/58)).
   Общие разделы двух руководств (1, 5, 6, 7, 8) с этого момента
   редактируются парно, одним коммитом.
4. **Синхронизация чисел** — количества примечаний яруса-2 (~800–900)
   зафиксированы до голосования МГ по четырем листам; после применения
   `decisions.json` обновить. Статус: заблокировано голосованием.

## Известные ограничения

- Числа (1058 примечаний, ~600 глосс, ~170 перекличек, ~50 помет) даны
  округленно и на дату создания — точные значения живут в
  [.ai_state.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/.ai_state.md)
  и отчетах сборки.
- Раздел 5.2 описывает механику листов голосования «на вырост»: первый
  шлагбаум проходит МГ, Леонову листы понадобятся только если сборочный
  гейт решат вести в том же инструменте.

## Intended use / known misuse

Единственный документ проекта, написанный целиком для М. Леонова —
человека без технической подготовки. Использовать по назначению: как
самостоятельную пошаговую инструкцию (общая картина, конкретные шаги
руками, механика листов/`decisions.json`, GitHub с нуля), не требуя от него
параллельного чтения [docs/MANUAL.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/MANUAL.md).
Известное неправильное использование: (а) отправлять Леонову вместо этого
руководства сам MANUAL или его выдержки — регистр MANUAL рассчитан на
техническую аудиторию и участников книги в целом, а не на «браузер и
почта без git/терминала»; (б) редактировать общие с руководством Костиной
разделы (1, 5, 6, 7, 8) без зеркальной правки в
[docs/KOSTINA_SUNDARAKANDA_GUIDE.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/KOSTINA_SUNDARAKANDA_GUIDE.md)
тем же коммитом — стоячее правило с 10-07-2026 (бэклог №3, вычитка
Костиной отменена именно в пользу парного редактирования); (в) читать
раздел 5.2 (механика листов голосования) как актуальную инструкцию для
Леонова уже сейчас — он написан «на вырост»: первый шлагбаум (гейт R1)
проходит МГ, Леонову листы понадобятся только если сборочный гейт решат
вести в том же инструменте (см. «Известные ограничения»).

## Maintenance & sunset plan

Владелец — МГ / агентная сессия по его указанию; общие разделы (1, 5, 6, 7,
8) правятся ПАРНО с [docs/KOSTINA_SUNDARAKANDA_GUIDE.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/KOSTINA_SUNDARAKANDA_GUIDE.md)
одним коммитом — главный риск устаревания при нарушении. Раздел 4.3
(формат сборочного гейта) переписывается из «договоритесь» в конкретную
инструкцию, как только Леонов выберет формат (экран vs распечатка) —
бэклог №2. После сдачи тома (~07-08-2026) и закрытия его четырех задач
руководство теряет операционную функцию и становится историческим —
отдельного плана архивации пока не заведено, по аналогии с планом MANUAL
§8 (см. метадок MANUAL.md, бэклог №4).

## Deprecation status

`active`

## Связанные документы

- [docs/KOSTINA_SUNDARAKANDA_GUIDE.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/KOSTINA_SUNDARAKANDA_GUIDE.md) — руководство-близнец для Е. Костиной (общие разделы правятся парно)
- [docs/MANUAL.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/MANUAL.md) — регламент книги для всех участников
- [docs/COMMENTARY_ROADMAP.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/COMMENTARY_ROADMAP.md) — редполитика §3 (на ратификацию Леоновым/Костиной)
- [ramayana-leonov/C0_COVER_LETTER.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/ramayana-leonov/C0_COVER_LETTER.md) — образец письма Леонову (эксперимент C0)
- [issue №58](https://github.com/gasyoun/CommentaryStrategies/issues/58) — личный чек-лист Леонова
- [RussianRamayana: роадмап среды переводчика](https://github.com/gasyoun/RussianRamayana/blob/main/docs/ROADMAP_LEONOV_TRANSLATOR_ENV_RAMAYANA_5_7_2026.md) — отдельная линия (автосноски к книгам V–VII), на которую с 12-07-2026 ссылается интро гайда; её памятка — [HOWTO_LEONOV.md](https://github.com/gasyoun/RussianRamayana/blob/main/translator-env/HOWTO_LEONOV.md)

## История ревизий субъекта

| Дата | Что изменилось | Кто |
|---|---|---|
| 10-07-2026 | Первая версия: 9 разделов, словарик, памятка | Fable 5 (`claude-fable-5`), H497 |
| 11-07-2026 | template v2 backfill (H663) | Sonnet 5 (`claude-sonnet-5`) |
| 12-07-2026 | В интро добавлен указатель на отдельную линию — среду автосносок к книгам V–VII (RussianRamayana); линии не смешиваются | Opus 4.8 (`claude-opus-4-8`) |

_Dr. Mārcis Gasūns_
