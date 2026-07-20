from pathlib import Path

KNOWLEDGE_BASE = (
    Path(__file__).parent.parent / "knowledge_base"
)

print("Knowledge base path:", KNOWLEDGE_BASE)
print("Exists:", KNOWLEDGE_BASE.exists())

def load_all_documents():
    documents = []

    files = list(KNOWLEDGE_BASE.glob("*.md"))
    print("Markdown files found:", files)

    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            documents.append(
                {
                    "filename": file.name,
                    "content": f.read()
                }
            )

    print("Documents loaded:", len(documents))
    return documents