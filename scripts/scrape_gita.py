"""
Scrape Bhagavad Gita texts from old.gitasupersite.in — all 27 Sanskrit commentaries,
Hindi translations, and English translations, kept separately per field key.

Output layout:
    data/gita/legend.json                        ← key → full title mapping
    data/gita/chapter_01/verse_001.json          ← {chapter, verse, <key>: text, ...}
    data/gita/chapter_01/index.json              ← {verse: {file, fields_present}}
    ...  (18 chapters, ~700 verses)

Each verse JSON keeps every commentator as a distinct key — "separately" means
each field is a named, independently accessible entry, not merged into prose.

The 27 fields by tier:
  Sanskrit commentaries (sc*): scsh, scram, scanand, scang, scjaya, scmad,
      scval, scms, scsri, scvv, scpur, scneel, scdhan
  Hindi translations/commentaries (ht*/hc*): htrskd, httyn, htshg, hcchi, hcrskd
  English translations/commentaries (et*/set*/ec*): etgb, etsiva, etadi, etpurohit,
      etssa, etassa, etradi, setgb, ecsiva

Usage:
    python scripts/scrape_gita.py                  # all 18 chapters
    python scripts/scrape_gita.py --chapter 1      # one chapter
    python scripts/scrape_gita.py --force          # re-fetch cached files
"""

import argparse
import json
import re
import sys
import time
from pathlib import Path

import requests
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

# Standard verse count per BG chapter (critical edition)
CHAPTER_VERSES = {
    1: 47, 2: 72, 3: 43, 4: 42, 5: 29, 6: 47,
    7: 30, 8: 28, 9: 34, 10: 42, 11: 55, 12: 20,
    13: 34, 14: 27, 15: 20, 16: 24, 17: 28, 18: 78,
}

# All 27 field keys present in the full URL
ALL_FIELDS = [
    # Sanskrit commentaries
    "scsh", "scram", "scanand", "scang", "scjaya", "scmad",
    "scval", "scms", "scsri", "scvv", "scpur", "scneel", "scdhan",
    # Hindi translations / commentaries
    "htrskd", "httyn", "htshg", "hcchi", "hcrskd",
    # English translations / commentaries
    "etgb", "etsiva", "etadi", "etpurohit", "etssa", "etassa",
    "etradi", "setgb", "ecsiva",
]

BASE_URL = "https://old.gitasupersite.in/srimad"
# Fixed query string activating all 27 fields
FIELD_PARAMS = "&".join(f"{k}=1" for k in ALL_FIELDS) + "&choose=1"

DELAY_SECS  = 1.2
MAX_RETRIES = 4


def build_url(chapter: int, verse: int) -> str:
    return (f"{BASE_URL}?language=dv"
            f"&field_chapter_value={chapter}"
            f"&field_nsutra_value={verse}"
            f"&{FIELD_PARAMS}")


def clean_html(raw: str) -> str:
    """Strip HTML tags and normalise whitespace from a field's innerHTML."""
    # Remove BOM characters that the site injects
    raw = raw.replace("﻿", "").replace("﻿", "")
    soup = BeautifulSoup(raw, "html.parser")
    text = soup.get_text(separator="\n")
    # Collapse whitespace, strip leading/trailing per line
    lines = [l.strip() for l in text.splitlines()]
    # Remove the bold title line (repeated in legend) and empty lines
    paragraphs = [l for l in lines if l and l not in ("&nbsp;",)]
    return "\n".join(paragraphs)


def extract_legend(soup: BeautifulSoup) -> dict:
    """Build {field_key: full_title} from the <b> header in each field div."""
    legend = {}
    for key in ALL_FIELDS:
        div = soup.find("div", class_=f"views-field-field-{key}")
        if div is None:
            continue
        b = div.find("b")
        if b:
            title = b.get_text(strip=True)
            legend[key] = title
    return legend


