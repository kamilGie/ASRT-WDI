#!/usr/bin/env python3
import os
import re
import sys

# Wzorce linii do usunięcia (z tolerancją na spacje/taby dookoła)
PATTERNS = [
    re.compile(r'^\s*-\s*\[Rosnotes-WDI\]\(https://github\.com/kamilGie/Rosnotes-WDI\)\s*-\s*Premiera wkrótce\s*$', re.UNICODE),
    re.compile(r'^\s*-\s*\[ASRT-ASD\]\(https://github\.com/kamilGie/Rosnotes-Dyskretna\)\s*-\s*Premiera wkrótce\s*$', re.UNICODE),
]

def should_skip_dir(dirname: str) -> bool:
    # Pomijamy typowe katalogi
    return dirname in {'.git', '.hg', '.svn', '.idea', '.vscode', '__pycache__', 'node_modules'}

def is_readme_md(filename: str) -> bool:
    return filename.lower() == 'readme.md'

def process_file(path: str) -> bool:
    """Zwraca True, jeśli plik został zmodyfikowany."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.read().splitlines()
    except UnicodeDecodeError:
        # Spróbuj w trybie 'utf-8' z ignorowaniem błędów — lepiej coś niż nic
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.read().splitlines()

    new_lines = []
    removed = 0

    for line in lines:
        if any(p.fullmatch(line) for p in PATTERNS):
            removed += 1
            continue
        new_lines.append(line)

    if removed > 0:
        # Zrób prostą kopię bezpieczeństwa
        backup_path = path + '.bak'
        try:
            if not os.path.exists(backup_path):
                with open(backup_path, 'w', encoding='utf-8') as b:
                    b.write("\n".join(lines) + ("\n" if lines else ""))
        except Exception as e:
            print(f"[WARN] Nie udało się utworzyć kopii {backup_path}: {e}", file=sys.stderr)

        with open(path, 'w', encoding='utf-8') as f:
            f.write("\n".join(new_lines) + ("\n" if new_lines else ""))
        print(f"[OK] Usunięto {removed} linie w: {path}")
        return True

    return False

def main(root: str) -> None:
    changed = 0
    for dirpath, dirnames, filenames in os.walk(root):
        # Filtruj katalogi in-place, aby os.walk nie wchodził dalej
        dirnames[:] = [d for d in dirnames if not should_skip_dir(d)]
        for filename in filenames:
            if is_readme_md(filename):
                fullpath = os.path.join(dirpath, filename)
                if process_file(fullpath):
                    changed += 1
    if changed == 0:
        print("Brak zmian — nie znaleziono dopasowań.")
    else:
        print(f"Gotowe. Zmieniono {changed} plik(ów) README.md.")

if __name__ == "__main__":
    root_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    main(root_dir)
