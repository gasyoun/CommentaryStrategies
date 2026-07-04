#!/usr/bin/env python3
"""Preserve Claude Code agent transcripts (the drafting-decision logs) in the repo.

The Phase-2 drafting agents' full transcripts — every verse-by-verse draft/reject
decision with its reasoning — live only in the session directory under
~/.claude/projects/<slug>/<session-id>/subagents/agent-*.jsonl and are lost when
that cache is cleaned. This script copies them into the repo and renders a
readable Markdown "reasoning log" per agent (assistant text + thinking blocks +
one-line tool-call summaries; bulky tool RESULTS are omitted — the raw .jsonl
keeps everything).

The MAIN session transcript is NOT copied raw: it embeds injected private
context (global CLAUDE.md, e-mail). Pass --orchestrator to extract only the
orchestrator's own assistant-text messages, which are safe.

Usage:
    python scripts/export_agent_logs.py <session_dir> <out_dir> [--orchestrator <main.jsonl>]

Example:
    python scripts/export_agent_logs.py \
        ~/.claude/projects/<slug>/<session-id> data/analysis/phase2_batch2/logs
"""
import sys
import os
import re
import json
import glob

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")


def detect_sarga(first_user_text):
    m = re.search(r"for sarga (\d+)", first_user_text or "")
    return int(m.group(1)) if m else None


def tool_summary(block):
    name = block.get("name", "?")
    inp = block.get("input") or {}
    hint = (inp.get("description") or inp.get("file_path") or inp.get("pattern")
            or (inp.get("command") or "").split("\n")[0][:100] or "")
    return f"`{name}` — {hint}".rstrip(" —")


def render_md(jsonl_path, title):
    """Assistant-side view of one transcript: text, thinking, tool-call one-liners."""
    out = [f"# {title}", ""]
    model = None
    for line in open(jsonl_path, encoding="utf-8"):
        try:
            d = json.loads(line)
        except json.JSONDecodeError:
            continue
        m = d.get("message") or {}
        if m.get("role") != "assistant":
            continue
        model = m.get("model") or model
        content = m.get("content")
        if not isinstance(content, list):
            continue
        for b in content:
            t = b.get("type")
            if t == "thinking" and b.get("thinking"):
                out += ["> **[thinking]**"]
                out += [f"> {l}" for l in b["thinking"].strip().split("\n")]
                out += [""]
            elif t == "text" and b.get("text", "").strip():
                out += [b["text"].strip(), ""]
            elif t == "tool_use":
                out += [f"- 🔧 {tool_summary(b)}"]
    out.insert(1, f"\n_Model: `{model}`; extracted by scripts/export_agent_logs.py;"
                  f" raw transcript alongside (.jsonl) holds the full record incl. tool results._\n")
    return "\n".join(out) + "\n"


def main():
    argv = sys.argv[1:]
    orch = None
    if "--orchestrator" in argv:
        i = argv.index("--orchestrator")
        orch = argv[i + 1]
        del argv[i:i + 2]
    if len(argv) != 2:
        sys.exit(__doc__)
    session_dir, out_dir = argv
    os.makedirs(out_dir, exist_ok=True)

    for p in sorted(glob.glob(os.path.join(session_dir, "subagents", "agent-*.jsonl"))):
        first_user = ""
        for line in open(p, encoding="utf-8"):
            d = json.loads(line)
            m = d.get("message") or {}
            if m.get("role") == "user" and isinstance(m.get("content"), str):
                first_user = m["content"]
                break
        sarga = detect_sarga(first_user)
        stem = f"sarga_{sarga:02d}" if sarga else os.path.basename(p).replace(".jsonl", "")
        raw_dst = os.path.join(out_dir, f"{stem}_transcript.jsonl")
        # copy raw minus harness "attachment" lines (tool/skill listings — noise,
        # not decision logic; the conversation itself is kept verbatim)
        with open(raw_dst, "w", encoding="utf-8") as dst:
            for line in open(p, encoding="utf-8"):
                try:
                    if json.loads(line).get("type") == "attachment":
                        continue
                except json.JSONDecodeError:
                    pass
                dst.write(line)
        md = render_md(p, f"Drafting reasoning log — sarga {sarga}" if sarga
                       else f"Agent log {stem}")
        with open(os.path.join(out_dir, f"{stem}_reasoning.md"), "w", encoding="utf-8") as fh:
            fh.write(md)
        print(f"{stem}: raw {os.path.getsize(raw_dst)} B + reasoning.md")

    if orch:
        md = render_md(orch, "Orchestrator log (assistant messages only)")
        with open(os.path.join(out_dir, "orchestrator_reasoning.md"), "w", encoding="utf-8") as fh:
            fh.write(md)
        print("orchestrator_reasoning.md written (raw main transcript deliberately NOT copied)")


if __name__ == "__main__":
    main()
