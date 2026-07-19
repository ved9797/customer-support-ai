from datetime import datetime
import uuid

from database.ticket_db import ticket_collection


def generate_ticket_id():
    """
    Example:
    TM-20260719-4A9C7F
    """

    date = datetime.now().strftime("%Y%m%d")

    random_id = uuid.uuid4().hex[:6].upper()

    return f"TM-{date}-{random_id}"


def detect_priority(message):

    message = message.lower()

    high_keywords = [
        "angry",
        "manager",
        "lawsuit",
        "legal",
        "fraud",
        "scam",
        "defective",
        "broken",
        "damaged",
        "urgent",
        "immediately",
        "refund",
    ]

    medium_keywords = [
        "complaint",
        "issue",
        "problem",
        "not working",
        "late",
        "delay",
    ]

    for word in high_keywords:
        if word in message:
            return "High"

    for word in medium_keywords:
        if word in message:
            return "Medium"

    return "Low"


def create_ticket(session_id, user_message):

    ticket_id = generate_ticket_id()

    priority = detect_priority(user_message)

    ticket = {
        "ticket_id": ticket_id,
        "session_id": session_id,
        "issue": user_message,
        "priority": priority,
        "status": "Open",
        "created_at": datetime.utcnow(),
    }

    ticket_collection.insert_one(ticket)

    return {
        "ticket_id": ticket_id,
        "priority": priority,
        "status": "Open",
    }