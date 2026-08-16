#!/usr/bin/env python3
"""Recursive inventory of a public Yandex.Disk folder (read-only, no auth).

H2832 — first step of the Goldman Rāmāyaṇa V PDF bake-off: before any OCR we
need to know WHAT is there (which volumes, which formats, which sizes) and
whether a PDF already carries a text layer.

The public REST endpoint needs no token:
    GET https://cloud-api.yandex.net/v1/disk/public/resources
        ?public_key=<url>&path=<subpath>&limit=<n>

Usage
-----
    python scripts/yadisk_inventory.py --key https://disk.yandex.ru/d/XXXX \
        --out data/goldman/inventory_XXXX.json [--max-depth 4] [--filter pdf]

    python scripts/yadisk_inventory.py --key <url> --download "<path>" --to <file>

Nothing here writes into a guarded main checkout by itself; pass an --out path
inside your worktree.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.parse
import urllib.request

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

API = "https://cloud-api.yandex.net/v1/disk/public/resources"
UA = "Mozilla/5.0 (compatible; CommentaryStrategies-inventory/1.0)"


def _get(url: str, retries: int = 3) -> dict:
    last = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=90) as fh:
                return json.loads(fh.read().decode("utf-8"))
        except Exception as exc:  # noqa: BLE001 - network is the whole point
            last = exc
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"GET failed after {retries} tries: {url}\n{last}")


def list_dir(public_key: str, path: str = "/", limit: int = 500) -> list[dict]:
    """Return the raw item dicts of one directory level (paginated)."""
    items: list[dict] = []
    offset = 0
    while True:
        qs = urllib.parse.urlencode(
            {"public_key": public_key, "path": path, "limit": limit, "offset": offset}
        )
        data = _get(f"{API}?{qs}")
        emb = data.get("_embedded") or {}
        batch = emb.get("items") or []
        items.extend(batch)
        offset += len(batch)
        if len(batch) < limit or offset >= (emb.get("total") or 0):
            break
    return items


def walk(public_key: str, path: str = "/", depth: int = 0, max_depth: int = 4) -> list[dict]:
    """Depth-first inventory. Returns flat records with a `path` field."""
    out: list[dict] = []
    try:
        items = list_dir(public_key, path)
    except RuntimeError as exc:
        print(f"  !! {path}: {exc}", file=sys.stderr)
        return out
    for it in items:
        rec = {
            "path": it.get("path", ""),
            "name": it.get("name", ""),
            "type": it.get("type", ""),
            "size": it.get("size"),
            "mime_type": it.get("mime_type"),
            "modified": it.get("modified"),
            "md5": it.get("md5"),
            "depth": depth,
        }
        out.append(rec)
        if rec["type"] == "dir" and depth < max_depth:
            out.extend(walk(public_key, rec["path"], depth + 1, max_depth))
    return out


def download(public_key: str, path: str, dest: str) -> int:
    """Fetch one file via the public download endpoint. Returns bytes written."""
    qs = urllib.parse.urlencode({"public_key": public_key, "path": path})
    meta = _get(f"{API}/download?{qs}")
    href = meta["href"]
    req = urllib.request.Request(href, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=600) as fh, open(dest, "wb") as out:
        n = 0
        while True:
            chunk = fh.read(1 << 20)
            if not chunk:
                break
            out.write(chunk)
            n += len(chunk)
    return n


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--key", required=True, help="public folder/file URL")
    ap.add_argument("--path", default="/", help="subpath inside the public folder")
    ap.add_argument("--max-depth", type=int, default=4)
    ap.add_argument("--out", help="write the flat inventory as JSON here")
    ap.add_argument("--filter", help="only print records whose name contains this (case-insensitive)")
    ap.add_argument("--download", help="download this exact path instead of listing")
    ap.add_argument("--to", help="destination file for --download")
    args = ap.parse_args()

    if args.download:
        if not args.to:
            print("--download needs --to", file=sys.stderr)
            return 2
        n = download(args.key, args.download, args.to)
        print(f"wrote {n} bytes -> {args.to}")
        return 0

    recs = walk(args.key, args.path, 0, args.max_depth)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            json.dump(
                {"public_key": args.key, "root": args.path, "count": len(recs), "items": recs},
                fh,
                ensure_ascii=False,
                indent=1,
            )
        print(f"{len(recs)} records -> {args.out}")

    needle = (args.filter or "").lower()
    for r in recs:
        if needle and needle not in r["name"].lower():
            continue
        size = "" if r["size"] is None else f"{r['size']:>12,}"
        print(f"{r['type']:4} {size}  {r['path']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
