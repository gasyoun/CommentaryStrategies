# CommentaryStrategies reviewer platform — architecture

_Created: 14-08-2026 · Last updated: 14-08-2026_

Decisions: [PLAN](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/PLAN_CommentaryStrategies_review-platform_2026Q3.md).
Delivery waves: [ROADMAP](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/ROADMAP_CommentaryStrategies_2026Q3.md).
Build order: [IMPLEMENTATION](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/IMPLEMENTATION_CommentaryStrategies_review-platform.md).
Acceptance: [VERIFICATION](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/VERIFICATION_CommentaryStrategies_review-platform.md).

## Architectural intent

Add a thin reviewer and submission layer around the existing apparatus pipeline.
JSON and the schema-v2 ledger remain canonical; GitHub Pages is the public read/
review surface; Cloudflare holds only drafts and OAuth/session material; GitHub
stores immutable final submissions and reviewed canonical changes.

```text
existing five-source JSON + schema-v2 ledger
                 |
                 v
       deterministic Python generators
                 |
      manifest + 68 scoped ballots
                 |
                 v
     GitHub Pages reviewer portal
        |                    |
        | localStorage       | HTTPS
        v                    v
 aggregate JSON       Cloudflare Worker (Free)
 fallback              | OAuth exchange
                       | D1 draft autosave
                       | explicit submit
                       v
                GitHub raw-submission PR
                       |
             validate, then trusted import
                       |
                       v
          schema-v2 dual-reviewer ledger
                       |
             agreement/disagreement queue
```

## Component boundaries

### 1. Existing corpus and apparatus core — retained

- `data/` remains the structured source of truth.
- `scripts/build_sarga_apparatus.py` retains five-source merge logic and
  reviewer-specific rendering inputs.
- `data/apparatus/gate_ledger.json` remains the canonical final-gate overlay.
- `scripts/gate_ledger.py` retains schema v2, with verdicts keyed by reviewer.
- Tier 1 stays display-only and can never acquire vote controls.

No reviewer UI may mutate these files directly.

### 2. Deterministic reviewer build

A portal generator emits:

- one manifest with data revision, schema version, sargas 1–68, note counts,
  source hashes, and URLs;
- one Kostina-scoped ballot per sarga, built from the existing normalized data;
- one official landing page with aggregate progress and recovery controls;
- shared JavaScript/CSS rather than 68 independent inline implementations.

Generated assets must reproduce byte-for-byte from committed inputs.

### 3. Browser client

The vanilla-JS client owns presentation and draft interaction only:

- reviewer-scoped `localStorage` provides immediate/offline resume;
- a shared manifest supports cross-sarga progress and one aggregate export;
- sync states are explicit: local, syncing, synced, offline, conflict, submitted;
- tokens are held only in memory/session scope and are never committed or
  included in exports;
- all content is escaped; repository text is treated as untrusted for DOM use;
- aggregate JSON download works even when authentication/backend is unavailable.

### 4. Cloudflare mediation layer — Free plan only

The Worker performs the operations a static Pages site cannot perform safely:

- OAuth code exchange with GitHub; client secret lives only in Cloudflare
  secrets;
- session verification and reviewer allow-list enforcement;
- D1-backed versioned draft autosave;
- final payload validation sufficient to reject malformed transport;
- creation of an immutable raw-submission branch/PR through the GitHub API.

