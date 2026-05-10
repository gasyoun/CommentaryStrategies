#!/usr/bin/env python3
"""
validate.py — CI validation for CommentaryStrategies.
Checks all text files for forbidden strings and structural rules.
Exit code 0 = pass, 1 = fail.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent

FORBIDDEN = [
    # (regex_pattern, human_readable_description)
    (r'М\.\s*:\s*Наука,\s*2022',          'Леонов 2022 том не существует'),
    (r'Парибок[аоу]',                      'Неверное склонение: должно быть «Парибка»'),
    (r'Goldman.*М\.\s*:\s*Наука',          'Смешение Goldman с русским изданием'),
    (r'М\.\s*:\s*Наука,\s*2022.*[Лл]еонов|[Лл]еонов.*М\.\s*:\s*Наука,\s*2022',
                                           'Леонов + 2022 в одной строке'),
]

EXTENSIONS = {'.html', '.md', '.txt', '.json', '.py'}

def check_file(path: Path) -> list[str]:
    errors = []
    try:
        text = path.read_text(encoding='utf-8', errors='replace')
    except Exception as e:
        return [f'{path}: read error: {e}']
    for pattern, desc in FORBIDDEN:
        for m in re.finditer(pattern, text):
            line_num = text[:m.start()].count('\n') + 1
            errors.append(f'{path}:{line_num}: [{desc}] -> "{m.group()}"')
    return errors

def main():
    skip_dirs = {'.git', '__pycache__', 'archive', 'महाभारत_files',
                 'Рамаяна. Книга 5. Сундараканда_files'}
    all_errors = []
    checked = 0
    for path in ROOT.rglob('*'):
        if any(part in skip_dirs for part in path.parts):
            continue
        if path.suffix.lower() not in EXTENSIONS:
            continue
        if not path.is_file():
            continue
        errs = check_file(path)
        all_errors.extend(errs)
        checked += 1

    print(f'Checked {checked} files.')
    if all_errors:
        print(f'\n[ERROR] {len(all_errors)} error(s) found:\n')
        for e in all_errors:
            print(' ', e)
        sys.exit(1)
    else:
        print('[PASS] All checks passed.')
        sys.exit(0)

if __name__ == '__main__':
    main()
