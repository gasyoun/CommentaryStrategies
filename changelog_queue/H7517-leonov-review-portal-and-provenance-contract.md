_Created: 30-10-2026 · Last updated: 30-10-2026_

# H7517 — портал рецензента Леонова: флаг `--reviewer` и правило двух коммитов для provenance

### Added

- **`scripts/build_apparatus_review_portal.py --reviewer`** — портал 68-саргового
  рецензирования параметризован по рецензенту. Для Костиной сохраняются прежние
  одиночные имена (`index.html`, `reviewer_manifest.json`, `review.webmanifest`,
  `review-sw.js`), поэтому её сохранённое состояние PWA и старые ссылки не меняются;
  остальные рецензенты получают суффикс слага (`index_leonov.html`,
  `reviewer_manifest_leonov.json`, `review_leonov.webmanifest`,
  `review-sw-leonov.js`), выведенный из той же карты `REVIEWER_SLUG`, что и в
  `build_sarga_apparatus.py`. Кириллица рецензента остаётся в данных, имена файлов
  латинские.
- **68 бюллетеней Леонова** — `data/apparatus/sarga_01…68_leonov.{json,html}`,
  2 502 заметки, 1 302 голосуемых, `_meta.built_for_reviewer == "Леонов"` во всех;
  портал `index_leonov.html` + `reviewer_manifest_leonov.json` +
  `review_leonov.webmanifest` + `review-sw-leonov.js`. Проверка дрейфа H4371
  (бюллетень ↔ view-only двойник) расширена на каждый набор бюллетеней на диске и
  проходит для обоих слагов; 68 костинских бюллетеней побайтово не тронуты.
- **`docs/REVIEW_PORTAL_PROVENANCE_CONTRACT.md`** — контракт provenance и правило
  двух коммитов, с таблицей доказательств на живых деревьях (PR #273, #274, #275).

### Fixed

- **Самоссылающийся provenance ронял обязательный чек `Review platform contracts`**
  (DeepSeek Flash, `deepseek-flash`, 30-10-2026). `source_revision()` берёт
  `repo_revision`/`generated_at` из `git log -1` по путям генератора и review-JS, а
  они входят в `manifest_hash` и в имя кэша service worker'а, — поэтому сам коммит,
  добавляющий `--reviewer`, делает оба манифеста устаревшими: на голове 2c88bec оба
  прогона `--check` выходили 1, а хэш `7c60f9b6…`, записанный в H7517 как PASS,
  принадлежал дереву до коммита кода. Лечение — отдельный data-only коммит, который
  не трогает ни одного пути из списка `source_revision()`: меняются только
  `repo_revision`/`generated_at`/`manifest_hash`/имя SW-кэша, оба `--check` — 0.
  Тот же приём, что `5264bbd` (H4742) для `f1c40e2` (H4371). Внутри PR это второй
  коммит, но squash-merge переписывает SHA, поэтому код-меняющий PR всё равно
  оставляет `main` self-stale и требует отдельного data-only PR: после squash #274
  на 5f34d92 оба `--check` снова выходили 1, и хил #275 вернул их в 0
  (`ee775d1a…` для Костиной, `32816f91…` для Леонова).
