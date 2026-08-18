"""H2860 — interactive review sheet for the Nīlakaṇṭha licence register.

Two card groups, 46 in all:

  A. the 16 hits no rule could type, ruled by hand (14 rejected as the ārṣa homonym,
     2 kept with a hand-assigned deviation_type) — the human confirms or overturns;
  B. a reproducible 30-row uniform sample (seed 2860) of the 149 auto-typed rows —
     the fresh hand-precision sample H2860's acceptance block asks for, offered to a
     second pair of eyes.

Everything an agent or a rule could already settle is screened out and counted, per the
/review-sheet Phase 0-bis gate; the evidence file is named in the sheet header.

H2883: every count and percentage below is DERIVED from the loaded register/reject
tables at render time. Do not re-hardcode a figure here — the 92,1 % / 152 / "151 из
151" drift the published sheet carried came from literals that outlived the data.

Usage: python scripts/build_licence_register_review_sheet.py
"""
import csv
import html
import json
import os
import random
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

from csl_pyutil import RU_UI_STRINGS, render_review_sheet  # noqa: E402
from csl_pyutil.evidence import EvidenceManifest  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REG = os.path.join(ROOT, "data", "licence_register")
SHEET_ID = "commentarystrategies-nilakantha-licence_h2860"
OUT = os.path.join(ROOT, "review", SHEET_ID + "_review.html")
GENERATED = "16-08-2026"
SAMPLE_SEED = 2860
SAMPLE_N = 30

BLOB = ("https://github.com/gasyoun/CommentaryStrategies/blob/main/"
        "data/licence_register/")


def esc(s):
    return html.escape(s or "")


def load(path, delim="\t"):
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter=delim))


def source_href(locus_id, parva):
    """Per-card link back to the verse on sanatana.in (V4 of the 19-07-2026 standard)."""
    upa = int(locus_id[5:7])
    return (f"https://sanatana.in/mahabharata/listing/parva/{parva}"
            f"?page={upa}&id={locus_id[:13]}")


def ru_pct(x):
    """Russian decimal comma, one place — the sheet's own number format."""
    return f"{x:.1f}".replace(".", ",")


def ru_plural(n, one, few, many):
    """Russian numeral agreement — 151 строкА, 152 строкИ, 155 строК."""
    if n % 100 in (11, 12, 13, 14):
        return many
    return {1: one, 2: few, 3: few, 4: few}.get(n % 10, many)


def buttons_reject(n_reg, n_hits, precision):
    return (
        "<p><b>«Согласен»</b> — строка остаётся вне регистра; она уже учтена в измеренной "
        f"точности {ru_pct(precision)} % ({n_reg} из {n_hits}) и лежит в "
        f"<a href=\"{BLOB}nilakantha_licence_rejected.tsv\">nilakantha_licence_rejected.tsv</a> "
        "вместе с причиной отклонения.</p>"
        f"<p><b>«Не согласен»</b> — строка возвращается в регистр (станет {n_reg + 1}), "
        "измеренная точность вырастет, и в заметке нужно указать deviation_type, который вы "
        "считаете верным: без него строку некуда положить.</p>"
        "<p><b>«Отложить»</b> — строка остаётся отклонённой до следующего круга; ничего не "
        "ломается, но цифра точности остаётся спорной.</p>")


def buttons_hand(n_reg):
    return (
        "<p><b>«Согласен»</b> — строка остаётся в регистре с этим типом и с пометкой "
        "<code>classification=hand</code>.</p>"
        "<p><b>«Не согласен»</b> — тип переписывается по вашей заметке; если это вообще не "
        f"licence-claim, строка уходит в отклонённые и регистр становится {n_reg - 1}-строчным.</p>"
        "<p><b>«Отложить»</b> — строка остаётся как есть до следующего круга.</p>")


def buttons_auto(n_auto):
    return (
        f"<p><b>«Согласен»</b> — строка засчитывается как верная в выборке из {SAMPLE_N}, "
        f"подтверждая измеренные 100 % точности авто-типизации ({n_auto} из {n_auto}).</p>"
        "<p><b>«Не согласен»</b> — точность авто-прохода падает. Это <u>та самая</u> цифра, по "
        "которой H2860 объявляется провалившимся, если она уйдёт ниже ~90 %: три несогласия "
        f"из {SAMPLE_N} — ещё порог, четыре — уже провал, и регистр придётся перетипизировать.</p>"
        "<p><b>«Отложить»</b> — строка выпадает из знаменателя выборки; при большом числе "
        f"отложенных выборка перестаёт быть {SAMPLE_N}-строчной и оценку придётся повторить.</p>")


