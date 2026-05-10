import os
from docx import Document
from lxml import etree

def find_tracked_changes(docx_path):
    doc = Document(docx_path)
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    
    print(f"Searching for tracked changes in {docx_path}...")
    
    # Get the XML string of the body
    xml_str = doc._body._element.xml
    root = etree.fromstring(xml_str.encode('utf-8'))
    
    # Find all comment references and tracked changes
    ins_nodes = root.xpath('.//w:ins', namespaces=ns)
    del_nodes = root.xpath('.//w:del', namespaces=ns)
    comment_ref_nodes = root.xpath('.//w:commentRangeStart', namespaces=ns)
    
    print(f"Found {len(ins_nodes)} insertions.")
    print(f"Found {len(del_nodes)} deletions.")
    print(f"Found {len(comment_ref_nodes)} comment ranges.")
    
    if len(ins_nodes) > 0:
        print("\nFirst 10 insertions:")
        for ins in ins_nodes[:10]:
            author = ins.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}author')
            text = "".join([t.text for t in ins.xpath('.//w:t', namespaces=ns) if t.text])
            if text.strip():
                print(f"- [{author}]: {text}")

    # If there are comment ranges, we need to read the comments.xml part
    try:
        comments_part = None
        for rel in doc.part.rels.values():
            if "comments" in rel.target_ref:
                comments_part = rel.target_part
                break
        
        if comments_part:
            comments_xml = etree.fromstring(comments_part.blob)
            comments = comments_xml.xpath('//w:comment', namespaces=ns)
            print(f"\nFound {len(comments)} actual comments in /word/comments.xml:")
            for comment in comments:
                cid = comment.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}id')
                author = comment.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}author')
                text = "".join([t.text for t in comment.xpath('.//w:t', namespaces=ns) if t.text])
                print(f"ID {cid} [{author}]: {text}")
    except Exception as e:
        print(f"Error reading comments part: {e}")

if __name__ == "__main__":
    path = r"c:\Users\user\Documents\GitHub\CommentaryStrategies\tronsky-XXX\CommentaryStrategies_Tronsky30_Kostina.docx"
    find_tracked_changes(path)
