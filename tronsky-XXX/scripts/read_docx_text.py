import os
from docx import Document

def read_text(docx_path, output_path):
    doc = Document(docx_path)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"Reading text from {docx_path}...\n")
        for i, para in enumerate(doc.paragraphs):
            if para.text.strip():
                f.write(f"L{i}: {para.text}\n")

if __name__ == "__main__":
    path = r"c:\Users\user\Documents\GitHub\CommentaryStrategies\tronsky-XXX\CommentaryStrategies_Tronsky30_Kostina.docx"
    out = "docx_text.txt"
    read_text(path, out)
