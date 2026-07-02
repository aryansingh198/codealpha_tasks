"""
CodeAlpha_BasicChatbot
------------------------
A rule-based chatbot with a bit of extra polish so it stands out:

Features:
- Keyword-based responses (hello, how are you, bye, etc.)
- Time-aware greeting (Good Morning/Afternoon/Evening)
- Handles multiple keywords in one sentence
- Remembers user's name once told, and uses it later in chat
- Fun extras: tells a joke, tells current time
- Saves full chat history to a .txt log file on exit

Key Concepts Used: if-elif, functions, loops, input/output
Author: Aryan
"""

import random
from datetime import datetime

user_name = None
chat_log = []

JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did the Python programmer not like function calls? They had too many arguments.",
    "I told my computer I needed a break, now it won't stop sending me KitKat ads.",
]


def get_time_greeting():
    hour = datetime.now().hour
    if hour < 12:
        return "Good Morning"
    elif hour < 17:
        return "Good Afternoon"
    else:
        return "Good Evening"


def log(speaker, message):
    chat_log.append(f"{speaker}: {message}")


def bot_reply(user_input):
    global user_name
    text = user_input.lower().strip()

    # Name detection
    if "my name is" in text:
        user_name = user_input.split("is", 1)[1].strip().title()
        return f"Nice to meet you, {user_name}! 😊"

    if any(word in text for word in ["hello", "hi", "hey"]):
        greet = f", {user_name}" if user_name else ""
        return f"{get_time_greeting()}{greet}! How can I help you today?"

    if "how are you" in text:
        return "I'm just a bunch of code, but I'm running smoothly! How about you?"

    if "your name" in text:
        return "I'm CodeAlpha Bot, your friendly rule-based assistant!"

    if "time" in text:
        return f"Current time is {datetime.now().strftime('%I:%M %p')}."

    if "joke" in text:
        return random.choice(JOKES)

    if any(word in text for word in ["thanks", "thank you"]):
        return "You're most welcome! 🙌"

    if any(word in text for word in ["bye", "goodbye", "exit", "quit"]):
        return "__EXIT__"

    if "help" in text:
        return ("I can chat about: greetings, how you're doing, my name, "
                 "the time, a joke, or just say 'bye' to leave!")

    return "Hmm, I didn't quite get that. Try saying 'help' to see what I can do!"


def main():
    print("=" * 55)
    print("        🤖  BASIC RULE-BASED CHATBOT  🤖")
    print("=" * 55)
    print("Type 'bye' anytime to end the chat.\n")

    bot_start = f"{get_time_greeting()}! I'm CodeAlpha Bot. What's your name?"
    print("Bot:", bot_start)
    log("Bot", bot_start)

    while True:
        user_input = input("You: ")
        log("You", user_input)

        reply = bot_reply(user_input)

        if reply == "__EXIT__":
            farewell = f"Goodbye{', ' + user_name if user_name else ''}! Take care. 👋"
            print("Bot:", farewell)
            log("Bot", farewell)
            break

        print("Bot:", reply)
        log("Bot", reply)

    # Save chat log
    filename = f"chat_log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    with open(filename, "w") as f:
        f.write("\n".join(chat_log))
    print(f"\n📁 Chat history saved to '{filename}'")


if __name__ == "__main__":
    main()