"""build_sarga_apparatus.py — the per-sarga ballot over all five note layers.

Target files: data/apparatus/sarga_{NN}.json + .html — regenerated from
scratch on every run, which is exactly the shape where a source that silently
stops loading erases curated cards from the reviewer's ballot. The five source
layers are pinned in tests/curated_floors.py.
"""
from conftest import Stage

SCRIPT = "build_sarga_apparatus.py"
BOOK = "data/sundara_commentary_to_add.json"
SEG = "data/analysis/sundara_commentary_segmented.json"
CH35 = "data/lexical/ch35.json"
KAVYA = "data/crosstext/kavya.json"
JSON_OUT = "data/apparatus/sarga_35.json"
HTML_OUT = "data/apparatus/sarga_35.html"
TARGETS = (JSON_OUT, HTML_OUT)


def staged(stage: Stage) -> Stage:
    stage.fixture("build_sarga_apparatus")
    stage.script(SCRIPT)
    stage.script("gate_ledger.py")
    stage.script("apparatus_notes.py")
    return stage


def all_notes(doc) -> list:
    return [n for v in doc["verses"] for n in v["notes"]]


def test_idempotent_rerun_is_byte_identical(stage):
    s = staged(stage)
    r1 = s.run(SCRIPT, "35")
    assert "sarga 35: 4/4 verses with notes" in r1.stdout
    snap1 = s.snapshot(*TARGETS)
    s.run(SCRIPT, "35")
    assert s.snapshot(*TARGETS) == snap1


def test_non_shrink_every_source_card_reaches_the_ballot(stage):
    s = staged(stage)
    s.run(SCRIPT, "35")
    doc = s.load(JSON_OUT)
    notes = all_notes(doc)

    by_layer = doc["_meta"]["notes_by_layer"]
    assert by_layer == {"tier1": 1, "lexical": 4, "phase2": 1,
                        "edition": 2, "crosstext": 1}
    assert len(notes) == sum(by_layer.values()) == 9, \
        "one ballot card per source record — the rebuild drops nothing"
    assert len({n["id"] for n in notes}) == len(notes), "note ids are unique"

    lex = {n["lemma_iast"] for n in notes if n["layer"] == "lexical"}
    assert lex == {"vadana", "vīkṣā", "guṇasampad", "śokaparāyaṇa"}, \
        "aggregate ∪ ch-file, deduped on (shloka, lemma_iast)"
    assert not any(n["layer"] == "lexical" and n.get("subtype") == "commentator"
                   for n in notes), "commentator notes belong to the phase2 layer"

    # sarga 36 is not built when only 35 is asked for
    assert not s.path("data/apparatus/sarga_36.json").exists()
    assert all(v["verse_id"].startswith("5.35.") for v in doc["verses"])


def test_gate_verdicts_and_tier1_segmentation_survive_the_rebuild(stage):
    s = staged(stage)
    s.run(SCRIPT, "35")
    notes = all_notes(s.load(JSON_OUT))
    by_id = {n["id"]: n for n in notes}

    gated = by_id["lexical:5.35.1:0"]
    assert gated["status"] == "правлено"
    assert gated["note_ru"] == "Вадана — лицо (правка Леонова)."
    assert gated["gate_verdicts"]["Леонов"]["action"] == "edit"
    assert gated["votable"] is False, "a neutral build is read-only"

    tier1 = by_id["tier1:5.35.1:0"]
    assert tier1["votable"] is False
    assert "[Е. Костина]" not in tier1["note_ru"], \
        "the editor's service reminder is lifted out of the printable prose"
    assert tier1["service"], "…and kept, not dropped"

    # a tier-1 note on the same verse flags the collision on the votable cards
    assert "collision_tier1" not in gated, "a card nobody may vote on is not flagged"
    assert by_id["lexical:5.35.1:1"]["votable"] is True
    assert by_id["lexical:5.35.1:1"]["collision_tier1"] is True

    edition = by_id["edition:5.35.3:0"]
    assert edition["scope"] == "несколько шлок подряд"
    assert "(3 шлок)" not in edition["note_ru"], "Russian numeral agreement is applied"

    ct = by_id["crosstext:5.35.4:0"]
    assert ct["cluster"] == "kavya" and ct["cluster_label"].startswith("кавья")

    html = s.path(HTML_OUT).read_text(encoding="utf-8")
    assert "Гунасампад" in html, "the ballot payload is embedded in the page"
    assert "/*DATA*/null" not in html, "the placeholder is replaced by the ballot data"


def test_truncated_book_aggregate_is_refused_without_a_ballot(stage):
    s = staged(stage)
    s.truncate(BOOK)
    r = s.run(SCRIPT, "35", expect=None)
    assert r.returncode != 0
    assert not s.path(JSON_OUT).exists() and not s.path(HTML_OUT).exists()


def test_truncated_crosstext_cluster_is_refused_without_a_ballot(stage):
    s = staged(stage)
    s.truncate(KAVYA)
    r = s.run(SCRIPT, "35", expect=None)
    assert r.returncode != 0
    assert not s.path(JSON_OUT).exists()


def test_truncated_source_never_overwrites_an_existing_ballot(stage):
    """The failure mode the floors exist for: a rebuild off a broken source
    must not replace yesterday's ballot with a thinner one."""
    s = staged(stage)
    s.run(SCRIPT, "35")
    snap = s.snapshot(*TARGETS)
    s.truncate(SEG)
    r = s.run(SCRIPT, "35", expect=None)
    assert r.returncode != 0
    s.assert_unchanged(snap)


def test_a_ch_file_card_that_vanishes_shrinks_the_ballot(stage):
    """Non-shrink stated as the negative: dropping one curated ch-file card
    costs exactly one ballot card — the count is load-bearing, not decorative."""
    s = staged(stage)
    s.run(SCRIPT, "35")
    full = s.load(JSON_OUT)["_meta"]["notes_by_layer"]["lexical"]

    doc = s.load(CH35)
    s.write_json(CH35, [doc[0]] + [n for n in doc[1:]
                                   if n["lemma_iast"] != "śokaparāyaṇa"])
    s.run(SCRIPT, "35")
    assert s.load(JSON_OUT)["_meta"]["notes_by_layer"]["lexical"] == full - 1
