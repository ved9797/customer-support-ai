from rag.knowledge_base import load_all_documents

docs = load_all_documents()

print(len(docs))

for doc in docs:
    print(doc["filename"])