"""
Scrape Yoga Sutras from old.gitasupersite.in — sutra text, Vyasa's bhashya,
and Bhoja's vritti for all 4 chapters (195 sutras total).

Output layout:
    data/yogasutra/chapter_1/sutra_001.json
    data/yogasutra/chapter_1/index.json
    ...  (4 chapters)

Each sutra JSON:
    {
      "chapter": 1,
      "sutra_num": 1,
      "sutra_id": "1.1",
      "sutra_text": "अथ योगानुशासनम्",
      "bhashya": "Vyasa commentary ...",
      "vritti": "Bhoja vritti ..."
    }

Site structure:
  URL: old.gitasupersite.in/yogasutra_content
       ?language=dv&field_chapter_value=C&field_nsutra_value=S
       &enable_sutra=1&enable_bhaysa=1&enable_vritti=1
  Three div fields per row:
    views-field-body         → sutra text (title label "सूत्र" in first <p>, text in second)
    views-field-field-bhaysa → Vyasa's bhashya
    views-field-field-vritti → Bhoja's vritti
  Sutra ID embedded as "।।C.S।।" in sutra text — mismatch = silent fallback → stop.

Usage:
    python scripts/scrape_yogasutra.py               # all 4 chapters
    python scripts/scrape_yogasutra.py --chapter 1   # one chapter
    python scripts/scrape_yogasutra.py --force       # re-fetch cached files
"""

import argparse
import json
import re
import sys
import time
from pathlib import Path

import requests
import urllib3
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASE_URL   = "https://old.gitasupersite.in/yogasutra_content"
MAX_SUTRA  = 60     # safe upper bound (chapter 2 and 3 have 55)
DELAY_SECS = 1.2
MAX_RETRIES = 4

CHAPTER_NAMES = {1: "samadhi_pada", 2: "sadhana_pada",
                 3: "vibhuti_pada", 4: "kaivalya_pada"}


def extract_field_text(field_div) -> str:
    """
    Extract content text from a views-field div, skipping the title label paragraph.
    Title labels are in <p align='center'><font color='#2c44bd'>; content is in
    <p align='justify'> or the second <p align='center'> (for the sutra itself).
    """
    if not field_div:
        return ""
    content_div = field_div.find("div", class_="field-content")
    if not content_div:
        return ""
    paras = content_div.find_all("p")
    # Skip the first <p> which is always the blue title label
    content_paras = paras[1:] if len(paras) > 1 else paras
    parts = []
    for p in content_paras:
        for br in p.find_all("br"):
            br.replace_with("\n")
        text = p.get_text()
        lines = [l.strip() for l in text.splitlines() if l.strip()]
        if lines:
            parts.extend(lines)
    return "\n".join(parts)


def extract_sutra_id(sutra_text: str) -> str:
    """Pull embedded ID like '1.1' from '।।1.1।।' in the sutra text."""
    m = re.search(r"।।\s*(\d+\.\d+)\s*।।", sutra_text)
    return m.group(1) if m else ""


def fetch_sutra(session: requests.Session, chapter: int, sutra_num: int) -> dict | None:
    """
    Fetch one sutra. Returns content dict, "FALLBACK" sentinel, or None on error.
    """
    params = {
        "language": "dv",
        "field_chapter_value": chapter,
        "field_nsutra_value": sutra_num,
        "enable_sutra": 1,
        "enable_bhaysa": 1,
        "enable_vritti": 1,
    }
    expected_id = f"{chapter}.{sutra_num}"

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = session.get(BASE_URL, params=params, timeout=60, verify=False)
            resp.raise_for_status()
        except requests.RequestException as e:
            if attempt == MAX_RETRIES:
                print(f"  ERROR {chapter}.{sutra_num} after {MAX_RETRIES} attempts: {e}",
                      file=sys.stderr)
                return None
            wait = 2 ** attempt
            print(f"  network error (attempt {attempt}/{MAX_RETRIES}, retry in {wait}s): {e}",
                  file=sys.stderr)
            time.sleep(wait)
            continue

        soup = BeautifulSoup(resp.content, "html.parser")
        row = soup.find("div", class_="views-row")
        if not row:
            if attempt < MAX_RETRIES:
                wait = 2 ** attempt
                print(f"  no views-row (attempt {attempt}/{MAX_RETRIES}, retry in {wait}s)",
                      file=sys.stderr)
                time.sleep(wait)
                continue
            return None

        sutra_div  = row.find("div", class_="views-field-body")
        bhashya_div = row.find("div", class_="views-field-field-bhaysa")
        vritti_div  = row.find("div", class_="views-field-field-vritti")

        sutra_text = extract_field_text(sutra_div)
        bhashya    = extract_field_text(bhashya_div)
        vritti     = extract_field_text(vritti_div)

        if not sutra_text and not bhashya:
            if attempt < MAX_RETRIES:
                wait = 2 ** attempt
                print(f"  all fields empty (attempt {attempt}/{MAX_RETRIES}, retry in {wait}s)",
                      file=sys.stderr)
                time.sleep(wait)
                continue
            return None

        embedded_id = extract_sutra_id(sutra_text)
        if embedded_id and embedded_id != expected_id:
            print(f"  sutra_id {embedded_id!r} ≠ expected {expected_id!r}"
                  f" — silent fallback, end of chapter", file=sys.stderr)
            return "FALLBACK"

        return {
            "sutra_id": embedded_id or expected_id,
            "sutra_text": sutra_text,
            "bhashya": bhashya,
            "vritti": vritti,
        }

    return None


