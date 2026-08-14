# CommentaryStrategies review platform — execution plan, 2026 Q3

_Created: 14-08-2026 · Last updated: 14-08-2026_

## Goal

Make CommentaryStrategies easier to operate correctly while unblocking the
Sundarakāṇḍa book: publish one official GitHub Pages review portal with all 68
Kostina ballots, durable local and server autosave, an aggregate download, and
an authenticated submission path that preserves Leonov's votes and routes
editorial disagreements explicitly. In the same 90-day program, encode a
conservative automation policy and bring the repository's roadmap, state, and
operator documentation back into agreement with the v1.17.1 reality.

## Plan layers

- [Roadmap — 90-day waves](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/ROADMAP_CommentaryStrategies_2026Q3.md)
- [Architecture — boundaries, contracts, and reuse verdicts](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/ARCHITECTURE_CommentaryStrategies_review-platform.md)
- [Implementation — ordered Wave-1 build](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/IMPLEMENTATION_CommentaryStrategies_review-platform.md)
- [Verification — acceptance criteria, risks, and spikes](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/VERIFICATION_CommentaryStrategies_review-platform.md)
- [Metadoc — provenance and improvement ledger](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/PLAN_CommentaryStrategies_review-platform_2026Q3.meta.md)

## Audit verdict

**PARTIAL — build only the gap.** The canonical apparatus generator, 68 neutral
per-sarga pages, schema-v2 dual-reviewer ledger, importer, agreement report,
reviewer-scoped sarga-1 Kostina ballot, corpus validator, and GitHub Pages site
already exist. They must be extended, not replaced. The missing pieces are the
68-ballot reviewer build, a discoverable portal, shared client code, durable
draft/submit transport, strict raw-submission validation, a compact disagreement
queue, a statistical automation policy, and synchronized control-plane docs.

Prior art consulted:

