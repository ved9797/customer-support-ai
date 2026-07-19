from rag.vector_store import VectorStore

vector_store = VectorStore()

vector_store.build_index()

results = vector_store.search(
    "How can I get my refund?"
)

print("\nTop Results:\n")

for result in results:

    print(result["source"])

    print(result["text"])

    print("-" * 60)