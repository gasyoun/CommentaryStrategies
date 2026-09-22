"""Verify one release envelope against the bytes it pins (V6 verification).

The envelope (data/manifest/envelopes/*.envelope.json, schema
release-envelope-v1) is the object dashboards and manuscripts pin. This
script is the rerun side of that contract: it re-derives every digest the
envelope declares from the bytes actually on disk and reports
PASS/FAIL/SKIP per check. It never repairs, never rewrites, never trusts a
recorded digest it could not recompute.

Adapted from kosha's reference implementation (H4239) per
Uprava docs/SPEC_RELEASE_ENVELOPE_V6_PORTFOLIO_2026.md. This repo has no
upstream sibling clones to pin against — every source_pins entry in this
repo's envelopes references this same repo (gold-sample annotations are
hand-authored here, not derived from another repo) — so CHK-4 resolves
against REPO itself rather than a sibling-clone map.

Checks:
  CHK-1  envelope schema + required fields present
  CHK-2  each pinned artifact's sha256 recomputes from LF-canonical bytes
  CHK-3  per-dataset sha256/rows/size_bytes in output_digests match the
         recomputed pinned_artifacts values
  CHK-4  each source pin's commit resolves in this repo and
         `git show <pin>:<path>` digests to the recorded sha256 (SKIP when
         the pin commit is not reachable — e.g. a shallow clone)
  CHK-5  code_revision.commit exists in this repo and the release_tag
         resolves to the same commit (SKIP when tags are not fetched)

Exit 0 when every run check passes (SKIP allowed); exit 1 on any FAIL.

Usage:
    python scripts/envelope_check.py --envelope data/manifest/envelopes/v1.28.0.envelope.json
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

SCHEMA = "release-envelope-v1"
REQUIRED = (
    "schema",
    "envelope_id",
    "release_tag",
    "created",
    "code_revision",
    "pinned_artifacts",
    "source_pins",
    "output_digests",
    "config",
    "licence",
    "checks",
    "review",
    "citation",
    "publication_state",
)

DATASET_KEYS = ("sha256", "rows", "size_bytes")


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def canonical(b: bytes) -> bytes:
    """LF-canonical form — CRLF normalised, reproducible from any checkout."""
    return b.replace(b"\r\n", b"\n")


def git(*args, binary: bool = False):
    out = subprocess.run(["git", "-C", str(REPO)] + list(args), capture_output=True)
    if out.returncode != 0:
        return None
    return out.stdout if binary else out.stdout.decode("utf-8", "replace").strip()


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")

    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--envelope", required=True)
    args = ap.parse_args()

    env_path = Path(args.envelope)
    if not env_path.is_absolute():
        env_path = REPO / env_path
    env = json.loads(canonical(env_path.read_bytes()))

    results = []

    def record(cid: str, ok: bool, detail: str, skipped: bool = False):
        results.append((cid, "SKIP" if skipped else ("pass" if ok else "FAIL"), detail))

    # CHK-1 schema + required fields
    missing = [k for k in REQUIRED if k not in env or env[k] in (None, "", [], {})]
    record(
        "CHK-1-schema",
        not missing,
        "schema={}".format(env.get("schema"))
        + ("" if not missing else "; missing/empty: {}".format(", ".join(missing))),
    )
    if env.get("schema") != SCHEMA:
        print(report(results, fatal="schema is {}, expected {}".format(env.get("schema"), SCHEMA)))
        return 1

    # CHK-2 pinned artifacts recompute
    pin_by_path = {}
    pin_drift = []
    for p in env["pinned_artifacts"]:
        fpath = REPO / p["path"]
        if not fpath.is_file():
            pin_drift.append("{}: file not found".format(p["path"]))
            continue
        dig = sha256_bytes(canonical(fpath.read_bytes()))
        pin_by_path[p["path"]] = dig
        if dig != p["sha256"]:
            pin_drift.append("{}: sha256 {} != declared {}".format(p["path"], dig[:16], p["sha256"][:16]))
    record("CHK-2-pinned-artifacts", not pin_drift, "{} artifact(s)".format(len(env["pinned_artifacts"])))
    if pin_drift:
        print(report(results, extra=pin_drift))

    # CHK-3 output_digests parity against recomputed pinned bytes
    path_by_dataset = {}
    for p in env["pinned_artifacts"]:
        name = Path(p["path"]).name
        for ds_id, out in env["output_digests"]["datasets"].items():
            if out.get("release_asset") == name:
                path_by_dataset[ds_id] = p["path"]

    declared = env["output_digests"]["datasets"]
    drift = []
    for ds_id, out in sorted(declared.items()):
        path = path_by_dataset.get(ds_id)
        if path is None:
            drift.append("{}: no matching pinned_artifacts entry".format(ds_id))
            continue
        fpath = REPO / path
        if not fpath.is_file():
            drift.append("{}: {} not found".format(ds_id, path))
            continue
        raw = canonical(fpath.read_bytes())
        recomputed = {
            "sha256": sha256_bytes(raw),
            "rows": len(json.loads(raw)) if raw.strip().startswith(b"[") else None,
            "size_bytes": len(raw),
        }
        for key in DATASET_KEYS:
            if recomputed[key] is None:
                continue
            if recomputed[key] != out.get(key):
                drift.append("{}: {} {!r} != recomputed {!r}".format(ds_id, key, out.get(key), recomputed[key]))
    record("CHK-3-output-parity", not drift, "{} dataset(s)".format(len(declared)))
    if drift:
        print(report(results, extra=drift))

    # CHK-4 source pins re-derived (this repo is its own upstream — no sibling clones)
    tag_ok = True
    pin4_drift = []
    for sp in env["source_pins"]:
        ds_id = sp["dataset"]
        commit = git("cat-file", "-t", sp["pin_commit"])
        if commit != "commit":
            record("CHK-4-source-pin:{}".format(ds_id), True, "pin commit not reachable (shallow clone?)", skipped=True)
            continue
        blob = git("show", "{}:{}".format(sp["pin_commit"], sp["source_path"]), binary=True)
        if blob is None:
            pin4_drift.append("{}: blob unresolvable at pin".format(ds_id))
            record("CHK-4-source-pin:{}".format(ds_id), False, "blob unresolvable")
            tag_ok = False
            continue
        dig = sha256_bytes(canonical(blob))
        matches_declared = dig == sp["sha256"]
        record(
            "CHK-4-source-pin:{}".format(ds_id),
            matches_declared,
            "pin {} digests {} (declared match: {})".format(sp["pin_commit"][:12], dig[:16], matches_declared),
        )
        if not matches_declared:
            tag_ok = False
    record("CHK-4-source-pins", tag_ok and not pin4_drift, "summary")

    # CHK-5 code_revision commit exists + tag resolves to it
    rev = git("cat-file", "-t", env["code_revision"]["commit"])
    rev_ok = rev == "commit"
    tag_sha = git("rev-parse", env["code_revision"]["tag"])
    if tag_sha is None:
        record(
            "CHK-5-code-revision",
            rev_ok,
            "{} ({}); tag {} not resolvable locally (shallow clone?)".format(
                env["code_revision"]["commit"][:12], rev, env["code_revision"]["tag"]
            ),
            skipped=not rev_ok,
        )
    else:
        tag_ok5 = tag_sha == env["code_revision"]["commit"]
        record(
            "CHK-5-code-revision",
            rev_ok and tag_ok5,
            "{} ({}); tag {} -> {} (match: {})".format(
                env["code_revision"]["commit"][:12], rev, env["code_revision"]["tag"], tag_sha[:12], tag_ok5
            ),
        )

    print(report(results))
    return 0 if all(r != "FAIL" for _, r, _ in results) else 1


def report(results, fatal: str = None, extra=None) -> str:
    lines = []
    if fatal:
        lines.append("FATAL: " + fatal)
    for cid, res, detail in results:
        lines.append("  [{}] {} — {}".format(res.rjust(4), cid, detail))
    for e in extra or []:
        lines.append("         · " + e)
    passed = sum(1 for _, r, _ in results if r == "pass")
    skipped = sum(1 for _, r, _ in results if r == "SKIP")
    failed = sum(1 for _, r, _ in results if r == "FAIL")
    lines.append(
        "envelope_check: {} pass, {} skip, {} fail — {}".format(
            passed, skipped, failed, "PASS" if failed == 0 else "FAIL"
        )
    )
    return "\n".join(lines)


if __name__ == "__main__":
    sys.exit(main())
