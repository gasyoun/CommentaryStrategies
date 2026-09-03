#!/usr/bin/env python3
"""Executable-code scope matcher for the OxAlpha review gate (H3551 Wave 3).

Design: docs/OXALPHA_STATUS_GATE_DESIGN_2026.md §2 — a PR is IN SCOPE when its
changed files, minus exclusions, contain at least one executable path. Scope is
derivable and auditable here, not prose: docs-only and data-only PRs skip the
gate entirely.

Usage:
  python scripts/gate_needs_review.py --files pr_files.txt --json
  git diff --name-only origin/main... | python scripts/gate_needs_review.py --files - --json
  python scripts/gate_needs_review.py --selftest
"""
from __future__ import annotations

import argparse
import fnmatch
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

# Design §2 include set: executable code and its CI surfaces.
# Gate is REQUIRED on main since 03-09-2026 (ruling «required now») — a
# change to this table re-arms oxalpha-review on every open PR.
INCLUDE = [
    "scripts/**",
    "review-api/**",
    "js/**",
    "review-tests/**",
    "mahabharata-nilakantha/*.py",
    "mahabharata-nilakantha/**/*.py",
    ".github/workflows/**",
    "css/**",
]

# Design §2 exclusions: generated or vote artifacts (CI's reproducibility gate
# already covers regeneration), documentation, reports.
EXCLUDE = [
    "data/**",
    "docs/**",
    "tei/**",
    "pages/**",
    "reports/**",
    "votes/**",
    "*.md",
    ".ai_state.md",
    "changelog*",
]


def _match(path: str, patterns: list[str]) -> bool:
    """fnmatch on posix separators; '*' crosses '/' (so dir/** matches deep)."""
    posix = path.replace("\\", "/").lstrip("/")
    return any(fnmatch.fnmatch(posix, pat) for pat in patterns)


def in_scope(path: str) -> bool:
    return _match(path, INCLUDE) and not _match(path, EXCLUDE)


def classify(files: list[str]) -> dict:
    hits = sorted({f for f in files if f and in_scope(f)})
    return {
        "applies": bool(hits),
        "in_scope": hits,
        "in_scope_count": len(hits),
        "files_seen": len([f for f in files if f]),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--files", type=str, default=None,
                    help="file with one changed path per line ('-' = stdin)")
    ap.add_argument("--json", action="store_true", dest="as_json",
                    help="machine-readable output on stdout")
    ap.add_argument("--selftest", action="store_true",
                    help="assert classifier fixtures and exit")
    args = ap.parse_args()

    if args.selftest:
        fixtures = [
            ("scripts/validate.py", True),
            ("review-api/src/drafts.js", True),
            ("review-api/test/worker.test.js", True),
            ("review-api/README.md", False),
            ("js/review-sync.js", True),
            ("review-tests/tests/review-platform.spec.js", True),
            ("mahabharata-nilakantha/nilakantha_parser.py", True),
            ("mahabharata-nilakantha/notes.txt", False),
            (".github/workflows/oxalpha-gate.yml", True),
            ("css/apparatus-review.css", True),
            ("data/apparatus/sarga_01.json", False),
            ("docs/OXALPHA_STATUS_GATE_DESIGN_2026.md", False),
            ("reports/OXALPHA_30D_CODE_REVIEW_2026-08-26.md", False),
            ("votes/sarga.md", False),
            ("README.md", False),
            ("CHANGELOG.md", False),
            (".ai_state.md", False),
        ]
        failed = [p for p, want in fixtures if in_scope(p) != want]
        if failed:
            print(f"FAIL: misclassified: {failed}")
            return 1
        print(f"PASS: {len(fixtures)} classifier fixtures")
        return 0

    if args.files is None:
        ap.error("need --files FILE ('-' for stdin) or --selftest")
    if args.files == "-":
        raw = sys.stdin.read()
    else:
        with open(args.files, encoding="utf-8") as fh:
            raw = fh.read()
    files = raw.splitlines()
    result = classify(files)
    if args.as_json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"files seen: {result['files_seen']}; in scope: "
              f"{result['in_scope_count']}; gate applies: {result['applies']}")
        for hit in result["in_scope"]:
            print(f"  {hit}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
