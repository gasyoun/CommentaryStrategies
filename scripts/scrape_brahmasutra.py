"""
Scrape Brahmasutra (Shankaracharya's Bhashya) from old.gitasupersite.in — all 4 adhyayas
× 4 padas × N sutras + one intro per pada.

Output layout:
    data/brahmasutra/adhyaya_1/pada_1/sutra_000.json   ← intro
    data/brahmasutra/adhyaya_1/pada_1/sutra_001.json   ← sutra 1
    ...
    data/brahmasutra/adhyaya_1/pada_1/index.json

Each sutra JSON:
    {
      "adhyaya": 1,
      "pada": 1,
      "sutra_num": 1,          # 0 = pada intro
      "sutra_id": "1.1.1",     # embedded A.P.S ID (empty for intro)
      "sutra_text": "अथातो ब्रह्मजिज्ञासा ।। 1.1.1 ।।",
      "bhashya": "जिज्ञासाधिकरणम् ..."
    }

Site structure:
  URL: old.gitasupersite.in/brahmasutra_content
       ?language=dv&field_chapter_value=A&field_quarter_value=P&field_nsutra_value=S
  One views-row per request, two named <p> tags:
    <p name="bs_sutra"> — sutra text with embedded "।।A.P.S।।" ID
    <p name="bs_comm">  — Shankaracharya's bhashya
  <p name="bs_intro">   — pada introduction (sutra_num=0 only)
  Fallback detection: site silently returns sutra 1 content for out-of-range S —
  detected by checking that embedded sutra ID matches the requested one.

Usage:
    python scripts/scrape_brahmasutra.py               # all 16 padas
    python scripts/scrape_brahmasutra.py --adhyaya 1   # adhyaya 1 only
    python scripts/scrape_brahmasutra.py --force       # re-fetch cached files
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

BASE_URL    = "https://old.gitasupersite.in/brahmasutra_content"
MAX_SUTRA   = 75    # safe upper bound for any pada
DELAY_SECS  = 1.2
MAX_RETRIES = 4


def clean_text(tag) -> str:
    """Extract clean text from a BeautifulSoup tag, collapsing whitespace."""
    if tag is None:
        return ""
    for br in tag.find_all("br"):
        br.replace_with("\n")
    lines = [l.strip() for l in tag.get_text().splitlines() if l.strip()]
    return "\n".join(lines)


def extract_sutra_id(sutra_text: str) -> str:
    """Pull embedded sutra ID like '1.1.1' from '।।1.1.1।।' in the sutra text."""
    m = re.search(r"।।\s*(\d+\.\d+\.\d+)\s*।।", sutra_text)
    return m.group(1) if m else ""


def fetch_sutra(session: requests.Session,
                adhyaya: int, pada: int, sutra_num: int) -> dict | None:
    """
    Fetch one sutra. Returns content dict or None on failure.
    sutra_num=0 fetches the pada introduction.
    Detects silent sarga-1-style fallback via embedded sutra ID mismatch.
    """
    params = {
        "language": "dv",
        "field_chapter_value": adhyaya,
        "field_quarter_value": pada,
        "field_nsutra_value": sutra_num,
    }
    expected_id = f"{adhyaya}.{pada}.{sutra_num}" if sutra_num > 0 else ""

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = session.get(BASE_URL, params=params, timeout=60, verify=False)
            resp.raise_for_status()
        except requests.RequestException as e:
            if attempt == MAX_RETRIES:
                print(f"  ERROR {adhyaya}.{pada}.{sutra_num} after {MAX_RETRIES} attempts: {e}",
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

        if sutra_num == 0:
            # Pada introduction
            p_intro = row.find("p", attrs={"name": "bs_intro"})
            intro_text = clean_text(p_intro)
            if not intro_text:
                # Some padas may have no introduction
                return {"sutra_id": "", "sutra_text": "", "bhashya": intro_text}
            return {"sutra_id": "", "sutra_text": "", "bhashya": intro_text}

        # Regular sutra
        p_sutra = row.find("p", attrs={"name": "bs_sutra"})
        p_comm  = row.find("p", attrs={"name": "bs_comm"})

        if not p_sutra and not p_comm:
            if attempt < MAX_RETRIES:
                wait = 2 ** attempt
                print(f"  no bs_sutra/bs_comm (attempt {attempt}/{MAX_RETRIES}, retry in {wait}s)",
                      file=sys.stderr)
                time.sleep(wait)
                continue
            return None

        sutra_text = clean_text(p_sutra)
        bhashya    = clean_text(p_comm)
        embedded_id = extract_sutra_id(sutra_text)

        # Fallback detection: site returns sutra 1 content for out-of-range numbers
        if expected_id and embedded_id and embedded_id != expected_id:
            print(f"  sutra_id {embedded_id!r} ≠ expected {expected_id!r}"
                  f" — silent fallback, treating as end of pada", file=sys.stderr)
            return "FALLBACK"

        return {
            "sutra_id": embedded_id or expected_id,
            "sutra_text": sutra_text,
            "bhashya": bhashya,
        }

    return None


def scrape_pada(adhyaya: int, pada: int, out_dir: Path, force: bool) -> dict:
    """Scrape all sutras for one pada. Returns index metadata."""
    index = {}
    session = requests.Session()
    session.headers["User-Agent"] = (
        "Mozilla/5.0 (compatible; research-scraper/1.0; CommentaryStrategies)"
    )

    for sutra_num in range(0, MAX_SUTRA + 1):
        out_file = out_dir / f"sutra_{sutra_num:03d}.json"

        if out_file.exists() and not force:
            data = json.loads(out_file.read_text(encoding="utf-8"))
            index[str(sutra_num)] = {
                "file": out_file.name,
                "sutra_id": data.get("sutra_id", ""),
                "chars": len(data.get("bhashya", "")),
            }
            label = "intro" if sutra_num == 0 else data.get("sutra_id", "?")
            print(f"  sutra {sutra_num:03d} [{label}] CACHED"
                  f" ({len(data.get('bhashya',''))} chars bhashya)")
            continue

        label = "intro" if sutra_num == 0 else f"{adhyaya}.{pada}.{sutra_num}"
        print(f"  sutra {sutra_num:03d} [{label}] ...", end=" ", flush=True)
        result = fetch_sutra(session, adhyaya, pada, sutra_num)

        if result == "FALLBACK":
            print(f"end of pada at sutra {sutra_num}")
            break

        if result is None:
            print("FAILED")
            continue

        record = {
            "adhyaya": adhyaya,
            "pada": pada,
            "sutra_num": sutra_num,
            **result,
        }
        out_file.write_text(
            json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        chars = len(result.get("bhashya", ""))
        index[str(sutra_num)] = {
            "file": out_file.name,
            "sutra_id": result.get("sutra_id", ""),
            "chars": chars,
        }
        print(f"ok ({chars} chars bhashya)")
        time.sleep(DELAY_SECS)

    return index


def main():
    parser = argparse.ArgumentParser(
        description="Scrape Brahmasutra Shankarabashya from old.gitasupersite.in"
    )
    parser.add_argument(
        "--adhyaya", type=int, choices=[1, 2, 3, 4], default=None,
        help="Scrape only this adhyaya 1-4 (default: all 4)"
    )
    parser.add_argument(
        "--force", action="store_true",
        help="Re-fetch even if output file already exists"
    )
    args = parser.parse_args()

    base = Path(__file__).parent.parent / "data" / "brahmasutra"
    base.mkdir(parents=True, exist_ok=True)

    adhyaya_range = [args.adhyaya] if args.adhyaya else [1, 2, 3, 4]
    grand_sutras = grand_chars = 0

    for adhyaya in adhyaya_range:
        for pada in [1, 2, 3, 4]:
            out_dir = base / f"adhyaya_{adhyaya}" / f"pada_{pada}"
            out_dir.mkdir(parents=True, exist_ok=True)

            index_path = out_dir / "index.json"
            index = (
                json.loads(index_path.read_text(encoding="utf-8"))
                if index_path.exists() else {}
            )

            print(f"\n{'='*55}")
            print(f"  ADHYAYA {adhyaya}  PADA {pada}")
            print(f"{'='*55}")

            new_index = scrape_pada(adhyaya, pada, out_dir, args.force)
            index.update(new_index)

            index_path.write_text(
                json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8"
            )

            n_sutras = len(index) - 1  # exclude intro
            n_chars  = sum(v.get("chars", 0) for v in index.values())
            print(f"\n  {adhyaya}.{pada}: {n_sutras} sutras, {n_chars:,} chars bhashya")
            grand_sutras += n_sutras
            grand_chars  += n_chars

    print(f"\n{'='*55}")
    print(f"  TOTAL: {grand_sutras} sutras, {grand_chars:,} chars bhashya")
    print(f"{'='*55}")


if __name__ == "__main__":
    main()
