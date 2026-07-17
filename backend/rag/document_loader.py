from pathlib import Path

KNOWLEDGE_PATH = Path(__file__).parent.parent.parent / "knowledge_base"

def load_document(filename):
    file_path = KNOWLEDGE_PATH / filename

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()