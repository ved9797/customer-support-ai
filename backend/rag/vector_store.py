import faiss
import numpy as np

from rag.embeddings import get_embeddings
from rag.knowledge_base import load_all_documents
from rag.text_splitter import split_text


class VectorStore:

    def __init__(self):
        self.index = None
        self.chunks = []
        self.is_built = False

    def build_index(self):

        if self.is_built:
            return

        all_chunks = []

        documents = load_all_documents()

        for document in documents:

            chunks = split_text(document["content"])

            for chunk in chunks:

                all_chunks.append(
                    {
                        "source": document["filename"],
                        "text": chunk
                    }
                )

        self.chunks = all_chunks

        embeddings = get_embeddings(
            [chunk["text"] for chunk in all_chunks]
        )

        embeddings = np.array(
            embeddings,
            dtype="float32"
        )

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(dimension)

        self.index.add(embeddings)

        self.is_built = True

        print(f"✅ Indexed {len(all_chunks)} chunks.")

    def search(self, query, k=3):

        if not self.is_built:
            self.build_index()

        query_embedding = get_embeddings([query])

        query_embedding = np.array(
            query_embedding,
            dtype="float32"
        )

        _, indices = self.index.search(
            query_embedding,
            k
        )

        return [
            self.chunks[i]
            for i in indices[0]
        ]