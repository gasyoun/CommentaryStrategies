import os
import subprocess
import re
from docx import Document
from docx.shared import Cm

def build_article():
    # Определяем абсолютные пути относительно расположения скрипта
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    
    input_md = os.path.join(parent_dir, "3_gasuns_tronsky-30_v21.md")
    temp_md = os.path.join(script_dir, "temp_article_anon.md")
    output_docx = os.path.join(parent_dir, "article_v_tronsky_anon.docx")
    
    # Предполагается, что reference.docx лежит в той же папке, что и скрипт
    reference_docx = os.path.join(script_dir, "tronsky_reference.docx") 
    
    pandoc_exe = r"C:\Users\user\Downloads\pandoc-3.9.0.2-windows-x86_64\pandoc-3.9.0.2\pandoc.exe"

    print("1. Чтение Markdown...")
    try:
        with open(input_md, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Ошибка: Не найден входной файл по пути {input_md}")
        return

    print("2. Анонимизация рукописи...")
    # Удаляем строку author: "Гасунс М. Ю." из YAML-заголовка
    text = re.sub(r'^author:\s*".*?"\s*\n', '', text, flags=re.MULTILINE)
    
    # Удаляем раздел "Сведения об авторе" целиком вплоть до следующего разделителя ---
    text = re.sub(r'## Сведения об авторе\n\n.*?(?=\n---|\Z)', '', text, flags=re.DOTALL)

    with open(temp_md, "w", encoding="utf-8") as f:
        f.write(text)

    print("3. Конвертация через Pandoc...")
    pandoc_cmd = [
        pandoc_exe,
        temp_md,
        "-o", output_docx,
        f"--reference-doc={reference_docx}",
        "-f", "markdown",
        "-t", "docx"
    ]

    try:
        subprocess.run(pandoc_cmd, check=True)
        print("   Pandoc успешно сформировал DOCX.")
    except subprocess.CalledProcessError as e:
        print(f"   Ошибка при запуске Pandoc: {e}")
        return
    except FileNotFoundError:
        print(f"   Ошибка: Pandoc не найден по пути {pandoc_exe}")
        return

    print("4. Постобработка: настройка ширины таблиц (макс. 11 см)...")
    try:
        doc = Document(output_docx)
        max_width = Cm(11.0)
        tables_modified = 0

        for table in doc.tables:
            table.autofit = False
            
            if len(table.columns) > 0:
                col_width = max_width / len(table.columns)
                for row in table.rows:
                    for cell in row.cells:
                        cell.width = col_width
                tables_modified += 1

        if tables_modified > 0:
            doc.save(output_docx)
            print(f"   Скорректировано таблиц: {tables_modified}.")
        else:
            print("   Таблицы в документе не найдены, постобработка не требуется.")
            
    except Exception as e:
        print(f"   Ошибка при обработке через python-docx: {e}")

    # Удаляем временный файл
    if os.path.exists(temp_md):
        os.remove(temp_md)

    print(f"\nГотово! Итоговый анонимизированный файл сохранен как: {output_docx}")

if __name__ == "__main__":
    build_article()