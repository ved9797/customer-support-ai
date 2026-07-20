from agents.router import detect_departments

from agents.billing_agent import billing_instructions
from agents.technical_agent import technical_instructions
from agents.product_agent import product_instructions
from agents.complaint_agent import complaint_instructions
from agents.faq_agent import faq_instructions

from rag.retriever import retrieve_context

from memory.chat_memory import add_message

from tickets.ticket_service import create_ticket
from tickets.escalation import should_escalate

from services.ai_service import generate_response


def process_chat(request, current_user):

    # Save user message only if user is logged in
    if current_user:
        add_message(
            "user",
            request.message,
            current_user["user_id"],
            request.session_id
        )

    # ---------- Human Escalation ----------

    if should_escalate(request.message):

        ticket = create_ticket(
            request.session_id,
            request.message
        )

        ai_reply = f"""
I understand your concern.

Your request has been escalated to a human support representative.

Ticket Details

• Ticket ID: {ticket['ticket_id']}
• Priority: {ticket['priority']}
• Status: {ticket['status']}

Our support team will contact you as soon as possible.

Thank you for your patience.
"""

        # Save assistant reply only if user is logged in
        if current_user:
            add_message(
                "assistant",
                ai_reply,
                current_user["user_id"],
                request.session_id
            )

        return {
            "departments": ["Human Support"],
            "your_message": request.message,
            "ticket": ticket,
            "ai_response": ai_reply,
        }

    # ---------- AI Workflow ----------

    departments = detect_departments(request.message)

    knowledge = retrieve_context(request.message)

    instructions = []

    if "Billing" in departments:
        instructions.append(billing_instructions())

    if "Technical" in departments:
        instructions.append(technical_instructions())

    if "Product" in departments:
        instructions.append(product_instructions())

    if "Complaint" in departments:
        instructions.append(complaint_instructions())

    if "FAQ" in departments:
        instructions.append(faq_instructions())

    if "General" in departments:
        instructions.append(
            """
You are a helpful AI customer support assistant.

Answer only using the supplied company knowledge.
"""
        )

    prompt = f"""
You are TechMart's AI Customer Support Assistant.

Departments:
{", ".join(departments)}

Department Instructions:

{"".join(instructions)}

Company Knowledge:

{knowledge}

Customer Question:

{request.message}

Rules:

- Combine the expertise of all departments.
- Produce ONE answer.
- Never repeat information.
- Answer ONLY using the supplied company knowledge.
- Be professional and concise.
"""

    ai_reply = generate_response(prompt)

    # Save assistant reply only if user is logged in
    if current_user:
        add_message(
            "assistant",
            ai_reply,
            current_user["user_id"],
            request.session_id
        )

    return {
        "departments": departments,
        "your_message": request.message,
        "ai_response": ai_reply,
    }