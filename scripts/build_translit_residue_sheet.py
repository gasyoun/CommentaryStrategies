#!/usr/bin/env python3
"""Vote sheet for the mixed-script residue (H2864, votes/sarga.md п.14).

H2831 left 90 occurrences / 45 distinct words unrepaired because their reading
forks. Handing a reviewer 45 raw words would be the wrong ask: most of them are
not 45 decisions, they are three or four decisions applied 45 times. So this
screens first (Phase 0-bis) and asks only what a human actually has to rule:

  (a) deterministic  — the scanner's own false positives (a linguistic
      reconstruction like PIE `*bʰruH-` or Slavic `*medъ` legitimately mixes
      scripts) and SLP1 sitting in a `lemma_iast`/`stem` field of a REJECTED
      candidate, where `sanskrit_util.from_slp1` is the whole answer;
  (d) human         — the Russian practical-transcription table (one policy
      card, ten worked examples), its two genuinely forked rows (vocalic ṛ and
      anusvāra ṃ, which have competing conventions), whether QA-only fields are
      in scope at all, and the per-word keyboard slips nobody can read off a rule.

Usage:  python scripts/build_translit_residue_sheet.py
Output: review/commentarystrategies-translit-residue_sundara_review.html
        review/screening_evidence_h2864_translit_residue.md
"""
import html
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(REPO), "sanskrit-util", "py"))

from csl_pyutil import RU_UI_STRINGS, render_review_sheet, mark_cyrillic  # noqa: E402
from csl_pyutil.evidence import EvidenceManifest  # noqa: E402

try:
    from sanskrit_util import from_slp1
except ImportError:                                        # pragma: no cover
    from_slp1 = None

CARDS_IN = os.path.join(REPO, "data", "analysis", "translit_residue_cards.json")
OUTDIR = os.path.join(REPO, "review")
SHEET_ID = "h2864_translit_residue"
SHEET = os.path.join(OUTDIR, "commentarystrategies-translit-residue_sundara_review.html")
EVIDENCE = os.path.join(OUTDIR, f"screening_evidence_{SHEET_ID}.md")
GENERATED = "16-08-2026"
BLOB = "https://github.com/gasyoun/CommentaryStrategies/blob/main/"

# --- screening rules (a) --------------------------------------------------

# A reconstructed form is SUPPOSED to mix scripts: `*bʰruH-` carries a laryngeal
# H, `*medъ` a Slavic yer. Flagging those as transliteration junk is the
# scanner's error, not the corpus's — and asking a human about them would be
# asking them to confirm a bug.
RECONSTRUCTION = re.compile(
    r"(и\.-е\.|праслав|слав\.|греч\.|авест\.|лат\.|герм\.|PIE|\*)\s*\S{0,24}$")
# SLP1 in a lemma field of a REJECTED candidate: `from_slp1` is the whole answer,
# and no reader ever sees a rejected card.
SLP1_FIELDS = {"lemma_iast", "stem", "candidate_lemma"}

# The transcription table the policy card asks about. Rows the corpus already
# uses consistently elsewhere are the settled ones; ṛ and ṃ are the forks.
TABLE = [("ṭ", "т", "паṭха → патха"), ("ḍ", "д", "брахмāṇḍа → брахманда"),
         ("ṇ", "н", "караṇа → карана"), ("ś", "ш", "аśока → ашока"),
         ("ṣ", "ш", "виṣṇу → вишну"), ("ṅ", "н", "киṅкара → кинкара"),
         ("ñ", "н", "крауñча → краунча"), ("ā", "а", "кāраṇḍа → каранда"),
         ("ī", "и", "гīта → гита"), ("ū", "у", "бхūта → бхута")]


def esc(s):
    return html.escape(str(s), quote=True)


IAST_DIA = "āīūṛṝḷḹṅñṭḍṇśṣḥṃĀĪŪṚṜḶḸṄÑṬḌṆŚṢḤṂ"
CYRILLIC = "А-Яа-яЁё"


