# Eval harness note (H6846)

_Created: 26-10-2026_

`evals/` now carries the repo's first eval suite, `apparatus-gate-locus`, a
deterministic canary over the human assembly gate:

- suite manifest: [`evals/manifest.json`](../evals/manifest.json)
- runner: [`evals/run_eval.py`](../evals/run_eval.py) (`--canary` proves the
  grader goes red on a mutated locus)
- gold: [`data/apparatus/gate_ledger.json`](../data/apparatus/gate_ledger.json)
  — existing committed human verdicts, not new annotation.

Scope is deliberately narrow: the suite guards gate-overlay integrity, not the
philological quality of individual notes. A future capability suite over the
same data would need a separately pre-registered reference solution and
negative class (H6714 eval contract).

CI: [`.github/workflows/eval-canary.yml`](../.github/workflows/eval-canary.yml)
runs the canary on PRs and pushes that touch `evals/` or `data/apparatus/`.

_Dr. Mārcis Gasūns_
