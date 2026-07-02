"""
Scrape Ramcharitmanas from manas.gitasupersite.in — all 7 kandas, Devanagari text.

Output layout:
    data/ramcharitmanas/kanda_1_baalkaanda/block_001.json
    data/ramcharitmanas/kanda_1_baalkaanda/index.json
    ...  (7 kandas, 1,074 blocks total)

Each block JSON:
    {
      "kanda": 1,
      "kanda_name": "baalkaanda",
      "block_id": "1.1",
      "block_num": 1,
      "segments": [
        {"type": "chaupai", "type_label": "चौपाई", "lines": ["..."]},
        {"type": "doha_sortha", "type_label": "दोहा/सोरठा", "lines": ["..."]}
      ]
    }

Site structure:
  URL: manas.gitasupersite.in/ramcharitmanas?tid={kanda}&tid_1=11&page=0,{N}
  One views-row per page, containing one block (chaupai + doha set).
  Type labels are <span style="font-size: x-large;"> nodes inside the body div.

Usage:
    python scripts/scrape_manas.py               # all 7 kandas
    python scripts/scrape_manas.py --kanda 5     # Sundar Kaanda only
    python scripts/scrape_manas.py --force       # re-fetch cached files
"""

import argparse
import json
import sys
import time
from pathlib import Path

import requests
import urllib3
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

KANDAS = {
    1: "baalkaanda",
    2: "ayodhyakaanda",
    3: "aranyakaanda",
    4: "kishkindhakaanda",
    5: "sundarkaanda",
    6: "lankakaanda",
    7: "uttarakaanda",
}

# Last page index (0-based) per kanda — verified from site pager
LAST_PAGE = {1: 360, 2: 325, 3: 45, 4: 29, 5: 59, 6: 120, 7: 129}

BASE_URL   = "https://manas.gitasupersite.in/ramcharitmanas"
DELAY_SECS = 1.2
MAX_RETRIES = 4

TYPE_MAP = {
    "चौपाई": "chaupai",
    "दोहा/सोरठा": "doha_sortha",
    "दोहा": "doha",
    "सोरठा": "sortha",
    "छंद": "chhand",
    "श्लोक": "shloka",
}


def normalize_type(label: str) -> str:
    return TYPE_MAP.get(label.strip(), label.strip().lower())


def is_type_label(tag) -> bool:
    """True if this element is a verse-type label (two formats found on the site)."""
    if tag.name == "span" and "x-large" in tag.get("style", ""):
        return True
    if tag.name == "font" and tag.get("size") == "5":
        return True
    return False


def parse_body(content_div) -> list:
    """
    Parse the field-content div into a list of segment dicts.

    The site uses two equivalent formats for type labels:
      <span style='font-size: x-large;'>चौपाई</span>
      <font size='5'>चौपाई</font>
    Segments may also be split across multiple <p> elements (e.g. block 4.10:
    chaupai in <p>1</p>, chhand in <p>2</p>, doha in <p>3</p>).

    Returns: [{"type": str, "type_label": str, "lines": [str, ...]}, ...]
    """
    paras = content_div.find_all("p")
    if not paras:
        paras = [content_div]

    TYPE_MARKER = "\x00TYPE\x00"
    result_text = ""

    for p in paras:
        for child in p.children:
            if not hasattr(child, "name"):
                result_text += str(child)
            elif child.name == "br":
                result_text += "\n"
            elif is_type_label(child):
                label = child.get_text(strip=True)
                result_text += f"\n{TYPE_MARKER}{label}{TYPE_MARKER}\n"
            else:
                result_text += child.get_text(separator="\n")

    parts = result_text.split(TYPE_MARKER)
    segments = []
    i = 1
    while i < len(parts):
        label = parts[i].strip()
        content = parts[i + 1] if i + 1 < len(parts) else ""
        lines = [l.strip() for l in content.splitlines() if l.strip()]
        if label:
            segments.append({
                "type": normalize_type(label),
                "type_label": label,
                "lines": lines,
            })
        i += 2

    return segments


