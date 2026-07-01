"""
Scrape Valmiki Ramayana shlokas (verse text + translations) from
valmiki.gitasupersite.in for all kandas.

Output layout (parallel to commentary folders):
    data/valmiki_shlokas/kanda_1_balakanda/sarga_01.json
    data/valmiki_shlokas/kanda_1_balakanda/index.json
    ...

Each sarga JSON is a list of verse objects:
    {
      "verse_id": "1.1.1",
      "sanskrit": "तपस्स्वाध्यायनिरतं ...",
      "word_by_word": "तपस्वी ascetic, ...",
      "explanation": "Ascetic Valmiki enquired of Narada ..."
    }

Usage:
    python scripts/scrape_valmiki_shlokas.py              # all kandas
    python scripts/scrape_valmiki_shlokas.py --kanda 1    # one kanda
    python scripts/scrape_valmiki_shlokas.py --force      # re-fetch cached
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

KANDAS = {
    1: "balakanda",
    2: "ayodhyakanda",
    3: "aranyakanda",
    4: "kishkindakanda",
    5: "sundarakanda",
    6: "yuddhakanda",
}

BASE_URL    = "https://valmiki.gitasupersite.in/sloka"
MAX_SARGA   = 140
DELAY_SECS  = 1.5
MAX_RETRIES = 4
EMPTY_LIMIT = 3


def get_field_text(row, field_class: str) -> str:
    div = row.find("div", class_=field_class)
    if div is None:
        return ""
    fc = div.find("div", class_="field-content")
    if fc is None:
        return ""
    for br in fc.find_all("br"):
        br.replace_with("\n")
    return "\n".join(l.strip() for l in fc.get_text().splitlines() if l.strip())


def extract_verse_id(sanskrit: str) -> str:
    """Pull verse number like 1.1.1 from the embedded ।।1.1.1।। marker."""
    m = re.search(r"।।\s*(\d+\.\d+\.\d+)\s*।।", sanskrit)
    return m.group(1) if m else ""


def fetch_sarga(session: requests.Session, kanda_tid: int, sarga: int) -> list | None:
    """
    Fetch one sarga's verses. Returns list of verse dicts or None.
    None means the page is genuinely absent (view-empty).
    Empty list [] means a transient blank that should be retried.
    """
    params = {
        "language": "dv",
        "field_kanda_tid": kanda_tid,
        "field_sarga_value": sarga,
    }
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = session.get(BASE_URL, params=params, timeout=45)
            resp.raise_for_status()
        except requests.RequestException as e:
            if attempt == MAX_RETRIES:
                print(f"  ERROR sarga {sarga} after {MAX_RETRIES} attempts: {e}",
                      file=sys.stderr)
                return None
            wait = 2 ** attempt
            print(f"  network error sarga {sarga} (attempt {attempt}/{MAX_RETRIES},"
                  f" retry in {wait}s): {e}", file=sys.stderr)
            time.sleep(wait)
            continue

        soup = BeautifulSoup(resp.content, "html.parser")

        # Drupal explicit "no record" — authoritative, no retry
        view_empty = soup.find("div", class_="view-empty")
        if view_empty is not None:
            print(f'  site says: "{view_empty.get_text(strip=True)}"', file=sys.stderr)
            return None

        rows = soup.find_all("div", class_="views-row")
        if not rows:
            if attempt < MAX_RETRIES:
                wait = 2 ** attempt
                print(f"  no verse rows in response (attempt {attempt}/{MAX_RETRIES},"
                      f" retry in {wait}s)", file=sys.stderr)
                time.sleep(wait)
                continue
            print(f"  no verse rows after {MAX_RETRIES} attempts", file=sys.stderr)
            return None

        verses = []
        for row in rows:
            sanskrit     = get_field_text(row, "views-field-body")
            word_by_word = get_field_text(row, "views-field-field-htetrans")
            explanation  = get_field_text(row, "views-field-field-explanation")
            if not sanskrit:
                continue
            verses.append({
                "verse_id":    extract_verse_id(sanskrit),
                "sanskrit":    sanskrit,
                "word_by_word": word_by_word,
                "explanation": explanation,
            })

        # Detect silent sarga-1 fallback: site returns sarga 1 content when a
        # requested sarga doesn't exist, instead of showing view-empty.
        # Check: first verse_id should start with "{kanda}.{sarga}."
        if verses and sarga > 1:
            first_id = verses[0]["verse_id"]
            expected_prefix = f"{kanda_tid}.{sarga}."
            if first_id and not first_id.startswith(expected_prefix):
                print(f"  verse_id {first_id!r} doesn't match expected"
                      f" {expected_prefix!r} — site fallback to sarga 1,"
                      f" treating as absent", file=sys.stderr)
                return None

        return verses

    return None


def scrape_kanda(kanda_num: int, out_dir: Path, force: bool) -> dict:
    """Scrape all sargas for one kanda. Returns index metadata."""
    index = {}
    session = requests.Session()
    session.headers["User-Agent"] = (
        "Mozilla/5.0 (compatible; research-scraper/1.0; CommentaryStrategies)"
    )
    consecutive_empty = 0

    for sarga in range(1, MAX_SARGA + 1):
        out_file = out_dir / f"sarga_{sarga:02d}.json"

        if out_file.exists() and not force:
            verses = json.loads(out_file.read_text(encoding="utf-8"))
            index[str(sarga)] = {"file": out_file.name, "verses": len(verses)}
            print(f"  sarga {sarga:02d} ... CACHED {len(verses)} verses")
            consecutive_empty = 0
            continue

        print(f"  sarga {sarga:02d} ...", end=" ", flush=True)
        verses = fetch_sarga(session, kanda_num, sarga)

        if verses is None:
            # Authoritative absence (view-empty)
            consecutive_empty += 1
            print(f"no content (gap {consecutive_empty}/{EMPTY_LIMIT})")
            if consecutive_empty >= EMPTY_LIMIT:
                print(f"  {EMPTY_LIMIT} consecutive empty — stopping")
                break
            continue

        consecutive_empty = 0
        out_file.write_text(
            json.dumps(verses, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        index[str(sarga)] = {"file": out_file.name, "verses": len(verses)}
        print(f"{len(verses)} verses → {out_file.name}")
        time.sleep(DELAY_SECS)

    return index


def main():
    parser = argparse.ArgumentParser(
        description="Scrape Valmiki Ramayana shloka text for all kandas"
    )
    parser.add_argument(
        "--kanda", type=int, choices=list(KANDAS.keys()), default=None,
        help="Scrape only this kanda 1–6 (default: all)",
    )
    parser.add_argument(
        "--force", action="store_true",
        help="Re-fetch even if output file already exists",
    )
    args = parser.parse_args()

    base = Path(__file__).parent.parent / "data" / "valmiki_shlokas"
    base.mkdir(parents=True, exist_ok=True)

    kanda_range = [args.kanda] if args.kanda else list(KANDAS.keys())
    grand_sargas = grand_verses = 0

    for kanda_num in kanda_range:
        kname = KANDAS[kanda_num]
        out_dir = base / f"kanda_{kanda_num}_{kname}"
        out_dir.mkdir(parents=True, exist_ok=True)

        index_path = out_dir / "index.json"
        index = (
            json.loads(index_path.read_text(encoding="utf-8"))
            if index_path.exists() else {}
        )

        print(f"\n{'='*60}")
        print(f"  KANDA {kanda_num}: {kname.upper()}")
        print(f"{'='*60}")

        new_index = scrape_kanda(kanda_num, out_dir, args.force)
        index.update(new_index)

        index_path.write_text(
            json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8"
        )

        k_sargas = len(index)
        k_verses = sum(v.get("verses", 0) for v in index.values())
        print(f"\n  {kname}: {k_sargas} sargas, {k_verses:,} verses")
        grand_sargas += k_sargas
        grand_verses += k_verses

    print(f"\n{'='*60}")
    print(f"  TOTAL: {grand_sargas} sargas, {grand_verses:,} verses")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
