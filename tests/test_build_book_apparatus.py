"""build_book_apparatus.py — the camera-ready ЛП print master (H268 WS-D).

Target files: data/book/sundarakanda_print_master.md and
data/book/BOOK_BUILD_REPORT.md — a full rewrite from the HTML translation
source plus the two note tiers. The invariant this guards: nothing loses its
gate status and no note silently drops out of the endnote apparatus.

Curated floor at authoring: data/sundara_commentary_to_add.json = 896 notes
(tests/curated_floors.py). Its other curated input, data/leonov_own_notes.json,
is unpinned — see .ai_state.md § H4368. The staged sa_align.py resolves its
optional `sanskrit-util` sibling relative to the sandbox, which has none, so
these tests exercise its stdlib `canon()` fallback.
"""
import re

from conftest import Stage

SCRIPT = "build_book_apparatus.py"
BOOK = "data/sundara_commentary_to_add.json"
T1 = "data/leonov_own_notes.json"
SRC = "ramayana-leonov/Рамаяна. Книга 5. Сундараканда 2026.html"
MASTER = "data/book/sundarakanda_print_master.md"
REPORT = "data/book/BOOK_BUILD_REPORT.md"
TARGETS = (MASTER, REPORT)


def staged(stage: Stage) -> Stage:
    stage.fixture("build_book_apparatus")
    stage.script(SCRIPT)
    stage.script("sa_align.py")
    return stage


def text(s: Stage, rel: str) -> str:
    return s.path(rel).read_text(encoding="utf-8")


def test_idempotent_rerun_is_byte_identical(stage):
    s = staged(stage)
    r1 = s.run(SCRIPT)
    assert "translation verses: 3/0; sargas: 2" in r1.stdout
    assert "t1 notes 2, kostina marks 1, t2 notes 5 (MG-gated 1)" in r1.stdout
    snap1 = s.snapshot(*TARGETS)
    assert all(snap1.values()), "every target was actually written"
    s.run(SCRIPT)
    assert s.snapshot(*TARGETS) == snap1


def test_non_shrink_every_note_of_both_tiers_reaches_the_master(stage):
    s = staged(stage)
    s.run(SCRIPT)
    master = text(s, MASTER)

    # tier 1 verbatim, service markers flagged rather than dropped
    assert "Сын ветра — Хануман, сын Ваю." in master
    assert "Комм.[Claude.AI — желательно] ? [кат.5 — текстология]" in master
    assert "⟦содержит рабочие пометы — к сборке⟧" in master

    # tier 2: every note of the aggregate, each with its gate status
    assert "*vadana* — Вадана — лицо. ⟨ярус 2 · лексический⟩ ⟦гейт М.Г. ✓" in master
    assert "*vākya* — Тилака поясняет" in master and "⟦ожидает гейта⟧" in master
    assert "*laṅkā* — Ср. «Махабхарата» III.266" in master
    # a gate-pending batch candidate is slotted with its batch and judge verdict
    assert "⟦ожидает гейта М.Г. (phase2_batch3, судья: keep)⟧" in master
    assert "Широмани отмечает форму аориста" in master
    # …and the judge-rejected one never enters the print path
    assert "Отклонённый судьёй кандидат" not in master
    # an un-judged batch-2 candidate is included — the gate, not the judge, decides
    assert "⟦ожидает гейта М.Г. (phase2_batch2)⟧" in master
    assert "Кандидат батча 2 без вердикта судьи" in master

    # Kostina's marks are a separate stratum, not reader endnotes
    assert "# Приложение А." in master, "the service-stratum appendix heading"
    body, appendix = master.split("# Приложение А.", 1)
    assert "Опущено сравнение" not in body
    assert "Опущено сравнение — вернуть по критическому изданию." in appendix

    # the translation body carries every verse of the HTML source
    assert "## Песнь 35" in master and "## Песнь 36" in master
    assert "**1.** Тогда она взглянула в лицо" in master
    assert "**1.** И увидел он город Ланку." in master

    # counts, not label prose: an editorial re-wording of a report line must not
    # red a test that is really about how many notes reached the apparatus
    report = text(s, REPORT)
    assert re.search(r"\*\*3 строф\*\* в 2 песнях", report)
    assert re.search(r"Примечания яруса 1[^\n]*: \*\*2\*\*", report)
    assert re.search(r"Пометы Костиной[^\n]*: \*\*1\*\*", report)
    assert re.search(r"Ноты яруса 2 в мастере: \*\*5\*\*[^\n]*гейтированы М\.Г\.: 1", report)


def test_a_verse_with_no_note_carries_no_endnote_marker(stage):
    s = staged(stage)
    s.run(SCRIPT)
    master = text(s, MASTER)
    assert "**1.** Тогда она взглянула в лицо  \nсына ветра.[^35-1]" in master, \
        "line breaks survive as Markdown hard breaks; the marker follows the verse"
    assert "**2.** Хануман молвил слово.[^35-2]" in master


def test_truncated_aggregate_is_refused_without_a_master(stage):
    s = staged(stage)
    s.truncate(BOOK)
    r = s.run(SCRIPT, expect=None)
    assert r.returncode != 0
    assert not s.path(MASTER).exists() and not s.path(REPORT).exists()


def test_truncated_tier1_notes_are_refused_without_a_master(stage):
    s = staged(stage)
    s.truncate(T1)
    r = s.run(SCRIPT, expect=None)
    assert r.returncode != 0
    assert not s.path(MASTER).exists()


def test_a_broken_source_never_overwrites_the_previous_master(stage):
    s = staged(stage)
    s.run(SCRIPT)
    snap = s.snapshot(*TARGETS)
    s.path(SRC).unlink()
    r = s.run(SCRIPT, expect=None)
    assert r.returncode != 0
    s.assert_unchanged(snap)
