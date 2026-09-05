_Created: 14-08-2026 · Last updated: 05-09-2026_

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

_Dr. Mārcis Gasūns_
