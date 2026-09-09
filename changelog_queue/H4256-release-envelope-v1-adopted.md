_Created: 09-09-2026 · Last updated: 09-09-2026_

# H4256 — release-envelope-v1 adopted for v1.28.0 (portfolio-wide adoption, OxAlpha)

### Added

- **[`data/manifest/envelopes/v1.28.0.envelope.json`](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/manifest/envelopes/v1.28.0.envelope.json)** —
  this repo's first `release-envelope-v1` object per Uprava
  [docs/SPEC_RELEASE_ENVELOPE_V6_PORTFOLIO_2026.md](https://github.com/gasyoun/Uprava/blob/main/docs/SPEC_RELEASE_ENVELOPE_V6_PORTFOLIO_2026.md)
  (kosha `data-v0.5.0` pilot, H4239, is the reference implementation). Pins the six
  gold-sample annotation files (`data/{erman,grintser,kalyanov,leonov,syrkin,vassilkov}_markup_50.json`,
  300 annotations total) by sha256 at the `v1.28.0` tag commit
  (`0ce386f79fbbfceebe2e0e1bc05bd9359044260f`), with source/output digests, code revision,
  licence (Apache-2.0), and the review provenance of `scripts/validate.py` (6159 files, PASS)
  and `scripts/derive_urn.py --check` (300/300 resolved, PASS), both rerun at authoring time.
- **[`scripts/envelope_check.py`](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/envelope_check.py)** —
  the rerun-side checker, adapted from kosha's stdlib-only reference implementation. Unlike
  kosha (which pins upstream sibling repos), every `source_pins` entry here resolves against
  this same repo — the gold sample is hand-authored in-house, not derived from another repo —
  so CHK-4 re-derives against `REPO` directly instead of a sibling-clone map. **11/11 PASS**
  on real bytes; a tampered-digest negative control correctly exits 1 (verified, not shipped).

### Deviation from the handoff's release_kind hint

H4256's mission line suggested `release_kind=paper/manuscript`. This repo's own
[`CITATION.cff`](https://github.com/gasyoun/CommentaryStrategies/blob/main/CITATION.cff) and
[`.zenodo.json`](https://github.com/gasyoun/CommentaryStrategies/blob/main/.zenodo.json) both
declare `type`/`upload_type: dataset` for the `v1.28.0` release, so the envelope's
`release_kind` is set to `data` instead — matching the artifact actually being pinned rather
than the generic hint.

### Honest gaps recorded in the envelope, not glossed over

- **`citation.concept_doi` / `version_doi`: `null`.** No Zenodo DOI has been minted yet —
  [README.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/README.md) already
  states the deposit is pending manual action by the repo owner
  ([docs/ZENODO_DEPOSIT.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/ZENODO_DEPOSIT.md)).
- **`publication_state.state: "draft"`, not `"published"`.** `v1.28.0` is a public git tag with
  matching `CITATION.cff`/`.zenodo.json` version fields, but `gh release view v1.28.0` returns
  "release not found" — no GitHub Release object exists for it yet.

### Additive only

Canonical stores untouched — `data/*_markup_50.json` are pinned by digest, not modified. One
release envelope, one repo, no batch adoption (H4239's cross-repo-adoption fence).

_Dr. Mārcis Gasūns_
