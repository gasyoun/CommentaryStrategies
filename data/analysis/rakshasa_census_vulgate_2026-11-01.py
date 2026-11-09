#!/usr/bin/env python3
"""Перепись ракшас-лексики Рамаяны + целевые чеки H7597 (том V ЛП, Сундараканда).

Источники:
  - CommentaryStrategies/data/valmiki_shlokas  — локальный текст южной вульгаты
    (Gita Supersite-подобный, деванагари, verse_id K.S.V);
  - data/edition_comparison/book_summary.json  — юж. вульгата (samskrtam.ru/GS),
    per_sarga_by_number_RAW: южные счёты стихов по саргам Сундары;
  - data/edition_comparison/critical_only_and_variants.json — southern_text (IAST)
    вариантных пар;
  - dcs-conllu/files/Ṛgveda/*.conllu — полный RV (DCS, IAST, колонка FORM).

Методика (досье «Ракшасы» §1): стем राक्षस как подстрока (семейство rākṣasa-,
включая rākṣasī); отдельно राक्षसी; отдельно средний род rakṣas- (रक्षः/रक्षो/रक्षांसि).
Плотность = токены / стихи × 100.

Usage: python3 rakshasa_census_vulgate_2026-11-01.py [--repo-root DIR]
Выход: JSON рядом со скриптом + отчёт в stdout.
"""
import json
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")
from pathlib import Path

REPO = Path(sys.argv[sys.argv.index("--repo-root") + 1]) if "--repo-root" in sys.argv else Path(__file__).resolve().parents[2]
SHLOKAS = REPO / "data" / "valmiki_shlokas"
EDC = REPO / "data" / "edition_comparison"
COMMENTS = REPO / "data" / "valmiki_commentaries" / "kanda_5_sundarakanda"
RV_DIR = Path.home() / "Documents" / "GitHub" / "dcs-conllu" / "files" / "Ṛgveda"

KANDAS = [
    ("Бала", "kanda_1_balakanda"),
    ("Аётья", "kanda_2_ayodhyakanda"),
    ("Аранья", "kanda_3_aranyakanda"),
    ("Кишикиндха", "kanda_4_kishkindakanda"),
    ("Сундара", "kanda_5_sundarakanda"),
    ("Юддха", "kanda_6_yuddhakanda"),
]

# Таблица 2 статьи (H7924, DH #1): эпизодальные блоки Сундары, сверяемые с
# sundara_tokens_by_sarga ниже. Сарга 13 — в блоке 9–13 (как в статье).
SUNDARA_BLOCKS = [(1, 8), (9, 13), (14, 21), (22, 27), (28, 41), (42, 54),
                  (55, 57), (58, 58), (59, 64), (65, 68)]

DEV_NEUTER = re.compile(r"रक्ष[ःों]|रक्षांसि")
IAST_FAMILY = re.compile(r"rākṣas")
IAST_NEUTER = re.compile(r"rakṣas[ः]?\b|rakṣo\b|rakṣāṃsi")


def clean(dev: str) -> str:
    # убираем англ. пояснения в [скобках] в начале поля sanskrit
    return "\n".join(l for l in dev.splitlines() if not l.strip().startswith("["))


def vid_parts(vid: str):
    """verse_id → (kanda, sarga, verse); пустые/нестандартные id → None."""
    p = str(vid or "").split(".")
    try:
        return int(p[0]), int(p[1]), int(p[2])
    except (IndexError, ValueError):
        return None


def devanagari_census():
    """Перепись по всем кхандам: стихи, семейство rākṣasa-, rākṣasī, ср. род, плотность."""
    rows, total = [], dict(verses=0, family=0, rakshasi=0, neuter=0)
    per_verse = []  # (verse_id, family_count) для сарговой карты
    for label, d in KANDAS:
        kd = SHLOKAS / d
        verses = family = rakshasi = neuter = 0
        for f in sorted(kd.glob("sarga_*.json")):
            for v in json.loads(f.read_text(encoding="utf-8")):
                verses += 1
                txt = clean(v.get("sanskrit", ""))
                c = txt.count("राक्षस")
                family += c
                rakshasi += txt.count("राक्षसी")
                neuter += len(DEV_NEUTER.findall(txt))
                vp = vid_parts(v.get("verse_id"))
                if c and vp:
                    per_verse.append(("%d.%d.%d" % vp, c))
        rows.append({
            "kanda": label, "verses": verses, "rākṣasa-family": family,
            "rākṣasī": rakshasi, "rakṣas-neuter": neuter,
            "per_100": round(family / verses * 100, 1) if verses else 0.0,
        })
        for k in total:
            total[k] += {"verses": verses, "family": family, "rakshasi": rakshasi, "neuter": neuter}[k]
    return rows, total, per_verse


