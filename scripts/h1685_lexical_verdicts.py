#!/usr/bin/env python3
"""H1685 — record the Opus adjudication of the 142 contested lexical cards.

The lexical queue already carried a Sonnet-5 judge pass (H276 WS-2). The 469
uncontested `keep` cards were rule-decided; what reaches here is every card the
judge did NOT keep, plus every `keep` whose independent evidence disagreed.

The adjudication was done by reading the cards; this script is how the reading
is written down reproducibly rather than as 142 hand-copied JSON objects. Each
group carries the finding that decided it, and every card that departs from its
group's finding is named in EXCEPTIONS with its own reason. Nothing is decided
by the group rule alone that was not read.

What the reading established, group by group:

flag_anchor (43) — CONFIRMED, 41 of them. The judge quotes each śloka's actual
    text showing the lemma is not in it, and the independent anchor re-search
    agrees; for 10 cards the re-search additionally names the śloka the note
    belongs to, which the judge could only guess at. Two are not anchor faults
    at all and are reclassified (see EXCEPTIONS).
reject (32) — CONFIRMED, 31 of them. These are fabricated etymologies and
    invented source-attributions. Five were re-verified directly against
    dic_mw.jsonl during this pass and every one held: vimada (MW 'free from
    intoxication' — the note inverts it to 'drunk'), vāyasa (MW 'fr. vayas',
    not vāyu), karṇikāra (MW has no funerary sense; the note attributes one to
    MW), koka (MW gives a flat 'a wolf', and cites this very passage, with no
    solitary-prey distinction), śātakumbha (MW derives it fr. śata-kumbhā, not
    from a hundred-pot refining process).
park (21) — CONFIRMED. Transparent compounds whose content the подстрочник
    already states, several verbatim; the notes re-dress the crib in
    terminology without adding a fact. non_triviality gate, not faithfulness.
edit (23) — CONFIRMED. Two recurring, fixable defects: corrupted characters
    spliced into the Russian ('dolce', 'viमāna', 'экувেṇI', 'марша&нīя') and
    precise citations that cannot be checked (MBh 1.212, Arthaśāstra 2.20,
    MBh 5.140, Rām 3.46.26) stated without hedge.
keep-with-anchor-flag (20) — ACCEPTED, all. Here MY check is the one that is
    wrong: the lemma is in the verse behind sandhi (uḍurāṭ in `ivoḍurāṭ`), in a
    variant stem (śāradāmbudhara for ambuda, airāvata for erāvata, maurkhyāt
    for mūrkhatā) or in a compound (`ekaveṇīdharā`, `uttarīyāṇi`). This is the
    measured recall limit of the anchor test and is reported as such.
keep-with-duplicate-flag (3) — ACCEPTED. The duplicate is a co-located note
    from another layer on the same lemma, not a second copy of this note.

Usage: python scripts/h1685_lexical_verdicts.py
"""
import sys
import os
import json
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
AD = os.path.join(REPO, "data", "analysis", "h1685_adjudication")
OUT = os.path.join(AD, "opus_verdicts_lexical.json")

ADJUDICATOR = "Opus 5 1M (claude-opus-5[1m])"
ANCHOR_OK = {"exact", "stem", "commentary_only"}

GROUP_VERDICT = {
    "flag_anchor": ("flag_anchor",
                    "Лемма не стоит в этом стихе: судья приводит текст шлоки, "
                    "независимый перепоиск подтверждает. Содержание заметки при "
                    "этом обычно верно — требуется перепривязка, а не снятие."),
    "reject": ("reject",
               "Провален шлюз faithfulness §3.4: выдуманная этимология либо "
               "приписанное источнику утверждение, которого в нём нет. Пять "
               "таких заявлений перепроверены напрямую по dic_mw.jsonl в этом "
               "проходе — все подтвердились."),
    "park": ("park",
             "Провален шлюз non_triviality: содержание уже дано подстрочником "
             "(часто дословно). Не отклоняется — заметка не ложна, а избыточна."),
    "edit": ("edit",
             "Содержание годно, дефект устраним: испорченные символы в русском "
             "тексте либо непроверяемая точная ссылка, поданная без оговорки."),
    "keep_anchor": ("accept",
                    "Принято вопреки МОЕЙ пометке: лемма в стихе есть — за "
                    "сандхи, в вариантной основе или внутри композита. Это "
                    "предел полноты якорного теста, а не дефект заметки."),
    "keep_dup": ("accept",
                 "Принято: пометка duplicate — это соседняя заметка ДРУГОГО "
                 "слоя на ту же лемму, а не второй экземпляр этой."),
}

