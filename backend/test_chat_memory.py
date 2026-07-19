from memory.chat_memory import add_message, get_history

add_message("user", "Hello MongoDB!")

add_message("assistant", "Hello Vedanshi!")

history = get_history()

print(history)