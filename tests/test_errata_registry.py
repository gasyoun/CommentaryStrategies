# tests/test_errata_registry.py — G86 (H5778): the guard for errata.yml.
# The registry park was "CommentaryStrategies errata.yml has no guarding test
# — grep-only / create-not-gate". The register now exists (seeded from the
# v1.15.1 CHANGELOG erratum) and this test enforces its schema, uniqueness,
# and cross-source consistency with the CHANGELOG entry the erratum corrects.
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
ERRATA = yaml.safe_load((ROOT / "errata.yml").read_text(encoding="utf-8"))
CHANGELOG = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

REQUIRED = {
    "id", "date", "version", "published_in", "where",
    "was", "now", "totals_unchanged", "evidence",
}


def _entries():
    entries = ERRATA.get("errata")
    assert isinstance(entries, list) and entries, "errata.yml lost its errata[]"
    return entries


def test_schema_every_entry_complete():
    for e in _entries():
        missing = REQUIRED - set(e)
        assert not missing, f"{e.get('id')}: missing fields {sorted(missing)}"
        assert re.fullmatch(r"ERR-\d{4}-\d{2}-\d{2}-\d{2}", e["id"]), e["id"]
        assert re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(e["date"])), e["date"]
        assert e["evidence"].startswith("https://github.com/"), e["evidence"]
        assert "data/analysis" in e["evidence"], (
            "evidence must point at the data file that arbitrates the figures")


def test_ids_unique():
    ids = [e["id"] for e in _entries()]
    assert len(ids) == len(set(ids)), f"duplicate errata ids: {ids}"


def test_entries_sorted_newest_first():
    dates = [str(e["date"]) for e in _entries()]
    assert dates == sorted(dates, reverse=True), (
        f"errata not sorted newest-first: {dates}")


def test_seeded_erratum_matches_changelog_v1151():
    # cross-source pin: the register's corrected shares must be the same
    # figures the v1.15.1 CHANGELOG entry prints (16/8 and 18/6, totals
    # unchanged 29/58/87) — a drift on either side fails here
    entry = next(e for e in _entries() if e["id"] == "ERR-2026-07-28-01")
    assert "16 / 8" in entry["now"]
    assert "18 / 6" in entry["now"]
    assert "V.11.12|rājīvanetri" in entry["now"]
    assert "29 починено, 58 отказано, 87 всего" in entry["totals_unchanged"]
    for fragment in ("16 / 8", "18 / 6", "29 починено, 58 отказано, 87 всего"):
        assert fragment in CHANGELOG, (
            f"CHANGELOG lost the erratum figure {fragment!r} — the v1.15.1 "
            "entry and errata.yml must stay in agreement")
