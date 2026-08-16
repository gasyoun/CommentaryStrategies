"""DeepSeek independent-reader collation of the sarga-1 lexical notes (H2833).

Second reader demanded by ballot point 19 («надо с deepseek досконально
сопоставить все примечания»): every card of data/lexical/ch1.json (after the
Grintser style pass) is judged by DeepSeek Flash as an independent
Sanskrit-lexicography reviewer — literal gloss, morphology, realia, register.
Divergences are a list for adjudication, not a verdict.

Key: DEEPSEEK_API_KEY from repo .env, then ../ORS-FAQ/.env (same as
run_blind_iaa_pass.py). Model: deepseek-v4-flash, thinking disabled,
temperature 0, JSON object output. Resumable: cards already present in the
output JSON are skipped.

Run: python scripts/deepseek_collate_lexical_ch1.py [--limit N]
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "lexical" / "ch1.json"
OUT = ROOT / "data" / "lexical" / "style_pass_h2833" / "deepseek_collation.json"
ENV_CANDIDATES = [ROOT / ".env", ROOT.parent / "ORS-FAQ" / ".env"]
MODEL = os.environ.get("LLM_MODEL") or "deepseek-v4-flash"
BASE_URL = os.environ.get("LLM_BASE_URL") or "https://api.deepseek.com"

SYSTEM = (
    "Ты — независимый рецензент-санскритолог, проверяющий лексические примечания "
    "к русскому переводу Сундараканды «Рамаяны» Вальмики. Для каждой карточки "
    "проверь ПО СУЩЕСТВУ: (1) верен ли буквальный перевод санскритской леммы; "
    "(2) верен ли морфологический/этимологический разбор; (3) верны ли реалии и "
    "мифологические сведения; (4) выдержан ли ровный академический регистр "
    "(без публицистики). Отвечай СТРОГО одним JSON-объектом: "
    '{"verdict": "agree" | "minor" | "major", "issues": ["..."], "comment": "..."} '
    "— verdict=agree если примечание верно; minor — мелкие уточнения; major — "
    "фактическая ошибка. issues — конкретные расхождения (пустой список, если их "
    "нет), по-русски, кратко."
)


def load_dotenv() -> None:
    for env_path in ENV_CANDIDATES:
        if not env_path.exists():
            continue
        for line in env_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            k, v = k.strip(), v.strip().strip('"').strip("'")
            if k and k not in os.environ:
                os.environ[k] = v


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    load_dotenv()
    key = os.environ.get("DEEPSEEK_API_KEY") or os.environ.get("LLM_API_KEY")
    if not key:
        print("ERROR: set DEEPSEEK_API_KEY (repo .env or ORS-FAQ/.env)")
        sys.exit(2)
    import openai

    client = openai.OpenAI(api_key=key, base_url=BASE_URL)

    cards = [c for c in json.loads(SRC.read_text(encoding="utf-8")) if "_meta" not in c]
    done: dict = {}
    if OUT.exists():
        done = {r["key"]: r for r in json.loads(OUT.read_text(encoding="utf-8"))["results"]}

    results = list(done.values())
    n_new = 0
    for c in cards:
        card_key = f"{c['shloka']}|{c['lemma_iast']}"
        if card_key in done:
            continue
        if args.limit and n_new >= args.limit:
            break
        user = (
            f"Стих: {c['shloka']} (Сундараканда). Лемма: {c['lemma_iast']}.\n"
            f"Словарная опора карточки: {c.get('source', '')}\n\n"
            f"Примечание:\n{c['note_ru']}"
        )
        text = ""
        for attempt in range(3):
            try:
                resp = client.chat.completions.create(
                    model=MODEL,
                    max_tokens=700,
                    temperature=0,
                    messages=[{"role": "system", "content": SYSTEM},
                              {"role": "user", "content": user}],
                    response_format={"type": "json_object"},
                    extra_body={"thinking": {"type": "disabled"}},
                )
                text = (resp.choices[0].message.content or "").strip()
                break
            except Exception as e:  # noqa: BLE001 — retry then surface
                print(f"  retry {attempt + 1} for {card_key}: {type(e).__name__}: {e}")
                time.sleep(3 * (attempt + 1))
        if not text:
            print(f"  FAILED: {card_key}")
            continue
        try:
            j = json.loads(text)
        except json.JSONDecodeError:
            j = {"verdict": "unparsed", "issues": [], "comment": text[:400]}
        rec = {"key": card_key, "shloka": c["shloka"], "lemma_iast": c["lemma_iast"],
               "verdict": j.get("verdict"), "issues": j.get("issues", []),
               "comment": j.get("comment", "")}
        results.append(rec)
        n_new += 1
        print(f"[{n_new}] {card_key}: {rec['verdict']}"
              + (f" — {'; '.join(rec['issues'])[:100]}" if rec["issues"] else ""))
        OUT.write_text(json.dumps(
            {"_meta": {"model": f"{MODEL} @ {BASE_URL}", "date": "2026-08-16",
                       "handoff": "H2833", "n": len(results)},
             "results": results},
            ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    from collections import Counter

    print("\nverdicts:", dict(Counter(r["verdict"] for r in results)))
    print(f"total {len(results)} / {len(cards)} cards")


if __name__ == "__main__":
    main()
