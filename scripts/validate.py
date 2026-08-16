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

def main():
    # `review/` holds gitignored vote sheets built by the org's shared emitter
    # (csl_pyutil.render_review_sheet). Those are self-contained by design — no
    # external stylesheet, their own shell — so the design-system check below
    # would fail every one of them. CI never sees the folder; this keeps a local
    # `validate.py` run from flagging an artifact this repo does not own the
    # markup for.
    skip_dirs = {'.git', '__pycache__', 'node_modules', 'test-results',
                 'playwright-report', 'archive', 'review', 'महाभारत_files',
                 'Рамаяна. Книга 5. Сундараканда_files'}
    # Rule-definition docs must quote the forbidden strings in order to define them —
    # don't let the validator flag its own rulebook.
    skip_files = {'CLAUDE.md'}
    all_errors = []
    checked = 0
    for path in ROOT.rglob('*'):
        if any(part in skip_dirs for part in path.parts):
            continue
        if path.name in skip_files:
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
