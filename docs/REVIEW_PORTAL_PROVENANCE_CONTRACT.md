_Created: 30-10-2026 · Last updated: 30-10-2026_

# Review-portal provenance contract — and the two-commit rule it forces

_Author: Dr. Mārcis Gasūns (DeepSeek Flash, `deepseek-flash`, via DSH) · Scope: `scripts/build_apparatus_review_portal.py --check`, the required `Review platform contracts` CI job, and the reviewer portals it generates._

## What the contract guarantees

`--check` is the CI gate on the 68-sarga reviewer portals: for the requested
reviewer it rebuilds the manifest, the index shell, the webmanifest, the service
worker and each ballot hash in memory, then compares them byte-for-byte with what
is committed. A portal that is committed without being regenerated fails the
`Review platform contracts` job.

## Where it becomes self-referential

[`source_revision()`](../scripts/build_apparatus_review_portal.py) derives the
manifest's `repo_revision` and `generated_at` from `git log -1 -- <paths>`, where
`paths` covers the generator, the three review JS modules, the CSS, the gate
ledger and the segmented commentary:

```python
paths = ["scripts/build_sarga_apparatus.py", "scripts/build_apparatus_review_portal.py",
         "js/apparatus-review.js", "js/review-portal.js", "js/review-sync.js",
         "css/apparatus-review.css", "data/apparatus/gate_ledger.json",
         "data/analysis/sundara_commentary_segmented.json"]
```

`repo_revision` and `generated_at` are then folded into `manifest_hash`, which is
also stamped into the service-worker cache name. Two consequences follow:

1. **A commit that edits any of those paths re-stales both manifests by existing.**
   The artifacts must record the commit that contains them, so they can never be
   generated, committed and verified inside one commit — the artifact would have
   to name a commit whose SHA does not exist yet.
2. **A data-only commit is stable.** It touches no path in that list, so
   `source_revision()` keeps pointing at the preceding code commit — which is
   exactly what the artifacts already record.

This is the same shape that produced the earlier heals on `main`: `f1c40e2`
(H4371) shipped the generator change with freshly built-but-self-stale artifacts,
and `5264bbd` (H4742) repaired it with a "regenerate provenance metadata (zero
content delta)" commit that touched only `data/apparatus/`. It is not a one-off
accident — it is the only shape that can pass.

## The rule

> Any PR that edits the portal generator, the review JS, the CSS, the gate ledger
> or the segmented commentary **must be followed by a second, data-only commit**
> that regenerates **every** reviewer portal. Do not close such a PR on a
> `--check` PASS produced in the working tree before the commit: that PASS is not
> evidence at the head.

Recipe (this is the whole of it):

```bash
python scripts/build_apparatus_review_portal.py                  # default reviewer
python scripts/build_apparatus_review_portal.py --reviewer Леонов
python scripts/build_review_test_fixtures.py                     # fixtures quote the manifest hash
git add data/apparatus tests/fixtures                            # data only — no scripts, no js
git commit -m "<H####>: regenerate portal provenance (data-only)"
python scripts/build_apparatus_review_portal.py --check                    # exit 0
python scripts/build_apparatus_review_portal.py --check --reviewer Леонов  # exit 0
python scripts/validate_apparatus_submission.py tests/fixtures/apparatus_submission_valid.json
python scripts/review_platform_selftest.py
```

## The second mirror: the submission fixtures

The regenerated manifest hash is quoted in one more place — the synthetic vote-free
submissions under `tests/fixtures/` that the same CI job validates:

```bash
python scripts/build_review_test_fixtures.py     # rewrites both fixtures from the live manifest
```

`build_review_test_fixtures.py` copies `manifest_hash`, `source_hash` and the
per-sarga hashes out of `data/apparatus/reviewer_manifest.json` and recomputes
`content_hash`. Skip it after a provenance regen and the job goes red with a
*different* message — `FAIL: manifest_hash mismatch` from
`validate_apparatus_submission.py`, and the same assertion inside
`review_platform_selftest.py` — while `--check` itself is green. Both fixtures
(`apparatus_submission_valid.json`, `apparatus_submission_invalid_identity.json`)
move together; the generator is the only thing that should write them.

Inside one PR this works as a second commit; across a **squash** merge it does
not, because squash rewrites the SHA the artifacts recorded. So a code-changing
PR always leaves `main` self-stale and owes a **follow-up data-only PR** — the
squash commit touches only data, so `source_revision()` stays on the code commit
and the regenerated artifacts verify. Probe the live URL after that PR lands.

## The acceptance-criterion hole

The natural local check — «`git status` shows no `data/apparatus/*kostina*`
modification» — cannot see the drift. The three files that actually go stale
(`index.html`, `review-sw.js`, `reviewer_manifest.json`) carry no `kostina` in
their names; only the ballots do, and the ballots never drift. State the criterion
as it is meant: **rebuild every portal, then `git diff --exit-code` over the whole
of `data/apparatus/`.**

## Evidence (30-10-2026)

Live states seen on this date, each reproduced from a clean tree:

| Tree | `--check` | `--check --reviewer Леонов` | manifest hash (Костина / Леонов) |
|---|---|---|---|
| `main` fe783d1 | exit 0 | n/a — no leonov ballot set | `1c9f1a50…` / — |
| PR #273 head 2c88bec | **exit 1** — stale `reviewer_manifest.json`, `index.html`, `review-sw.js` | **exit 1** — stale `reviewer_manifest_leonov.json`, `index_leonov.html`, `review-sw-leonov.js` | `1c9f1a50…` / `7c60f9b6…` — both recording the pre-PR revision `f1c40e2` |
| `main` 5f34d92 (squash of #274) | **exit 1** — same three files | **exit 1** — same three files | recorded `39646fe8…` (the branch tip, not the squash) |
| `main` + data-only heal (#275) | exit 0 | exit 0 | `ee775d1a…` / `32816f91…` |

The `7c60f9b6…` hash that H7517 recorded as its leonov PASS evidence is the one
belonging to the pre-code-commit tree: the artifacts had been built before the
`--reviewer` change was committed, and were never rebuilt after it. The same
mechanism re-staled `main` the moment #274 was squash-merged, which is why the
heal is part of the delivery and not an optional tidy-up.

## Related

- PR [#273](https://github.com/gasyoun/CommentaryStrategies/pull/273) — H7517 v1, closed after the gate findings; [#274](https://github.com/gasyoun/CommentaryStrategies/pull/274) — v2 with the oxalpha findings fixed and the ballots regenerated in-PR; [#275](https://github.com/gasyoun/CommentaryStrategies/pull/275) — this data-only heal of `main`.
- [`docs/OXALPHA_STATUS_GATE_DESIGN_2026.md`](OXALPHA_STATUS_GATE_DESIGN_2026.md) — the `oxalpha-review` gate that sits beside the red job; it mirrors a session verdict and never fabricates a pass.
