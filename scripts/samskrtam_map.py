#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Маппинг CTS-URN примечаний на ID параллельного корпуса samskrtam.ru (шаг B2 дорожной карты).

Каждому примечанию ставится в соответствие якорь (id) страницы параллельного
корпуса и полный URL вида

    https://samskrtam.ru/parallel-corpus/<страница>#<якорь>

Схемы идентификаторов корпуса (сверены с HTML страниц, 2026-08-28):

    Рамаяна, кн. V (Сундараканда, подстрочник Леонова):
        стих  id="<sarga>.<стих>"   (напр. id="1.1"); глава id="<sarga>"
    Рамаяна, кн. I–III (пер. Гринцера) и Махабхарата, парвы 1–18:
        глава id="chapter_<sarga|adhyāya>"; постиховых якорей страница не несёт
    Упанишады (Сыркин) и Рам. кн. IV, VI, VII:
        в корпусе отсутствуют → status "not-in-corpus"

Расхождение нумерации (наш URN — нумерация критического издания / издания
переводчика, страница корпуса — своя разбивка) не маскируется: такие записи
получают status "anchor-missing" с ожидаемым якорем — это сигнал сверки
адресов, а не готовая ссылка. Запуск:

    python scripts/samskrtam_map.py --check   # регенерация + сравнение с файлом (CI)
    python scripts/samskrtam_map.py --emit    # записать data/samskrtam_id_map.json
