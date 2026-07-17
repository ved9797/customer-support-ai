from rag.retriever import retrieve_context

def technical_prompt(user_message):

    knowledge = retrieve_context(
        "UserManual.md",
        user_message
    )

    return f"""
You are a Technical Support Executive.

Use the company knowledge below to answer the customer's question.

Company Knowledge:

{knowledge}

Customer Question:

{user_message}

Rules:
- Answer only from the company knowledge.
- If the answer isn't available, politely say so.
- Keep your response professional.
"""