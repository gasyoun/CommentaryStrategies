#!/usr/bin/env python3
"""One-off: back-fill a `why_proposed` motivation label onto the 16 pilot notes.

Going forward the Sonnet drafting contract emits `why_proposed` natively (see
docs/PHASE2_METHOD.md §3.1). The pilot notes predate that field, so this script
injects Opus-authored rationales (why each note earns a place beyond the
подстрочник) into the per-sarga candidate files in place. Idempotent.

Usage: python scripts/backfill_why_proposed.py
"""
import sys
import os
import json
import glob

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
PILOT_DIR = os.path.join(REPO, "data", "analysis", "phase2_pilot")

WHY = {
    "5.35.3": "Уточняет bhūyaḥ: не «ещё раз», а «подробнее» — меняет интонацию просьбы Ситы; подстрочник различия не даёт.",
    "5.35.11": "Вскрывает скрытый богословский подтекст (аватара) в бытовой формуле «защитник варн» — уровень смысла, невидимый в переводе.",
    "5.35.45": "Реалия: отождествляет «огненную гору» с горой Мальяват и мифом об огне Самварта (реалия + связь с Бхишмапарвой МБх).",
    "5.35.81": "Топоним + генеалогия Ханумана; связывает с примечанием к 5.35.45 (та же горная цепь).",
    "5.35.82": "Идентифицирует малоизвестного асуру и мотив (по повелению риши) — реалия, отсутствующая в подстрочнике.",
    "5.35.89": "Объясняет, зачем Хануман повторяет рассказ о рождении — логика узнавания против мнимого посланца; снимает вопрос о «лишнем» повторе.",
    "5.36.13": "Предлагает альтернативное прочтение (ревнивый упрёк vs риторический довод) — расхождение интерпретаций, важное для тона сцены.",
    "5.36.17": "Разъясняет шастрическую доктрину четырёх upāya за «двойным/тройным средством» — доктринальная реалия.",
    "5.36.33": "Раскрывает миф (Индра/Шачи/Анухрада), на который опирается сравнение — иначе троп непрозрачен.",
    "5.36.38": "Показывает, что клятва не случайна (жизнью, не набор святынь) — логика образа.",
    "5.36.40": "Текстологический вариант (nāga-/nāka-) с расхождением комментаторов; фиксирует, какому чтению следует перевод.",
    "5.36.41": "Исправляет вероятное недопонимание: «пятая доля» = время трапезы, не количество — иначе теряется смысл аскезы.",
    "5.37.3": "Вскрывает подтекст-предвестие гибели Раваны за общей сентенцией о роке — экзегетический слой.",
    "5.37.12": "Тилака маркирует эпизод как «семя» будущего перехода Вибхишаны — нарративная связка для читателя целого.",
    "5.37.25": "Текстологический вариант (nāga-/naga-), меняющий образ (слон Айравата vs вершина горы); перевод следует одному чтению.",
    "5.37.36": "Объясняет постановочную деталь (спрыгивает, чтобы треск ветвей не выдал) — мотивировка, не проясняемая подстрочником.",
}


def main():
    changed = 0
    for f in sorted(glob.glob(os.path.join(PILOT_DIR, "sarga_*_candidates.json"))):
        d = json.load(open(f, encoding="utf-8"))
        for n in d.get("notes", []):
            w = WHY.get(n["verse_id"])
            if w and n.get("why_proposed") != w:
                n["why_proposed"] = w
                changed += 1
        with open(f, "w", encoding="utf-8") as fh:
            json.dump(d, fh, ensure_ascii=False, indent=2)
    missing = [vid for vid in WHY if not any(True for _ in [1])]  # noqa (kept simple)
    print(f"back-filled why_proposed on {changed} notes across per-sarga files")


if __name__ == "__main__":
    main()