def fetch_block(session: requests.Session, kanda_tid: int, page_num: int) -> dict | None:
    """
    Fetch one block (page). Returns parsed block dict or None on failure.
    page_num=0 → first block, page_num=N → (N+1)-th block.
    """
    params = {"tid": kanda_tid, "tid_1": 11, "page": f"0,{page_num}"}

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = session.get(BASE_URL, params=params, timeout=45, verify=False)
            resp.raise_for_status()
        except requests.RequestException as e:
            if attempt == MAX_RETRIES:
                print(f"  ERROR page {page_num} after {MAX_RETRIES} attempts: {e}",
                      file=sys.stderr)
                return None
            wait = 2 ** attempt
            print(f"  network error page {page_num} (attempt {attempt}/{MAX_RETRIES},"
                  f" retry in {wait}s): {e}", file=sys.stderr)
            time.sleep(wait)
            continue

        soup = BeautifulSoup(resp.content, "html.parser")

        rows = soup.find_all("div", class_="views-row")
        if not rows:
            if attempt < MAX_RETRIES:
                wait = 2 ** attempt
                print(f"  no views-row on page {page_num}"
                      f" (attempt {attempt}/{MAX_RETRIES}, retry in {wait}s)",
                      file=sys.stderr)
                time.sleep(wait)
                continue
            print(f"  no views-row after {MAX_RETRIES} attempts — skipping",
                  file=sys.stderr)
            return None

        row = rows[0]

        # Verse number (e.g. "1.1")
        vnum_div = row.find("div", class_="views-field-field-verse-number")
        block_id = vnum_div.find("div", class_="field-content").get_text(strip=True) if vnum_div else ""

        # Body content
        body_div = row.find("div", class_="views-field-body")
        if not body_div:
            if attempt < MAX_RETRIES:
                wait = 2 ** attempt
                print(f"  no body div on page {page_num}"
                      f" (attempt {attempt}/{MAX_RETRIES}, retry in {wait}s)",
                      file=sys.stderr)
                time.sleep(wait)
                continue
            print(f"  no body div after {MAX_RETRIES} attempts — skipping",
                  file=sys.stderr)
            return None

        content_div = body_div.find("div", class_="field-content")
        if not content_div:
            if attempt < MAX_RETRIES:
                wait = 2 ** attempt
                print(f"  no field-content on page {page_num}"
                      f" (attempt {attempt}/{MAX_RETRIES}, retry in {wait}s)",
                      file=sys.stderr)
                time.sleep(wait)
                continue
            return None

        segments = parse_body(content_div)
        if not segments:
            if attempt < MAX_RETRIES:
                wait = 2 ** attempt
                print(f"  segments empty on page {page_num}"
                      f" (attempt {attempt}/{MAX_RETRIES}, retry in {wait}s)",
                      file=sys.stderr)
                time.sleep(wait)
                continue
            print(f"  segments empty after {MAX_RETRIES} attempts — skipping",
                  file=sys.stderr)
            return None

        return {"block_id": block_id, "segments": segments}

    return None


def scrape_kanda(kanda_num: int, out_dir: Path, force: bool) -> dict:
    """Scrape all blocks for one kanda. Returns index metadata."""
    index = {}
    last_page = LAST_PAGE[kanda_num]
    session = requests.Session()
    session.headers["User-Agent"] = (
        "Mozilla/5.0 (compatible; research-scraper/1.0; CommentaryStrategies)"
    )

    for page_num in range(0, last_page + 1):
        block_num = page_num + 1
        out_file = out_dir / f"block_{block_num:04d}.json"

        if out_file.exists() and not force:
            data = json.loads(out_file.read_text(encoding="utf-8"))
            n_seg = len(data.get("segments", []))
            n_lines = sum(len(s["lines"]) for s in data.get("segments", []))
            index[str(block_num)] = {
                "file": out_file.name,
                "block_id": data.get("block_id", ""),
                "segments": n_seg,
                "lines": n_lines,
            }
            print(f"  block {block_num:04d} [{data.get('block_id','')}] CACHED"
                  f" ({n_seg} segs, {n_lines} lines)")
            continue

        print(f"  block {block_num:04d} ...", end=" ", flush=True)
        result = fetch_block(session, kanda_num, page_num)

        if result is None:
            print("FAILED")
            continue

        block_id = result["block_id"]
        segments = result["segments"]
        n_lines = sum(len(s["lines"]) for s in segments)

        record = {
            "kanda": kanda_num,
            "kanda_name": KANDAS[kanda_num],
            "block_id": block_id,
            "block_num": block_num,
            "segments": segments,
        }
        out_file.write_text(
            json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        index[str(block_num)] = {
            "file": out_file.name,
            "block_id": block_id,
            "segments": len(segments),
            "lines": n_lines,
        }
        seg_types = "+".join(s["type"] for s in segments)
        print(f"[{block_id}] {seg_types} ({n_lines} lines) → {out_file.name}")
        time.sleep(DELAY_SECS)

    return index


def main():
    parser = argparse.ArgumentParser(
        description="Scrape Ramcharitmanas from manas.gitasupersite.in"
    )
    parser.add_argument(
        "--kanda", type=int, choices=list(KANDAS.keys()), default=None,
        metavar="1-7", help="Scrape only this kanda (default: all 7)"
    )
    parser.add_argument(
        "--force", action="store_true",
        help="Re-fetch even if output file already exists"
    )
    args = parser.parse_args()

    base = Path(__file__).parent.parent / "data" / "ramcharitmanas"
    base.mkdir(parents=True, exist_ok=True)

    kanda_range = [args.kanda] if args.kanda else list(KANDAS.keys())
    grand_blocks = grand_lines = 0

    for kanda_num in kanda_range:
        kname = KANDAS[kanda_num]
        out_dir = base / f"kanda_{kanda_num}_{kname}"
        out_dir.mkdir(parents=True, exist_ok=True)

        index_path = out_dir / "index.json"
        index = (
            json.loads(index_path.read_text(encoding="utf-8"))
            if index_path.exists() else {}
        )

        total = LAST_PAGE[kanda_num] + 1
        print(f"\n{'='*60}")
        print(f"  KANDA {kanda_num}: {kname.upper()}  ({total} blocks)")
        print(f"{'='*60}")

        new_index = scrape_kanda(kanda_num, out_dir, args.force)
        index.update(new_index)

        index_path.write_text(
            json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8"
        )

        k_blocks = len(index)
        k_lines = sum(v.get("lines", 0) for v in index.values())
        print(f"\n  {kname}: {k_blocks} blocks, {k_lines:,} lines")
        grand_blocks += k_blocks
        grand_lines += k_lines

    print(f"\n{'='*60}")
    print(f"  TOTAL: {grand_blocks} blocks, {grand_lines:,} lines")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