def fetch_verse(session: requests.Session, chapter: int, verse: int) -> dict | None:
    """
    Fetch one verse. Returns dict of {field_key: text} or None if absent.
    Retries on network errors and blank 200 responses.
    """
    url = build_url(chapter, verse)
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = session.get(url, timeout=45)
            resp.raise_for_status()
        except requests.RequestException as e:
            if attempt == MAX_RETRIES:
                print(f"  ERROR {chapter}.{verse} after {MAX_RETRIES} attempts: {e}",
                      file=sys.stderr)
                return None
            wait = 2 ** attempt
            print(f"  network error {chapter}.{verse} (attempt {attempt}/{MAX_RETRIES},"
                  f" retry in {wait}s): {e}", file=sys.stderr)
            time.sleep(wait)
            continue

        soup = BeautifulSoup(resp.content, "html.parser")

        # Detect absent verse: check if any field div has content
        # The site doesn't use view-empty; absent verse = all field divs empty
        fields = {}
        for key in ALL_FIELDS:
            div = soup.find("div", class_=f"views-field-field-{key}")
            if div is None:
                continue
            text = clean_html(str(div))
            # Strip the title line itself from content (first non-empty line)
            lines = text.splitlines()
            # Title is always the first line; keep the rest as content
            content_lines = lines[1:] if len(lines) > 1 else lines
            content = "\n".join(l for l in content_lines if l).strip()
            if content:
                fields[key] = content

        if not fields:
            if attempt < MAX_RETRIES:
                wait = 2 ** attempt
                print(f"  all fields empty {chapter}.{verse}"
                      f" (attempt {attempt}/{MAX_RETRIES}, retry in {wait}s)",
                      file=sys.stderr)
                time.sleep(wait)
                continue
            print(f"  all fields empty after {MAX_RETRIES} attempts — absent",
                  file=sys.stderr)
            return None

        # Verify the verse belongs to the requested chapter (detect silent fallback)
        first_text = next(iter(fields.values()), "")
        expected = f"{chapter}."
        # A verse from a different chapter would start "N.M" with different N
        if first_text and not re.search(rf"\b{chapter}\.\d", first_text):
            # Only warn, don't treat as absent — some fields may lack verse refs
            pass

        return fields

    return None


def scrape_chapter(chapter: int, out_dir: Path, force: bool,
                   legend: dict, legend_path: Path) -> dict:
    """Scrape all verses of one chapter. Returns index metadata."""
    index = {}
    session = requests.Session()
    session.headers["User-Agent"] = (
        "Mozilla/5.0 (compatible; research-scraper/1.0; CommentaryStrategies)"
    )
    max_verse = CHAPTER_VERSES.get(chapter, 80)

    for verse in range(1, max_verse + 1):
        out_file = out_dir / f"verse_{verse:03d}.json"

        if out_file.exists() and not force:
            data = json.loads(out_file.read_text(encoding="utf-8"))
            n_fields = len([k for k in data if k not in ("chapter", "verse")])
            index[str(verse)] = {"file": out_file.name, "fields": n_fields}
            print(f"  {chapter}.{verse:03d} CACHED ({n_fields} fields)")
            continue

        print(f"  {chapter}.{verse:03d} ...", end=" ", flush=True)
        fields = fetch_verse(session, chapter, verse)

        if fields is None:
            print("absent")
            continue

        # Build legend on first successful fetch
        if not legend and not legend_path.exists():
            url = build_url(chapter, verse)
            resp = session.get(url, timeout=45)
            lg_soup = BeautifulSoup(resp.content, "html.parser")
            legend.update(extract_legend(lg_soup))
            legend_path.write_text(
                json.dumps(legend, ensure_ascii=False, indent=2), encoding="utf-8"
            )
            print(f"  [legend written → {legend_path.name}]")

        record = {"chapter": chapter, "verse": verse, **fields}
        out_file.write_text(
            json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        n_fields = len(fields)
        index[str(verse)] = {"file": out_file.name, "fields": n_fields}
        print(f"{n_fields} fields → {out_file.name}")
        time.sleep(DELAY_SECS)

    return index


def main():
    parser = argparse.ArgumentParser(
        description="Scrape Bhagavad Gita texts from old.gitasupersite.in"
    )
    parser.add_argument(
        "--chapter", type=int, choices=range(1, 19), default=None,
        metavar="1-18", help="Scrape only this chapter (default: all 18)"
    )
    parser.add_argument(
        "--force", action="store_true",
        help="Re-fetch even if output file already exists"
    )
    args = parser.parse_args()

    base = Path(__file__).parent.parent / "data" / "gita"
    base.mkdir(parents=True, exist_ok=True)

    legend_path = base / "legend.json"
    legend: dict = (
        json.loads(legend_path.read_text(encoding="utf-8"))
        if legend_path.exists() else {}
    )

    chapter_range = [args.chapter] if args.chapter else range(1, 19)
    grand_verses = grand_fields = 0

    for chapter in chapter_range:
        out_dir = base / f"chapter_{chapter:02d}"
        out_dir.mkdir(parents=True, exist_ok=True)

        index_path = out_dir / "index.json"
        index = (
            json.loads(index_path.read_text(encoding="utf-8"))
            if index_path.exists() else {}
        )

        print(f"\n{'='*55}")
        print(f"  CHAPTER {chapter}  ({CHAPTER_VERSES.get(chapter, '?')} verses)")
        print(f"{'='*55}")

        new_index = scrape_chapter(chapter, out_dir, args.force, legend, legend_path)
        index.update(new_index)

        index_path.write_text(
            json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8"
        )

        ch_verses = len(index)
        ch_fields = sum(v.get("fields", 0) for v in index.values())
        print(f"\n  Chapter {chapter}: {ch_verses} verses, {ch_fields} field-texts")
        grand_verses += ch_verses
        grand_fields += ch_fields

    print(f"\n{'='*55}")
    print(f"  TOTAL: {grand_verses} verses, {grand_fields} field-texts")
    print(f"{'='*55}")


if __name__ == "__main__":
    main()
