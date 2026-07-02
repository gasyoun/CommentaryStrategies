"""Inspect yogasutra_content page — field discovery and structure."""
import re, requests, urllib3, sys, time
from bs4 import BeautifulSoup
urllib3.disable_warnings()
sys.stdout.reconfigure(encoding="utf-8")

s = requests.Session()
s.headers["User-Agent"] = "Mozilla/5.0"

# Fetch sutra 1.1 with all flags enabled
r = s.get("https://old.gitasupersite.in/yogasutra_content",
          params={"language": "dv", "field_chapter_value": 1, "field_nsutra_value": 1,
                  "enable_sutra": 1, "enable_bhaysa": 1, "enable_vritti": 1},
          timeout=60, verify=False)
print("Status:", r.status_code, "  len:", len(r.content))
soup = BeautifulSoup(r.content, "html.parser")

# All select dropdowns
print("\n=== SELECT elements ===")
for sel in soup.find_all("select"):
    print(f"  name={sel.get('name')!r}")
    for opt in sel.find_all("option"):
        print(f"    value={opt.get('value')!r} text={opt.get_text(strip=True)!r}")

# Checkboxes / enable_* params
print("\n=== Checkboxes / input elements ===")
for inp in soup.find_all("input"):
    print(f"  name={inp.get('name')!r} type={inp.get('type')!r} value={inp.get('value')!r}")

# Named paragraphs (like bs_sutra / bs_comm)
row = soup.find("div", class_="views-row")
print(f"\nviews-row count: {len(soup.find_all('div', class_='views-row'))}")
if row:
    print("\n=== Named <p> elements ===")
    for p in row.find_all("p"):
        name = p.get("name", "")
        text = p.get_text(strip=True)[:100]
        print(f"  name={name!r}: {text!r}")

    print("\n=== ALL views-field divs ===")
    for d in row.find_all("div", class_=lambda c: c and "views-field" in c):
        key = [c for c in d.get("class",[]) if c.startswith("views-field-")]
        key = key[-1].replace("views-field-","") if key else "?"
        print(f"  {key!r:40s}  {d.get_text(strip=True)[:100]!r}")

    print("\n=== FULL ROW HTML (first 3000) ===")
    print(row.prettify()[:3000])
