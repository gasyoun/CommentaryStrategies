"""run_blind_iaa_pass.py — DeepSeek Flash axis labels (H1469 / H2490 / H2677).

Default path (H1469 Pass B): first 50 notes × 6 translators → data/{tr}_full.json.
Remainder path (H2677): unlabeled notes that are NOT the 300-note gold, written
to a sidecar so gold file hashes stay unchanged.

Loads DEEPSEEK_API_KEY from repo .env, then sibling ORS-FAQ/.env. Never uses
the Anthropic backend.

Usage:
    python scripts/run_blind_iaa_pass.py --inventory
    python scripts/run_blind_iaa_pass.py --remainder
    python scripts/run_blind_iaa_pass.py --remainder --limit 1
    python scripts/run_blind_iaa_pass.py --only vassilkov,erman
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
SOURCES = ROOT / "sources"
TRANSLATORS = ["kalyanov", "vassilkov", "erman", "grintser", "syrkin", "leonov"]
GOLD_FULL = [DATA / f"{tr}_full.json" for tr in TRANSLATORS]
GOLD_MARKUP = [DATA / f"{tr}_markup_50.json" for tr in TRANSLATORS]
ENV_CANDIDATES = [
    ROOT / ".env",
    ROOT.parent / "ORS-FAQ" / ".env",
]
REMAINDER_DIR = DATA / "iaa" / "flash_w1"
LEONOV_OWN = DATA / "leonov_own_notes.json"


def load_dotenv() -> None:
    for env_path in ENV_CANDIDATES:
        if not env_path.exists():
            continue
        for line in env_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            k, v = k.strip(), v.strip().strip('"').strip("'")
            if k and k not in os.environ:
                os.environ[k] = v


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def n_list(path: Path) -> int:
    if not path.exists():
        return -1
    obj = json.loads(path.read_text(encoding="utf-8"))
    return len(obj) if isinstance(obj, list) else -2


def gold_texts() -> set[str]:
    texts: set[str] = set()
    for path in GOLD_FULL + GOLD_MARKUP:
        if not path.exists():
            continue
        for rec in json.loads(path.read_text(encoding="utf-8")):
            t = (rec.get("raw_text") or "").strip()
            if t:
                texts.add(t)
    return texts


def gold_hashes() -> list[tuple[str, str]]:
    rows = []
    for path in GOLD_FULL + GOLD_MARKUP:
        if path.exists():
            rows.append((path.name, sha256(path)))
    return rows


def build_leonov_own_worklist() -> tuple[list[dict], dict]:
    """Notes from leonov_own_notes.json that are not in the gold 300."""
    blob = json.loads(LEONOV_OWN.read_text(encoding="utf-8"))
    notes_in = blob.get("notes") or []
    skip = gold_texts()
    out: list[dict] = []
    skipped_gold = 0
    skipped_empty = 0
    already_axed = 0
    for n in notes_in:
        raw = (n.get("raw_text") or "").strip()
        if not raw:
            skipped_empty += 1
            continue
        if n.get("axis_2_kazansky") or n.get("axis_4_paribok"):
            already_axed += 1
            continue
        if raw in skip:
            skipped_gold += 1
            continue
        cid = n.get("comment_id") or f"comment_{n.get('sarga')}_{n.get('verse')}"
        rec = {
            "raw_text": raw,
            "comment_id": f"leonov/{cid}",
            "shloka_addr": n.get("verse_id") or "",
        }
        if n.get("editor"):
            rec["editor"] = n["editor"]
        out.append(rec)
    stats = {
        "source_notes": len(notes_in),
        "unlabeled": len(out),
        "skipped_gold_overlap": skipped_gold,
        "skipped_empty": skipped_empty,
        "already_had_axes": already_axed,
    }
    return out, stats


def inventory() -> dict:
    iaa_rows = []
    total_src = total_full = 0
    for tr in TRANSLATORS:
        src_n = n_list(SOURCES / f"{tr}_notes.json")
        full_n = n_list(DATA / f"{tr}_full.json")
        total_src += max(src_n, 0)
        total_full += max(full_n, 0)
        iaa_rows.append({
            "translator": tr,
            "source_n": src_n,
            "full_n": full_n,
            "unlabeled_in_iaa_sources": max(src_n, 0) - max(full_n, 0),
        })
    _work, leonov_stats = build_leonov_own_worklist()
    return {
        "iaa_sources": iaa_rows,
        "iaa_source_total": total_src,
        "iaa_full_total": total_full,
        "iaa_unlabeled": total_src - total_full,
        "leonov_own": leonov_stats,
        "gold_hashes": gold_hashes(),
        "pending_year1_sources": [
            "sementsov_notes.json",
            "burba_notes.json",
            "petrov_notes.json",
            "smirnov_notes.json",
            "blinderman_notes.json",
        ],
        "already_typed_layers": [
            "data/sundara_ch*_commentary_to_add.json (type А/В/…)",
            "data/hist_cultural/ch*.json (type Г)",
            "data/lexical/ch*.json (lexical layer)",
        ],
    }


def write_inventory_md(inv: dict, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# H2677 — unlabeled CS notes inventory",
        "",
        f"_Created: 14-08-2026 · Last updated: 14-08-2026_",
        "",
        "W1-CS inventory for [H2677 (Grok 4.6) — W1 Flash IAA on unlabeled CS notes](https://github.com/gasyoun/Uprava/blob/main/handoffs/H2677-Grok_CommentaryStrategies_deepseek-w1-cs-unlabeled-axes_13.08.26.md).",
        "Gold 300 is skipped. IAA `sources/{tr}_notes.json` is already the gold sample.",
        "",
        "## IAA pipeline (sources → data/*_full.json)",
        "",
        "| translator | source n | already in *_full.json | unlabeled |",
        "|---|---:|---:|---:|",
    ]
    for row in inv["iaa_sources"]:
        lines.append(
            f"| {row['translator']} | {row['source_n']} | {row['full_n']} | {row['unlabeled_in_iaa_sources']} |"
        )
    lines += [
        "",
        f"Total source={inv['iaa_source_total']}; already labelled={inv['iaa_full_total']}; unlabeled in this format={inv['iaa_unlabeled']}.",
        "",
        "## Unlabeled remainder (this pass)",
        "",
        "Machine-readable translator notes with `raw_text` and **no** `axis_2`/`axis_4`, not in the gold 300:",
        "",
        "| pile | n |",
        "|---|---:|",
        f"| [data/leonov_own_notes.json](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/leonov_own_notes.json) notes | {inv['leonov_own']['source_notes']} |",
        f"| already had axes | {inv['leonov_own']['already_had_axes']} |",
        f"| gold-text overlap (skipped) | {inv['leonov_own']['skipped_gold_overlap']} |",
        f"| empty raw_text | {inv['leonov_own']['skipped_empty']} |",
        f"| **Flash worklist** | **{inv['leonov_own']['unlabeled']}** |",
        "",
        "Year-1 pending source files (no file on disk — parked, D21): "
        + ", ".join(f"`{n}`" for n in inv["pending_year1_sources"]) + ".",
        "",
        "Already-typed layers (not unlabeled; not this pass): "
        + "; ".join(inv["already_typed_layers"]) + ".",
        "",
        "## Gold 300 SHA-256 (must stay unchanged)",
        "",
        "| file | sha256 |",
        "|---|---|",
    ]
    for name, digest in inv["gold_hashes"]:
        lines.append(f"| `{name}` | `{digest}` |")
    lines += ["", "_Dr. Mārcis Gasūns_", ""]
    path.write_text("\n".join(lines), encoding="utf-8", newline="\n")


def apply_flash_env() -> int:
    load_dotenv()
    key = os.environ.get("DEEPSEEK_API_KEY") or os.environ.get("LLM_API_KEY")
    if not key:
        print("ERROR: set DEEPSEEK_API_KEY or LLM_API_KEY (repo .env or ORS-FAQ/.env)")
        return 2
    os.environ["LLM_API_KEY"] = key
    os.environ["LLM_BASE_URL"] = os.environ.get("LLM_BASE_URL") or "https://api.deepseek.com"
    os.environ["LLM_MODEL"] = os.environ.get("LLM_MODEL") or "deepseek-v4-flash"
    os.environ["LLM_BACKEND"] = "openai"
    return 0


def run_annotate(translator: str, *, limit: int | None, sleep: float,
                 source: Path | None = None, output: Path | None = None,
                 jsonl: Path | None = None, dry_run: bool = False) -> int:
    if output is not None:
        gold = {p.resolve() for p in GOLD_FULL + GOLD_MARKUP}
        if output.resolve() in gold:
            print(f"ERROR: remainder must not write gold file {output}")
            return 3
    cmd = [
        sys.executable, str(ROOT / "scripts" / "annotate_batch.py"), translator,
        "--backend", "openai",
        "--model", os.environ["LLM_MODEL"],
        "--sleep", str(sleep),
    ]
    if limit is not None:
        cmd += ["--limit", str(limit)]
    if source is not None:
        cmd += ["--source", str(source)]
    if output is not None:
        cmd += ["--output", str(output)]
    if jsonl is not None:
        cmd += ["--jsonl", str(jsonl)]
    if dry_run:
        cmd.append("--dry-run")
    print(" ".join(cmd))
    r = subprocess.run(cmd, cwd=str(ROOT), env=os.environ.copy())
    return r.returncode


def validate_records(path: Path) -> dict:
    recs = json.loads(path.read_text(encoding="utf-8"))
    required = ("comment_id", "translator", "raw_text", "axis_1_topic",
                "axis_2_kazansky", "axis_4_paribok")
    ok = 0
    bad = []
    for rec in recs:
        missing = [k for k in required if k not in rec]
        if missing:
            bad.append((rec.get("comment_id"), f"missing {missing}"))
            continue
        if rec["axis_2_kazansky"] not in {"A", "B", "V", "G"}:
            bad.append((rec["comment_id"], f"axis_2={rec['axis_2_kazansky']}"))
            continue
        if rec["axis_4_paribok"] not in {"P", "K", "D"}:
            bad.append((rec["comment_id"], f"axis_4={rec['axis_4_paribok']}"))
            continue
        if rec["translator"] not in TRANSLATORS:
            bad.append((rec["comment_id"], f"translator={rec['translator']}"))
            continue
        ok += 1
    return {"n": len(recs), "valid": ok, "invalid": len(bad), "bad": bad[:20]}


def summarize_jsonl(path: Path) -> dict:
    n = n_ok = n_err = 0
    cost = 0.0
    pin = pout = preason = 0
    if not path.exists():
        return {"calls": 0, "ok": 0, "errors": 0, "cost_usd": 0.0,
                "prompt_tokens": 0, "completion_tokens": 0, "reasoning_tokens": 0}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        rec = json.loads(line)
        n += 1
        if rec.get("ok"):
            n_ok += 1
        else:
            n_err += 1
        cost += float(rec.get("cost_usd") or 0)
        pin += int(rec.get("prompt_tokens") or 0)
        pout += int(rec.get("completion_tokens") or 0)
        preason += int(rec.get("reasoning_tokens") or 0)
    return {
        "calls": n, "ok": n_ok, "errors": n_err, "cost_usd": round(cost, 6),
        "prompt_tokens": pin, "completion_tokens": pout, "reasoning_tokens": preason,
        "error_rate": (n_err / n) if n else 0.0,
    }


def write_report(path: Path, inv: dict, schema: dict, spend: dict,
                 hashes_after: list[tuple[str, str]], hashes_ok: bool) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# H2677 — W1 Flash IAA unlabeled CS notes",
        "",
        f"_Created: 14-08-2026 · Last updated: 14-08-2026_",
        "",
        f"Run UTC: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M')}Z. "
        "Model `deepseek-v4-flash` @ `https://api.deepseek.com`. "
        "Executor Grok 4.6 (`grok-4.6`).",
        "",
        "## Counts",
        "",
        "| item | n |",
        "|---|---:|",
        f"| IAA source notes (gold sample) | {inv['iaa_source_total']} |",
        f"| already in DeepSeek/IAA `*_full.json` | {inv['iaa_full_total']} |",
        f"| unlabeled in IAA sources | {inv['iaa_unlabeled']} |",
        f"| leonov_own worklist | {inv['leonov_own']['unlabeled']} |",
        f"| labelled this file | {schema.get('n', 0)} |",
        f"| schema-valid | {schema.get('valid', 0)} |",
        f"| schema-invalid | {schema.get('invalid', 0)} |",
        f"| API calls | {spend['calls']} |",
        f"| API errors | {spend['errors']} |",
        f"| error rate | {spend['error_rate']:.4f} |",
        f"| prompt tokens | {spend['prompt_tokens']} |",
        f"| completion tokens | {spend['completion_tokens']} |",
        f"| reasoning tokens | {spend['reasoning_tokens']} |",
        f"| **cost USD** (pre-16-08 Flash card) | **{spend['cost_usd']:.4f}** |",
        "",
        f"Schema-valid %: {100.0 * schema['valid'] / schema['n']:.1f}%" if schema.get("n") else "Schema-valid %: n/a",
        "",
        "## Gold 300 hashes",
        "",
        f"Unchanged: **{'yes' if hashes_ok else 'NO — REGRESSION'}**",
        "",
        "| file | sha256 after |",
        "|---|---|",
    ]
    for name, digest in hashes_after:
        lines.append(f"| `{name}` | `{digest}` |")
    lines += [
        "",
        "Gold `data/{tr}_full.json` / `{tr}_markup_50.json` were not opened for write.",
        "Anthropic `annotate_batch.py --backend anthropic` was not used.",
        "",
        "_Dr. Mārcis Gasūns_",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8", newline="\n")


def remainder(limit: int | None, sleep: float, dry_run: bool) -> int:
    REMAINDER_DIR.mkdir(parents=True, exist_ok=True)
    inv = inventory()
    inv_path = DATA / "iaa" / "H2677_UNLABELED_INVENTORY.md"
    write_inventory_md(inv, inv_path)
    print(f"Inventory → {inv_path}")
    print(f"  IAA unlabeled={inv['iaa_unlabeled']}  leonov_own worklist={inv['leonov_own']['unlabeled']}")

    work, _stats = build_leonov_own_worklist()
    if limit is not None:
        work = work[:limit]
    src_path = REMAINDER_DIR / "leonov_own_unlabeled_source.json"
    out_path = REMAINDER_DIR / "leonov_own_flash.json"
    jsonl_path = REMAINDER_DIR / "calls.jsonl"
    src_path.write_text(json.dumps(work, ensure_ascii=False, indent=2) + "\n",
                        encoding="utf-8", newline="\n")
    print(f"Worklist {len(work)} → {src_path}")

    rc = apply_flash_env()
    if rc:
        return rc
    print(f"Remainder model: {os.environ['LLM_MODEL']} @ {os.environ['LLM_BASE_URL']}")
    print("Backend: openai (DeepSeek). Anthropic not used.")

    rc = run_annotate(
        "leonov",
        limit=None,
        sleep=sleep,
        source=src_path,
        output=out_path,
        jsonl=jsonl_path,
        dry_run=dry_run,
    )
    if rc:
        return rc
    if dry_run:
        return 0

    schema = validate_records(out_path) if out_path.exists() else {
        "n": 0, "valid": 0, "invalid": 0, "bad": [],
    }
    spend = summarize_jsonl(jsonl_path)
    before = {n: d for n, d in inv["gold_hashes"]}
    after = gold_hashes()
    hashes_ok = all(before.get(n) == d for n, d in after) and len(after) == len(before)
    write_report(REMAINDER_DIR / "H2677_W1_CS_REPORT.md", inv, schema, spend, after, hashes_ok)
    print(f"schema valid={schema['valid']}/{schema['n']}  $={spend['cost_usd']}  err={spend['error_rate']:.4f}")
    print(f"gold hashes unchanged: {hashes_ok}")
    if not hashes_ok:
        return 4
    if schema["n"] and schema["invalid"]:
        return 5
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="", help="Comma-separated translator slugs (gold path)")
    ap.add_argument("--limit", type=int, default=None,
                    help="Gold path default 50; remainder: cap worklist head")
    ap.add_argument("--sleep", type=float, default=0.3)
    ap.add_argument("--skip-existing", action="store_true",
                    help="Skip translator if data/{tr}_full.json already has --limit notes")
    ap.add_argument("--inventory", action="store_true",
                    help="Write inventory markdown and exit (no API)")
    ap.add_argument("--remainder", action="store_true",
                    help="H2677: label unlabeled notes into data/iaa/flash_w1/ (not gold)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if args.inventory:
        inv = inventory()
        dest = DATA / "iaa" / "H2677_UNLABELED_INVENTORY.md"
        write_inventory_md(inv, dest)
        print(json.dumps({
            "iaa_unlabeled": inv["iaa_unlabeled"],
            "leonov_own_unlabeled": inv["leonov_own"]["unlabeled"],
            "inventory": str(dest),
        }, ensure_ascii=False, indent=2))
        return 0

    if args.remainder:
        return remainder(args.limit, args.sleep, args.dry_run)

    rc = apply_flash_env()
    if rc:
        return rc
    limit = 50 if args.limit is None else args.limit
    targets = [t.strip() for t in args.only.split(",") if t.strip()] or TRANSLATORS
    print(f"Pass B model: {os.environ['LLM_MODEL']} @ {os.environ['LLM_BASE_URL']}")
    print(f"Translators: {targets}")
    for tr in targets:
        out = DATA / f"{tr}_full.json"
        if args.skip_existing and out.exists():
            n = len(json.loads(out.read_text(encoding="utf-8")))
            if n >= limit:
                print(f"  [{tr}] skip — {out.name} already has {n} notes")
                continue
        print(f"\n=== {tr} ===")
        r = run_annotate(tr, limit=limit, sleep=args.sleep, dry_run=args.dry_run)
        if r:
            print(f"ERROR: {tr} exited {r}")
            return r
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
