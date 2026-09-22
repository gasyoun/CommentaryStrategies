"""Every destructive applier the suite claims to cover is actually invoked.

Guards the H4351 fail condition «an applier counted as covered whose test
never actually invokes it»: each name in DESTRUCTIVE_APPLIERS must appear as a
``.run(<name>…)`` target (via the SCRIPT constant) in some tests/test_*.py, the
script must exist under scripts/, and a fixture tree must exist for it.
"""
import re
from pathlib import Path

import pytest

from conftest import DESTRUCTIVE_APPLIERS, FIXTURES, SCRIPTS

TESTS = Path(__file__).resolve().parent


def _modules_invoking(name: str) -> list:
    hits = []
    for p in sorted(TESTS.glob("test_*.py")):
        if p.name == Path(__file__).name:
            continue
        src = p.read_text(encoding="utf-8")
        if re.search(r'SCRIPT\s*=\s*"' + re.escape(name) + '"', src) and ".run(SCRIPT" in src:
            hits.append(p.name)
    return hits


@pytest.mark.parametrize("name", DESTRUCTIVE_APPLIERS)
def test_applier_is_invoked_and_staged(name):
    assert (SCRIPTS / name).is_file(), f"scripts/{name} missing"
    assert (FIXTURES / name[:-3]).is_dir(), f"no fixture tree for {name}"
    assert _modules_invoking(name), f"no test module runs {name}"


def test_fixtures_never_point_at_live_data():
    """Fixture JSON may name data/… paths only as *relative* strings; no
    absolute checkout path, no Windows drive."""
    bad = []
    for p in FIXTURES.rglob("*.json*"):
        txt = p.read_text(encoding="utf-8")
        if "Users/user/Documents/GitHub" in txt or "/Users/mac/" in txt:
            bad.append(str(p))
    assert not bad
