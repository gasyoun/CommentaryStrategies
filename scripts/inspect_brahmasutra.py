"""Verify sutra counts beyond 31 and intro paragraph structure."""
import re, requests, urllib3, sys, time
from bs4 import BeautifulSoup
urllib3.disable_warnings()
sys.stdout.reconfigure(encoding="utf-8")

s = requests.Session()
s.headers["User-Agent"] = "Mozilla/5.0"

def fetch(adhyaya, pada, sutra):
    r = s.get("https://old.gitasupersite.in/brahmasutra_content",
              params={"language": "dv", "field_chapter_value": adhyaya,
                      "field_quarter_value": pada, "field_nsutra_value": sutra},
              timeout=45, verify=False)
    soup = BeautifulSoup(r.content, "html.parser")
    row = soup.find("div", class_="views-row")
    if not row:
        return None
    p_sutra = row.find("p", attrs={"name": "bs_sutra"})
    p_comm  = row.find("p", attrs={"name": "bs_comm"})
    p_intro = row.find("p", attrs={"name": "bs_intro"})
    sutra_text = p_sutra.get_text(strip=True)[:120] if p_sutra else ""
    comm_text  = p_comm.get_text(strip=True)[:80]  if p_comm  else ""
    intro_text = p_intro.get_text(strip=True)[:80] if p_intro else ""
    # Extract embedded sutra ID like "।।1.1.31।।"
    m = re.search(r"।।(\d+\.\d+\.\d+)।।", sutra_text)
    embedded_id = m.group(1) if m else "?"
    return {"sutra_text": sutra_text, "embedded_id": embedded_id,
            "comm": comm_text, "intro": intro_text}

# Check pada 3.3 — expected ~66 sutras
print("=== pada 3.3 boundary test ===")
for n in [40, 60, 65, 66, 67, 68]:
    d = fetch(3, 3, n)
    if d:
        print(f"  3.3.{n}: embedded_id={d['embedded_id']!r}  {d['sutra_text'][:60]!r}")
    time.sleep(0.5)

print()
# Verify intro (sutra=0) structure
print("=== intro (sutra=0) all padas ===")
for (a, p) in [(1,1), (1,2), (2,1), (3,3)]:
    d = fetch(a, p, 0)
    if d:
        print(f"  {a}.{p}.0: intro={d['intro'][:80]!r}")
    time.sleep(0.5)