def sundara_vs_southern(per_verse):
    """Локальные счёты сарг Сундары против южной вульгаты (book_summary RAW)."""
    bs = json.loads((EDC / "book_summary.json").read_text(encoding="utf-8"))
    southern_by_sarga = {r["sarga"]: r["southern_verses"] for r in bs["per_sarga_by_number_RAW"]}
    # полный проход по всем стихам Сундары: счёт стихов не должен зависеть от токенов
    local_by_sarga, tokens_by_sarga, female_by_sarga = {}, {}, {}
    for f in sorted((SHLOKAS / "kanda_5_sundarakanda").glob("sarga_*.json")):
        sarga = int(f.stem.split("_")[1])
        verses = json.loads(f.read_text(encoding="utf-8"))
        local_by_sarga[sarga] = len(verses)
        tokens_by_sarga[sarga] = sum(clean(v.get("sanskrit", "")).count("राक्षस") for v in verses)
        female_by_sarga[sarga] = sum(clean(v.get("sanskrit", "")).count("राक्षसी") for v in verses)
    gaps, top = [], []
    for s in sorted(southern_by_sarga):
        loc = local_by_sarga.get(s, 0)
        sou = southern_by_sarga[s]
        if sou - loc > 5:
            gaps.append({"sarga": s, "local": loc, "southern": sou, "gap": sou - loc,
                         "tokens_local": tokens_by_sarga.get(s, 0)})
    for s, c in sorted(tokens_by_sarga.items(), key=lambda kv: -kv[1])[:12]:
        top.append({"sarga": s, "tokens": c, "local_verses": local_by_sarga.get(s, 0),
                    "southern_verses": southern_by_sarga.get(s)})
    bt = bs["book_totals"]
    blocks = []
    for a, b in SUNDARA_BLOCKS:
        tot = sum(tokens_by_sarga.get(n, 0) for n in range(a, b + 1))
        fem = sum(female_by_sarga.get(n, 0) for n in range(a, b + 1))
        blocks.append({"sargas": [a, b], "tokens": tot, "female": fem,
                       "male_other": tot - fem})
    return {
        "southern_total_sundara": bt["southern_verses"],
        "local_total_sundara": sum(local_by_sarga.values()),
        "gaps_over_5": gaps,
        "top_token_sargas": top,
        "density_if_southern_denominator": round(
            sum(tokens_by_sarga.values()) / bt["southern_verses"] * 100, 1),
        # H7924 (DH #1): машинный экспорт для Таблицы 2 и гендерного микрораздела.
        # Таблица 2 статьи сверяется с sundara_blocks; доля rākṣasī — с
        # sundara_tokens_by_sarga (female) и census_by_kanda (rākṣasī).
        "sundara_tokens_by_sarga": [
            {"sarga": s, "verses": local_by_sarga[s], "tokens": tokens_by_sarga[s],
             "female": female_by_sarga[s]}
            for s in sorted(tokens_by_sarga)],
        "sundara_blocks": blocks,
    }


def southern_variant_tokens():
    """Токены в southern_text вариантных пар (IAST) Сундары — где юж. текст переформулирован."""
    d = json.loads((EDC / "critical_only_and_variants.json").read_text(encoding="utf-8"))
    hits = []
    for v in d.get("variants", []):
        st = v.get("southern_text", "")
        c = len(IAST_FAMILY.findall(st))
        if c:
            hits.append({"southern": v.get("southern"), "tokens": c,
                         "text": st.replace("\n", " ")[:160]})
    return {"variant_pairs_with_rākṣas": len(hits), "tokens": sum(h["tokens"] for h in hits),
            "sample": hits[:8]}


def hanuman_check():
    """Чек (а): стихи сарг 5.43–50, где Хануман назван rākṣasa-."""
    out = []
    for n in range(43, 51):
        f = SHLOKAS / "kanda_5_sundarakanda" / f"sarga_{n:02d}.json"
        for v in json.loads(f.read_text(encoding="utf-8")):
            txt = clean(v.get("sanskrit", ""))
            if "राक्षस" in txt and "हनुम" in txt:
                vp = vid_parts(v.get("verse_id"))
                out.append({"verse_id": "%d.%d.%d" % vp if vp else v.get("verse_id"),
                            "text": txt.replace("\n", " ⏎ ")})
    return out


def context_5_2_43():
    """Чек (г): контекст 5.2.43 rākṣasa-rūpa."""
    f = SHLOKAS / "kanda_5_sundarakanda" / "sarga_02.json"
    out = []
    for v in json.loads(f.read_text(encoding="utf-8")):
        vp = vid_parts(v.get("verse_id"))
        if vp and 40 <= vp[2] <= 46:
            out.append({"verse_id": "%d.%d.%d" % vp,
                        "text": clean(v.get("sanskrit", "")).replace("\n", " ⏎ ")})
    return out