- [Current architecture](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/ARCHITECTURE.md)
- [Sundarakāṇḍa operator manual](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/MANUAL.md)
- [Existing commentary roadmap](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/COMMENTARY_ROADMAP.md)
- [Schema-v2 integrity issue](https://github.com/gasyoun/CommentaryStrategies/issues/160)
- [Kostina's open editorial issue](https://github.com/gasyoun/CommentaryStrategies/issues/57)
- [Leonov's vote issue](https://github.com/gasyoun/CommentaryStrategies/issues/58)
- [Existing live Kostina sarga-1 ballot](https://gasyoun.github.io/CommentaryStrategies/data/apparatus/sarga_01_kostina.html)

## Decisions taken

The rightmost column preserves the user's ruling verbatim; interpretation fixes
the executable meaning without silently widening it.

| # | Decision | Executable interpretation | Verbatim ruling |
|---:|---|---|---|
| 1 | Priority | Coherence, Sundarakāṇḍa delivery, and corpus reliability form one program, in that order. | `1 a + b +c` |
| 2 | Scope | Diagnose repository-wide; Wave 1 is Sundarakāṇḍa-centered. | `2 a + b` |
| 3 | Definition of better | Make correct operation easier through one current control plane and explicit gates. | `3 a` |
| 4 | Horizon | Plan for 90 days. | `4 a` |
| 5 | Human gates | Preserve necessary gates, improve autonomous areas, and replace defensible item-level gates with measured agent adjudication. | `5 a + improve fully autonomous areas + Replace as many human gates as defensibly possible with agent adjudication.` |
| 6 | Known state | Treat Leonov's existing votes as immutable evidence; the Kostina delivery surface is the immediate gap. | `Leonov has voted, but there is no github.io link for Kostina to vote` |
| 7 | Reviewer surface | One landing page covers the full review. | `1 a` |
| 8 | Rollout | Publish all 68 Kostina ballots immediately. | `2 b` |
| 9 | Automation | Use risk-tiered automation. | `3 a` |
| 10 | Disagreement | Dual acceptance passes; veto or disagreement enters an evidence-backed queue. | `4 a` |
| 11 | Vote return | Provide both one aggregate JSON and direct hosted submission. | `5 a + d` |
| 12 | Pages role | GitHub Pages becomes the official reviewer/researcher interface. | `6 a` |
| 13 | Submission target | GitHub remains the repository-facing submission path. | `1 c` |
| 14 | Authentication intent | Authentication must be reviewer-friendly; this was superseded by decision 19 after the security follow-up. | `2 a` |
| 15 | Saving | Local autosave plus backend autosave, with explicit final submit. | `3 a` |
| 16 | Canonicalization | Immutable raw submission, then validated import into the dual-reviewer ledger. | `4 a` |
| 17 | Frontend | Shared vanilla JavaScript/CSS; no framework migration. | `5 a` |
| 18 | Automation policy | Encode policy and thresholds in versioned data. | `6 a` |
| 19 | Auth transport | GitHub authentication is mediated; no secret is placed in Pages. | `1 b`, later superseded by the security follow-up below |
| 20 | Verification | Publication-grade end-to-end acceptance. | `2 a` |
| 21 | Statistical bar | Deterministic invariants or a preregistered class whose lower 95% confidence bound is at least 0.95. | `3 a` |
| 22 | Ambiguity | Park the affected item, log evidence, and continue. | `4 a` |
| 23 | Authority and fence | Executor may commit, push, PR, merge, and deploy after gates; never create real votes/contact reviewers; protect tier 1, articles, four axes, Leonov votes, rights, and secrets. | `5 a` and `6 a` |

### Security follow-up ruling

The audit found that a static Pages client cannot safely hold the GitHub OAuth
secret needed for a normal web flow. The user therefore chose a minimal
Cloudflare Worker mediator **only if it remains free of cost**: `a - if free of
cost`.

This condition is satisfied for the expected two-reviewer workload by the
current official free allowances: [Workers Free permits 100,000 requests/day](https://developers.cloudflare.com/workers/platform/pricing/)
and [D1 Free includes 5 million rows read/day, 100,000 rows written/day, and 5 GB total storage](https://developers.cloudflare.com/d1/platform/pricing/).
The build must select the Free plan, configure fail-closed limits, and stop
before any paid-plan activation. If the free allowances or terms change before
deployment, direct hosted submission is parked and aggregate JSON remains the
working fallback.

## Autonomy contract

### On ambiguity

Park only the affected item, record the evidence and reason, and continue with
independent work. Never improvise a scholarly or editorial ruling. A changed
external pricing/security premise uses the marked fallback rather than silently
accepting cost or weakening authentication.

### Stop conditions

Stop the affected deployment or import on any of the following:

- a secret would need to enter Git, Pages, browser storage, logs, or a ballot;
- Cloudflare requires a paid plan or payment activation;
- any existing Leonov verdict changes, disappears, or is reattributed;
- schema/source hashes do not match and a safe park is impossible;
- raw submissions would be mutable or canonical ledger writes would originate
  from the browser;
- corpus validation, ledger self-tests, browser tests, or required CI fail;
- the change crosses the do-not-touch fence.

Ordinary per-item ambiguity is not a global stop: park it and continue.

### Commit, publication, and deployment authority

The Wave-1 executor may create a branch/worktree, commit, push, open and merge a
PR after all required checks pass, publish all 68 Pages ballots, and deploy the
free-tier mediator. It may create only synthetic/mocked verification
submissions. It must not insert real Kostina votes, alter Leonov votes, contact
either reviewer, or send the invitation link.

### Do-not-touch fence

Do not change tier-1 scholarly text, article content, the four-axis analytical
framework, existing Leonov verdicts, rights rulings, or secrets. Ledger changes
are limited to tested schema-v2-compatible validation/import operations.
Generated reviewer artifacts may expose only already-public repository content;
no unpublished personal data may be added.

### Default when reality diverges

Use the documented conservative fallback: local autosave plus aggregate JSON,
with the affected hosted feature parked. Never replace the chosen provider,
lower the statistical bar, broaden token permissions, or add a paid service
without a new human ruling.

## Wave-1 launch instruction

The execution handoff must begin literally with:

```text
Read C:\Users\user\Documents\GitHub\CommentaryStrategies\docs\PLAN_CommentaryStrategies_review-platform_2026Q3.md and execute it.
```

_Dr. Mārcis Gasūns_
