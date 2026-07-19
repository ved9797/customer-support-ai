def split_text(text, chunk_size=500):
    """
    Split markdown text by paragraphs while keeping chunks
    under the maximum size.
    """

    paragraphs = text.split("\n\n")

    chunks = []
    current_chunk = ""

    for paragraph in paragraphs:

        if len(current_chunk) + len(paragraph) < chunk_size:

            current_chunk += paragraph + "\n\n"

        else:

            if current_chunk:
                chunks.append(current_chunk.strip())

            current_chunk = paragraph + "\n\n"

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks