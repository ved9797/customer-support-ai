from rag.document_loader import load_document
from rag.text_splitter import split_text


def retrieve_context(filename, question):

    text = load_document(filename)

    chunks = split_text(text)

    question = question.lower()

    best_chunk = ""

    max_matches = 0

    for chunk in chunks:

        score = 0

        for word in question.split():

            if word in chunk.lower():
                score += 1

        if score > max_matches:
            max_matches = score
            best_chunk = chunk

    return best_chunk