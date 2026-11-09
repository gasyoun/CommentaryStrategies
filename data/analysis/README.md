_Created: 09-11-2026 · Last updated: 09-11-2026_

# data/analysis — машинные переписи и журналы чисел

 DH #3 (H7924): вход в воспроизводимые числа статьи
`articles/intro_article_lp5_draft.md`. Каждое число статьи —
в журнале чисел метадока статьи
(`articles/intro_article_lp5_draft.meta.md`, раздел «Числовой журнал»).

## Перепись ракшас-лексики (стр. §1.4.2, микрораздел о женской доле)

- Скрипт: `rakshasa_census_vulgate_2026-11-01.py` (репозиторий — корень
  CommentaryStrategies; запуск: `python3 data/analysis/rakshasa_census_vulgate_2026-11-01.py`).
- Выход: `rakshasa_census_vulgate_2026-11-01.json` (рядом со скриптом).
- Ключи, цитируемые статьёй:
  - `census_by_kanda` — строки Таблицы 1 (стихи, rākṣasa-, rākṣasī,
    rakṣas- ср. рода, плотность на 100 шлок);
  - `totals` — итог 1 566 / 120 / 193 / 8,5;
  - `sundara_vs_southern.sundara_tokens_by_sarga` — все 68 сарг
    (стихи/токены/female), сумма 326, female 65;
  - `sundara_vs_southern.sundara_blocks` — блоки Таблицы 2
    (tokens + female + male_other; стр. 22–27: 79 = 31 ж. + 48 м./н.);
  - `rigveda_full` — RV-перепись (DCS, колонка FORM);
  - `hanuman_rakshasa_5_43_50`, `context_5_2_40_46` — целевые чеки;
  - `dossier_compatibility` — досье 2 029 против чистой переписи 1 566.
- Методика: подстрока стема в тексте стиха (`data/valmiki_shlokas`,
  Gita Supersite); словарные глоссы исключены (см. сноску [^8] статьи).
- Корпусные пины: DCS — через `git rev-parse HEAD` в локальном
  клоне (если клон отсутствует на хосте перепрогона, RV-значения
  заморожены, а не зануляются — containment, H7924 DH #9).
- Права: Gita Supersite — CC BY 4.0, атрибуция дословно —
  `data/RIGHTS.md` / `data/valmiki_PERMISSION.md`.

## Прочие журналы (вне scope этой переписи)

- `leonov_commentator_stats.json` — иерархия цитирования тик
  (1 058 / 368 / 34,8 % / 108 / 10,2 %; §4 статьи).
- `phase2_pilot/pilot_rejected.json` — ≈67 % отклонений пилота —
  «пересказ подстрочника» (§6 статьи).

_к.ф.н. М.Ю. Гасунс_
