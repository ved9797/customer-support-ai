def detect_departments(message):

    message = message.lower()

    departments = []

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
        departments.append("Billing")

    # Technical
    if (
        "password" in message
        or "login" in message
        or "error" in message
        or "bug" in message
        or "install" in message
        or "setup" in message
        or "update" in message
        or "charger" in message
        or "overheat" in message
        or "overheating" in message
    ):
        departments.append("Technical")

    # Product
    if (
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
        departments.append("Product")

    # Complaint
    if (
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
        departments.append("Complaint")

    # FAQ
    if (
        "support hours" in message
        or "working hours" in message
        or "customer support" in message
        or "contact" in message
        or "email" in message
        or "address" in message
    ):
        departments.append("FAQ")

    if not departments:
        departments.append("General")

    return departments