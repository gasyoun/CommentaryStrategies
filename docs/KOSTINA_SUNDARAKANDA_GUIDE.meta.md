# Метадок: KOSTINA_SUNDARAKANDA_GUIDE.md

_Created: 10-07-2026 · Last updated: 11-07-2026_

Метадок для [docs/KOSTINA_SUNDARAKANDA_GUIDE.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/KOSTINA_SUNDARAKANDA_GUIDE.md).

## Назначение и аудитория

Руководство для Е. Костиной — первого комментатора и литературного
редактора тома «Сундараканда», в паре с
[docs/LEONOV_SUNDARAKANDA_GUIDE.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/LEONOV_SUNDARAKANDA_GUIDE.md).
Тот же нетехнический уровень (браузер и почта), общие разделы (устройство
проекта, механика страниц, GitHub, словарик) параллельны леоновским, но
раздел 4 — ее собственная четверка задач из
[issue №57](https://github.com/gasyoun/CommentaryStrategies/issues/57):
ратификация редполитики §3, судьба ~427 помет `***[Е. Костина]***`
(блокирует верстку), статус «Анатолий», сборочный гейт с Леоновым.

## Происхождение

Написано 10-07-2026, Fable 5 (`claude-fable-5`), handoff
[H517](https://github.com/gasyoun/Uprava/blob/main/handoffs/H517-Fable_CommentaryStrategies_kostina_sundarakanda_guide_10.07.26.md),
по решению МГ: вычитку леоновского руководства Костиной отменить, вместо
нее — отдельное руководство под ее роль. Фактура — из
[issue №57](https://github.com/gasyoun/CommentaryStrategies/issues/57),
[docs/MANUAL.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/MANUAL.md),
[docs/COMMENTARY_ROADMAP.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/COMMENTARY_ROADMAP.md).

## Бэклог улучшений (ранжирован)

1. **Синхронные правки с леоновским близнецом** — общие разделы (1, 5, 6,
   7, 8) редактировать парно: правка механики в одном руководстве обязана
   попадать во второе тем же коммитом. Статус: стоячее правило.
2. **Скриншоты** для разделов 5.1/5.2 — как и у близнеца. Статус: открыто.
3. **Актуализация задачи 2 после ее решения** — когда Костина выберет
   «А»/«Б» по пометам, переписать раздел из вопроса в констатацию.
   Статус: заблокировано ее ответом.
4. **Синхронизация чисел** (~427 помет, ~900 черновиков) после
   голосования МГ и применения `decisions.json`. Статус: заблокировано.

## Известные ограничения

- Технический уровень Костиной не выяснялся отдельно — руководство
  калибровано по худшему случаю («совсем не технарь»), как и леоновское;
  для редактора это может быть избыточно подробно, но не вредно.
- Числа даны округленно на дату создания.

## Intended use / known misuse

Документ для одного читателя — Е. Костиной, некалиброванного технически
(браузер и почта), с ее личной четверкой задач из
[issue №57](https://github.com/gasyoun/CommentaryStrategies/issues/57).
Использовать по назначению: отправлять ей как самостоятельное руководство
«что делать именно тебе», не требуя параллельного чтения
[docs/MANUAL.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/MANUAL.md).
Известное неправильное использование: (а) редактировать общие с леоновским
близнецом разделы (1, 5, 6, 7, 8) в одном руководстве, не зеркаля правку в
[docs/LEONOV_SUNDARAKANDA_GUIDE.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/LEONOV_SUNDARAKANDA_GUIDE.md)
тем же коммитом — это прямое нарушение бэклог-правила №1, расхождение
близнецов проверить сложно, а обнаруживается поздно; (б) выдавать
Костиной эту версию раздела 4 после того, как она выберет вариант «А»/«Б»
по ~427 пометам `***[Е. Костина]***`, не переписав раздел из вопроса в
констатацию (бэклог №3) — устаревший вопрос читается как открытый, хотя
решение уже принято.

## Maintenance & sunset plan

Владелец — МГ / агентная сессия по его указанию; общие разделы правятся
ПАРНО с [docs/LEONOV_SUNDARAKANDA_GUIDE.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/LEONOV_SUNDARAKANDA_GUIDE.md)
одним коммитом — стоячее правило (бэклог №1), нарушение которого — главный
риск устаревания документа. Раздел 4 (личные задачи Костиной) обновляется
по факту ее ответов (бэклог №3–4). После сдачи тома (~07-08-2026) и
закрытия ее четырех задач руководство теряет операционную функцию и
становится историческим — отдельного плана архивации пока не заведено,
по аналогии с планом MANUAL §8 (см. метадок MANUAL.md, бэклог №4).

## Deprecation status

`active`

## Связанные документы

- [docs/LEONOV_SUNDARAKANDA_GUIDE.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/LEONOV_SUNDARAKANDA_GUIDE.md) — руководство-близнец переводчика
- [docs/MANUAL.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/MANUAL.md) — регламент книги
- [docs/COMMENTARY_ROADMAP.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/COMMENTARY_ROADMAP.md) — редполитика §3 на ратификацию
- [issue №57](https://github.com/gasyoun/CommentaryStrategies/issues/57) — личный чек-лист Костиной

## История ревизий субъекта

| Дата | Что изменилось | Кто |
|---|---|---|
| 10-07-2026 | Первая версия: 9 разделов, ее четыре задачи, словарик | Fable 5 (`claude-fable-5`), H517 |
| 11-07-2026 | template v2 backfill (H663) | Sonnet 5 (claude-sonnet-5) |

_Dr. Mārcis Gasūns_
