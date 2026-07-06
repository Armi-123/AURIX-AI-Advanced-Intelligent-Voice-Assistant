import re
from config import EXIT_COMMANDS

# ==========================================
# AI Intent Detection
# ==========================================
def detect_intent(command):

    command = command.lower().strip()

    # TIME
    if any(x in command for x in [
        "time",
        "current time",
        "what time"
    ]):
        return "time"

    # DATE
    elif any(x in command for x in [
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

    # MUSIC
    elif command.startswith("play "):
        return "play"

    # WEATHER
    elif (
        "weather in" in command
        or "weather at" in command
        or command.startswith("weather")
    ):
        return "weather"

    # WIKIPEDIA
    elif any(x in command for x in [
        "who is",
        "what is",
        "tell me about",
        "define",
        "explain",
        "information about"
    ]):
        return "wiki"

    # Calculator
    elif (
        command.startswith("calculate")
        or command.startswith("solve")
        or re.search(r"\d+\s*[\+\-\*/%x]\s*\d+", command)
        or "plus" in command
        or "minus" in command
        or "times" in command
        or "multiply" in command
        or "divided by" in command
        or "divide" in command
    ):
        return "calculator"

    # REMINDER
    elif "remind me" in command:
        return "reminder"

    # WEB SEARCH
    elif command.startswith("search for"):
        return "search"

    # OPEN APPLICATION
    elif command.startswith("open"):
        return "open_app"

    # JOKE
    elif "joke" in command:
        return "joke"

    # MOTIVATIONAL QUOTE
    elif (
        "quote" in command
        or "motivation" in command
        or "motivational" in command
        or "motivate me" in command
    ):
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

    # GREETINGS
    elif any(x in command for x in [
        "hello",
        "hi",
        "good morning",
        "good afternoon",
        "good evening"
    ]):
        return "greeting"

    # THANKS
    elif any(x in command for x in [
        "thank you",
        "thanks"
    ]):
        return "thanks"

    # EXIT
    elif any(word in command for word in [
        "exit",
        "quit",
        "stop",
        "bye"
    ]):
        return "exit"
    
    # EXIT
    elif any(exit_cmd in command for exit_cmd in EXIT_COMMANDS):
        return "exit"

    return "chat"


# ==========================================
# Entity Extractor
# ==========================================
def extract_entity(command, keyword=""):

    command = command.lower()

    if keyword:
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
        "search for",
        "weather in",
        "weather at",
        "calculate",
        "the",
        "a",
        "an",
        "define",
        "definition",
        "explain",
        "about",
        "information",
        "two line",
        "in two lines"
    ]

    for word in remove_words:
        command = command.replace(word, "")

    command = re.sub(r"\s+", " ", command)

    return command.strip()