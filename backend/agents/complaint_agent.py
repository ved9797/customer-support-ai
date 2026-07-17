from rag.retriever import retrieve_context

def complaint_prompt(user_message):

    knowledge = retrieve_context(
        "ComplaintPolicy.md",
        user_message
    )

    return f"""
You are a Complaint Resolution Executive.

Company Knowledge:

{knowledge}

Customer Question:

{user_message}

Rules:

- Answer only using the company knowledge.
- If the answer isn't available, politely say so.
- Keep the response professional.
"""