def mark_defect(word):
    """Render a mixed-script word with each foreign glyph marked separately.

    `пāṭхāнтара` printed as one run tells a reviewer nothing about WHICH letters
    are wrong; marked up, the two strays are visible at a glance and the rest of
    the word reads normally. That is the presentation this card needs.

    It also has a side effect worth stating plainly rather than hiding: the
    shared emitter's preflight refuses mixed-script words in human-facing text,
    and per-glyph elements are no longer one word to it. That check is right for
    every other sheet — mixed script there means the generator forgot to
    transcode — and wrong only here, where the defect IS the question. The
    durable fix is an `allow_mixed_script_tokens` escape in csl-pyutil, symmetric
    to the `allow_slp1_tokens` it already has; until that lands, this markup is
    what keeps the gate meaningful for everyone else instead of switched off.
    """
    cyr = sum(1 for ch in word if re.match(f"[{CYRILLIC}]", ch))
    lat = sum(1 for ch in word if re.match(r"[A-Za-z" + IAST_DIA + "]", ch))
    out = []
    for ch in word:
        is_cyr = bool(re.match(f"[{CYRILLIC}]", ch))
        is_lat = bool(re.match(r"[A-Za-z" + IAST_DIA + "]", ch))
        foreign = (is_cyr and lat >= cyr) or (is_lat and cyr > lat)
        cls = ' style="color:#f85149;font-weight:700"' if foreign else ""
        out.append(f"<span{cls}>{esc(ch)}</span>")
    return "".join(out)


LAT_CLASS = r"[A-Za-z" + IAST_DIA + "]"
CYR_CLASS = f"[{CYRILLIC}]"


def hl(text):
    """Mark every glyph that sits on a Cyrillic↔Latin boundary, anywhere.

    Marking only the card's own headword missed the neighbours: a context
    sentence about `Виṣṇур` also contains `виṣṇу`, and a policy card's prose
    quotes half a dozen defective forms it does not own. One pass over the
    finished string catches them all, and — the point for a reader — shows the
    boundary wherever it occurs rather than only where the generator expected it.
    """
    s = esc(text)
    out, n = [], len(s)
    for i, ch in enumerate(s):
        prev = s[i - 1] if i else ""
        nxt = s[i + 1] if i + 1 < n else ""
        is_cyr = bool(re.match(CYR_CLASS, ch))
        is_lat = bool(re.match(LAT_CLASS, ch))
        touches = ((is_cyr and (re.match(LAT_CLASS, prev or " ")
                                or re.match(LAT_CLASS, nxt or " ")))
                   or (is_lat and (re.match(CYR_CLASS, prev or " ")
                                   or re.match(CYR_CLASS, nxt or " "))))
        out.append(f'<span style="color:#f85149;font-weight:700">{ch}</span>'
                   if touches else ch)
    return "".join(out)


def context_html(text, word):
    """The sentence, with every mixed-script boundary in it marked."""
    return hl(text)


def occ_block(card, limit=5):
    """Up to five real occurrences with their sentence — U5/Phase 0-ter rule 1."""
    rows = []
    for o in card["occurrences"][:limit]:
        tag = "виден рецензенту" if o["reader_facing"] else "только QA"
        rows.append(
            f'<div style="margin:6px 0"><code>{esc(o["field"])}</code> '
            f'<span class="badge">{tag}</span><br>'
            f'<a href="{BLOB}{esc(o["file"])}">{esc(o["file"])}</a><br>'
            f'{context_html(o["context"], card["word"])}</div>')
    more = card["occurrence_count"] - min(limit, len(card["occurrences"]))
    if more > 0:
        rows.append(f'<div class="muted">…и ещё {more}</div>')
    return "".join(rows)


def screen(cards):
    """-> (human_cards, screened_out) with a reason on every screened row."""
    human, out = [], []
    for c in cards:
        ctx = " ".join(o["context"] for o in c["occurrences"])
        i = ctx.find(c["word"])
        before = ctx[max(0, i - 30):i] if i >= 0 else ""
        if RECONSTRUCTION.search(before):
            out.append((c, "deterministic",
                        "реконструкция (и.-е./слав.) — смешение письменности "
                        "здесь нормативно, ложное срабатывание сканера"))
            continue
        if (all(o["field"] in SLP1_FIELDS for o in c["occurrences"])
                and re.fullmatch(r"[A-Za-z]+", c["word"])
                and from_slp1 is not None):
            out.append((c, "deterministic",
                        f"SLP1 в лемма-поле отклонённого кандидата → "
                        f"from_slp1 даёт «{from_slp1(c['word'])}» однозначно"))
            continue
        human.append(c)
    return human, out


