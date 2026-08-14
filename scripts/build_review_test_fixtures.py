#!/usr/bin/env python3
"""Generate synthetic, vote-free submission fixtures from the live manifest."""
import copy
import hashlib
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "tests" / "fixtures"
manifest = json.loads((ROOT / "data" / "apparatus" / "reviewer_manifest.json").read_text(encoding="utf-8"))
doc = {"schema_version": 1, "reviewer": "Костина", "manifest_hash": manifest["manifest_hash"],
       "source_hash": manifest["source_hash"], "client_timestamp": "2026-08-14T00:00:00Z",
       "sargas": [{"sarga": row["sarga"], "source_hash": row["source_hash"], "decisions": {}}
                   for row in manifest["sargas"]]}
canonical = lambda value: json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
doc["content_hash"] = hashlib.sha256(canonical(doc)).hexdigest()
invalid = copy.deepcopy(doc)
invalid["reviewer"] = "Неизвестный"
OUT.mkdir(parents=True, exist_ok=True)
(OUT / "apparatus_submission_valid.json").write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
(OUT / "apparatus_submission_invalid_identity.json").write_text(json.dumps(invalid, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("wrote synthetic vote-free submission fixtures")
