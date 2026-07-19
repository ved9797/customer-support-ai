def should_escalate(message: str) -> bool:

    message = message.lower()

    escalation_phrases = [
        "talk to a human",
        "human agent",
        "customer representative",
        "support representative",
        "real person",
        "live agent",
        "connect me to support",
        "escalate",
        "manager",
        "supervisor",
        "this is my third complaint",
        "i have contacted you before",
        "nobody helped",
        "still not resolved",
        "not satisfied",
    ]

    return any(
        phrase in message
        for phrase in escalation_phrases
    )