"""
Scrape all Sanskrit commentaries from valmiki.gitasupersite.in for all Ramayana kandas.

Output layout:
    data/valmiki_commentaries/kanda_1_balakanda/{commentary}_sarga_{N:02d}.txt
    data/valmiki_commentaries/kanda_1_balakanda/index.json
    data/valmiki_commentaries/kanda_2_ayodhyakanda/...
    ...  (one folder per kanda, commentaries do not intermix across kandas)

Usage:
    python scripts/scrape_valmiki_commentaries.py              # all kandas, all commentaries
    python scripts/scrape_valmiki_commentaries.py --kanda 1    # one kanda
    python scripts/scrape_valmiki_commentaries.py --commentary kataka --kanda 1
    python scripts/scrape_valmiki_commentaries.py --force      # re-fetch cached files
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

COMMENTARIES = {
    "tilaka":       13,
    "bhusana":      14,
    "siromani":     10,
    "tattvadipika": 12,
    "dharmakutam":   9,
    "kataka":        8,
    "tanisloki":    11,
}

COMMENTARY_NAMES_SA = {
    "tilaka":       "तिलकटीका",
    "bhusana":      "रामायणभूषण",
    "siromani":     "शिरोमणि",
    "tattvadipika": "तत्त्वदीपिका",
    "dharmakutam":  "धर्मकूटम्",
    "kataka":       "काटकम्",
    "tanisloki":    "तनिश्लोकी",
}

KANDAS = {
    1: "balakanda",
    2: "ayodhyakanda",
    3: "aranyakanda",
    4: "kishkindakanda",
    5: "sundarakanda",
    6: "yuddhakanda",
}

BASE_URL   = "https://valmiki.gitasupersite.in/commentaries"
MAX_SARGA  = 130   # upper bound; Yuddhakanda has 128 sargas
DELAY_SECS = 1.5
MAX_RETRIES = 4
EMPTY_LIMIT = 3    # consecutive empty sargas before stopping


def kanda_dir(base: Path, kanda_num: int) -> Path:
    return base / f"kanda_{kanda_num}_{KANDAS[kanda_num]}"


def fetch_sarga(session: requests.Session, commentary_tid: int,
                kanda_tid: int, sarga: int) -> str | None:
    """Fetch one sarga. Retries on network errors AND on blank-200 responses."""
    params = {
        "language": "dv",
        "field_commnetary_tid": commentary_tid,
        "field_kanda_tid":      kanda_tid,
        "field_sarga_value":    sarga,
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

        # Drupal's explicit "no record" message — authoritative, no retry needed
        view_empty = soup.find("div", class_="view-empty")
        if view_empty is not None:
            print(f'  site says: "{view_empty.get_text(strip=True)}"',
                  file=sys.stderr)
            return None

        content_div = soup.find("div", class_="field-content")
        if content_div is None:
            if attempt < MAX_RETRIES:
                wait = 2 ** attempt
                print(f"  HTTP {resp.status_code} but no field-content div"
                      f" (attempt {attempt}/{MAX_RETRIES}, retry in {wait}s)",
                      file=sys.stderr)
                time.sleep(wait)
                continue
            print(f"  HTTP {resp.status_code}, neither view-empty nor field-content"
                  f" after {MAX_RETRIES} attempts", file=sys.stderr)
            return None

        for br in content_div.find_all("br"):
            br.replace_with("\n")
        text = "\n\n".join(
            line for line in (l.strip() for l in content_div.get_text().splitlines()) if line
        )

        if not text.strip():
            if attempt < MAX_RETRIES:
                wait = 2 ** attempt
                print(f"  field-content div present but body is empty"
                      f" (attempt {attempt}/{MAX_RETRIES}, retry in {wait}s)",
                      file=sys.stderr)
                time.sleep(wait)
                continue
            print(f"  field-content div present but body empty after"
                  f" {MAX_RETRIES} attempts", file=sys.stderr)
            return None

        return text

    return None


def count_verses(text: str, kanda: int) -> int:
    return len(re.findall(rf"।।\s*{kanda}\.\d+\.\d+", text))


def scrape_one_kanda(name: str, tid: int, kanda_num: int,
                     out_dir: Path, force: bool) -> dict:
    """Scrape all sargas of one commentary for one kanda. Returns metadata dict."""
    meta = {
        "name": name, "tid": tid,
        "name_sa": COMMENTARY_NAMES_SA[name],
        "kanda": kanda_num, "kanda_name": KANDAS[kanda_num],
        "sargas": {},
    }
    session = requests.Session()
    session.headers["User-Agent"] = (
        "Mozilla/5.0 (compatible; research-scraper/1.0; CommentaryStrategies)"
    )
    consecutive_empty = 0

    for sarga in range(1, MAX_SARGA + 1):
        existing = out_dir / f"{name}_sarga_{sarga:02d}.txt"
        if existing.exists() and not force:
            text = existing.read_text(encoding="utf-8")
            meta["sargas"][str(sarga)] = {
                "file": existing.name,
                "chars": len(text),
                "verses": count_verses(text, kanda_num),
            }
            print(f"  [{name}] sarga {sarga:02d} ... CACHED {len(text):,} chars")
            consecutive_empty = 0
            continue

        print(f"  [{name}] sarga {sarga:02d} ...", end=" ", flush=True)
        text = fetch_sarga(session, tid, kanda_num, sarga)

        if text is None:
            consecutive_empty += 1
            print(f"no content (gap {consecutive_empty}/{EMPTY_LIMIT})")
            if consecutive_empty >= EMPTY_LIMIT:
                print(f"  [{name}] {EMPTY_LIMIT} consecutive empty — stopping")
                break
            continue

        consecutive_empty = 0
        existing.write_text(text, encoding="utf-8")
        vc = count_verses(text, kanda_num)
        meta["sargas"][str(sarga)] = {
            "file": existing.name, "chars": len(text), "verses": vc,
        }
        print(f"{len(text):,} chars, ~{vc} verses → {existing.name}")
        time.sleep(DELAY_SECS)

    return meta


def migrate_flat_sundarakanda(base: Path):
    """Move existing flat sundarakanda .txt files into kanda_5_sundarakanda/."""
    dest = kanda_dir(base, 5)
    dest.mkdir(parents=True, exist_ok=True)
    moved = 0
    for f in base.glob("*_sarga_*.txt"):
        target = dest / f.name
        if not target.exists():
            f.rename(target)
            moved += 1
    if moved:
        print(f"  Migrated {moved} existing Sundarakanda files → {dest.name}/")
    # migrate flat index.json entries into kanda subfolder
    flat_index = base / "index.json"
    if flat_index.exists():
        data = json.loads(flat_index.read_text(encoding="utf-8"))
        kanda_index = dest / "index.json"
        if not kanda_index.exists():
            kanda_index.write_text(
                json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
            )
            print(f"  Migrated flat index.json → {dest.name}/index.json")
        flat_index.unlink()


def main():
    parser = argparse.ArgumentParser(
        description="Scrape all Sanskrit commentaries on all Valmiki Ramayana kandas"
    )
    parser.add_argument(
        "--kanda", type=int, choices=list(KANDAS.keys()), default=None,
        help="Scrape only this kanda number 1–6 (default: all)",
    )
    parser.add_argument(
        "--commentary", choices=list(COMMENTARIES.keys()), default=None,
        help="Scrape only this commentary (default: all seven)",
    )
    parser.add_argument(
        "--force", action="store_true",
        help="Re-fetch even if the output file already exists",
    )
    args = parser.parse_args()

    base = Path(__file__).parent.parent / "data" / "valmiki_commentaries"
    base.mkdir(parents=True, exist_ok=True)

    # One-time migration: move pre-restructure flat Sundarakanda files into subfolder
    if any(base.glob("*_sarga_*.txt")):
        print("Migrating existing flat Sundarakanda files to kanda_5_sundarakanda/…")
        migrate_flat_sundarakanda(base)

    kanda_range  = [args.kanda] if args.kanda else list(KANDAS.keys())
    commentary_targets = (
        {args.commentary: COMMENTARIES[args.commentary]}
        if args.commentary else COMMENTARIES
    )

    grand_sargas = grand_chars = 0

    for kanda_num in kanda_range:
        kname = KANDAS[kanda_num]
        out_dir = kanda_dir(base, kanda_num)
        out_dir.mkdir(parents=True, exist_ok=True)

        index_path = out_dir / "index.json"
        index = (
            json.loads(index_path.read_text(encoding="utf-8"))
            if index_path.exists() else {}
        )

        print(f"\n{'='*60}")
        print(f"  KANDA {kanda_num}: {kname.upper()}")
        print(f"{'='*60}")

        for name, tid in commentary_targets.items():
            print(f"\n--- {name} (tid={tid}) ---")
            meta = scrape_one_kanda(name, tid, kanda_num, out_dir, args.force)
            if meta["sargas"]:
                index[name] = meta
            elif name in index:
                pass  # keep cached entry

        index_path.write_text(
            json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8"
        )

        k_sargas = sum(len(v.get("sargas", {})) for v in index.values())
        k_chars  = sum(
            s["chars"] for v in index.values() for s in v.get("sargas", {}).values()
        )
        print(f"\n  {kname}: {k_sargas} sarga files, {k_chars:,} chars")
        grand_sargas += k_sargas
        grand_chars  += k_chars

    print(f"\n{'='*60}")
    print(f"  TOTAL: {grand_sargas} sarga files, {grand_chars:,} chars")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
