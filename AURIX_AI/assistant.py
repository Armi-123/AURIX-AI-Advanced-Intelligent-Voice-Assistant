import webbrowser
import pywhatkit
from calculator import calculate
from speech import speak
from nlp import detect_intent, extract_entity

from utils import (
    current_time,
    current_date,
    random_joke,
    motivational_quote,
)

from config import (
    GOOGLE_URL,
    YOUTUBE_URL,
)

from memory import (
    set_user_name,
    get_user_name,
    add_history,
)

from reminder import add_reminder
from weather import get_weather
from wikipedia_search import search_wiki
from browser import search_web
from applications import open_app
from chatbot import chatbot_response
from sentiment import detect_sentiment


# ===========================================
# MEMORY HANDLER
# ===========================================

def handle_memory(command):

    command = command.lower()

    # Save Name
    if "my name is" in command:

        name = command.replace("my name is", "").strip()

        if name:
            set_user_name(name)

            response = f"Nice to meet you {name}"

            speak(response)
            add_history(command, response)

            return True

    # Recall Name
    elif "what is my name" in command:

        name = get_user_name()

        if name:
            response = f"Your name is {name}"
        else:
            response = "I don't know your name yet. Please tell me."

        speak(response)
        add_history(command, response)

        return True

    return False



# ===========================================
# MAIN AI ENGINE
# ===========================================

def process_command(command):

    command = command.lower().strip()

    # -----------------------------
    # MEMORY
    # -----------------------------
    if handle_memory(command):
        return True

    intent = detect_intent(command)

    response = ""

    # ===========================================
    # TIME
    # ===========================================

    if intent == "time":

        response = f"Current time is {current_time()}"

        speak(response)

    # ===========================================
    # DATE
    # ===========================================

    elif intent == "date":

        response = f"Today's date is {current_date()}"

        speak(response)

    # ===========================================

    elif intent == "greeting":

        response = "Good Morning! How can I help you?"

        speak(response)
    # ===========================================
    # GOOGLE
    # ===========================================

    elif intent == "google":

        response = "Opening Google"

        speak(response)

        webbrowser.open(GOOGLE_URL)

    # ===========================================
    # YOUTUBE
    # ===========================================

    elif intent == "youtube":

        response = "Opening YouTube"

        speak(response)

        webbrowser.open(YOUTUBE_URL)

    # ===========================================
    # PLAY MUSIC
    # ===========================================

    elif intent == "play":

        song = extract_entity(command, "play")

        if not song:

            response = "Please tell me which song to play."

        else:

            response = f"Playing {song}"

            speak(response)

            pywhatkit.playonyt(song)

    # ===========================================
    # WIKIPEDIA
    # ===========================================

    elif intent == "wiki":

        topic = (
            command.replace("who is", "")
                .replace("what is", "")
                .replace("tell me about", "")
                .strip()
        )
        
        if len(topic) < 2:

            response = "Please tell me what you want to search."

            speak(response)

        else:

            speak(f"Searching Wikipedia for {topic}")

            result = search_wiki(topic)

            response = result

            speak(result)

    # ===========================================
    # WEATHER
    # ===========================================

    elif intent == "weather":

        city = extract_entity(command, "weather")

        if not city:
            city = command.replace("weather in", "").strip()
        if not city:

            response = "Please tell me a city name."

        else:

            response = get_weather(city)
        # response = get_weather(city)

        speak(response)

    # ===========================================
    # REMINDER
    # ===========================================

    elif intent == "reminder":

        try:

            task, reminder_time = (
                command.replace("remind me to", "")
                .split("at")
            )

            response = add_reminder(
                task.strip(),
                reminder_time.strip()
            )

            speak(response)

        except ValueError:

            response = (
                "Please say like "
                "remind me to study at 18:30"
            )

            speak(response)

    # ===========================================
    # WEB SEARCH
    # ===========================================

    elif intent == "search":

        query = command.replace("search for", "").strip()

        response = search_web(query)

        speak(response)

    # ===========================================
    # OPEN APPLICATIONS
    # ===========================================

    elif intent == "open_app":

        app = extract_entity(command, "open")

        response = open_app(app)

        speak(response)

    # ===========================================
    # SENTIMENT
    # ===========================================

    elif (
        "i feel" in command
        or "how do i feel" in command
        or "i am feeling" in command
    ):

        mood = detect_sentiment(command)

        response = f"You seem {mood}"

        speak(response)

    # ===========================================
    # JOKE
    # ===========================================

    elif intent == "joke":

        response = random_joke()

        speak(response)

    # ===========================================
    # MOTIVATIONAL QUOTE
    # ===========================================

    elif intent == "quote":

        response = motivational_quote()

        speak(response)

    # ===========================================
    # EXIT
    # ===========================================

    elif intent == "exit":

        response = "Goodbye! Have a great day."

        speak(response)

        add_history(command, response)

        return False
# ===========================================

    elif intent == "thanks":

        response = "You're welcome."

        speak(response)
        
  # ===========================================
      
    elif (
        "calculate" in command
        or "what is" in command
        or "solve" in command
    ):

        math_symbols = [
            "+", "-", "*", "/", "%",
            "plus", "minus", "times",
            "multiply", "divide"
        ]

        if any(symbol in command for symbol in math_symbols):

            response = calculate(command)

            speak(response)

        else:
            topic = extract_entity(command, "")
            response = search_wiki(topic)
            speak(response)
            
    # ===========================================
    # DEFAULT CHATBOT
    # ===========================================

    else:

        response = chatbot_response(command)

        speak(response)
    
    # ===========================================
    # SAVE HISTORY
    # ===========================================

    if response:
        add_history(command, response)

    return True