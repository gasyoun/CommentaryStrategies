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
   generated, committed and verified inside one commit.
2. **A data-only commit is stable.** It touches no path in that list, so
   `source_revision()` keeps pointing at the preceding code commit — which is
   precisely what the artifacts already record.

This is the same shape that produced the two earlier heals on `main`: `f1c40e2`
(H4371) shipped the generator change with freshly built-but-self-stale artifacts,
and `5264bbd` (H4742) repaired it with a "regenerate provenance metadata (zero
content delta)" commit that touched only `data/apparatus/`. That was not a
one-off accident — it is the only shape that can pass.

## The rule

> Any PR that edits the portal generator, the review JS, the CSS, the gate ledger
> or the segmented commentary **must end with a second, data-only commit** that
> regenerates **every** reviewer portal. Do not merge such a PR while
> `Review platform contracts` is red on the claim that `--check` passes locally:
> a PASS from the working tree before the commit is not evidence at the head.

Recipe (this is the whole of it):

```bash
python scripts/build_apparatus_review_portal.py                  # default reviewer
python scripts/build_apparatus_review_portal.py --reviewer Леонов
git add data/apparatus                                           # data only — no scripts, no js
git commit -m "<H####>: regenerate portal provenance (data-only)"
python scripts/build_apparatus_review_portal.py --check                 # exit 0
python scripts/build_apparatus_review_portal.py --check --reviewer Леонов  # exit 0
```

After a **squash** merge the heal has to be repeated: squash rewrites the SHA, so
`source_revision()` moves to the squash commit and `main` is self-stale again
until a data-only regen commit lands on top of it. Plan for that commit before
announcing the merge, and probe the live URL afterwards.

## The acceptance-criterion hole

The natural local check — «`git status` shows no `data/apparatus/*kostina*`
modification» — cannot see the drift. The three files that actually go stale
(`index.html`, `review-sw.js`, `reviewer_manifest.json`) carry no `kostina` in
their names; only the ballots do, and the ballots never drift. H7517's first head
(2c88bec) passed that informal check while both `--check` runs failed. State the
criterion as it is meant: **rebuild every portal, then `git diff --exit-code` over
the whole of `data/apparatus/`.**

## Evidence (30-10-2026, PR #273)

| Tree | `--check` | `--check --reviewer Леонов` | manifest hash |
|---|---|---|---|
| `origin/main` fe783d1 | exit 0 | n/a — no leonov ballot set | `1c9f1a50…` |
| PR head 2c88bec | **exit 1** — stale `reviewer_manifest.json`, `index.html`, `review-sw.js` | **exit 1** — stale `reviewer_manifest_leonov.json`, `index_leonov.html`, `review-sw-leonov.js` | `1c9f1a50…` / `1c9f1a50…` (both recorded the pre-PR revision `f1c40e2`) |
| PR head + data-only commit a636416 | exit 0 | exit 0 | `b0681db5…` / `872e7311…` |

Both manifests recorded `repo_revision f1c40e2 / generated_at 2026-09-08` at the
red head, i.e. the leonov artifacts had never been regenerated after the code
commit that introduced them.

## Related

- PR [#273](https://github.com/gasyoun/CommentaryStrategies/pull/273) — H7517, the `--reviewer` parameterization that exposed this.
- [`docs/OXALPHA_STATUS_GATE_DESIGN_2026.md`](OXALPHA_STATUS_GATE_DESIGN_2026.md) — the `oxalpha-review` gate that sits beside the red job; it mirrors a session verdict and never fabricates a pass.
