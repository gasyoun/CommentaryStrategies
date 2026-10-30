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
  `build_sarga_apparatus.py`. Карта `REVIEWER_SLUG`/`REVIEWER_GEN`/`REVIEWER_DISPLAY`
  держит кириллицу в стороне от имён файлов.
- **68 бюллетеней Леонова** — `data/apparatus/sarga_01…68_leonov.{json,html}`,
  2 502 заметки, 1 302 голосуемых, `_meta.built_for_reviewer == "Леонов"` во всех;
  портал `index_leonov.html` + `reviewer_manifest_leonov.json` +
  `review_leonov.webmanifest` + `review-sw-leonov.js`. Проверка дрейфа H4371
  (бюллетень ↔ view-only двойник) расширена на каждый набор бюллетеней на диске и
  проходит для обоих слагов; 68 костинских бюллетеней побайтово не тронуты.
- **`docs/REVIEW_PORTAL_PROVENANCE_CONTRACT.md`** — контракт provenance и правило
  двух коммитов, с таблицей доказательств на живых деревьях.

### Fixed

- **Самоссылающийся provenance ронял обязательный чек `Review platform contracts`**
  (DeepSeek Flash, `deepseek-flash`, 30-10-2026). `source_revision()` берёт
  `repo_revision`/`generated_at` из `git log -1` по путям генератора и review-JS, а
  они входят в `manifest_hash` и в имя кэша service worker'а, — поэтому сам коммит,
  добавляющий `--reviewer`, делает оба манифеста устаревшими (костинский остался на
  `f1c40e2`, леоновский вообще не перегенерировался после кодового коммита). На
  голове 2c88bec оба прогона `--check` выходили 1. Лечение — отдельный data-only
  коммит, который не трогает ни одного пути из списка `source_revision()`:
  перегенерированы оба портала, меняются только `repo_revision`/`generated_at`/
  `manifest_hash`/имя SW-кэша (`1c9f1a50…` → `b0681db5…` для Костиной,
  `872e7311…` для Леонова), оба `--check` — 0. Тот же приём, что `5264bbd` (H4742)
  для `f1c40e2` (H4371); после squash-merge хил нужно повторить, потому что squash
  переписывает SHA.
