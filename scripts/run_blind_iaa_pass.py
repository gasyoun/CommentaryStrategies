"""run_blind_iaa_pass.py — drive annotate_batch for H1469 Pass B.

Loads DEEPSEEK_API_KEY from .env (or env), sets OpenAI-compatible route, runs
all six translators (or --only). Resumable via annotate_batch itself.

Usage:
    python scripts/run_blind_iaa_pass.py
    python scripts/run_blind_iaa_pass.py --only vassilkov,erman
"""
from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
TRANSLATORS = ["kalyanov", "vassilkov", "erman", "grintser", "syrkin", "leonov"]


def load_dotenv() -> None:
    env_path = ROOT / ".env"
    if not env_path.exists():
        return
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        k, v = k.strip(), v.strip().strip('"').strip("'")
        if k and k not in os.environ:
            os.environ[k] = v


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="", help="Comma-separated translator slugs")
    ap.add_argument("--limit", type=int, default=50)
    ap.add_argument("--sleep", type=float, default=0.3)
    ap.add_argument("--skip-existing", action="store_true",
                    help="Skip translator if data/{tr}_full.json already has 50 notes")
    args = ap.parse_args()

    load_dotenv()
    key = os.environ.get("DEEPSEEK_API_KEY") or os.environ.get("LLM_API_KEY")
    if not key:
        print("ERROR: set DEEPSEEK_API_KEY or LLM_API_KEY")
        return 2

    os.environ["LLM_API_KEY"] = key
    os.environ["LLM_BASE_URL"] = os.environ.get("LLM_BASE_URL") or "https://api.deepseek.com"
    os.environ["LLM_MODEL"] = os.environ.get("LLM_MODEL") or "deepseek-v4-flash"
    os.environ["LLM_BACKEND"] = "openai"

    targets = [t.strip() for t in args.only.split(",") if t.strip()] or TRANSLATORS
    print(f"Pass B model: {os.environ['LLM_MODEL']} @ {os.environ['LLM_BASE_URL']}")
    print(f"Translators: {targets}")

    for tr in targets:
        out = ROOT / "data" / f"{tr}_full.json"
        if args.skip_existing and out.exists():
            import json
            n = len(json.loads(out.read_text(encoding="utf-8")))
            if n >= args.limit:
                print(f"  [{tr}] skip — {out.name} already has {n} notes")
                continue
        cmd = [
            sys.executable, str(ROOT / "scripts" / "annotate_batch.py"), tr,
            "--backend", "openai",
            "--model", os.environ["LLM_MODEL"],
            "--limit", str(args.limit),
            "--sleep", str(args.sleep),
        ]
        print(f"\n=== {tr} ===")
        r = subprocess.run(cmd, cwd=str(ROOT), env=os.environ.copy())
        if r.returncode != 0:
            print(f"ERROR: {tr} exited {r.returncode}")
            return r.returncode
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
