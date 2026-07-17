from rag.retriever import retrieve_context

question = "Can I get a refund after 10 days?"

chunk = retrieve_context(
    "RefundPolicy.md",
    question
)

print(chunk)