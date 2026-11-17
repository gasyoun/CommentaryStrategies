_Created: 14-08-2026 · Last updated: 17-11-2026_

# Review API deployment (Free plan only)

This Worker is optional transport around the always-working Pages/local/export
flow. D1 stores versioned drafts; GitHub raw-submission PRs are canonical final
evidence. The Worker cannot edit `data/apparatus/gate_ledger.json`.

Before deployment, the operator must verify the Cloudflare dashboard says
Workers Free and D1 Free and does not request billing activation. Create the D1
database, replace only the deployment-time database ID, run migration
`0001_initial.sql`, and configure these encrypted Worker secrets without printing
them: `SESSION_SECRET`, `GITHUB_OAUTH_CLIENT_ID`, `GITHUB_OAUTH_CLIENT_SECRET`,
`GITHUB_APP_ID`, `GITHUB_APP_INSTALLATION_ID`, `GITHUB_APP_PRIVATE_KEY`, and the
confirmed `ALLOWED_GITHUB_LOGIN`. The GitHub App is limited to this repository
with Contents write and Pull requests write; no PAT is supported.

Set `PAGES_PORTAL_URL` to the official portal and keep `PAGES_ORIGIN` exactly
`https://gasyoun.github.io`. Then run `npm ci && npm test` before `wrangler deploy`.
Verify `/health` reports `plan: free` and perform only a clearly synthetic test
against a test namespace/repository. If billing, identity, permissions, or secret
setup is unavailable, do not deploy: Pages local save plus aggregate download is
the documented fail-closed result.

## 17-11-2026 — the ghost Workers Builds project (`commentarystrategies`)

Every PR carries a standing red check **`Workers Builds: commentarystrategies`**
(fails in 0 s, project id `bbe7b1fb9232577e254c5e030d7781b2`, build example
`c3cfa61f…`). Diagnosed 17-11-2026 (MG directive «чинить внешний CF»); the repo
never declared that project — it is a dashboard-side ghost, not a deploy of this
Worker:

- The only wrangler config in ANY branch is this file's `wrangler.jsonc`, whose
  `name` is `commentarystrategies-review-api` — not `commentarystrategies`. A
  Workers Builds project refuses a config whose `name` differs from the project
  (and fails instantly when the configured root has no config at all); either
  case is the observed 0 s failure.
- The config still carries the provisioning placeholder
  `database_id: "SET_DURING_FREE_D1_PROVISIONING"` — so nothing was ever deployed
  through it; there is no D1 database, no migration run, no Worker secret, and
  the repo has zero Actions secrets and zero deploy workflow (`gh api
  …/actions/secrets` → `[]`, 17-11-2026). Repo-side `wrangler deploy --dry-run`
  builds green (16.11 KiB), so the code itself is fine.
- No Cloudflare API token or wrangler OAuth session exists on the agent box, so
  the dashboard build log is not reachable from the repo lane; the fix is one
  dashboard act (MG), two arms below.

**Arm A — disconnect the ghost (recommended; the Worker was never provisioned).**
Dashboard → Workers & Pages → `commentarystrategies` → Settings → Build →
disconnect the Git integration; then delete the empty service. The check
disappears from new PRs (old PRs keep their stale red until merged/closed).
Nothing in this repo needs to change.

**Arm B — make the review-api real (only if the D1 reviewer flow is wanted now).**
Dashboard: create the free D1 database `commentary-review-drafts`; take its real
UUID into `wrangler.jsonc` via a PR (replace ONLY the placeholder); add the seven
encrypted Worker secrets listed above; run `wrangler d1 migrations apply`; then
the manual `wrangler deploy` per this README. If Workers Builds is reconnected
afterwards, its project name must be `commentarystrategies-review-api` to match
the config.

Until either arm lands, treat the red as the ghost it is: the documented
fail-closed result (Pages local save + aggregate download) remains in force, and
the check does not reflect this repo's code.

_Dr. Mārcis Gasūns_
