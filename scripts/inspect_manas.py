"""Inspect a specific page's raw HTML to debug empty-segment failures."""
import requests, urllib3, sys
from bs4 import BeautifulSoup
urllib3.disable_warnings()
sys.stdout.reconfigure(encoding="utf-8")

s = requests.Session()
s.headers["User-Agent"] = "Mozilla/5.0"

# Kishkindha kanda, page 9 (block 10) — the one that fails
r = s.get("https://manas.gitasupersite.in/ramcharitmanas",
          params={"tid": 4, "tid_1": 11, "page": "0,9"},
          timeout=60, verify=False)

soup = BeautifulSoup(r.content, "html.parser")
rows = soup.find_all("div", class_="views-row")
print(f"views-row count: {len(rows)}")

if rows:
    print("\n=== FULL ROW HTML ===")
    print(rows[0].prettify())