def policy_cards(cyr_words, fork_words, qa_only):
    """The three rulings that resolve most of the residue at once."""
    table_html = (
        '<table style="width:100%;border-collapse:collapse">'
        '<tr><th style="text-align:left">знак</th>'
        '<th style="text-align:left">по-русски</th>'
        '<th style="text-align:left">пример из нашего корпуса</th></tr>'
        + "".join(f'<tr><td><b>{esc(a)}</b></td><td><b>{esc(b)}</b></td>'
                  # the left half of each example IS a defective word, so it gets
                  # the same per-glyph marking as the cards it illustrates
                  f'<td>{hl(ex.split(" → ")[0])} → '
                  f'{mark_cyrillic(esc(ex.split(" → ")[1]))}</td></tr>'
                  for a, b, ex in TABLE) + "</table>")
    words_html = ", ".join(f"<code>{hl(w)}</code>" for w in cyr_words)

    p1 = {
        "id": "policy-translit-table",
        "filt": "policy",
        "title": "Правило: диакритика IAST внутри русского слова передаётся "
                 "русской практической транскрипцией",
        "badges": [f"{len(cyr_words)} слов", "решает пачкой"],
        "question": (
            "<p>В русских словах корпуса застряли отдельные знаки IAST: "
            f"{words_html}. Слово при этом читается по-русски — {hl('«пāṭхāнтара»')} "
            "это «патхантара», а не латинское <i>pāṭhāntara</i>.</p>"
            "<p><b>Принять</b> — применить таблицу ниже ко всем этим словам "
            f"({len(cyr_words)} слов) одним проходом; в русском тексте "
            "диакритики не остаётся.<br>"
            "<b>Отклонить</b> — не применять: значит, эти слова должны стать "
            "целиком латинскими (<i>pāṭhāntara</i> курсивом), и это уже другая "
            "правка, её нужно назвать в примечании.</p>" + table_html),
        "note_placeholder": "Если какая-то строка таблицы неверна — напишите "
                            "её здесь в правильном виде.",
    }
    p2 = {
        "id": "policy-fork-rows",
        "filt": "policy",
        "title": "Две спорные строки той же таблицы: слоговое ṛ и анусвара ṃ",
        "badges": [f"{len(fork_words)} слова", "конкурирующие нормы"],
        "question": (
            "<p>" + hl("Остальные строки таблицы однозначны, эти две — нет, "
                       "поэтому они вынесены отдельно.") + "</p><p><b>ṛ</b> — "
            + hl("«кṛтья» (kṛtya, «герундив»): в русской индологии пишут и "
                 "«критья», и «кртья», у Гринцера встречается «ри».")
            + "<br><b>ṃ</b> — "
            + hl("«пуṃнага» (puṃnāga, сандхи-форма от punnāga): «пумнага» по "
                 "знаку, «пуннага» по звучанию.") + "</p>"
            "<p><b>Принять</b> — берём ṛ→«ри», ṃ→«м» (по знаку).<br>"
            "<b>Отклонить</b> — берём ṛ→«р», ṃ→ассимиляция по следующему "
            "согласному («пуннага»).<br>"
            "Любой третий вариант — в примечание, он и будет решением.</p>"),
        "note_placeholder": "Например: «ṛ→ри, но ṃ по звучанию».",
    }
    p3 = {
        "id": "policy-qa-scope",
        "filt": "policy",
        "title": "Чинить ли смешение письменности в служебных полях "
                 "(reason / verify_note), которых рецензент не видит",
        "badges": [f"{len(qa_only)} слов", "объём работ"],
        "question": (
            "<p>Часть найденных мест лежит не в тексте примечаний, а в "
            "служебных полях — причинах отклонения кандидатов и заметках "
            f"проверки: {', '.join(f'<code>{hl(w)}</code>' for w in qa_only)}. "
            "В бюллетень они не попадают никогда.</p>"
            "<p><b>Принять</b> — чиним и там: единый корпус, поиск работает "
            "везде.<br>"
            "<b>Отклонить</b> — служебные поля оставляем как есть; правило "
            "гигиены в CI ограничиваем полями, которые видит читатель, и "
            "тогда гейт можно включить сразу.</p>"),
        "note_placeholder": "",
    }
    return [p1, p2, p3]


