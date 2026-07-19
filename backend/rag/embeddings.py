from sentence_transformers import SentenceTransformer

# Load embedding model only once
model = SentenceTransformer("all-MiniLM-L6-v2")


def get_embeddings(texts):
    """
    Convert a list of text chunks into embeddings.
    """
    return model.encode(texts)