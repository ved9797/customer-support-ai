print("Test started")

from rag.document_loader import load_document
from rag.text_splitter import split_text

text = load_document("RefundPolicy.md")

chunks = split_text(text)

print("Total Chunks:", len(chunks))

for i, chunk in enumerate(chunks):
    print(f"\n------ Chunk {i+1} ------")
    print(chunk)