D1 is a draft/transport store, not the scholarly source of truth. The service
must run on the [Workers Free allowance](https://developers.cloudflare.com/workers/platform/pricing/)
and [D1 Free allowance](https://developers.cloudflare.com/d1/platform/pricing/).
No billing upgrade is authorized. Limit exhaustion degrades to local save plus
download; it must never lose local work.

### 5. Immutable raw submissions

Final submission writes a new content-addressed path such as:

`votes/submissions/kostina/<UTC>-<sha256>.json`

Contracts:

- create-only; a repeated identical submit is idempotent;
- payload identifies reviewer, source revision, manifest hash, schema, sargas,
  decisions, and client timestamp;
- browser/Worker cannot write the ledger;
- CI validates raw evidence before any trusted importer runs;
- corrections produce a new raw submission, never rewrite history.

### 6. Trusted validation and import

The importer runs locally or in a reviewed GitHub workflow after raw validation.
It validates all independent content before one write, preserves every existing
Leonov verdict, and parks stale/unknown/ambiguous items. Reviewer identity is
derived from authenticated submission metadata and cross-checked with the
payload; it is not accepted from a CLI flag alone.

### 7. Editorial outcome and disagreement

Verdicts remain independent evidence. Derived outcome rules are:

- accept + accept: eligible for inclusion;
- reject + reject: exclude;
- any accept/reject, accept/edit, reject/edit, or materially different edit text:
  editorial queue;
- any reject is a veto against automatic inclusion until resolved;
- missing second vote is pending, not agreement;
- agents may summarize evidence but never silently choose the winner.

### 8. Automation policy

`data/apparatus/adjudication_policy.json` is versioned, validated policy data.
Each class declares stable ID/definition, evidence, data revision, risk,
permitted action, sample size, successes, confidence method/lower bound, and
invariant tests.

- Deterministic transforms: `auto_apply` only when every declared invariant
  passes.
- Agent-derived classes: `auto_apply` only when preregistered and the lower 95%
  confidence bound on a blind sample is at least 0.95.
- Changed definitions, missing evidence, disagreement, scholarly interpretation,
  uncertain anchors, or edits: park or human escalation.

## Data contracts

### Reviewer manifest

Required fields: `schema_version`, `reviewer`, `repo_revision`, `generated_at`,
`source_hash`, and exactly 68 unique sarga entries containing URL, note count,
ballot hash, and source hash.

### Draft record

Keyed by reviewer + manifest revision + sarga. Holds decisions, monotonic version,
updated timestamp, and hash. Optimistic concurrency rejects stale writes and
returns both versions for client-side recovery; it never overwrites silently.

### Aggregate submission

Contains all selected sarga decisions, source hashes, reviewer identity, schema,
and one stable content hash. It contains no tokens, secrets, email addresses, or
unpublished personal metadata.

### Ledger

The existing shape remains authoritative:

```json
{
  "entries": {
    "<note-id>": {
      "verdicts": {
        "Леонов": {"action": "accept"},
        "Костина": {"action": "edit", "edited_note": "..."}
      }
    }
  }
}
```

No flattening to one `reviewer` field is permitted.

## Security and privacy boundaries

- OAuth/GitHub secrets exist only as encrypted Cloudflare secrets.
- D1 draft rows are accessible only to the authenticated reviewer and operator.
- Allowed origin is the exact GitHub Pages origin; state/PKCE, CSRF protection,
  short-lived sessions, strict CORS, rate limiting, and audit logging are required.
- Browser code receives only the minimum session capability; no repository-wide
  token is persisted client-side.
- Content Security Policy and output escaping protect repository text rendering.
- Synthetic accounts/fixtures are used in verification; tests never submit real
  votes.
- Free-tier hard limits and alarms prevent cost escalation.

## Build-versus-reuse verdicts

| Concern | Verdict | Canonical source / gap |
|---|---|---|
| Five-source apparatus merge | Reuse | Existing `scripts/build_sarga_apparatus.py`; add shared rendering/build-all mode only. |
| Dual-reviewer storage | Reuse | Existing schema-v2 `scripts/gate_ledger.py`; do not invent another ledger. |
| Existing Leonov votes | Preserve | Existing `data/apparatus/gate_ledger.json`; hash-regression invariant. |
| Per-sarga application | Extend | Existing `scripts/apply_apparatus_decisions.py`; add aggregate validated path and preserve compatibility. |
| Agreement reporting | Extend | Existing `scripts/gate_reviewer_agreement.py`; add content-sensitive disagreement queue. |
| Reviewer portal | New gap | No official index/progress/recovery surface exists. |
| Kostina ballots 2–68 | New generated gap | Only sarga 1 is reviewer-scoped today. |
| Local persistence/export | Reuse and centralize | Existing ballot localStorage/download logic; extract shared client. |
| Auth/draft transport | New thin service | Static Pages cannot safely store OAuth secret or durable private drafts. |
| Canonical final storage | Reuse | GitHub raw PR + reviewed import; D1 is not canonical. |
| Agent adjudication evidence | Extend | Reuse H1685 evidence/IAA conventions; add frozen policy and confidence gate. |

## Deployment topology

- Public UI: existing `https://gasyoun.github.io/CommentaryStrategies/` Pages
  deployment from `main`.
- API: one Cloudflare Worker on the Free plan.
- Draft store: one D1 Free database with indexed reviewer/revision/sarga keys.
- Final evidence: GitHub PR containing only immutable raw submission.
- Canonical result: reviewed merge/import into schema-v2 ledger.

If Cloudflare ceases to be free or cannot meet security acceptance, API and
remote autosave stay undeployed; Pages + local autosave + aggregate download
remain fully functional.

## Non-functional requirements

- Keyboard and mobile operability; visible focus and announced sync status.
- No vote loss across refresh, offline edits, conflicts, or failed submission.
- Deterministic generated artifacts.
- Fail-closed import and automation policy.
- Idempotent submit/import.
- Full provenance without secrets or unpublished personal data.

_Dr. Mārcis Gasūns_
