def detect_department(message):

    message = message.lower()

    # Billing
    if (
        "payment" in message
        or "refund" in message
        or "invoice" in message
        or "subscription" in message
        or "pay" in message
        or "billing" in message
        or "charged" in message
    ):
        return "Billing"

    # Technical
    elif (
        "password" in message
        or "login" in message
        or "error" in message
        or "bug" in message
        or "install" in message
        or "setup" in message
        or "update" in message
        or "charger" in message
    ):
        return "Technical"

    # Product
    elif (
        "price" in message
        or "pricing" in message
        or "cost" in message
        or "feature" in message
        or "available" in message
        or "comparison" in message
        or "premium" in message
        or "laptop" in message
        or "phone" in message
        or "smartphone" in message
    ):
        return "Product"

    # Complaint
    elif (
        "complaint" in message
        or "bad service" in message
        or "disappointed" in message
        or "manager" in message
        or "angry" in message
        or "damaged" in message
        or "broken" in message
        or "defective" in message
        or "delivery issue" in message
    ):
        return "Complaint"

    # FAQ
    elif (
        "support hours" in message
        or "working hours" in message
        or "customer support" in message
        or "contact" in message
        or "email" in message
        or "address" in message
    ):
        return "FAQ"

    return "General"