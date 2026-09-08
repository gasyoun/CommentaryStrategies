"""sundara_ch2_68_pipeline.py — generate ch.2–68 and re-aggregate the book.

Target files: data/sundara_ch{N}_commentary_to_add.json for every chapter, plus
the two curated aggregates data/sundara_commentary_to_add.json (floor 896 notes)
and data/sundara_book_stats.json. The ch.1 notes are NOT regenerated here — they
are read from data/sundara_ch1_commentary_to_add.json and carried into the
aggregate, which is precisely the curated slice a bad rerun can erase.

The script pins two Windows checkout paths; conftest rewrites both into the
sandbox (HARDCODED_LINES).
"""
from conftest import Stage, records

SCRIPT = "sundara_ch2_68_pipeline.py"
CH1 = "data/sundara_ch1_commentary_to_add.json"
CH2 = "data/sundara_ch2_commentary_to_add.json"
CH3 = "data/sundara_ch3_commentary_to_add.json"
BOOK = "data/sundara_commentary_to_add.json"
STATS = "data/sundara_book_stats.json"
TARGETS = (CH2, CH3, BOOK, STATS)


def staged(stage: Stage) -> Stage:
    stage.fixture("sundara_ch2_68_pipeline")
    stage.script(SCRIPT, root=str(stage.root), jsonl=str(stage.root / "corpus"))
    return stage


def test_idempotent_rerun_is_byte_identical(stage):
    s = staged(stage)
    r1 = s.run(SCRIPT)
    assert "Seeded 2 lemmas from ch.1" in r1.stdout
    assert "ch.2: 5 notes / 2 verses" in r1.stdout
    assert "ch.3: 1 notes / 1 verses" in r1.stdout
    snap1 = s.snapshot(*TARGETS)
    s.run(SCRIPT)
    assert s.snapshot(*TARGETS) == snap1


def test_non_shrink_the_ch1_slice_survives_the_re_aggregation(stage):
    s = staged(stage)
    ch1_before = records(s.load(CH1))
    s.run(SCRIPT)

    book = records(s.load(BOOK))
    keys = {(n["shloka"], n["lemma_iast"]) for n in book}
    assert {(n["shloka"], n["lemma_iast"]) for n in ch1_before} <= keys, \
        "every ch.1 note must survive into the rebuilt aggregate"
    for b in ch1_before:
        assert b in book, "ch.1 notes are carried verbatim, not re-derived"
    assert len(book) == len(ch1_before) + len(records(s.load(CH2))) \
        + len(records(s.load(CH3))) == 8
    assert s.path(CH1).read_bytes() == s.read(CH1), "the ch.1 seed file is read-only"

    # book-wide first-appearance dedup: a lemma noted in ch.1 never re-fires
    lemmas = [n["lemma_iast"] for n in book]
    assert lemmas.count("cāraṇa") == 1
    assert all(n["review_required"] is True for n in book)
    assert book == sorted(book, key=lambda n: (int(n["shloka"].split(".")[1]),
                                               int(n["shloka"].split(".")[2])))


def test_generated_notes_and_stats_agree_with_the_aggregate(stage):
    s = staged(stage)
    s.run(SCRIPT)

    ch2 = records(s.load(CH2))
    by_lemma = {n["lemma_iast"]: n for n in ch2}
    assert set(by_lemma) == {"kapivara", "mahābala", "bala", "hanūmān", "rāghava"}
    assert by_lemma["kapivara"]["trigger"] == "epithet"
    assert by_lemma["kapivara"]["note_ru"].endswith("Первое вхождение в кн. V.")
    # rāghava was already noted in ch.1, so ch.2 can only produce its omission note
    om = by_lemma["rāghava"]
    assert om["trigger"] == "omission" and om["priority"] == "low"
    assert om["src_candidate_id"] == "auto/sundara/2.2.om"
    assert s.load(CH2)[0]["_meta"]["notes_count"] == len(ch2) == 5
    assert s.load(CH2)[0]["_meta"]["verses_total"] == 2

    # a chapter with no corpus verses still gets its file, with zero notes
    ch9 = s.load("data/sundara_ch9_commentary_to_add.json")
    assert records(ch9) == [] and ch9[0]["_meta"]["verses_total"] == 0

    book = s.load(BOOK)
    bm = book[0]["_meta"]
    stats = s.load(STATS)
    assert bm["total_notes"] == stats["total_notes"] == len(records(book))
    assert bm["per_chapter_notes"]["1"] == 2, "the ch.1 slice is counted, not recomputed"
    assert stats["per_chapter_notes"]["1"] == 2
    assert bm["chapter_verse_counts"]["1"] == 213
    assert bm["per_chapter_notes"]["2"] == len(ch2)
    assert bm["verses_without_note"] == bm["total_verses"] - bm["verses_with_note"]


def test_truncated_ch1_seed_is_refused_without_any_write(stage):
    s = staged(stage)
    s.truncate(CH1)
    r = s.run(SCRIPT, expect=None)
    assert r.returncode != 0
    for rel in TARGETS:
        assert not s.path(rel).exists(), f"{rel} must not be written"


def test_truncated_ch1_seed_never_overwrites_a_previous_aggregate(stage):
    s = staged(stage)
    s.run(SCRIPT)
    snap = s.snapshot(*TARGETS)
    s.truncate(CH1)
    r = s.run(SCRIPT, expect=None)
    assert r.returncode != 0
    s.assert_unchanged(snap)


def test_an_unreadable_corpus_shrinks_the_aggregate_silently(stage):
    """Characterisation, not approval — the shape scripts/curated_floors_check.py
    exists to catch. load_jsonl() swallows every corpus read error and only warns,
    so a run with the corpus gone still exits 0 and writes an aggregate holding
    the ch.1 slice alone. Nothing in the script refuses it; the live-file floor
    is the only thing standing between that run and a silent curated loss."""
    s = staged(stage)
    s.run(SCRIPT)
    full = len(records(s.load(BOOK)))

    s.path("corpus/05_ramayana-sundarakanda.jsonl").unlink()
    r = s.run(SCRIPT)
    assert "WARN" in r.stderr
    shrunk = records(s.load(BOOK))
    assert len(shrunk) == 2 < full, "the ch.2–68 slice is gone, exit code still 0"
    assert {n["lemma_iast"] for n in shrunk} == {"cāraṇa", "rāghava"}
