#!/usr/bin/env python
"""Tamper proof for the CommentaryStrategies <- SamudraManthanam edge contract.

SHARED_CODE s24 rule: every vendored-asset drift contract ships proof it fails
loud — flipping ONE byte of the pinned upstream must make
`corpus_truth_census.py --check` exit 1, even when the note count is unchanged.

Method: hardlink-copy the sibling jsonl dir into a temp dir (no data copy),
byte-patch one pinned work file (a byte flip inside an html attribute keeps
every count identical), run the checker with CORPUS_JSONL_DIR pointed at the
copy, and require exit 1 + the s24 message. Control run against the untouched
hardlink copy must stay exit 0. The real sibling is never written.

Polite skip (exit 0, one note) when the sibling corpus is absent — same
contract as the census itself.
"""
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

REPO = Path(__file__).resolve().parents[1]
CENSUS = REPO / "scripts" / "corpus_truth_census.py"
REAL = Path(os.environ.get(
    "CORPUS_JSONL_DIR",
    str(REPO.parent / "SamudraManthanam" / "web" / "corpus_builder" / "jsonl")))


def hardlink_dir(src: Path, dst: Path):
    dst.mkdir(parents=True)
    for f in src.iterdir():
        if f.is_file():
            os.link(f, dst / f.name)


def run_check(env_dir: str):
    env = dict(os.environ, CORPUS_JSONL_DIR=env_dir)
    return subprocess.run([sys.executable, str(CENSUS), "--check"],
                          capture_output=True, encoding='utf-8', env=env)


def main():
    if not REAL.is_dir():
        print(f"SKIP: sibling corpus absent at {REAL} — tamper proof needs it (same contract as the census).")
        return 0
    doc_reconciliation = REPO / "data" / "analysis" / "corpus_truth_reconciliation.json"
    import json
    works = json.load(open(doc_reconciliation, encoding='utf-8'))["works"]
    victim = works[0]["slug"]

    with tempfile.TemporaryDirectory() as td:
        clean = Path(td) / "clean"
        patched = Path(td) / "patched"
        hardlink_dir(REAL, clean)
        hardlink_dir(REAL, patched)

        # control: untouched copy must pass
        r = run_check(str(clean))
        if r.returncode != 0:
            print("FAIL: control run against an untouched hardlink copy did not pass:\n" + r.stdout[-2000:])
            return 1

        # tamper: flip one ASCII byte inside the pinned file (count must stay equal)
        target = patched / f"{victim}.jsonl"
        raw = bytearray(target.read_bytes())
        flipped = False
        for i, b in enumerate(raw):
            if 0x41 <= b <= 0x5A:            # 'A'-'Z' inside markup/attributes
                raw[i] = b ^ 0x20            # case flip — no JSON structure touched
                flipped = True
                break
        if not flipped:
            print("FAIL: no flippable byte found in the victim file")
            return 1
        # HARDLINK SAFETY (realized 04-09-2026, H4075): write_bytes on a hardlink
        # truncates the SHARED inode — the real sibling was byte-flipped through it
        # once. Unlink first so the patched copy gets a fresh inode.
        os.unlink(target)
        target.write_bytes(bytes(raw))

        r = run_check(str(patched))
        out = r.stdout
        if r.returncode != 1:
            print(f"FAIL: tampered corpus did NOT fail loud (exit {r.returncode}):\n" + out[-2000:])
            return 1
        if "upstream moved — rebuild and re-commit" not in out:
            print("FAIL: exit 1 but the s24 message is missing:\n" + out[-2000:])
            return 1
        if f"{victim}: upstream moved" not in out:
            print("FAIL: s24 message does not name the tampered work:\n" + out[-2000:])
            return 1

    print(f"tamper proof OK: 1-byte flip in {victim}.jsonl -> --check exit 1 with the s24 message; control copy passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
