# Большие `.docx/.pdf` — релизные ассеты? Правовая раскладка и прогон (B6)

_Created: 29-08-2026 · Last updated: 29-08-2026_

> Пункт [ROADMAP_2026H2.md §B6](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/ROADMAP_2026H2.md):
> «Большие `.docx/.pdf` — в релизы. Замер 26-08-2026: отслеживаемых бинарников
> ≈ 21,8 МБ, из них 20 МБ — один файл…» — выкладка охраняемого текста релизным
> ассетом = правовое решение человека (Дорожка C). Repo-side половина готова
> (см. «Статус»); само решение и прогон — за М.Г., по ≈10 минут на одобренный файл.

## Замер 29-08-2026: все отслеживаемые бинарники (8 файлов, ≈ 20,9 МБ)

Перепись не ручная — [`scripts/release_binaries.py`](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/release_binaries.py)
(снапшот: [data/binary_census.json](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/binary_census.json)):

| Файл | Размер | Класс | Кто решает |
|---|---|---|---|
| [tronsky-XXX/sources/kazansky_1987.pdf](https://github.com/gasyoun/CommentaryStrategies/blob/main/tronsky-XXX/sources/kazansky_1987.pdf) | 19,70 МБ | **rights** — скан чужой статьи (Казанский, 1987) | только М.Г.: письменное разрешение правообладателя **или** подтверждение, что текст уже публичен (тогда не ассет, а ссылка) |
| [data/book/sundarakanda_print_master.docx](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/book/sundarakanda_print_master.docx) | 0,65 МБ | **timing** — camera-ready мастер тома ЛП | М.Г. + издательство «Литературные памятники»; до выхода книги не публикуется |
| [ramayana-leonov/02_Lidova_31-66.pdf](https://github.com/gasyoun/CommentaryStrategies/blob/main/ramayana-leonov/02_Lidova_31-66.pdf) | 0,38 МБ | **rights** — скан материала Лидовой | только М.Г.: как строка выше |
| [tronsky-XXX/CommentaryStrategies_Tronsky30_Kostina.docx](https://github.com/gasyoun/CommentaryStrategies/blob/main/tronsky-XXX/CommentaryStrategies_Tronsky30_Kostina.docx) | 0,05 МБ | **timing** — черновик статьи с соавтором | М.Г. + согласие Костиной |
| [tronsky-XXX/archive/CommentaryStrategies-Tronsky30.docx](https://github.com/gasyoun/CommentaryStrategies/blob/main/tronsky-XXX/archive/CommentaryStrategies-Tronsky30.docx) | 0,03 МБ | **timing** — архивный черновик той же статьи | покрыт решением по статье |
| [tronsky-XXX/article_v_tronsky_anon.docx](https://github.com/gasyoun/CommentaryStrategies/blob/main/tronsky-XXX/article_v_tronsky_anon.docx) | 0,03 МБ | **timing** — анонимизированная версия (слепое ревью) | покрыт решением по статье |
| [tronsky-XXX/scripts/custom-reference.docx](https://github.com/gasyoun/CommentaryStrategies/blob/main/tronsky-XXX/scripts/custom-reference.docx) | 0,01 МБ | **build-input** — pandoc style reference | никто: остаётся в git, ассетом не бывает |
| [tronsky-XXX/scripts/tronsky_reference.docx](https://github.com/gasyoun/CommentaryStrategies/blob/main/tronsky-XXX/scripts/tronsky_reference.docx) | 0,01 МБ | **build-input** — pandoc style reference | никто: остаётся в git, ассетом не бывает |

**Итог классификации: механически выкладываемых файлов сегодня — ноль.**
Оба скана — охраняемые чужие тексты; рукописи — неопубликованные произведения
с соавторами и издательскими обязательствами. Это и есть причина, почему
чекбокс B6 закрывается разделённо, а не переносом «одной командой».

## Почему файлы пока остаются в git (и не вычёркиваются)

- Репозиторий **публичный**, но «лежит в git» ≠ «опубликован как ассет»: git-копия
  не выдаётся в UI релизов и не индексируется как раздаточный материал. Решение
  о *публикации* всё равно за человеком; удалять сканы из git без решения нельзя —
  свежий клон их потеряет (это источник, из которого собран анализ, ср. H3558:
  `.html` остались под версией именно потому, что их читают парсеры).
- Для будущих сканов дисциплина уже другая (прецедент H2832, Goldman): охраняемые
  сканы в `.gitignore`, в репо — только инвентари и метрики. Гейт переписи (ниже)
  не даст новому бинарнику появиться в git без класса и переписи.

## Статус: что уже готово repo-side

| Артефакт | Состояние |
|---|---|
| [`scripts/release_binaries.py`](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/release_binaries.py) | перепись (по магическим байтам + расширениям), классы VERDICTS, гейт `--check`, guarded `upload` (dry-run по умолчанию, allowlist обязателен, класс `rights` не проходит без `--rights-cleared`) |
| [data/binary_census.json](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/binary_census.json) | снапшот переписи 29-08-2026 (8 файлов, 21 881 990 байт) |
| CI, job «Corpus integrity» | шаг «Tracked-binary census gate»: новый отслеживаемый бинарник без вердикта краснит CI — замер 26-08 больше не может незаметно повториться |
| Прогон выкладки | см. «Прогон» ниже — одна команда на одобренный файл |

## Прогон: когда решение по файлу принято

1. Создать/выбрать релиз (релизная конвенция уже живая: теги `vX.Y.Z`, см.
   [docs/ZENODO_DEPOSIT.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/ZENODO_DEPOSIT.md) —
   Zenodo забирает релизы GitHub, ассеты поедут в депозит вместе с архивом,
   поэтому права проверяются **до** выкладки, не после).
2. Записать решение в allowlist-файл (по одному пути на строку, `#` —
   комментарии). Файл можно держать вне репо — allowlist это вход команды,
   не коммит; но строку «решил(а) такого-то числа, основание …» стоит оставить
   в этом чекбоксе B6.
3. Dry-run: `python scripts/release_binaries.py upload --release vX.Y.Z --allowlist <файл>`
4. Реальная выкладка: то же + `--execute` (для класса `rights` — только вместе
   с `--rights-cleared`; флаг лишь фиксирует, что бумажное разрешение у вас).
5. Перечислить выложенное в чекбоксе B6 — пункт закрывается целиком.

## Что решение НЕ трогает

- `*_files/` веб-дампов и рукописные `*_commentary_analysis.html` — вне
  этого чекбокса (H3558 закрыт 26-08-2026).
- Слой Примечаний пяти изданий и слой Vālmīki — их правовой режим уже
  зафиксирован ([data/RIGHTS.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/RIGHTS.md),
  [data/valmiki_PERMISSION.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/valmiki_PERMISSION.md));
  они не входят в «большие бинарники» и в релизах едут внутри архива, как раньше.

---

_Dr. Mārcis Gasūns_
