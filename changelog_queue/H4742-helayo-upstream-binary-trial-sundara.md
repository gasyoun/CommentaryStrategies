_Created: 15-09-2026 · Last updated: 15-09-2026_

# H4742 — upstream `helayo` binary trialled on Sundarakāṇḍa witnesses (first real run)

### Added

- **`scripts/trial_helayo_upstream.py`** — runs the REAL upstream `helayo`
  (chchch/sanskrit-alignment `dist/macOS-latest` binary, commit `ed643c3`) over a
  deterministic 30-verse critical↔southern sample (19 spike pairs of sargas 3/6 + 11
  seeded extras stratified by difflib similarity, seed 42), in both `-l aksara` and
  `-l character` modes, writing FASTT inputs, TEI alignment XML and
  `data/analysis/helayo_upstream_trial/trial_results.json`. The 12-07-2026 spike
  (`scripts/spike_helayo_align.py`) reimplemented the *method* and explicitly never ran
  the upstream binary — H4742 closes exactly that gap.
- **`docs/TRIAL_HELAYO_UPSTREAM_SUNDARA_2026.md`** — trial report: round-trip canary
  60/60 PASS (both witnesses, both modes), 108 word-level apparatus loci (aksara), the
  spike's showcase loci reproduce exactly from the untouched upstream tool
  (`supuṣṭabalasaṃguptāṃ|sampuṣṭāṃ`, `vaidūryatala|kṛta`, `ketumāla|kapimukhya`);
  known failure mode confined to reworded verses (sim ≲ 0.7, word-grouped readings
  fragment while columns stay correct); upstream default matrix weaker than the spike's
  near-equivalence matrix. Adopt decision unchanged → H776 (human); the "never actually
  ran it" risk is retired.
- Trial artifacts committed: `data/analysis/helayo_upstream_trial/` (30 FASTT + 60 TEI XML + results
  JSON = 91 data files). The foreign binary itself is NOT committed — re-fetch per upstream provenance.

### Unchanged

- Spike script/docs, `compare_editions.py`, `sa_align.py`, `build_edition_footnotes.py`,
  all apparatus data — nothing rewired; H776 owns the adopt call.

_Dr. Mārcis Gasūns_
