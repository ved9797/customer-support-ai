from rag.vector_store import VectorStore

vector_store = VectorStore()


def retrieve_context(question):

    results = vector_store.search(question)

    context = "\n\n".join(
        result["text"]
        for result in results
    )

    return context