# Cards whose verdict departs from their group's finding, each with its reason.
EXCEPTIONS = {
    "V.68.13|upādhi": ("edit",
        "Не якорная ошибка, а неверная лемма. В стихе стоит upadhinā (upadhi, "
        "краткое a) — «обман, уловка»; заметка этимологизирует upādhi (вриддхи) "
        "— «условие, ограничение», позднейший ведантический термин. Это две "
        "разные словарные статьи MW. Правка: перевести заметку на upadhi и "
        "снять ведантический материал; сама сцена (золотой олень) описана верно."),
    "V.1.101|hiraṇyanābha": ("edit",
        "Не якорная ошибка, а несогласованный заголовок: в стихе hiraṇyagarbho "
        "maināko, и сама заметка это цитирует, противореча собственной лемме "
        "hiraṇyanābha. Правка: переименовать лемму в hiraṇyagarbha и заменить "
        "«золотопупый» на «золотоутробный»."),
    "V.54.26|stanaṃdhaya": ("edit",
        "ПЕРЕСМОТРЕНО против судьи. Судья отклонил заметку за корень: «√dhā "
        "значит „класть“, а сосать — √dhē». Но у Уитни dhā(y)/dhī «сосать» "
        "стоит отдельным корнем-омонимом, и ссылка заметки (Whitney #681) "
        "может относиться именно к нему; MW при этом подтверждает и разбор, и "
        "значение («stanaṃdhaya — sucking the breast»). Смешение омонимов — "
        "устранимая неточность, а не ложное содержание: правка — явно развести "
        "√dhā «класть» и √dhā(y)/√dhē «сосать»."),
}


def load(p):
    with open(p, encoding="utf-8") as fh:
        return json.load(fh)


def group_of(card):
    j = (card.get("judge") or {}).get("verdict")
    e = card["evidence"]
    if j != "keep":
        return j
    if e.get("duplicate_in_book"):
        return "keep_dup"
    return "keep_anchor"


def main():
    pk = load(os.path.join(AD, "packet_lexical.json"))
    verdicts = []
    for c in pk["cards"]:
        g = group_of(c)
        e = c["evidence"]
        if c["key"] in EXCEPTIONS:
            verdict, reason = EXCEPTIONS[c["key"]]
            disposition = "OVERTURNED"
        else:
            verdict, reason = GROUP_VERDICT[g]
            disposition = ("confirmed" if verdict == (c.get("judge") or {}).get("verdict")
                           else "OVERTURNED" if g.startswith("keep") is False
                           else "confirmed")
        cited = [f"judge={(c.get('judge') or {}).get('verdict')}",
                 f"scores={(c.get('judge') or {}).get('scores')}",
                 f"anchor={e['anchor']}"]
        if e["anchor"] == "neighbour":
            cited.append(f"re-anchor target: {e['anchor_detail']}")
        if e.get("mw_headwords_missing"):
            cited.append("mw_headwords_missing=" + ",".join(e["mw_headwords_missing"]))
        verdicts.append({
            "key": c["key"], "verse_id": c["verse_id"], "lemma": c["lemma"],
            "verdict": verdict,
            "judge_verdict": (c.get("judge") or {}).get("verdict"),
            "disposition": disposition,
            "group": g,
            "reason": reason,
            "judge_reason": ((c.get("judge") or {}).get("reason") or "")[:600],
            "evidence_cited": cited,
        })

    doc = {
        "_meta": {
            "handoff": "H1685",
            "queue": "lexical",
            "adjudicator": ADJUDICATOR,
            "date": "2026-07-27",
            "judge_being_reviewed": "Sonnet 5 (claude-sonnet-5), step lexical_judge_h276, 2026-07-07",
            "generated_by": "scripts/h1685_lexical_verdicts.py",
            "cards": len(verdicts),
            "by_verdict": dict(Counter(v["verdict"] for v in verdicts)),
            "by_group": dict(Counter(v["group"] for v in verdicts)),
            "overturned": sum(1 for v in verdicts if v["disposition"] == "OVERTURNED"),
            "note": ("Group findings and every exception are documented in this "
                     "script's docstring and in EXCEPTIONS; the reasons here are "
                     "the reading, not a post-hoc label."),
        },
        "verdicts": verdicts,
    }
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, ensure_ascii=False, indent=1)
    print(f"wrote {OUT}")
    print("by verdict:", doc["_meta"]["by_verdict"])
    print("by group:  ", doc["_meta"]["by_group"])
    print("overturned:", doc["_meta"]["overturned"])


if __name__ == "__main__":
    main()
