#!/usr/bin/env python3
"""Offline acceptance fixtures for raw validation/import/queue invariants."""
from __future__ import annotations
import copy
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")
HERE=Path(__file__).resolve().parent;ROOT=HERE.parent;sys.path.insert(0,str(HERE))
import gate_ledger  # noqa: E402
from build_gate_disagreement_queue import build  # noqa: E402
from validate_apparatus_submission import canonical,validate  # noqa: E402

manifest=json.loads((ROOT/"data/apparatus/reviewer_manifest.json").read_text(encoding="utf-8"))
base=json.loads((ROOT/"tests/fixtures/apparatus_submission_valid.json").read_text(encoding="utf-8"))
assert not validate(base),validate(base)
bad=copy.deepcopy(base);bad["sargas"][0]["source_hash"]="0"*64
assert any("source_hash mismatch" in e for e in validate(bad))
ballot=json.loads((ROOT/"data/apparatus/sarga_01_kostina.json").read_text(encoding="utf-8"))
verse,note=next((v,n) for v in ballot["verses"] for n in v["notes"] if n.get("votable"))
decision={"action":"reject","reject_reason":"synthetic veto","verse_id":verse["verse_id"],"layer":note["layer"],"ts":"2026-08-14T00:00:00Z"}
submission=copy.deepcopy(base);submission["sargas"][0]["decisions"]={note["id"]:decision};submission.pop("content_hash");submission["content_hash"]=hashlib.sha256(canonical(submission)).hexdigest();assert not validate(submission),validate(submission)
with tempfile.TemporaryDirectory() as tmp:
    tmp=Path(tmp);ledger_path=tmp/"ledger.json";submission_path=tmp/"submission.json"
    fixture=gate_ledger.default_ledger();gate_ledger.record(fixture,note["id"],"Леонов",{"layer":note["layer"],"verse_id":verse["verse_id"]},{"action":"accept","gated_date":"2026-07-11"});gate_ledger.save(str(ledger_path),fixture);submission_path.write_text(json.dumps(submission,ensure_ascii=False),encoding="utf-8")
    command=[sys.executable,str(HERE/"import_apparatus_submission.py"),str(submission_path),"--ledger",str(ledger_path)]
    subprocess.run(command,check=True,encoding="utf-8");subprocess.run(command,check=True,encoding="utf-8")
    imported=gate_ledger.load(str(ledger_path));assert imported["entries"][note["id"]]["verdicts"]["Леонов"]["action"]=="accept"
    report=build(imported);assert report["counts"]["editorial_queue"]==1 and report["queue"][0]["editorial_veto"]
print("PASS: malformed/stale rejection, transactional import, idempotency, Leonov preservation, reject veto")
