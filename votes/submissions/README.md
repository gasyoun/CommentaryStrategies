_Created: 14-08-2026 · Last updated: 05-09-2026_

# Immutable reviewer submissions

Final reviewer payloads are raw evidence. Store each accepted payload at
`votes/submissions/<reviewer>/<UTC>-<sha256>.json` in a create-only pull request.
Never edit or replace an existing path; a correction is a new submission.

The browser and review API may create only this raw PR. They cannot write
`data/apparatus/gate_ledger.json`. CI validates the submission schema, identity,
manifest/source hashes, decision IDs, required edit/reject text, and content hash
before a trusted operator runs the importer.

No real reviewer submission is committed by automated tests. Fixtures live under
`tests/fixtures/` and use the synthetic reviewer identity explicitly allowed by
the validator's `--allow-synthetic` test mode.

_Dr. Mārcis Gasūns_
