#!/usr/bin/env python3
"""Fail-closed validator for the versioned Sundara adjudication policy."""
from __future__ import annotations

import copy
import json
import math
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
POLICY = ROOT / "data" / "apparatus" / "adjudication_policy.json"
ALLOWED_ACTIONS = {"auto_apply", "auto_exclude", "sample_review", "human_escalation"}
ALLOWED_KINDS = {"deterministic", "agent", "editorial"}
BAR = 0.95


def errors(doc: dict) -> list[str]:
    out: list[str] = []
    if doc.get("schema_version") != 1:
        out.append("schema_version must be 1")
    configured_bar = (doc.get("statistical_bar") or {}).get("minimum_lower_bound")
    if configured_bar != BAR:
        out.append(f"minimum_lower_bound must remain locked at {BAR}")
    classes = doc.get("classes")
    if not isinstance(classes, list) or not classes:
        return out + ["classes must be a non-empty list"]
    seen: set[str] = set()
    for i, item in enumerate(classes):
        tag = f"classes[{i}]"
        cid = item.get("id")
        if not cid or cid in seen:
            out.append(f"{tag}: id missing or duplicate")
        seen.add(cid)
        kind, action = item.get("kind"), item.get("action")
        if kind not in ALLOWED_KINDS:
            out.append(f"{tag}: unknown kind {kind!r}")
        if action not in ALLOWED_ACTIONS:
            out.append(f"{tag}: unknown action {action!r}")
        if not item.get("definition") or not item.get("evidence_revision"):
            out.append(f"{tag}: frozen definition and evidence_revision are required")
        if action in {"auto_apply", "auto_exclude"}:
            if kind == "deterministic":
                inv = item.get("invariants")
                if not isinstance(inv, dict) or not inv or not all(v is True for v in inv.values()):
                    out.append(f"{tag}: deterministic automation requires all invariants true")
            elif kind == "agent":
                sample = item.get("sample") or {}
                audit = item.get("audit") or {}
                lower = sample.get("lower_95")
                if not sample.get("preregistered") or not sample.get("blind"):
                    out.append(f"{tag}: agent automation requires preregistered blind evidence")
                if not isinstance(sample.get("size"), int) or sample.get("size", 0) <= 0:
                    out.append(f"{tag}: agent automation requires a positive sample size")
                if not isinstance(lower, (int, float)) or not math.isfinite(lower) or lower < BAR:
                    out.append(f"{tag}: lower_95 must be >= {BAR}")
                if any(audit.get(k) in (None, "", "unassigned") for k in
                       ("model", "prompt_revision", "data_revision")):
                    out.append(f"{tag}: frozen model/prompt/data provenance required")
            else:
                out.append(f"{tag}: editorial classes cannot automate")
        if kind == "editorial" and action != "human_escalation":
            out.append(f"{tag}: editorial work must remain human_escalation")
    return out


def selftest(doc: dict) -> list[str]:
    failures: list[str] = []
    base = {
        "id": "boundary", "definition": "frozen", "kind": "agent",
        "risk": "low", "action": "auto_apply", "evidence_revision": "rev",
        "sample": {"preregistered": True, "blind": True, "size": 100,
                   "successes": 100, "method": "wilson", "lower_95": BAR},
        "audit": {"model": "frozen", "prompt_revision": "p1",
                  "data_revision": "d1", "reversible": True},
    }
    cases = [(BAR - 0.0001, False), (BAR, True), (BAR + 0.0001, True)]
    for value, expected in cases:
        probe = copy.deepcopy(doc)
        row = copy.deepcopy(base)
        row["sample"]["lower_95"] = value
        probe["classes"] = [row]
        passed = not errors(probe)
        if passed != expected:
            failures.append(f"boundary {value} expected {expected}, got {passed}")
    for mutation, label in [({"kind": "mystery"}, "unknown class"),
                            ({"definition": ""}, "missing definition"),
                            ({"evidence_revision": ""}, "missing evidence")]:
        probe = copy.deepcopy(doc)
        row = copy.deepcopy(base)
        row.update(mutation)
        probe["classes"] = [row]
        if not errors(probe):
            failures.append(f"{label} unexpectedly passed")
    return failures


def main() -> int:
    doc = json.loads(POLICY.read_text(encoding="utf-8"))
    failures = errors(doc) + selftest(doc)
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1
    print(f"PASS: {POLICY.relative_to(ROOT)}; {len(doc['classes'])} classes; bar={BAR}")
    print("PASS: below/at/above boundary and fail-closed mutation fixtures")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
