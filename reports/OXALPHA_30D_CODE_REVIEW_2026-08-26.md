# OxAlpha 30-day retrospective code review — evidence report (H3551)

_Created: 03-09-2026 · Last updated: 03-09-2026_
Executor: OxAlpha (`zai-coding-plan/glm-5.3-flash`, opencode) · Handoff: [Uprava H3551](https://github.com/gasyoun/Uprava/blob/main/handoffs/H3551-OxAlpha_CommentaryStrategies_oxalpha-30d-risk-review-gate_26.08.26.md) · Plan: [PLAN_COMMENTARYSTRATEGIES_OXALPHA_CODE_REVIEW_HARDENING_2026Q3](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/PLAN_COMMENTARYSTRATEGIES_OXALPHA_CODE_REVIEW_HARDENING_2026Q3.md)

Fixed evidence window: **merges 26-07-2026 .. 25-08-2026** (inclusive). Review pass date: 03-09-2026 (main at `7bf8a87` + this handoff's merged PRs, [§7](#7-merged-prs-from-this-handoff)).

## 1. Method

1. Ten candidate slices were named by the implementation plan; each was validated against the window and the executable-code filter before review. **All ten retained; zero replaced.**
2. Each slice got two **independent** passes over its executable diff: **Standards** (repo rules + named smells, exact hunks) and **Spec** (requirement source resolved in the ruled order PR body → issue → handoff/plan → matching doc; quoted, or `no spec available`).
3. Exclusion rule: generated/vendor/data-only churn is listed per slice but carries no verdict weight; every retained slice has executable code in the diff.
4. Finding bar (plan decision #9): severity, exact location, demonstrable failure mode, repro/test. **One finding below the bar is listed as hardening, not counted as a defect.**

Commands run live during the pass (all green): `python scripts/validate.py` (6055 files PASS) · `python scripts/footnote_review_required.py --selftest` (9 asserts PASS) · `python scripts/review_platform_selftest.py` (PASS) · `python scripts/gate_ledger_selftest.py` (PASS) · `python scripts/translit_hygiene.py --check` (`PASS: only the 3 declared exceptions remain`; 235 files, 4 residue occurrences = the declared ones) · `cd review-api && npm test` (8/8 after the fix PR; 6/6 before, red on the new regression).

## 2. Risk ranking (executable + critical-path risk outranks churn)

| # | Slice | Window merge | Executable surface | Why this rank |
|---|---|---|---|---|
| 1 | [#167](https://github.com/gasyoun/CommentaryStrategies/pull/167) | 14-08 | `review-api/src/*` (OAuth, session, CSRF, D1 drafts, GitHub App submission), `js/review-*.js`, `js/apparatus-review.js`, CI review-platform job, `data/apparatus/review-sw.js` | Authentication + immutable submission = the named critical path |
| 2 | [#159](https://github.com/gasyoun/CommentaryStrategies/pull/159) | 10-08 | `scripts/gate_ledger.py` (+124), `apply_apparatus_decisions.py`, `build_sarga_apparatus.py`, `gate_reviewer_agreement.py` | Canonical gate ledger integrity (two-gatekeeper schema v2) |
| 3 | [#170](https://github.com/gasyoun/CommentaryStrategies/pull/170) | 15-08 | `scripts/translit_hygiene.py` (new, 337 ln), ballot builder data + sw touch | Corpus-wide automated data mutation (643 places) + a CI gate |
| 4 | [#175](https://github.com/gasyoun/CommentaryStrategies/pull/175) | 16-08 | `scripts/build_translit_residue_sheet.py` (+408), `build_translit_residue_cards.py` (+155), `validate.py` skip-set, Playwright spec | Gating vote-sheet generator + validator loosening |
| 5 | [#185](https://github.com/gasyoun/CommentaryStrategies/pull/185) | 16-08 | `scripts/footnote_review_required.py` (new, 340 ln), `build_edition_footnotes.py` | Changes the review_required default — gate-burden semantics |
| 6 | [#178](https://github.com/gasyoun/CommentaryStrategies/pull/178) | 16-08 | `mahabharata-nilakantha/nilakantha_parser.py` (+116−3), `build_licence_register_nilakantha.py` (+410) | Live-scraper repair (silent-empty-corpus trap fixed here) |
| 7 | [#182](https://github.com/gasyoun/CommentaryStrategies/pull/182) | 16-08 | `.github/workflows/ci.yml` (+5: translit gate), vote application (data) | Applies a returned ballot; gate goes mandatory in CI |
| 8 | [#194](https://github.com/gasyoun/CommentaryStrategies/pull/194) | 18-08 | 2 sheet generators (`ui_strings` override, +9/+10 ln) | Small, source-only chrome fix |
| 9 | [#181](https://github.com/gasyoun/CommentaryStrategies/pull/181) | 16-08 | `build_licence_register_review_sheet.py` (+74−35: derive figures at render) | Removes hardcode drift class from a published sheet |
| 10 | [#183](https://github.com/gasyoun/CommentaryStrategies/pull/183) | 16-08 | 11 `scripts/goldman_*.py` + `pdf_textlayer_probe.py` + `yadisk_inventory.py` (research pipeline) | One-off bake-off harness; no shared critical path |

**Slice #167 content boundary.** The Worker/auth code entered `main` as direct `ai-wip` pushes (`69225d8`…`7d08795`, 14-08, no PR) immediately before the #167 squash. The reviewable H2736 slice is therefore the diff `f136172..e5b4415f` (subsumes the direct pushes + the squash); GitHub's recorded base `0f2cfdfe` is listed for the record. Direct pushes inside the review window are themselves a process finding — see [§5 F9](#f9--process--window-work-landed-as-direct-pushes-to-main).

## 3. Slice verdicts — independent Standards and Spec passes

| Slice | Standards verdict (evidence) | Spec source (ruled order) | Spec verdict |
|---|---|---|---|
| #167 | **PASS w/ findings** — auth fail-closed (origin allow-list, session HMAC, CSRF double-submit, PKCE S256, login allow-list), submission immutability (content-hash transport validation, 68-sarga contract, idempotent by `content_hash`), importer keeps Leonov subtree hash + refuses conflicting re-import; worker tests cover all of it. Findings F1–F5, §7. | PR body («Verif» section) + plan PR [#165](https://github.com/gasyoun/CommentaryStrategies/pull/165) (H2736 plan: 68 ballots, one portal, locked 0.95 policy, browser/Worker/CI gates) | **PASS** — 68 ballots + portal published; contracts testable in CI; OAuth/submission fail closed (tests: origin/403, session/401, wrong-state/403, non-allow-listed/403) |
| #159 | **PASS** — schema v2 nesting is the fix for the documented v1 silent-overwrite; `record()` can only replace a reviewer's OWN prior verdict; `conflict()`/`derived_outcome()` never auto-resolve; the `votable` intrinsic-vs-built-state fix is explained at the exact hunk (126/127 false "tier-1" rejections, H2574). F6 hardening. | PR body quoting ruling R1 (Leonov AND Kostina gate assembly) + handoff H2574 | **PASS** — both gatekeepers now storable and κ-computable; re-vote/immutability semantics match R1 |
| #170 | **PASS** — `translit_hygiene.py` separates defect classes by repair safety; ambiguous letters fork per-word against a corpus lexicon, unresolved words reported never guessed; repairs decided on the parsed tree, applied to raw text, `json.loads` re-checked before write. F7 hardening. | [votes/sarga.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/votes/sarga.md) — 19 items (Kostina/MG) | **PASS** — 17 closed in-slice with per-item responses ([SUNDARA_BALLOT_REVIEW_RESPONSE_SARGA01](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/SUNDARA_BALLOT_REVIEW_RESPONSE_SARGA01.md)); 2 explicitly handed to H2832/H2833 |
| #175 | **PASS** — sheets use the org emitter (`csl_pyutil.render_review_sheet`) with evidence manifest; `validate.py` skip of gitignored `review/` is justified at the hunk (self-contained emitter output this repo does not own). | PR body: #170's 90 unresolved places needed a gating artifact, not a Markdown list | **PASS** — 24 cards published to the vote hub; decisions later applied by #182 |
| #185 | **PASS** — predicate is independent of the generator's own Jaccard; named outcomes; frozen sample sizes; selftest 9 asserts green. | PR body encoding step 0 of the voting-queue method (H2809) + VOTING_QUEUE_BURDEN_REDUCTION METHOD §4 | **PASS** — `review_required` default flips to false only via named, checkable predicates; assembly-gate overlap stays gated |
| #178 | **PASS** — the dead-endpoint trap (HTTP 200 + 1-byte body read as «end of parvan» → valid-looking empty corpus) is fixed at the parser with the live endpoint; scrape reproduces the 11-07 census (83 971 shlokas); precision measured over ALL 165 hits (91.5%), 14 rejections carry written reasons. | Handoff [H2860](https://github.com/gasyoun/Uprava/blob/main/handoffs/H2860-Opus_CommentaryStrategies_commentary-licence-register-build-nilakantha_15.08.26.md) on the GO of H1324 | **PASS** — register + density census + corrected feasibility numbers, all derived |
| #182 | **PASS** — CI gate added only after the vote settled the residue to 3 declared exceptions; gate is exact (`--check` fails on any UNDECLARED mixed-script word). | Returned ballot `h2864_translit_residue` (23 decisions) + issue #173's gate ask | **PASS** — 643 → 3 declared exceptions; `--check` PASS live in this review and green in CI since merge |
| #194 | **PASS** — both generators now pass `ui_strings` (RU) with a per-sheet `save_banner` override, documented why the banner is excluded from `RU_UI_STRINGS`; source-only for already-applied artifacts. | H3103 U6 audit (Russian-only reviewer chrome) | **PASS** — scanner 260→116 and 183→61 with the remainders explicitly declared as accepted exceptions |
| #181 | **PASS** — figures (92,1% / 152 / counts) derived from the register tables at render time; the drift class that motivated the PR is named in a comment forbidding re-hardcoding. | PR body: H2860 residual — published sheet carried stale literals | **PASS** — sheet figures now cannot outlive the data |
| #183 | **PASS** — bake-off harness fixes pages and engines before running; verdicts carry CER/mechanism evidence; the sarga-1 join error is corrected with an alignment manifest. | Handoff [H2832](https://github.com/gasyoun/Uprava/blob/main/handoffs/H2832-Opus_CommentaryStrategies_goldman-pdf-ocr-bakeoff_15.08.26.md), `votes/sarga.md` item 4 | **PASS** — conclusion («text layer is a trap») is evidence-backed per engine on a frozen sample |

No slice received a Spec verdict of `no spec available`; every PR body named or linked its requirement source.

## 4. Exclusions applied inside slices

- #167/#170/#175/#182: sarga JSON/HTML ballot bulk and `data/analysis/*` vote outputs — generated or vote artifacts, not hand-executed code (validated by the reproducibility gate in CI instead).
- #183: `data/goldman/*.json` bulk (19 077-line inventory) — bake-off output; the reviewable surface is the harness scripts.
- #178: `data/licence_register/*` tables — verified artifact (re-verified separately by H2883/#181), not hand-executed code.
- #192 (dependabot `actions/setup-node` 6→7, in-window) — **excluded slice**: vendor bump, no executable repo code; CI green on it.

## 5. Findings

Severity scale: P0 = data loss/corruption or security hole on a live path; P1 = correctness defect with demonstrable failure on a real path; P2 = latent contract break (unreachable in shipped config) or exploitable-in-theory; P3 = hardening. **Fix bar per plan decision #10: proven P0/P1 only.**

### F1 — P1 — review-api draft saves could silently lose work (FIXED, [#214](https://github.com/gasyoun/CommentaryStrategies/pull/214))
- **Location:** `review-api/src/drafts.js` `putDraft()` (pre-fix state at `#214^`; module line 4 pre-fix).
- **Failure mode:** the optimistic-versioning check was a read (`getDraft`) then a separate awaited write (`INSERT … ON CONFLICT DO UPDATE SET version=excluded.version`), so two concurrent PUTs carrying the same expected version both read `version=N`, both wrote `N+1`, and **both returned 200** — the first reviewer's saved decisions silently overwritten while the UI reported success. Violates the module's own documented 409-conflict contract for any overlapping requests.
- **Repro/test:** `review-api/test/worker.test.js` «concurrent same-version draft saves cannot both win» — two overlapping same-version PUTs; asserted `200,409`; **failed `200,200` before the fix** (red run recorded during this review), green after. Follow-up test walks the expected>0 UPDATE path after a 409.
- **Fix:** single-statement compare-and-set (D1-atomic): expected-0 upsert guarded `WHERE drafts.version=0`; expected>0 `UPDATE … WHERE version=?`; 0 changed rows → 409 with the remote draft. npm test 8/8 green; PR #214 merged with all checks green.

### F2 — P2 (latent) — per-sarga final submit can never satisfy the server contract
- **Location:** `js/apparatus-review.js:117` `aggregate()` builds `sargas:[{…current sarga only}]`; server contract `review-api/src/submit.js:6` requires exactly ordered sargas 1–68.
- **Failure mode:** on any deployment where `REVIEW_CONFIG.apiBase` is set, the ballot page's «Окончательная отправка» POSTs a 1-sarga payload and is guaranteed HTTP 422 «submission must contain ordered sargas 1–68». In the shipped portal `apiBase:""` (hardcoded in every built ballot page), so the button degrades to the «Hosted sync is not configured» state and the path is unreachable — hence latent P2, not P1.
- **Repro:** unit-level — `aggregate()` output fails `validateTransport` by construction; no live repro possible without configuring `apiBase`.
- **Disposition:** documented, not fixed (below the P0/P1 bar). Recommendation: either accept partial per-sarga immutable submissions server-side (keyed by `manifest_hash`+sarga) or disable/reshape the per-sarga submit button to the aggregate-export contract.

### F3 — P3 (hardening) — HMAC comparison is not constant-time
- **Location:** `review-api/src/auth.js:6` (`verified`: `await hmac(secret,body)!==sig`).
- **Failure mode (theoretical):** string-compare timing on session/MAC verification. Across a network on Workers, jitter makes exploitation impractical; listed for a `crypto.subtle.verify`/constant-time compare on next touch. No demonstrable exploit → below the fix bar.

### F4 — P3 — malformed JSON on mutating routes maps to 500 instead of 400
- **Location:** `review-api/src/index.js:4` (`JSON.parse(text)` on `/submissions`, `request.json()` on drafts PUT; the outer handler catches → 500).
- **Failure mode:** wrong status class for a client error; no data impact. Hardening.

### F5 — P3 — submission file path derives from client-supplied `client_timestamp`
- **Location:** `review-api/src/github.js:6` (`stamp` → `votes/submissions/kostina/${stamp}-${hash}.json`; only `[:.]` replaced).
- **Failure mode:** authenticated-only reviewer could shape the path (GitHub contents API rejects `..`, so no traversal; worst case an odd nested path or upstream 422). Sanitize to `[A-Za-z0-9-]` on next touch.

### F6 — P3 — gate ledger writes are not atomic
- **Location:** `scripts/gate_ledger.py:89` `save()` (direct `json.dump` to the canonical path).
- **Failure mode:** a crash mid-write corrupts canonical gate evidence (git + CI would catch, but the working copy is lost). tmp-file + `os.replace` recommended.

### F7 — P3 — `translit_hygiene --fix` applies camel repairs file-wide in raw text
- **Location:** `scripts/translit_hygiene.py:281` (`raw.replace(bad, good)` over the whole file for every suggested repair).
- **Failure mode:** camel repairs are field-scoped at detection (`CAMEL_FIELDS`) but applied everywhere in the file; a same-spelling token in an SLP1-carrier `stem` field would be rewritten. With the current 7-entry `CAMEL_FIXES` (verse-verified readings) a collision is implausible; `json.loads` re-check guards syntax, not semantics.

### F8 — P3 — importer would IndexError on a colon-less note id
- **Location:** `scripts/import_apparatus_submission.py:67` (`parts[1]`).
- **Failure mode:** unreachable through `validate()` today (allowed ids carry the `{layer}:{verse}:{idx}` shape); latent robustness only.

### F9 — process — window work landed as direct pushes to main
- The H2736 platform core (`review-api/`, `js/`, `review-tests/`) entered `main` as unreviewed direct `ai-wip` commits (`69225d8`…`7d08795`) inside the review window, outside any PR — the exact surface this plan calls the critical path. No code defect beyond F1–F5 resulted, but the adapter's PR-intake discipline should apply to this repo's own agents too (see the [future gate design](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/OXALPHA_STATUS_GATE_DESIGN_2026.md), which proposes an executable-path required check).

**Count:** 0 P0 · 1 P1 (fixed with regression test) · 1 P2 (documented) · 6 P3 (hardening ledger) · 1 process finding. Zero unsupported findings; none silently dropped.

## 6. Verification runs (this pass)

| Check | Result |
|---|---|
| `python scripts/validate.py` | PASS — 6055 files |
| `review-api && npm test` (after #214) | 8/8 pass (regression red before fix) |
| `scripts/review_platform_selftest.py` | PASS (immutable import, idempotency, Leonov preservation, reject veto) |
| `scripts/gate_ledger_selftest.py` | PASS |
| `scripts/footnote_review_required.py --selftest` | PASS (9 asserts) |
| `scripts/translit_hygiene.py --check` | PASS — only the 3 declared exceptions remain (235 files scanned) |
| PR CI (#213, #214) | all repo checks green (CodeQL, ruff/black, pytest 3.10–3.12, Corpus integrity, Review platform contracts, changelog lint, YAML lint) |

## 7. Merged PRs from this handoff

| PR | Wave | Content |
|---|---|---|
| [#213](https://github.com/gasyoun/CommentaryStrategies/pull/213) | 0 | Canonical adapter bootstrap: `docs/agents/{issue-tracker,triage-labels,domain}.md`, CLAUDE.md Agent-skills block, four canonical labels. PR intake OFF. No gate enabled. |
| [#214](https://github.com/gasyoun/CommentaryStrategies/pull/214) | 2 | F1 P1 fix with regression tests (draft compare-and-set). |

Wave 3 (future-gate design) ships as [docs/OXALPHA_STATUS_GATE_DESIGN_2026.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/OXALPHA_STATUS_GATE_DESIGN_2026.md) — **design only, nothing enabled** (no workflow, no protection rule, no required check was added or modified by this handoff).

## 8. Caveats

- The window's PR-side metadata (GitHub base SHAs) and the effective content boundary differ for #167 because of the direct pushes (§2); both are recorded.
- The Cloudflare «Workers Builds» check was red on `main` before and during this pass (pre-existing, deploy-infra, not a repo check); all repo-level checks green. Not reviewed — outside the fixed window and not a code slice.
- F2's live behavior was not reproducible without configuring `apiBase` on a real Worker; the contract mismatch is proven by code reading + the shared `validateTransport`, not by a live 422.

_Dr. Mārcis Gasūns_
