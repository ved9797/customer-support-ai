from rag.text_splitter import split_text

text = """
Artificial Intelligence is changing customer support.
FAISS helps perform semantic search.
Sentence Transformers convert text into embeddings.
"""

chunks = split_text(text)

print("Number of Chunks:", len(chunks))

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i+1}")
    print(chunk)