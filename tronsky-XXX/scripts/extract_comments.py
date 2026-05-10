import os
from docx import Document

def extract_comments(docx_path):
    doc = Document(docx_path)
    # The standard python-docx doesn't provide a direct way to access comments easily via the high-level API
    # But let's try to see if they are in the paragraphs or if we can find them in the part
    
    print(f"Analyzing {docx_path}...")
    
    # Let's try to access the comments part directly via the underlying zip structure or internal parts
    try:
        comments_part = doc.part.related_parts.get('/word/comments.xml')
        if not comments_part:
            # Try by relationship type
            for rel in doc.part.rels.values():
                if "comments" in rel.target_ref:
                    comments_part = rel.target_part
                    break
        
        if comments_part:
            from lxml import etree
            xml_content = comments_part.blob
            root = etree.fromstring(xml_content)
            # Find all comments
            # Namespaces for Word
            ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
            comments = root.xpath('//w:comment', namespaces=ns)
            print(f"Found {len(comments)} editorial comments:")
            for comment in comments:
                author = comment.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}author')
                text_nodes = comment.xpath('.//w:t', namespaces=ns)
                text = "".join([t.text for t in text_nodes if t.text])
                print(f"- [{author}]: {text}")
        else:
            print("No /word/comments.xml found in the docx.")
            
    except Exception as e:
        print(f"Error extracting comments: {e}")

if __name__ == "__main__":
    path = r"c:\Users\user\Documents\GitHub\CommentaryStrategies\tronsky-XXX\CommentaryStrategies_Tronsky30_Kostina.docx"
    extract_comments(path)
