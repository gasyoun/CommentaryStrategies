#!/usr/bin/env python3
"""
validate.py — CI validation for CommentaryStrategies.
Checks all text files for forbidden strings and structural rules.
Exit code 0 = pass, 1 = fail.
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from taxonomy import (  # noqa: E402
    TRANSLATORS, AXIS1_TOPICS, AXIS2_KAZANSKY, AXIS3_LAKSHANA,
    AXIS4_PARIBOK, REQUIRED, URN_PREFIX)

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"

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

def validate_html_structure(path: Path) -> list[str]:
    """Ensures analytical HTML files use the new design system."""
    errors = []
    # Skip index.html and internal templates if any
    if path.name == 'index.html' or 'old' in path.name.lower():
        return []
    
    # Skip primary source directories
    if 'mahabharata-nilakantha' in path.parts or 'ramayana-leonov' in path.parts:
        return []
    
    text = path.read_text(encoding='utf-8', errors='replace')
    
    # 1. Check for CSS link
    if 'css/commentary.css' not in text:
        errors.append(f'{path}: Missing link to "css/commentary.css"')
        
    # 2. Check for breadcrumb (analytical reports should have one)
    if 'breadcrumb' not in text and 'аналитика' in text.lower():
        errors.append(f'{path}: Missing breadcrumb navigation')
        
    # 3. Check for main container
    if '<main class="container">' not in text:
        errors.append(f'{path}: Missing <main class="container"> wrapper')

    return errors

def validate_corpus() -> list[str]:
    """Проверка записей корпуса против кодов схемы (taxonomy.py, единый источник).

    Ловит класс багов из код-ревью: дрейф enum (translator «vasilkov» vs данные;
    тема «poetics» вне enum), пропуск обязательных полей, неверный URN/тип.
    """
    errors = []
    files = sorted(DATA.glob('*_markup_50.json')) + sorted(DATA.glob('*_full.json'))
    records_checked = 0
    for path in files:
        try:
            records = json.loads(path.read_text(encoding='utf-8'))
        except Exception as e:
            errors.append(f'{path.name}: JSON parse error: {e}')
            continue
        if not isinstance(records, list):
            continue
        for i, r in enumerate(records):
            if not isinstance(r, dict):
                errors.append(f'{path.name} [#{i}]: record is not an object')
                continue
            records_checked += 1
            cid = r.get('comment_id', f'#{i}')
            for field in REQUIRED:
                if field not in r:
                    errors.append(f"{path.name} [{cid}]: missing required field '{field}'")
            checks = [
                ('translator', r.get('translator'), TRANSLATORS),
                ('axis_2_kazansky', r.get('axis_2_kazansky'), AXIS2_KAZANSKY),
                ('axis_4_paribok', r.get('axis_4_paribok'), AXIS4_PARIBOK),
            ]
            for field, val, allowed in checks:
                if val is not None and val not in allowed:
                    errors.append(f"{path.name} [{cid}]: {field} '{val}' not in schema enum {list(allowed)}")
            for topic in r.get('axis_1_topic', []):
                if topic not in AXIS1_TOPICS:
                    errors.append(f"{path.name} [{cid}]: axis_1_topic '{topic}' not in schema enum")
            for lak in r.get('axis_3_lakshana', []):
                if lak not in AXIS3_LAKSHANA:
                    errors.append(f"{path.name} [{cid}]: axis_3_lakshana '{lak}' not in schema enum")
            urn = r.get('urn')
            if urn is not None and not str(urn).startswith(URN_PREFIX):
                errors.append(f"{path.name} [{cid}]: urn '{urn}' missing prefix {URN_PREFIX}")
            if 'has_iast' in r and not isinstance(r['has_iast'], bool):
                errors.append(f"{path.name} [{cid}]: has_iast is not boolean")
    print(f'Validated {records_checked} corpus records across {len(files)} files.')
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
            
        # Standard content checks
        errs = check_file(path)
        all_errors.extend(errs)
        
        # HTML Structural checks
        if path.suffix.lower() == '.html':
            html_errs = validate_html_structure(path)
            all_errors.extend(html_errs)
            
        checked += 1

    # Record-level corpus validation against the schema (single source of truth)
    all_errors.extend(validate_corpus())

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
