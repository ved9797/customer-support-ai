chat_history = []

def add_message(role, message):

    chat_history.append(
        {
            "role": role,
            "message": message
        }
    )

def get_history():

    return chat_history

def get_conversation():

    conversation = ""

    for chat in chat_history:
        conversation += f"{chat['role']}: {chat['message']}\n"

    return conversation