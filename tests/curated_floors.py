"""Curated-record floors for the destructive appliers (H4351, 08-09-2026).

Kept in a module with NO third-party imports so that
``scripts/curated_floors_check.py`` can load it in the `corpus` CI job,
where pytest is not installed; ``tests/conftest.py`` re-exports it.
"""

# Curated record counts read ONCE from the live files at authoring time
# (08-09-2026, Fable 5.1 claude-fable-5-1) and frozen here as literals. They are
# the documented non-shrink floor per target file; the tests themselves assert
# the invariant on fixtures and never open the live files; the literals are
# enforced against the live files by scripts/curated_floors_check.py, which the
# `corpus` CI job runs on every push (--print re-derives them for re-pinning).
CURATED_FLOORS_2026_09_08 = {
    "data/apparatus/gate_ledger.json:entries": 126,
    "data/lexical/ch1.json:cards": 58,
    "data/lexical/ch2.json:cards": 16,
    "data/lexical/ch3.json:cards": 13,
    "data/analysis/phase2_pilot/pilot_candidates.json:notes": 16,
    "data/analysis/phase2_pilot/sarga_35_candidates.json:notes": 6,
    "data/sundara_ch35_commentary_to_add.json:notes": 6,
    "data/sundara_ch36_commentary_to_add.json:notes": 6,
    "data/sundara_ch37_commentary_to_add.json:notes": 4,
    "data/sundara_commentary_to_add.json:notes": 896,
    "data/sundara_commentary_to_add.json:type_В": 155,
    "data/sundara_commentary_to_add.json:cross_text": 170,
    "data/sundara_decision_ledger.json:entries": 5507,
    "data/analysis/translit_residue_cards.json:cards": 45,
    "data/crosstext/kavya.json:notes": 18,   # records, not the stale _meta.notes_count (12)
    "data/crosstext/gita.json:notes": 24,
    # -- wave 2 (H4368, 08-09-2026, Opus 5 claude-opus-5): the curated files the
    # eight re-runnable writers own that were not already pinned above.
    "data/lexical/ch11.json:cards": 3,        # after the H276 anchor fix (-7 parked, -2 moved)
    "data/lexical/ch11.qa_removed.json:cards": 7,   # the parked cards ARE the record of the fix
    "data/lexical/ch17.json:cards": 9,        # +1 re-anchored kṣāma @ V.17.30
    "data/lexical/ch25.json:cards": 6,        # +1 re-anchored vivarṇa @ V.25.8
    "data/sundara_ch1_commentary_to_add.json:notes": 30,  # the seed sundara_ch2_68_pipeline.py reads
}
