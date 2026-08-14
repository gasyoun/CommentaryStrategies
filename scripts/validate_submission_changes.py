#!/usr/bin/env python3
"""CI guard: immutable raw submission paths are create-only."""
import os
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")
base=os.environ.get("GITHUB_BASE_REF")
revision=f"origin/{base}...HEAD" if base else "HEAD^...HEAD"
run=subprocess.run(["git","diff","--name-status",revision,"--","votes/submissions"],capture_output=True,encoding="utf-8")
if run.returncode:
    print(run.stderr);raise SystemExit(run.returncode)
bad=[]
for line in run.stdout.splitlines():
    status,*paths=line.split("\t")
    if status!="A" or not paths[-1].endswith(".json"):
        bad.append(line)
if bad:
    print("FAIL: raw submissions are create-only JSON paths:",*bad,sep="\n")
    raise SystemExit(1)
print("PASS: raw submission changes are create-only")