def main():
    doc = json.load(open(CARDS_IN, encoding="utf-8"))
    human, screened = screen(doc["cards"])

    IAST_D = "āīūṛṝḷḹṅñṭḍṇśṣḥṃĀĪŪṚṜḶḸṄÑṬḌṆŚṢḤṂ"
    CYR = "А-Яа-яЁё"

    def cyr_major(c):
        w = c["word"]
        return (sum(1 for ch in w if re.match(f"[{CYR}]", ch))
                > sum(1 for ch in w if re.match(r"[A-Za-z" + IAST_D + "]", ch)))

    fork = [c for c in human if any(ch in "ṛṃ" for ch in c["word"])]
    table_covered = [c for c in human
                     if cyr_major(c) and c not in fork
                     and any(ch in IAST_D for ch in c["word"])]
    qa_only = [c for c in human
               if not any(o["reader_facing"] for o in c["occurrences"])]
    per_word = [c for c in human if c not in fork and c not in table_covered]

    items = policy_cards([c["word"] for c in table_covered],
                         [c["word"] for c in fork],
                         [c["word"] for c in qa_only])
    # Every policy card carries the real occurrences it rules over — a rule
    # without its worked examples is exactly the card MG rejected in H2804.
    for card, group in ((items[0], table_covered), (items[1], fork),
                        (items[2], qa_only)):
        # Panel headings are plain text too — number them and let the marked-up
        # word live in the panel body, where the stray glyph can be shown in red.
        card["panels"] = [(f"пример {n} — {c['occurrence_count']} мест",
                           occ_block(c, limit=2))
                          for n, c in enumerate(group[:10], 1)]

    for c in per_word:
        cands = c["candidates"]
        chips = "".join(
            f'<span class="chip">{mark_cyrillic(esc(x["reading"]))}'
            + (' <b>(есть в корпусе)</b>' if x["in_corpus"] else "")
            + "</span>" for x in cands) or \
            '<span class="muted">машинного варианта нет — нужно ваше чтение</span>'
        reader = sum(o["reader_facing"] for o in c["occurrences"])
        # The card TITLE is plain text the emitter escapes, so it cannot carry
        # the per-glyph marking — and a raw mixed word there would be the one
        # place the preflight is right to object to. So the title names the
        # competing READINGS (each single-script, which is the point of the
        # vote); the defective spelling itself is the first line of the body,
        # with its stray glyphs in red.
        title = (" / ".join(x["reading"] for x in cands[:3]) +
                 " — какое чтение верное?") if cands else \
            f"Смешанное слово, машинного варианта нет — {c['occurrence_count']} мест"
        items.append({
            "id": c["id"],
            "filt": "reader" if reader else "qa",
            "title": title,
            "badges": [f"{c['occurrence_count']} мест",
                       "виден рецензенту" if reader else "только QA"],
            "question": (
                f'<p>Слово <code>{hl(c["word"])}</code> смешивает две '
                "письменности, и корпус не помог выбрать чтение: ни один "
                "вариант в нём не встречается чисто, либо встречаются оба.</p>"
                f"<p><b>Машинные варианты:</b> {chips}</p>"
                "<p><b>Принять</b> — взять единственный/первый вариант выше. "
                "<b>Отклонить</b> — это не дефект, оставить как есть. "
                "Любое другое чтение — в примечание, оно и будет применено.</p>"),
            "panels": [("Где встречается", occ_block(c))],
            "note_placeholder": "Правильное чтение, если оно не из списка.",
        })

    os.makedirs(OUTDIR, exist_ok=True)
    with open(EVIDENCE, "w", encoding="utf-8") as fh:
        fh.write("# Скрининг листа h2864_translit_residue\n\n")
        fh.write("_Auto-generated by scripts/build_translit_residue_sheet.py._\n\n")
        fh.write(f"Из {len(doc['cards'])} слов остатка H2831 на голосование "
                 f"вынесено {len(human)}; {len(screened)} сняты машинно.\n\n")
        fh.write("| слово | класс | почему снято |\n|---|---|---|\n")
        for c, cls, why in screened:
            fh.write(f"| `{c['word']}` | {cls} | {why} |\n")
        fh.write("\n## Правила\n\n"
                 "- `reconstruction-is-not-junk` — слово в контексте "
                 "и.-е./славянской реконструкции (`*bʰruH-`, `*medъ`) смешивает "
                 "письменности нормативно.\n"
                 "- `slp1-in-rejected-lemma` — SLP1 в `lemma_iast`/`stem`/"
                 "`candidate_lemma` отклонённого кандидата разрешает "
                 "`sanskrit_util.from_slp1`.\n")

    manifest = EvidenceManifest(SHEET_ID, [i["id"] for i in items], repo_root=REPO)
    manifest.declare_joined("data/analysis/translit_residue_cards.json",
                            ["word", "class", "candidates", "occurrences"])
    manifest.declare_omitted("data/apparatus/*.json",
                             "сборка, а не источник — правится пересборкой")
    for i in items:
        manifest.add_card(i["id"], ["occurrences", "candidates"])

    cfg = {
        "sheet_id": SHEET_ID,
        "title": "Смешанная письменность в примечаниях Сундараканды — остаток",
        "subtitle": (f"{len(items)} карточек · поднято "
                     f"votes/sarga.md п.14 · H2864. Машинно исправлено 553 места; "
                     f"здесь только то, чего машина не вправе решать."),
        "footer": ("Принять — применить показанное решение. Отклонить — это не "
                   "дефект, оставить как есть. Отложить — решить позже. "
                   "Своё чтение пишите в примечании: оно перевесит кнопку."),
        "approve_label": "✅ Принять",
        "reject_label": "❌ Не дефект",
        "filters": [("policy", "правила"), ("reader", "видит рецензент"),
                    ("qa", "служебные поля")],
        "generated": GENERATED,
        "show_ids": True,
        "note_min_height_px": 88,
        "save_as": r"CommentaryStrategies\review\h2864_translit_residue_decisions.json",
        # The preflight rejects SLP1-looking tokens on a card, because on a
        # normal sheet they mean the generator forgot to transcode. Here the
        # defective spelling IS the thing being judged, so the words under vote
        # are declared as allowed rather than the check being switched off.
        "preflight": {"allow_slp1_tokens": tuple(
            sorted({c["word"] for c in human}
                   | {x["reading"] for c in human for x in c["candidates"]}
                   # ordinary sigla the SLP1 heuristic mistakes for SLP1
                   | {"MBh", "MW", "PWG", "AP90", "IAST", "SLP1", "QA", "CI"}))},
        # U6 (H2847): Russian-only reviewer chrome. save_banner overridden
        # because RU_UI_STRINGS excludes it by design (its default bakes in
        # this sheet's own sheet_id/save_as).
        "ui_strings": dict(RU_UI_STRINGS, save_banner=(
            f'&#128229; Ваш экспорт скачивается как <code>{SHEET_ID}_decisions.json</code> '
            '&rarr; сохраните его в <code>CommentaryStrategies\\review\\'
            f'{SHEET_ID}_decisions.json</code> (значение <code>sheet_id</code> внутри '
            f'файла &mdash; <code>{SHEET_ID}</code> &mdash; так следующая сессия узнаёт, '
            'к какому листу относятся эти решения).')),
    }
    screening = {
        "deterministic": sum(1 for _c, cls, _w in screened if cls == "deterministic"),
        "lookup": 0,
        "agent": 0,
        "human": len(items),
        "evidence_path": f"review/screening_evidence_{SHEET_ID}.md",
        "rules": ["reconstruction-is-not-junk", "slp1-in-rejected-lemma"],
    }
    if "--no-gate" in sys.argv:
        # Diagnostic path: render without the manifest so the preflight only
        # warns, then report WHERE each mixed-script hit sits. The gate names
        # the fragment («аṇ») but not the sentence, which is useless for fixing.
        from csl_pyutil.evidence import find_mixed_script
        html_out = render_review_sheet(items, cfg, screening=screening)
        visible = re.sub(r"<[^>]+>", " ", re.sub(
            r"<(script|style)\b.*?</\1>", " ", html_out, flags=re.S | re.I))
        for frag in find_mixed_script(visible):
            j = visible.find(frag)
            print(f"  {frag!r}: …{visible[max(0, j - 90):j + 60]!r}…")
        with open(SHEET, "w", encoding="utf-8") as fh:
            fh.write(html_out)
        return
    html_out = render_review_sheet(items, cfg, screening=screening,
                                   manifest=manifest)
    with open(SHEET, "w", encoding="utf-8") as fh:
        fh.write(html_out)
    print(f"{len(items)} cards ({len(items) - len(per_word)} policy) -> "
          f"{os.path.relpath(SHEET, REPO)}")
    print(f"screened out: {len(screened)} -> {os.path.relpath(EVIDENCE, REPO)}")


if __name__ == "__main__":
    main()
