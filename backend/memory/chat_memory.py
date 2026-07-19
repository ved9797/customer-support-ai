from datetime import datetime
from database.mongodb import chat_collection


def add_message(role, message, user_id, session_id="default"):

    chat_collection.insert_one(
        {
            "user_id":user_id,
            "session_id": session_id,
            "role": role,
            "message": message,
            "timestamp": datetime.utcnow()
        }
    )

def get_history(user_id, session_id="default"):

    history = chat_collection.find(
        {
            "user_id": user_id,
            "session_id": session_id
        },
        {"_id": 0}
    ).sort("timestamp", 1)

    return list(history)


def get_conversation(session_id="default"):

    chats = get_history(session_id)

    conversation = ""

    for chat in chats:

        conversation += (
            f"{chat['role']}: {chat['message']}\n"
        )

    return conversation