def dcs_pin():
    """H7924 (DH #2): пин корпуса через git rev-parse, не хардкод.
    Возвращает (sha, источник) для первого найденного локального
    dcs-conllu/DCS-клона; (None, ...) если клона нет на машине."""
    for cand in (RV_DIR.parents[2], Path.home() / "Documents" / "GitHub" / "DCS"):
        if (cand / ".git").exists():
            try:
                sha = subprocess.run(
                    ["git", "-C", str(cand), "rev-parse", "HEAD"],
                    capture_output=True, text=True, timeout=10).stdout.strip()
            except Exception:
                sha = ""
            if sha:
                return sha, "git rev-parse HEAD in %s" % cand
    return None, "corpus clone absent on this host at re-run; frozen pin retained"


def rv_census():
    """Чек (в): rakṣas-токены по полному RV (DCS conllu, колонка FORM).
    DH #9 (containment): при отсутствии корпуса массивы не зануляются —
    main() сохраняет замороженные значения rigveda_full из прошлого JSON
    и помечает их, вместо записи пустого счёта."""
    if not RV_DIR.is_dir() or not any(RV_DIR.glob("*.conllu")):
        return {"status": "corpus absent at re-run; frozen values preserved by main()",
                "pin": dcs_pin()[0], "pin_source": dcs_pin()[1]}
    forms = {}
    chapters = 0
    for f in sorted(RV_DIR.glob("*.conllu")):
        if f.name.endswith("_parsed"):
            continue
        chapters += 1
        for line in f.read_text(encoding="utf-8").splitlines():
            if not line or line.startswith("#"):
                continue
            cols = line.split("\t")
            if len(cols) < 3:
                continue
            form, lemma = cols[1], cols[2]
            if re.search(r"^r[āa]kṣ", form) or form.startswith("rakṣ"):
                forms.setdefault((form, lemma), 0)
                forms[(form, lemma)] += 1
    by_lemma = {}
    for (form, lemma), n in forms.items():
        by_lemma[lemma] = by_lemma.get(lemma, 0) + n
    sha, how = dcs_pin()
    return {
        "chapters": chapters,
        "total_tokens": sum(forms.values()),
        "by_form": sorted(({"form": f, "lemma": l, "n": n} for (f, l), n in forms.items()),
                          key=lambda x: -x["n"]),
        "by_lemma": dict(sorted(by_lemma.items(), key=lambda kv: -kv[1])),
        "pin": sha, "pin_source": how,
        "source": "dcs-conllu/files/Ṛgveda (DCS), FORM column, pin %s (%s)" % (sha, how),
    }


def commentary_probe():
    """Живые цитаты Тилакa/Бхушаны по ракшас-плотным саргам (деванагари + IAST)."""
    wanted = {4, 22, 27, 43, 44, 48, 52, 53, 54, 58}
    hits = []
    for f in sorted(COMMENTS.glob("*.txt")):
        parts = f.stem.split("_sarga_")
        if len(parts) != 2 or int(parts[1]) not in wanted:
            continue
        text = f.read_text(encoding="utf-8")
        for pat, kind in (("राक्षस", "dev"), ("rākṣas", "iast")):
            if pat in text:
                hits.append({"file": f.name, "script": kind,
                             "count": text.count(pat)})
                break
    return hits


def dossier_compatibility():
    """Диагностика: счёт только текста стиха vs +глоссы word_by_word (метод досье 01-11).
    Досье (Сундара 437/всего 2029) считало и словарные глоссы; статья считает текст поэмы."""
    poem, gloss_only = 0, 0
    for _, d in KANDAS:
        for f in sorted((SHLOKAS / d).glob("sarga_*.json")):
            for v in json.loads(f.read_text(encoding="utf-8")):
                poem += clean(v.get("sanskrit", "")).count("राक्षस")
                gloss_only += v.get("word_by_word", "").count("राक्षस")
    return {"poem_text_only": poem, "word_by_word_glosses": gloss_only,
            "dossier_method_total": poem + gloss_only}


def main():
    rows, total, per_verse = devanagari_census()
    out = Path(__file__).with_suffix(".json")
    prev = {}
    if out.exists():
        try:
            prev = json.loads(out.read_text(encoding="utf-8"))
        except ValueError:
            prev = {}
    rv = rv_census()
    if rv.get("status"):
        # корпус отсутствует: сохраняем замороженные RV-значения, а не нули
        frozen = dict(prev.get("rigveda_full") or {})
        frozen.update({"repro_status": rv["status"], "pin": rv["pin"],
                       "pin_source": rv["pin_source"]})
        rv = frozen
    report = {
        "census_by_kanda": rows,
        "totals": {**total, "per_100": round(total["family"] / total["verses"] * 100, 1)},
        "sundara_vs_southern": sundara_vs_southern(per_verse),
        "southern_variant_tokens_sundara": southern_variant_tokens(),
        "hanuman_rakshasa_5_43_50": hanuman_check(),
        "context_5_2_40_46": context_5_2_43(),
        "rigveda_full": rv,
        "dossier_compatibility": dossier_compatibility(),
        "commentary_file_hits": commentary_probe(),
    }
    out = Path(__file__).with_suffix(".json")
    out.write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=1))
    print(f"\n[saved] {out}")


if __name__ == "__main__":
    main()