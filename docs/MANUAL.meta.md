# Метадок: MANUAL.md

_Created: 10-07-2026 · Last updated: 11-07-2026_

Метадок для [docs/MANUAL.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/MANUAL.md).
Заведен 10-07-2026 — позже субъекта (создан 07-07-2026): в сессии тройки
ролевых руководств MANUAL правился дважды, и записывать его ревизии стало
негде.

## Назначение и аудитория

Операторский справочник тома «Рамаяна. Книга V. Сундараканда» (ЛП/Наука):
два яруса аппарата, принцип двойного гейта, конвейер §4, четыре браузерных
листа §5, применение решений §6, типовые сценарии §7, текущие блокеры §8.
Аудитория — все три участника книги и агентные сессии. С 10-07-2026
разделение труда с ролевыми руководствами зафиксировано в самом MANUAL:
он — «как всё устроено», руководства
([Леонов](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/LEONOV_SUNDARAKANDA_GUIDE.md) ·
[Костина](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/KOSTINA_SUNDARAKANDA_GUIDE.md) ·
[Гасунс](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/GASUNS_SUNDARAKANDA_GUIDE.md)) —
«что делать именно тебе и в каком порядке».

## Происхождение

Создан 07-07-2026 ([PR #55](https://github.com/gasyoun/CommentaryStrategies/pull/55),
коммит `1e97f19`) в H268-контуре подготовки camera-ready как единый
операторский документ по итогам машинной фазы. Правки 10-07-2026 — сессия
тройки руководств, Fable 5 (`claude-fable-5`), handoffs
[H497](https://github.com/gasyoun/Uprava/blob/main/handoffs/H497-Fable_CommentaryStrategies_leonov_sundarakanda_guide_10.07.26.md)/[H533](https://github.com/gasyoun/Uprava/blob/main/handoffs/H533-Fable_CommentaryStrategies_gasuns_sundarakanda_guide_10.07.26.md).

## Бэклог улучшений (ранжирован)

1. **§5/§8 живут — обновлять по факту**: после каждого проголосованного
   листа вычеркивать его из §5-таблицы и §8-блокеров; §8 датирован
   07-07-2026 и начнет врать первым. Статус: стоячее правило.
2. **Счетчики нот** (партия-3 227, лексический 604+7 и т.д.) после apply
   пересверить с фактическими `decisions.json`. Статус: заблокировано
   голосованием.
3. **§7 use cases** — добавить сценарий «участник заблудился» → отсылка к
   его ролевому руководству (частично закрыто блоком в §1). Статус: открыто,
   низкий приоритет.
4. **Судьба §8 после сдачи тома** — раздел станет историческим; при сдаче
   заменить на короткий пост-мортем со ссылкой на релизы. Статус:
   заблокировано сдачей (~07-08-2026).

## Известные ограничения

- Числа и статусы в §3/§5/§8 — снимок на 07-07-2026; живое состояние — в
  [.ai_state.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/.ai_state.md)
  и трех персональных issues ([№56](https://github.com/gasyoun/CommentaryStrategies/issues/56) ·
  [№57](https://github.com/gasyoun/CommentaryStrategies/issues/57) ·
  [№58](https://github.com/gasyoun/CommentaryStrategies/issues/58)).
- MANUAL сознательно не дублирует метод-детали —
  [docs/PHASE2_METHOD.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/PHASE2_METHOD.md)
  остается каноном рубрики судьи и контракта черновиков.

## Связанные документы

- Тройка ролевых руководств (выше) и их метадоки — у близнецов Леонова/Костиной
  парное правило правки общих разделов.
- [docs/COMMENTARY_ROADMAP.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/COMMENTARY_ROADMAP.md) — редполитика §3, открытые решения.
- [docs/LP_APPARATUS_DESIGN.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/LP_APPARATUS_DESIGN.md) — четыре калибровочных решения МГ.

## История ревизий субъекта

| Дата | Что изменилось | Кто / PR |
|---|---|---|
| 07-07-2026 | Первая версия: роли, ярусы, конвейер, листы, apply, use cases, блокеры | H268-контур, [PR #55](https://github.com/gasyoun/CommentaryStrategies/pull/55) |
| 10-07-2026 | Имя переводчика: «А. Леонов» → «М. Леонов» (×2) | Fable 5 (`claude-fable-5`), H497, [PR #61](https://github.com/gasyoun/CommentaryStrategies/pull/61) |
| 10-07-2026 | Блок о тройке ролевых руководств в §1 + строка в §8 у персональных issues | Fable 5 (`claude-fable-5`), [PR #66](https://github.com/gasyoun/CommentaryStrategies/pull/66) |
| 11-07-2026 | §6: сборочный гейт Леонова/Костиной — новый `apply_apparatus_decisions.py` + оверлей `gate_ledger.json`; строка в схеме §4 | Opus 4.8 (`claude-opus-4-8`), H732 |

_Dr. Mārcis Gasūns_
