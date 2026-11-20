# CommentaryStrategies eval harness

_Created: 26-10-2026 · H6846 (eval-harness scaffold rollout)_

Minimal, deterministic eval scaffold over data this repo already treats as gold.
It creates no new gold and adds no annotation.

## Suite `apparatus-gate-locus`

Grades the human final-assembly gate overlay (`data/apparatus/gate_ledger.json`)
against the per-sarga apparatus files it was applied to:

- every verdict key `layer:verse_id:index` resolves to a real note in `data/apparatus/sarga_NN.json`;
- the entry's `layer` and `verse_id` agree with the key and the resolved note;
- `lemma_iast` agrees with the note when both are present;
- every reviewer action is one of `accept` / `reject`.

The gold is the committed 126-entry ledger from the R1/R3 gate
(H141/H2829/H2830, last applied 2026-07-11). Nothing is generated.

## Run

```sh
python evals/run_eval.py            # gold replay
python evals/run_eval.py --canary   # gold passes AND a mutated ledger fails
```

`--canary` re-points one verdict at a nonexistent verse (`5.99.99`) and requires
the grader to reject it. Exit code 0 means the gold replay passed (and, with
`--canary`, the mutation was caught).

The same command runs on PRs touching `evals/` or `data/apparatus/` via
`.github/workflows/eval-canary.yml`.

_Dr. Mārcis Gasūns_
