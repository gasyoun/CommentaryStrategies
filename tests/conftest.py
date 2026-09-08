"""Test harness for the destructive appliers (H4351, 08-09-2026).

Every applier under test is copied into a throw-away tree (tmp_path/scripts +
tmp_path/data + tmp_path/votes …) and executed there as a REAL subprocess with
``cwd`` set to that tree. Both path conventions the scripts use therefore land
inside the sandbox:

* ``__file__``-relative (``REPO = dirname(dirname(__file__))``) — the copy under
  tmp_path/scripts resolves REPO to tmp_path;
* cwd-relative (``data/lexical/ch1.json``) — cwd is tmp_path.

Two scripts hard-code a Windows checkout path; ``Stage.script`` rewrites exactly
that one assignment line to the sandbox (and fails loudly if the line moved, so
the rewrite can never silently point at the wrong place).

No test reads or writes under the real ``data/``: fixtures live under
``tests/fixtures/appliers/<applier>/`` as miniature copies of the real column
shapes, and the sandbox root is asserted to be outside the checkout.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))

REPO = Path(__file__).resolve().parents[1]
SCRIPTS = REPO / "scripts"
FIXTURES = Path(__file__).resolve().parent / "fixtures" / "appliers"

# The ten destructive appliers this suite covers (rank-2 row of Uprava
# reports/TEST_GAP_CENSUS_ORGWIDE_08-09-2026.md). test_coverage_manifest.py
# asserts each one is actually invoked by some test.
DESTRUCTIVE_APPLIERS = (
    "apply_apparatus_decisions.py",
    "apply_grintser_pass.py",
    "apply_grintser_pass_ch1.py",
    "apply_phase2_decisions.py",
    "apply_translit_decisions.py",
    "backfill_grintser_crossrefs.py",
    "backfill_why_proposed.py",
    "merge_new_crosstext.py",
    "merge_phase2_pilot.py",
    "rebuild_crosstext.py",
)

# Curated record floors live in tests/curated_floors.py (pytest-free, so the
# `corpus` CI job can import it without pytest); re-exported here for tests.
from curated_floors import CURATED_FLOORS_2026_09_08  # noqa: E402,F401

# Exact source lines that pin a Windows checkout; rewritten per sandbox.
HARDCODED_LINES = {
    "backfill_grintser_crossrefs.py": (
        "S='C:/Users/user/Documents/GitHub/SamudraManthanam/web/corpus_builder/jsonl/'",
        "S={jsonl!r}",
    ),
    "merge_new_crosstext.py": (
        'CS_DIR  = Path(r"C:\\Users\\user\\Documents\\GitHub\\CommentaryStrategies")',
        "CS_DIR  = Path({root!r})",
    ),
}


class Stage:
    """A sandboxed copy of ``scripts/<applier>`` plus fixture data."""

    def __init__(self, root: Path):
        assert REPO not in root.resolve().parents and root.resolve() != REPO, (
            "sandbox must live outside the checkout")
        self.root = root
        self.data = root / "data"
        self.scripts = root / "scripts"
        self.scripts.mkdir(parents=True, exist_ok=True)
        self.data.mkdir(parents=True, exist_ok=True)

    # -- staging -----------------------------------------------------------
    def script(self, name: str, **fmt) -> Path:
        """Copy scripts/<name> into the sandbox, rewriting a hard-coded path."""
        src = (SCRIPTS / name).read_text(encoding="utf-8")
        if name in HARDCODED_LINES:
            old, new = HARDCODED_LINES[name]
            assert old in src, (f"{name}: expected hard-coded line not found — "
                                f"update HARDCODED_LINES in conftest")
            src = src.replace(old, new.format(**fmt))
        dst = self.scripts / name
        dst.write_text(src, encoding="utf-8")
        return dst

    def fixture(self, applier: str) -> "Stage":
        """Copy tests/fixtures/appliers/<applier>/ over the sandbox root."""
        srcdir = FIXTURES / applier
        assert srcdir.is_dir(), f"no fixture tree for {applier}"
        shutil.copytree(srcdir, self.root, dirs_exist_ok=True)
        return self

    # -- execution ---------------------------------------------------------
    def run(self, name: str, *args: str, expect: int | None = 0,
            ) -> subprocess.CompletedProcess:
        env = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONDONTWRITEBYTECODE="1")
        proc = subprocess.run(
            [sys.executable, str(self.scripts / name), *args],
            cwd=self.root, capture_output=True, text=True, encoding="utf-8",
            env=env, timeout=120)
        if expect is not None:
            assert proc.returncode == expect, (
                f"{name} {' '.join(args)} exit {proc.returncode} != {expect}\n"
                f"--- stdout ---\n{proc.stdout}\n--- stderr ---\n{proc.stderr}")
        return proc

    # -- files -------------------------------------------------------------
    def path(self, rel: str) -> Path:
        return self.root / rel

    def read(self, rel: str) -> bytes:
        return self.path(rel).read_bytes()

    def load(self, rel: str):
        return json.loads(self.path(rel).read_text(encoding="utf-8"))

    def write_json(self, rel: str, obj) -> None:
        p = self.path(rel)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n",
                     encoding="utf-8")

    def truncate(self, rel: str, keep: float = 0.6) -> None:
        """Cut a file mid-stream, the shape of an interrupted export."""
        raw = self.read(rel)
        self.path(rel).write_bytes(raw[: max(1, int(len(raw) * keep))])

    def snapshot(self, *rels: str) -> dict:
        return {r: (self.read(r) if self.path(r).exists() else None) for r in rels}

    def assert_unchanged(self, snap: dict) -> None:
        for rel, before in snap.items():
            after = self.read(rel) if self.path(rel).exists() else None
            assert after == before, f"{rel} was modified by a run that must not write"


@pytest.fixture
def stage(tmp_path: Path) -> Stage:
    return Stage(tmp_path / "sandbox")


def records(doc) -> list:
    """Data records of a CommentaryStrategies note list (drops the _meta head)."""
    return [x for x in doc if isinstance(x, dict) and "_meta" not in x]