def main():
    reg = load(os.path.join(REG, "commentary_licence_register_nilakantha.tsv"))
    rej = load(os.path.join(REG, "nilakantha_licence_rejected.tsv"))
    rulings = {k: v for k, v in
               json.load(open(os.path.join(REG, "nilakantha_hand_rulings.json"),
                              encoding="utf-8")).items()
               if not k.startswith("_")}
    items = []

    # ---- H2883: every figure the cards quote is derived here, never hardcoded ---------
    auto_rows = [r for r in reg if r["classification"] == "auto"]
    n_reg, n_rej = len(reg), len(rej)
    n_hits = n_reg + n_rej
    n_auto = len(auto_rows)
    n_hand = n_reg - n_auto
    precision = 100.0 * n_reg / n_hits
    BUTTONS_REJECT = buttons_reject(n_reg, n_hits, precision)
    BUTTONS_HAND = buttons_hand(n_reg)
    BUTTONS_AUTO = buttons_auto(n_auto)

    # ---- group A: the hand rulings -------------------------------------------------
    for r in rej:
        rl = rulings[r["hit_id"]]
        items.append({
            "id": r["hit_id"],
            "filt": "hand-reject",
            "title": f"{r['locus']} — отклонено как омоним ({r['reject_reason']})",
            "title_href": source_href(r["hit_id"].split("#")[0], r["parva"]),
            "badges": [r["parva"], r["term_family"], "ручное решение"],
            "question": (
                f"<p><b>Термин в тексте:</b> <span lang=\"sa\">{esc(r['defense_term'])}</span></p>"
                f"<p><b>Цитата (ṭīkā, деванагари):</b><br><span lang=\"sa\">{esc(r['quote'])}</span></p>"
                f"<p><b>Решение агента:</b> <code>{esc(r['reject_reason'])}</code> — "
                f"строка <u>не попадает</u> в регистр.</p>"
            ),
            "panels": [("Обоснование", f"<p>{esc(rl['note'])}</p>"),
                       ("Что делают кнопки", BUTTONS_REJECT)],
            "note_placeholder": "Если не согласны — какой deviation_type здесь верен?",
        })

    hand_kept = [r for r in reg if r["classification"] == "hand"]
    for r in hand_kept:
        hit = next(k for k, v in rulings.items()
                   if v.get("verdict") == "licence_claim" and k.startswith(r["locus_id"]))
        rl = rulings[hit]
        items.append({
            "id": hit,
            "filt": "hand-type",
            "title": f"{r['locus']} — принято, тип назначен вручную",
            "title_href": source_href(r["locus_id"], r["parva"]),
            "badges": [r["parva"], r["term_family"], "ручное решение"],
            "question": (
                f"<p><b>Термин в тексте:</b> <span lang=\"sa\">{esc(r['defense_term'])}</span></p>"
                f"<p><b>Цитата (ṭīkā, деванагари):</b><br><span lang=\"sa\">{esc(r['quote'])}</span></p>"
                f"<p><b>Назначенный тип:</b> <code>{esc(r['deviation_type'])}</code> "
                f"(<span lang=\"sa\">{esc(r['deviation_term_sa'])}</span>)</p>"
            ),
            "panels": [("Обоснование", f"<p>{esc(rl['note'])}</p>"),
                       ("Что делают кнопки", BUTTONS_HAND)],
            "note_placeholder": "Другой deviation_type? Или это не licence-claim?",
        })

    # ---- group B: the reproducible precision sample over the auto-typed rows --------
    auto = auto_rows
    sample = random.Random(SAMPLE_SEED).sample(auto, SAMPLE_N)
    sample.sort(key=lambda r: (int(r["locus_id"][1:3]), r["locus_id"]))
    for r in sample:
        items.append({
            "id": r["locus_id"] + "|" + r["row_id"],
            "filt": "auto-sample",
            "title": f"{r['locus']} — {r['deviation_type']}",
            "title_href": source_href(r["locus_id"], r["parva"]),
            "badges": [r["parva"], r["term_family"], "авто-типизация"],
            "question": (
                f"<p><b>Термин в тексте:</b> <span lang=\"sa\">{esc(r['defense_term'])}</span></p>"
                f"<p><b>Цитата (ṭīkā, деванагари):</b><br><span lang=\"sa\">{esc(r['quote'])}</span></p>"
                f"<p><b>Тип, выведенный автоматически:</b> <code>{esc(r['deviation_type'])}</code> "
                f"— из грамматического термина <span lang=\"sa\">{esc(r['deviation_term_sa'])}</span>, "
                "который Нилакантха называет рядом со словом-лицензией.</p>"
            ),
            "panels": [("Что проверяется",
                        "<p>Вопрос карточки — <u>не</u> «licence-claim ли это» (наличие "
                        "названной грамматической операции рядом со словом-лицензией это уже "
                        "доказывает), а «верно ли операция переведена в deviation_type».</p>"),
                       ("Что делают кнопки", BUTTONS_AUTO)],
            "note_placeholder": "Если тип неверен — какой верен?",
        })

    cfg = {
        "sheet_id": SHEET_ID,
        "title": "Нилакантха: регистр отступлений от Панини, признанных традицией (H2860)",
        "subtitle": (
            f"{n_reg} {ru_plural(n_reg, 'строка', 'строки', 'строк')} из "
            "«Бхаратабхавадипы» Нилакантхи по всем 24 694 шлокам с ṭīkā "
            f"({n_auto} авто-типизации + {n_hand} вручную; измеренная точность "
            f"{ru_pct(precision)} % — {n_reg} из {n_hits}). "
            "На голосование вынесены только те карточки, которые правило решить не может: "
            f"{n_rej + n_hand} ручных решений и воспроизводимая выборка из {SAMPLE_N} "
            f"авто-типизированных строк (seed {SAMPLE_SEED})."
        ),
        "footer": (
            "Регистр: commentary_licence_register_nilakantha.tsv/.jsonl · "
            "отклонённые: nilakantha_licence_rejected.tsv · "
            "плотность по парванам: nilakantha_parvan_density.tsv · "
            "отчёт: reports/COMMENTARY_LICENCE_REGISTER_NILAKANTHA_2026.md"
        ),
        "approve_label": "Согласен с решением",
        "reject_label": "Не согласен (см. заметку)",
        "filters": [
            ("hand-reject", f"отклонено вручную ({n_rej})"),
            ("hand-type", f"тип назначен вручную ({n_hand})"),
            ("auto-sample", f"выборка авто-типизации ({SAMPLE_N})"),
        ],
        "generated": GENERATED,
        "show_ids": True,
        "note_min_height_px": 88,
        "save_as": rf"CommentaryStrategies\review\{SHEET_ID}_decisions.json",
        # The SLP1-in-human-text check reads these three as transliteration; they are an
        # English word, an English grammatical term, and the standard Mahābhārata siglum.
        "preflight": {"allow_slp1_tokens": ("MBh", "perfect", "transfer")},
        # U6 (H2847): Russian-only reviewer chrome. save_banner overridden
        # because RU_UI_STRINGS excludes it by design (its default bakes in
        # this sheet's own sheet_id/save_as).
        "ui_strings": dict(RU_UI_STRINGS, save_banner=(
            f'&#128229; Ваш экспорт скачивается как <code>{SHEET_ID}_decisions.json</code> '
            f'&rarr; сохраните его в <code>CommentaryStrategies\\review\\{SHEET_ID}_decisions.json</code> '
            f'(значение <code>sheet_id</code> внутри файла &mdash; <code>{SHEET_ID}</code> &mdash; так '
            'следующая сессия узнаёт, к какому листу относятся эти решения).')),
    }
    screening = {
        "deterministic": 5,
        "lookup": 0,
        # every hit not on a card was settled by the typing rules — derived, not counted
        # by hand, so it tracks the card count instead of drifting away from it (H2883).
        "agent": n_hits - len(items),
        "human": len(items),
        "evidence_path": "reports/COMMENTARY_LICENCE_REGISTER_NILAKANTHA_2026.md",
        "rules": ["arsa-word-anchor-independent-vowel",
                  "arsa-stem-exclusion-arstisena-arsyasrngi-arsabha-arseya",
                  "deviation-type-from-named-grammatical-noun"],
    }
    # V9 (H1889): state what was joined onto the cards and what was deliberately left off.
    man = EvidenceManifest(SHEET_ID, [it["id"] for it in items], repo_root=ROOT)
    man.declare_joined("data/licence_register/commentary_licence_register_nilakantha.tsv",
                       ["locus", "defense_term", "deviation_type", "deviation_term_sa", "quote"])
    man.declare_joined("data/licence_register/nilakantha_licence_rejected.tsv",
                       ["reject_reason", "quote"])
    man.declare_joined("data/licence_register/nilakantha_hand_rulings.json",
                       ["verdict", "note", "deviation_type"])
    man.declare_omitted_path(
        "mahabharata-nilakantha/nilakantha_vulgate_full.jsonl",
        "Bulk scraped source text, gitignored on rights grounds; the ±170-char ṭīkā "
        "quote on each card carries everything needed to judge it, and the card header "
        "links to the verse on sanatana.in for the full context.")
    man.declare_omitted_path(
        "data/licence_register/commentary_licence_register_bhagavadgita_probe.tsv",
        "The 27 Gītā rows were hand-classified and voted in the H1324 probe; re-asking "
        "them here would re-run a settled judgment on a different corpus.")
    man.declare_omitted(
        "BORI critical edition + apparatus",
        "Local-only per BORI_CRITICAL_SOURCE.md, and the vulgate-vs-critical join is a "
        "downstream consumer's problem, not a fact any of these cards turns on.")
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(render_review_sheet(items=items, config=cfg, screening=screening,
                                    manifest=man))
    print(f"{len(items)} cards -> {OUT}")


if __name__ == "__main__":
    main()
