from pathlib import Path

KNOWLEDGE_BASE = (
    Path(__file__).parent.parent.parent / "knowledge_base"
)


def load_all_documents():
    """
    Load every markdown file from the knowledge_base folder.
    """

    documents = []

    for file in KNOWLEDGE_BASE.glob("*.md"):

        with open(file, "r", encoding="utf-8") as f:

            documents.append(
                {
                    "filename": file.name,
                    "content": f.read()
                }
            )

    return documents