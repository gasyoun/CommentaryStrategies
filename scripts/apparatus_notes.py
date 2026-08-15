#!/usr/bin/env python3
"""Note shaping for the apparatus ballot — H2830, answering votes/sarga.md.

`build_sarga_apparatus.py` used to hand the ballot each tier-1 note as one
undifferentiated `raw_text` blob. Kostina's own prose, her service reminders to
herself, and the machine's «желательно прокомментировать» stubs all ran together
in a single paragraph, which is what produced the reviewer's п.5, п.13 and п.17:

    надо выделить [Е. Костина] — потому что в печатном тексте этого не будет
    Комм.[Claude.AI — желательно] ? [кат.5 — текстология] — убрать
    почему не завершено и не стоит точка в конце?

They are not typography complaints. Three kinds of text with three different
fates — one goes to print, one never does, one is a proposal awaiting a verdict —
had no representation in the data at all, so the page had nothing to style them
by. This module gives them one.

It also builds the Cologne deep links behind п.18 («почему не кликабельно на
Cologne?») and translates the three English `source` strings behind п.9 («только
на русском»).
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)

# The canonical transcoder, per the org SHARED_CODE rule: one IAST->SLP1 for the
# whole org, never a local re-implementation. Absent sibling clone -> no links,
# never a wrong link.
sys.path.insert(0, os.path.join(os.path.dirname(REPO), "sanskrit-util", "py"))
try:
    from sanskrit_util import to_slp1
except ImportError:                                        # pragma: no cover
    to_slp1 = None

# ---------------------------------------------------------------- tier-1 split

# A tier-1 blob is a run of segments, each opened by a bracketed author tag.
# `Комм.` is a leftover prefix the generator once emitted before the machine's
# tag; п.17 asks for it gone, so it is consumed here rather than displayed.
TIER1_MARK = re.compile(r"(Комм\.\s*)?\[(Е\.\s*Костина|Claude\.AI\s*[—-]\s*[^\]]+)\]")
SUG_KIND = re.compile(r"^\s*\??\s*\[\s*(термин|кат\.\s*\d+[^\]]*)\s*\]\s*")
SUG_ACC = re.compile(r"^\s*\((учтено|не\s+учтено)\)\s*")
OMIT_LEMMA = re.compile(r"^\s*«([^»]+)»\s*")
# «введено в :» with nothing between the preposition and the colon is a template
# whose source reference was never filled in — 18 of them shipped to the ballot.
UNFINISHED = re.compile(r"(введено\s+в\s*:\s*$)|(:\s*$)|(введено\s+в\s*$)")


# п.17: «Написано дурно. Такой и подобные переписать.» The machine emitted a
# handful of fixed sentences into the translator's file, and they read like
# machine output — a dash where a clause belongs, no finite verb, no full stop.
# Rewriting them at parse time fixes every past occurrence at once; the
# generator that produced them is a separate repair (H2830 follow-up).
POLISH = {
    "Место отмечено как требующее комментария — возможны расхождения редакций":
        "Здесь возможны расхождения между редакциями текста, поэтому место "
        "требует комментария",
}


def polish(text):
    for bad, good in POLISH.items():
        text = text.replace(bad, good)
    return text


def _strength(tag):
    """'Claude.AI — желательно' -> 'желательно'."""
    m = re.search(r"[—-]\s*(.+)$", tag)
    return m.group(1).strip() if m else ""


def segment_tier1(raw):
    """Split a tier-1 `raw_text` into prose / service notes / machine proposals.

    Returns {"note_ru", "service": [...], "suggestions": [...]}.
    A blob with no markers comes back as pure prose, which is the common case.
    """
    raw = (raw or "").strip()
    marks = list(TIER1_MARK.finditer(raw))
    if not marks:
        return {"note_ru": raw, "service": [], "suggestions": []}

    prose = raw[:marks[0].start()].strip()
    service, suggestions = [], []
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(raw)
        body = raw[m.end():end].strip()
        tag = m.group(2)
        if tag.startswith("Е."):
            lemma = ""
            lm = OMIT_LEMMA.match(body)
            if lm:
                lemma = lm.group(1)
                body = body[lm.end():].strip()
            # п.13: «Опущено -> опущено, тут и везде, не надо рябить заглавными
            # буквами» — the capital is an artefact of the lemma being lifted out
            # in front of it, not a sentence start.
            body = re.sub(r"^Опущено", "опущено", body)
            service.append({
                "author": "Е. Костина",
                "lemma_iast": lemma,
                "kind": "omission" if "пущено" in body else "note",
                "text": body,
            })
            continue
        kind, accounted = "", ""
        km = SUG_KIND.match(body)
        if km:
            kind = re.sub(r"\s+", " ", km.group(1)).strip()
            body = body[km.end():].strip()
        am = SUG_ACC.match(body)
        if am:
            accounted = re.sub(r"\s+", " ", am.group(1)).strip()
            body = body[am.end():].strip()
        body = polish(body)
        incomplete = bool(UNFINISHED.search(body)) or not body
        if not incomplete and not body.endswith((".", "!", "?", "»")):
            body += "."                      # п.17: «не стоит точка в конце»
        suggestions.append({
            "author": "Claude.AI",
            "strength": _strength(tag),
            "kind": kind,
            "accounted": accounted,
            "text": body,
            "incomplete": incomplete,
        })
    return {"note_ru": prose, "service": service, "suggestions": suggestions}


# ------------------------------------------------------------- Cologne linking

CDSL = ("https://www.sanskrit-lexicon.uni-koeln.de/scans/{scan}/2020/web/"
        "webtc/indexcaller.php?key={key}")
# Scan directory per dictionary siglum, as served by CDSL today.
SCANS = {"MW": "MWScan", "MWE": "MWEScan", "APTE": "AP90Scan", "AP90": "AP90Scan",
         "AP": "APScan", "PW": "PWScan", "PWG": "PWGScan", "GRA": "GRAScan",
         "BEN": "BENScan", "CAE": "CAEScan"}
# `dic_mw:kAmarUpin` — the key is already SLP1, so it is used verbatim.
DIC_REF = re.compile(r"\bdic_(\w+):([A-Za-z]+)")
SV_REF = re.compile(r"\b(MW|MWE|Apte|AP90|AP|PW|PWG|GRA)\s+s\.\s?v\.\s*([^;,.]+)")


def source_links(source):
    """'MW s.v. amarāvatī; Apte s.v. amarāvatī' -> [{label, url}] (п.18).

    Both forms the corpus uses are covered: the human `s.v.` citation and the
    machine `dic_mw:<SLP1 key>` provenance string.
    """
    if not source:
        return []
    out, seen = [], set()
    for m in DIC_REF.finditer(source):
        scan = SCANS.get(m.group(1).upper())
        if not scan:
            continue
        key = m.group(2)
        url = CDSL.format(scan=scan, key=key)
        if url not in seen:
            seen.add(url)
            out.append({"label": f"{m.group(1).upper()} {key}", "url": url})
    for m in SV_REF.finditer(source):
        siglum = m.group(1).upper()
        scan = SCANS.get(siglum)
        headword = m.group(2).strip()
        if not scan or not headword or to_slp1 is None:
            continue
        key = to_slp1(headword)
        if not re.fullmatch(r"[A-Za-z]+", key):
            continue                      # not a clean headword — no fake link
        url = CDSL.format(scan=scan, key=key)
        if url not in seen:
            seen.add(url)
            out.append({"label": f"{m.group(1)} s.v. {headword}", "url": url})
    return out


# ------------------------------------------------------- Russian source labels

# п.9: «только на русском, без английского языка нужно». These three strings are
# machine provenance, not citations — they are the ONLY English left in the
# reader-facing `Источник:` line, and they cover 95 of its occurrences.
SOURCE_RU = {
    "first occurrence in кн. V; Grintser index / commentators where cited "
    "(verse-level, soft)":
        "первое вхождение в кн. V; указатель Гринцера / комментаторы, где "
        "процитировано (привязка к стиху, нестрогая)",
    "gazetteer (analysis §09б / formulas tt.1-2) — first occurrence in кн. V "
    "(verse-level, soft)":
        "указатель имён и названий (анализ §09б / формулы тт. 1–2) — первое "
        "вхождение в кн. V (привязка к стиху, нестрогая)",
    "parallel-text divergence (verse-level, soft)":
        "расхождение параллельных текстов (привязка к стиху, нестрогая)",
    "Phase-2: комментаторский диалог (Tilaka/Bhūṣaṇa/Śiromaṇi; Gita Supersite, "
    "CC BY 4.0)":
        "фаза 2: диалог комментаторов (Тилака / Бхушана / Широмани; Gita "
        "Supersite, CC BY 4.0)",
}


def ru_source(source):
    """Russify the machine provenance strings; leave real citations alone."""
    s = (source or "").strip()
    return SOURCE_RU.get(s, s)


# ------------------------------------------------- Russian numeral agreement

def shlok_plural(n):
    """2 шлоки / 5 шлок — the ballot printed «(2 шлок)» for every count."""
    n = abs(int(n))
    if 11 <= n % 100 <= 14:
        return "шлок"
    return {1: "шлока", 2: "шлоки", 3: "шлоки", 4: "шлоки"}.get(n % 10, "шлок")


COUNT_RE = re.compile(r"\((\d+)\s+шлок[а-я]*\)")


def fix_shlok_count(text):
    return COUNT_RE.sub(lambda m: f"({m.group(1)} {shlok_plural(m.group(1))})",
                        text or "")
