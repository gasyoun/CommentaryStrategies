#!/usr/bin/env python3
"""OxAlpha review gate — status machinery (H3551, design §3/§6 step 3).

The gate is a REQUIRED commit-status context `oxalpha-review` on `main`.
Two actors write it:

  * CI / sweep — `ensure`: sets `pending` on in-scope PR heads (review owed)
    or `success` on docs/data-only heads (gate skip, scope-evidenced).
  * An OxAlpha SESSION after an independent Standards+Spec review pass —
    `verdict`: the only writer of terminal states.

Status states (never a silent pass — design §3):
    pass    -> success   (evidence-backed; --evidence URL is mandatory)
    fail    -> failure   (>=1 P0/P1 finding with location+failure mode+repro)
    neutral -> error     (infra unavailable; BLOCKS merge until retried)

`main` is PR-only under this gate: direct pushes are rejected by branch
protection because the required status never ran on them.

Usage:
  python scripts/oxalpha_gate.py status  --pr 216
  python scripts/oxalpha_gate.py ensure  --pr 216
  python scripts/oxalpha_gate.py verdict --pr 216 --verdict pass \
      --evidence https://github.com/.../reviews/... --note "2-axis pass, no P0/P1"
  python scripts/oxalpha_gate.py sweep          # all open PRs, idempotent
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

CONTEXT = "oxalpha-review"
HERE = __file__
STATES = {"pass": "success", "fail": "failure", "neutral": "error"}


def gh(*args: str, data: str | None = None) -> str:
    out = subprocess.run(
        ["gh", "api", *args],
        capture_output=True,
        text=True,
        input=data,
        check=False,
    )
    if out.returncode != 0:
        sys.exit(f"ERROR: gh api {' '.join(args[:2])}: {out.stderr.strip()}")
    return out.stdout


def repo() -> str:
    out = subprocess.run(
        [
            "gh",
            "repo",
            "view",
            "--json",
            "owner,name",
            "--jq",
            '.owner.login + "/" + .name',
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    if out.returncode != 0:
        sys.exit(f"ERROR: gh repo view: {out.stderr.strip()}")
    return out.stdout.strip()


def head_sha(r: str, pr: int) -> str:
    return gh(f"repos/{r}/pulls/{pr}", "--jq", ".head.sha").strip()


def current(r: str, sha: str) -> dict | None:
    raw = gh(
        f"repos/{r}/commits/{sha}/status",
        "--jq",
        f'[.statuses[] | select(.context == "{CONTEXT}")][0]',
    )
    doc = json.loads(raw) if raw.strip() else None
    return doc or None


def post(
    r: str, sha: str, state: str, description: str, target_url: str | None
) -> None:
    body: dict = {"state": state, "context": CONTEXT, "description": description[:140]}
    if target_url:
        body["target_url"] = target_url
    gh("-X", "POST", f"repos/{r}/statuses/{sha}", "--input", "-", data=json.dumps(body))
    print(f"SET {CONTEXT}={state} on {sha[:12]}: {description}")


def scope_files(r: str, pr: int) -> list[str]:
    raw = gh(
        f"repos/{r}/pulls/{pr}/files?per_page=100", "--paginate", "--jq", ".[].filename"
    )
    return raw.splitlines()


def classify(r: str, pr: int) -> dict:
    here = __import__("os").path.dirname(__import__("os").path.abspath(HERE))
    sys.path.insert(0, here)
    from gate_needs_review import classify

    return classify(scope_files(r, pr))


def ensure(r: str, pr: int, dry: bool = False) -> str:
    sha = head_sha(r, pr)
    have = current(r, sha)
    if have:
        print(f"PR #{pr}: {CONTEXT} already {have['state']} on {sha[:12]} — keep")
        return have["state"]
    scope = classify(r, pr)
    if scope["applies"]:
        state = "pending"
        desc = (
            f"review owed: {scope['in_scope_count']} executable file(s) — "
            f"an OxAlpha session must run the 2-axis pass and record a verdict"
        )
    else:
        state = "success"
        desc = (
            f"gate skip: {scope['files_seen']} changed, 0 executable (docs/data-only)"
        )
    print(
        f"PR #{pr} {sha[:12]}: {scope['in_scope_count']}/"
        f"{scope['files_seen']} in scope -> {state}"
    )
    if not dry:
        post(r, sha, state, desc, f"https://github.com/{r}/pull/{pr}")
    return state


def verdict(
    r: str, pr: int, verdict: str, evidence: str, note: str, dry: bool = False
) -> None:
    sha = head_sha(r, pr)
    have = current(r, sha)
    if have and have["state"] in ("success", "failure", "error"):
        sys.exit(
            f"ERROR: {CONTEXT} is already terminal "
            f"({have['state']}) on {sha[:12]}; push a new commit to "
            f"re-open review"
        )
    desc = f"OxAlpha verdict: {verdict}" + (f" — {note}" if note else "")
    if not dry:
        post(r, sha, STATES[verdict], desc, evidence)
    else:
        print(f"DRY: would set {STATES[verdict]} with {desc} -> {evidence}")


def sweep(r: str, dry: bool = False) -> None:
    raw = gh(
        f"repos/{r}/pulls?state=open&per_page=50", "--paginate", "--jq", ".[].number"
    )
    for num in [int(n) for n in raw.split()]:
        try:
            ensure(r, num, dry=dry)
        except SystemExit as exc:
            print(f"PR #{num}: ensure failed — {exc}")


def wait(r: str, pr: int, timeout_sec: int, poll_sec: int = 20) -> int:
    """Mirror loop for the required Actions check run (job `oxalpha-review`).

    GitHub's required-check policy matches check RUNS from the Actions app —
    a bare commit status alone does not satisfy it. This job therefore polls
    the authoritative commit status (written only by `ensure`/`verdict`) and
    mirrors it as its own conclusion:

      status success          -> exit 0 (check green; merge allowed)
      status failure / error  -> exit 1 fast (verdict fail / infra-neutral)
      status pending / absent -> poll until timeout, then exit 1 (blocked —
                                 never a silent pass)
    """
    import time

    deadline = time.monotonic() + timeout_sec
    sha = head_sha(r, pr)
    while time.monotonic() < deadline:
        have = current(r, sha)
        if have:
            desc = have.get("description", "")
            if have["state"] == "success":
                print(f"gate PASS: {desc}")
                return 0
            if have["state"] in ("failure", "error"):
                print(f"gate FAIL ({have['state']}): {desc}")
                return 1
            print(f"waiting on verdict… ({desc})")
        else:
            print("status not armed yet…")
        time.sleep(poll_sec)
    print(
        f"TIMEOUT after {timeout_sec}s: oxalpha-review never reached success "
        f"— merge stays blocked; re-run this job after the session verdict lands"
    )
    return 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument(
        "cmd", choices=["status", "ensure", "verdict", "sweep", "wait"]
    )
    ap.add_argument("--pr", type=int, default=None)
    ap.add_argument("--timeout-sec", type=int, default=2100,
                    help="wait subcommand: poll budget (default 2100s)")
    ap.add_argument("--verdict", choices=sorted(STATES), default=None)
    ap.add_argument(
        "--evidence",
        default=None,
        help="URL of the evidence (report/comment) — mandatory for verdict",
    )
    ap.add_argument("--note", default="")
    ap.add_argument("--repo", default=None, help="override owner/name")
    ap.add_argument("--dry", action="store_true")
    args = ap.parse_args()
    r = args.repo or repo()

    if args.cmd == "status":
        if not args.pr:
            ap.error("--pr required")
        sha = head_sha(r, args.pr)
        print(
            json.dumps(
                {"sha": sha, "gate": current(r, sha)}, ensure_ascii=False, indent=2
            )
        )
    elif args.cmd == "ensure":
        if not args.pr:
            ap.error("--pr required")
        ensure(r, args.pr, dry=args.dry)
    elif args.cmd == "verdict":
        if not (args.pr and args.verdict and args.evidence):
            ap.error("--pr, --verdict and --evidence are all required")
        verdict(r, args.pr, args.verdict, args.evidence, args.note, dry=args.dry)
    elif args.cmd == "sweep":
        sweep(r, dry=args.dry)
    elif args.cmd == "wait":
        if not args.pr:
            ap.error("--pr required")
        raise SystemExit(wait(r, args.pr, args.timeout_sec))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
