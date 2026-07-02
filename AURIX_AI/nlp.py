import re


# ==========================================
# AI Intent Detection
# ==========================================
def detect_intent(command):

    command = command.lower().strip()

    # TIME
    if any(word in command for word in [
        "time",
        "current time",
        "what time"
    ]):
        return "time"

    # DATE
    elif any(word in command for word in [
        "date",
        "today",
        "today's date"
    ]):
        return "date"

    # GOOGLE
    elif "open google" in command:
        return "google"

    # YOUTUBE
    elif "open youtube" in command:
        return "youtube"

    # WIKIPEDIA / KNOWLEDGE
    elif any(word in command for word in [
        "who is",
        "what is",
        "tell me about",
        "define",
        "explain",
        "information about"
    ]):
        return "wiki"

    # PLAY MUSIC
    elif command.startswith("play "):
        return "play"

    # WEATHER
    elif "weather" in command:
        return "weather"

    # REMINDER
    elif "remind me" in command:
        return "reminder"

    # SEARCH
    elif command.startswith("search for"):
        return "search"

    # OPEN APPLICATION
    elif command.startswith("open"):
        return "open_app"

    # JOKE
    elif "joke" in command:
        return "joke"

    # QUOTE
    elif "quote" in command or "motivate" in command:
        return "quote"

    # SENTIMENT
    elif (
        "i feel" in command
        or "i am feeling" in command
        or "how do i feel" in command
    ):
        return "sentiment"

    # MEMORY
    elif "my name is" in command:
        return "save_name"

    elif "what is my name" in command:
        return "get_name"

    # EXIT
    elif any(word in command for word in [
        "exit",
        "quit",
        "stop",
        "bye"
    ]):
        return "exit"

    # DEFAULT
    return "chat"


# ==========================================
# Extract Entity
# ==========================================
def extract_entity(command, keyword):

    command = command.lower()

    command = command.replace(keyword, "")

    remove_words = [
        "who is",
        "what is",
        "tell me about",
        "define",
        "explain",
        "information about",
        "play",
        "open",
        "search for"
    ]

    for word in remove_words:
        command = command.replace(word, "")

    command = re.sub(r"\s+", " ", command)

    return command.strip()
