#!/usr/bin/env python3
"""Remove sarga-1 fallback duplicates from the scraped Valmiki corpus, rebuild indexes.

valmiki.gitasupersite.in silently serves sarga-1 content when an out-of-range sarga
is requested. An early pre-guard scrape cached these as real files (every kanda padded
to a uniform ~130 sargas; real counts are 77/119/75/67/68/128). This script detects the
fallbacks by content and deletes them, then rebuilds each index.json to the surviving
file set. Fully reversible: regenerate with scripts/scrape_valmiki_*.py --force.

Usage:
    python scripts/clean_valmiki_corpus.py            # report only (dry-run)
    python scripts/clean_valmiki_corpus.py --apply    # delete duplicates + rebuild indexes
"""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
SHLOKA_DIR = ROOT / "data" / "valmiki_shlokas"
COMM_DIR = ROOT / "data" / "valmiki_commentaries"
REAL_SARGAS = {1: 77, 2: 119, 3: 75, 4: 67, 5: 68, 6: 128}  # canonical Valmiki counts


def kanda_num(dirname):
    m = re.match(r"kanda_(\d+)_", dirname)
    return int(m.group(1)) if m else None


def first_verse_id(path):
    for e in json.load(open(path, encoding="utf-8")):
        vid = (e.get("verse_id") or "").strip()
        if vid:
            return vid
    return ""


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def clean_shlokas(apply):
    deleted = []
    for kdir in sorted(SHLOKA_DIR.glob("kanda_*")):
        k = kanda_num(kdir.name)
        for f in sorted(kdir.glob("sarga_*.json")):
            sn = int(re.match(r"sarga_(\d+)\.json", f.name).group(1))
            if sn == 1:
                continue
            if first_verse_id(f) == f"{k}.1.1":  # sarga-1 content served for sarga sn
                deleted.append(f)
                if apply:
                    f.unlink()
        if apply:
            idx_path = kdir / "index.json"
            old = json.load(open(idx_path, encoding="utf-8"))
            new = {}
            for f in sorted(kdir.glob("sarga_*.json")):
                s = str(int(re.match(r"sarga_(\d+)\.json", f.name).group(1)))
                if s in old and old[s].get("file") == f.name:
                    new[s] = old[s]  # preserve known metadata
                else:  # orphan file never indexed by the scrape — add it
                    verses = sum(1 for e in json.load(open(f, encoding="utf-8")) if (e.get("verse_id") or "").strip())
                    new[s] = {"file": f.name, "verses": verses}
            new = {s: new[s] for s in sorted(new, key=int)}
            json.dump(new, open(idx_path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    return deleted


def clean_commentaries(apply):
    deleted = []
    for kdir in sorted(COMM_DIR.glob("kanda_*")):
        for s1 in sorted(kdir.glob("*_sarga_01.txt")):
            comm = s1.name[: -len("_sarga_01.txt")]
            ref = sha(s1)
            for f in sorted(kdir.glob(f"{comm}_sarga_*.txt")):
                sn = int(re.search(r"_sarga_(\d+)\.txt", f.name).group(1))
                if sn == 1:
                    continue
                if sha(f) == ref:
                    deleted.append(f)
                    if apply:
                        f.unlink()
        if apply:
            idx_path = kdir / "index.json"
            if idx_path.exists():
                idx = json.load(open(idx_path, encoding="utf-8"))
                for meta in idx.values():
                    if isinstance(meta, dict) and "sargas" in meta:
                        meta["sargas"] = {
                            s: sm for s, sm in meta["sargas"].items() if (kdir / sm["file"]).exists()
                        }
                json.dump(idx, open(idx_path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    return deleted


def report_coverage():
    print("  surviving shloka sargas per kanda (target in []):")
    for kdir in sorted(SHLOKA_DIR.glob("kanda_*")):
        k = kanda_num(kdir.name)
        n = len(list(kdir.glob("sarga_*.json")))
        flag = "OK" if n == REAL_SARGAS[k] else "CHECK"
        print(f"    kanda {k} {kdir.name.split('_', 2)[2]:14s}: {n:3d}  [{REAL_SARGAS[k]}]  {flag}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="delete duplicates + rebuild indexes")
    args = ap.parse_args()
    sh = clean_shlokas(args.apply)
    cm = clean_commentaries(args.apply)
    print(f"shloka fallback files     : {len(sh)}")
    print(f"commentary duplicate files: {len(cm)}")
    print(f"MODE: {'APPLIED (files deleted, indexes rebuilt)' if args.apply else 'dry-run — pass --apply to execute'}")
    if args.apply:
        report_coverage()


if __name__ == "__main__":
    main()