"""

import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
OUT = DATA / "samskrtam_id_map.json"

BASE = "https://samskrtam.ru/parallel-corpus/"
VERIFIED_DATE = "2026-08-28"

RAM_PAGES = {
    "1": "01_ramayana-balakanda.html",
    "2": "02_ramayana-ayodhyakanda.html",
    "3": "03_ramayana-aranyakanda.html",
    "5": "05_ramayana-sundarakanda2026.html",
}
MBH_PAGES = {
    "1": "01_mahabharata-adiparva.html",
    "2": "02_mahabharata-sabhaparva.html",
    "3": "03_mahabharata-vanaparva.html",
    "4": "04_mahabharata-virataparva.html",
    "5": "05_mahabharata-udyogaparva.html",
    "6": "06_mahabharata-bhishmaparva.html",
    "7": "07_mahabharata-dronaparva.html",
    "8": "08_mahabharata-karnaparva.html",
    "9": "09_mahabharata-shalyaparva.html",
    "10": "10_mahabharata-sauptikaparva.html",
    "11": "11_mahabharata-striparva.html",
    "12": "12_mahabharata-shantiparva.html",
    "13": "13_mahabharata-anushasanaparva.html",
    "14": "14_mahabharata-ashvamedhikaparva.html",
    "15": "15_mahabharata-ashramavasikaparva.html",
    "16": "16_mahabharata-mausalaparva.html",
    "17": "17_mahabharata-mahaprasthanikaparva.html",
    "18": "18_mahabharata-svargarohanikaparva.html",
}
# Страницы, где каждый ожидаемый якорь был сверен с реальным HTML (а не только
# existence-проверка страницы): якоря вне этого списка не считаются доказанными.
ANCHOR_VERIFIED = {
    "01_ramayana-balakanda.html",
    "05_ramayana-sundarakanda2026.html",
    "01_mahabharata-adiparva.html",
    "06_mahabharata-bhishmaparva.html",
    "16_mahabharata-mausalaparva.html",
    "17_mahabharata-mahaprasthanikaparva.html",
    "18_mahabharata-svargarohanikaparva.html",
}

# Адреса, для которых сверка с HTML (ANCHOR_VERIFIED) НЕ нашла якоря: нумерация
# нашего URN (критическое издание / издание переводчика) расходится с разбивкой
# страницы корпуса. Ключ (work, book) → множество ожидаемых якорей.
# Обновляется только по факту новой постиховой сверки.
KNOWN_ANCHOR_MISSING = {
    ("ramayana", "1"): {"chapter_80"},
    ("ramayana", "5"): {"31.44"},
    ("mahabharata", "6"): {"chapter_115", "chapter_120"},
    ("mahabharata", "18"): {"chapter_6"},
}

URN_RE = re.compile(r"^urn:cts:sanskritLit:([A-Za-z]+):(\d+(?:\.\d+)*)$")


def map_urn(urn):
    """URN → запись маппинга (status: mapped / anchor-missing / not-in-corpus / unparseable)."""
    rec = {"urn": urn, "status": None, "granularity": None, "anchor": None, "url": None}
    m = URN_RE.match(urn or "")
    if not m:
        rec["status"] = "unparseable"
        return rec
    work, passage = m.group(1), m.group(2)
    rec["work"] = work
    rec["passage"] = passage
    parts = passage.split(".")

    if work == "ramayana":
        book, sarga = parts[0], parts[1]
        book_key = book
        if book == "5":
            page, anchor, gran = RAM_PAGES["5"], f"{sarga}.{parts[2]}", "verse"
        elif book in RAM_PAGES:
            page, anchor, gran = RAM_PAGES[book], f"chapter_{sarga}", "chapter"
        else:
            rec["status"] = "not-in-corpus"
            rec["note"] = "книга Рамаяны вне параллельного корпуса (страницы нет)"
            return rec
    elif work == "mahabharata":
        parva, adhyaya = parts[0], parts[1]
        book_key = parva
        page, anchor, gran = MBH_PAGES[parva], f"chapter_{adhyaya}", "chapter"
    else:
        rec["status"] = "not-in-corpus"
        rec["note"] = "произведение вне параллельного корпуса (корпус: Ригведа, Атхарваведа, Рамаяна I–III/V, Мхб. I–XVIII)"
        return rec

    rec["granularity"] = gran
    rec["anchor"] = anchor
    rec["page"] = page
    rec["url"] = f"{BASE}{page}#{anchor}"
    if anchor in KNOWN_ANCHOR_MISSING.get((work, book_key), set()):
        rec["status"] = "anchor-missing"
        rec["note"] = (
            "якоря с таким id на странице корпуса нет (сверка с HTML "
            f"{VERIFIED_DATE}): нумерация URN расходится с разбивкой страницы — сигнал к сверке адресов"
        )
    else:
        rec["status"] = "mapped"
    return rec


def build():
    notes = []
    for f in sorted(DATA.glob("*_markup_50.json")):
        for n in json.loads(f.read_text(encoding="utf-8")):
            rec = {"comment_id": n["comment_id"], "translator": n["translator"]}
            rec.update(map_urn(n.get("urn", "")))
            rec.pop("urn", None)
            rec["urn"] = n.get("urn", "")
            notes.append(rec)

    cov = {}
    for rec in notes:
        cov[rec["status"]] = cov.get(rec["status"], 0) + 1

    return {
        "provenance": {
            "corpus": "samskrtam.ru — Параллельный санскритско-русский корпус (Общество ревнителей санскрита)",
            "corpus_base": BASE,
            "generated_by": "scripts/samskrtam_map.py --emit (деривация из urn, не ручная разметка)",
            "verification_date": VERIFIED_DATE,
            "verification": (
                "Все задействованные страницы корпуса подтверждены GET-запросом (на этом сервере "
                "HEAD 200 / HTTP 200 не доказательство существования: отсутствующая страница "
                "отдаёт главную корпуса, ровно 33 857 байт). Постиховая сверка якорей выполнена на "
                "страницах: " + ", ".join(sorted(ANCHOR_VERIFIED)) +
                " (для 05_ramayana-sundarakanda2026.html — по сохранённой копии "
                "ramayana-leonov/Рамаяна. Книга 5. Сундараканда 2026.html + живая копия); "
                "остальные страницы existence-only. Страница кн. V отсутствует в "
                "index_ramayana.html, но доступна и является каноническим URL корпуса для "
                "Сундараканды. status=anchor-missing не фиктивен: нумерация нашей выборки "
                "(крит. издание) расходится с разбивкой страницы корпуса — сигнал к сверке адресов."
            ),
            "id_schemes": {
                "ramayana_kanda5_verse": 'id="<sarga>.<стих>"',
                "chapter_level": 'id="chapter_<sarga|adhyāya>"',
            },
        },
        "coverage": {
            "total_notes": len(notes),
            "by_status": dict(sorted(cov.items())),
        },
        "notes": notes,
    }


def render(doc):
    return json.dumps(doc, ensure_ascii=False, indent=2) + "\n"


def main():
    doc = build()
    text = render(doc)
    if "--emit" in sys.argv:
        OUT.write_text(text, encoding="utf-8")
        cov = doc["coverage"]
        print(f"OK {OUT.name}: {cov['total_notes']} notes, by_status={cov['by_status']}")
    else:
        if not OUT.exists():
            sys.exit(f"FAIL {OUT.name}: нет файла; запустите с --emit")
        committed = OUT.read_text(encoding="utf-8")
        if committed != text:
            sys.exit(f"FAIL {OUT.name}: расходится с регенерацией — запустите scripts/samskrtam_map.py --emit и закоммитьте")
        cov = doc["coverage"]
        print(f"OK {OUT.name}: parity, {cov['total_notes']} notes, by_status={cov['by_status']}")


if __name__ == "__main__":
    main()