def scrape_chapter(chapter: int, out_dir: Path, force: bool) -> dict:
    """Scrape all sutras for one chapter. Returns index metadata."""
    index = {}
    session = requests.Session()
    session.headers["User-Agent"] = (
        "Mozilla/5.0 (compatible; research-scraper/1.0; CommentaryStrategies)"
    )

    for sutra_num in range(1, MAX_SUTRA + 1):
        out_file = out_dir / f"sutra_{sutra_num:03d}.json"

        if out_file.exists() and not force:
            data = json.loads(out_file.read_text(encoding="utf-8"))
            index[str(sutra_num)] = {
                "file": out_file.name,
                "sutra_id": data.get("sutra_id", ""),
                "bhashya_chars": len(data.get("bhashya", "")),
                "vritti_chars": len(data.get("vritti", "")),
            }
            print(f"  {chapter}.{sutra_num:03d} CACHED"
                  f" (bhashya {len(data.get('bhashya',''))} / vritti {len(data.get('vritti',''))} chars)")
            continue

        print(f"  {chapter}.{sutra_num:03d} ...", end=" ", flush=True)
        result = fetch_sutra(session, chapter, sutra_num)

        if result == "FALLBACK":
            print(f"end of chapter at sutra {sutra_num}")
            break

        if result is None:
            print("FAILED")
            continue

        record = {
            "chapter": chapter,
            "chapter_name": CHAPTER_NAMES.get(chapter, ""),
            "sutra_num": sutra_num,
            **result,
        }
        out_file.write_text(
            json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        b_chars = len(result.get("bhashya", ""))
        v_chars = len(result.get("vritti", ""))
        index[str(sutra_num)] = {
            "file": out_file.name,
            "sutra_id": result.get("sutra_id", ""),
            "bhashya_chars": b_chars,
            "vritti_chars": v_chars,
        }
        print(f"ok (bhashya {b_chars} / vritti {v_chars} chars)")
        time.sleep(DELAY_SECS)

    return index


def main():
    parser = argparse.ArgumentParser(
        description="Scrape Yoga Sutras from old.gitasupersite.in"
    )
    parser.add_argument(
        "--chapter", type=int, choices=[1, 2, 3, 4], default=None,
        help="Scrape only this chapter 1-4 (default: all)"
    )
    parser.add_argument(
        "--force", action="store_true",
        help="Re-fetch even if output file already exists"
    )
    args = parser.parse_args()

    base = Path(__file__).parent.parent / "data" / "yogasutra"
    base.mkdir(parents=True, exist_ok=True)

    chapter_range = [args.chapter] if args.chapter else [1, 2, 3, 4]
    grand_sutras = grand_b = grand_v = 0

    for chapter in chapter_range:
        out_dir = base / f"chapter_{chapter}_{CHAPTER_NAMES.get(chapter,'')}"
        out_dir.mkdir(parents=True, exist_ok=True)

        index_path = out_dir / "index.json"
        index = (
            json.loads(index_path.read_text(encoding="utf-8"))
            if index_path.exists() else {}
        )

        print(f"\n{'='*55}")
        print(f"  CHAPTER {chapter}: {CHAPTER_NAMES.get(chapter,'').upper()}")
        print(f"{'='*55}")

        new_index = scrape_chapter(chapter, out_dir, args.force)
        index.update(new_index)

        index_path.write_text(
            json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8"
        )

        n = len(index)
        b = sum(v.get("bhashya_chars", 0) for v in index.values())
        v = sum(v.get("vritti_chars", 0) for v in index.values())
        print(f"\n  Chapter {chapter}: {n} sutras, {b:,} bhashya chars, {v:,} vritti chars")
        grand_sutras += n
        grand_b += b
        grand_v += v

    print(f"\n{'='*55}")
    print(f"  TOTAL: {grand_sutras} sutras")
    print(f"  bhashya: {grand_b:,} chars  |  vritti: {grand_v:,} chars")
    print(f"{'='*55}")


if __name__ == "__main__":
    main()
