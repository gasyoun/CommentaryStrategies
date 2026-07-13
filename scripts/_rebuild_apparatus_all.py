#!/usr/bin/env python3
"""H830: rebuild the MBh apparatus for a batch of parvas with the fixed
akshara aligner (H776 + the space-token bugfix). Thin wrapper around
build_edition_apparatus.py's main() logic, mirroring
scripts/run_all_mbh_parvas.py's CLI args but WITHOUT rerunning
compare_editions_mbh.py (already fresh)."""
import sys
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)

PARVA_NAMES = {
    1: "adiparva", 2: "sabhaparva", 3: "vanaparva", 4: "virataparva",
    5: "udyogaparva", 6: "bhishmaparva", 7: "dronaparva", 8: "karnaparva",
    9: "shalyaparva", 10: "sauptikaparva", 11: "striparva", 12: "shantiparva",
    13: "anushasanaparva", 14: "ashwamedhikaparva", 15: "ashramavasikaparva",
    16: "mausalaparva", 17: "mahaprasthanikaparva", 18: "swargarohanaparva",
}
RU_NAMES = {
    "adiparva": "Ādипарва", "sabhaparva": "Сабхāпарва", "vanaparva": "Ванапарва",
    "virataparva": "Вирāтапарва", "udyogaparva": "Удьйогапарва",
    "bhishmaparva": "Бхӣшмапарва", "dronaparva": "Дроṇапарва",
    "karnaparva": "Карṇапарва", "shalyaparva": "Шальяпарва",
    "sauptikaparva": "Саупатикапарва", "striparva": "Стрӣпарва",
    "shantiparva": "Шāнтипарва", "anushasanaparva": "Анушāсанапарва",
    "ashwamedhikaparva": "Ашвамедхикапарва", "ashramavasikaparva": "Āшрамавāсикапарва",
    "mausalaparva": "Маусалапарва", "mahaprasthanikaparva": "Махāпрастхāникапарва",
    "swargarohanaparva": "Сваргарохаṇапарва",
}


def main():
    parvas = [int(a) for a in sys.argv[1:]]
    for n in parvas:
        slug = PARVA_NAMES[n]
        outdir = os.path.join(REPO, "data", "edition_comparison_mbh", slug)
        print(f"\n===== parva {n} ({slug}) =====", flush=True)
        r = subprocess.run(
            [sys.executable, os.path.join(HERE, "build_edition_apparatus.py"),
             "--input", os.path.join(outdir, "critical_only_and_variants.json"),
             "--outdir", outdir,
             "--title", f"{RU_NAMES[slug]} — BORI critical <-> Nilakantha vulgate variant apparatus",
             "--work-label", f"MBh-{slug.capitalize()}",
             "--other-key", "vulgate", "--chapter-label", "adhyaya"],
            cwd=REPO)
        if r.returncode != 0:
            raise SystemExit(f"FAILED parva {n}")


if __name__ == "__main__":
    main()
