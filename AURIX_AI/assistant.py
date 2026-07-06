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
    """
    Handles user memory:
    - Save user's name
    - Recall user's name
    """

    command = command.lower().strip()

    # -----------------------------
    # SAVE USER NAME
    # -----------------------------
    if "my name is" in command:

        name = command.replace("my name is", "").strip()

        if not name:
            speak("Please tell me your name.")
            return True

        set_user_name(name)

        response = f"Nice to meet you, {name.title()}."

        speak(response)
        add_history(command, response)

        return True

    # -----------------------------
    # RECALL USER NAME
    # -----------------------------
    if "what is my name" in command:

        name = get_user_name()

        if name:
            response = f"Your name is {name.title()}."
        else:
            response = (
                "I don't know your name yet. "
                "Please tell me by saying 'My name is ...'."
            )

        speak(response)
        add_history(command, response)

        return True

    return False

# ===========================================
# MAIN AI ENGINE
# ===========================================

def process_command(command):

    try:

        command = command.lower().strip()

        # -----------------------------------
        # MEMORY
        # -----------------------------------
        if handle_memory(command):
            return True

        intent = detect_intent(command)

        response = ""

        # ===================================
        # GREETING
        # ===================================

        if intent == "greeting":

            response = "Hello! I'm AURIX AI. How can I help you today?"

            speak(response)

        # ===================================
        # TIME
        # ===================================

        elif intent == "time":

            response = f"Current time is {current_time()}"

            speak(response)

        # ===================================
        # DATE
        # ===================================

        elif intent == "date":

            response = f"Today's date is {current_date()}"

            speak(response)

        # ===================================
        # GOOGLE
        # ===================================

        elif intent == "google":

            response = "Opening Google"

            speak(response)

            webbrowser.open(GOOGLE_URL)

        # ===================================
        # YOUTUBE
        # ===================================

        elif intent == "youtube":

            response = "Opening YouTube"

            speak(response)

            webbrowser.open(YOUTUBE_URL)

        # ===================================
        # PLAY MUSIC
        # ===================================

        elif intent == "play":

            song = extract_entity(command, "play")

            if not song:

                response = "Please tell me which song you want to play."

                speak(response)

            else:

                response = f"Playing {song}"

                speak(response)

                try:
                    pywhatkit.playonyt(song)

                except Exception:

                    response = "Sorry, I couldn't play that song."

                    speak(response)

        # ===================================
        # CALCULATOR
        # ===================================

        elif intent == "calculator":

            # print("Calculator block reached")

            response = calculate(command)

            # print("Calculator Response:", response)

            speak(response)
            
        # ===================================
        # WIKIPEDIA
        # ===================================

        elif intent == "wiki":

            topic = (
                command.replace("who is", "")
                    .replace("what is", "")
                    .replace("tell me about", "")
                    .replace("define", "")
                    .replace("explain", "")
                    .replace("information about", "")
                    .strip()
)

            if not topic:

                response = "Please tell me what you want to search."

                speak(response)

            else:

                speak(f"Searching Wikipedia for {topic}")

                response = search_wiki(topic)

                print("\nWikipedia Result:\n")
                print(response)

                words = response.split()

                short_response = (
                    " ".join(words[:30]) + "..."
                    if len(words) > 30
                    else response
                )

                speak(short_response)
                
        # ===================================
        # WEATHER
        # ===================================

        elif intent == "weather":

            response = get_weather(command)

            speak(response)

        # ===================================
        # REMINDER
        # ===================================

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

            except Exception:

                response = (
                    "Please say like "
                    "'Remind me to study at 18:30'."
                )

            speak(response)

        # ===================================
        # WEB SEARCH
        # ===================================

        elif intent == "search":

            query = extract_entity(command, "search for")

            response = search_web(query)

            speak(response)

        # ===================================
        # OPEN APPLICATION
        # ===================================

        elif intent == "open_app":

            app = extract_entity(command, "open")

            if not app:

                response = "Please tell me which application you want to open."

            else:

                response = open_app(app)

            speak(response)

        # ===================================
        # SENTIMENT
        # ===================================

        elif intent == "sentiment":

            mood = detect_sentiment(command)

            response = f"You seem {mood}."

            speak(response)

        # ===================================
        # JOKE
        # ===================================

        elif intent == "joke":

            response = random_joke()

            speak(response)

        # ===================================
        # MOTIVATIONAL QUOTE
        # ===================================

        elif intent == "quote":

            response = motivational_quote()

            speak(response)

        # ===================================
        # THANKS
        # ===================================

        elif intent == "thanks":

            response = "You're welcome. Happy to help."

            speak(response)

        # ===================================
        # EXIT
        # ===================================

        elif intent == "exit":

            response = "Goodbye! Have a great day."

            speak(response)

            add_history(command, response)

            return False

        # ===================================
        # CHATBOT
        # ===================================

        else:

            response = chatbot_response(command)

            speak(response)

        # ===================================
        # SAVE HISTORY
        # ===================================

        if response:

            add_history(command, response)

        return True

    except Exception as e:
        print(f"[AURIX ERROR] {e}")
        speak("Sorry, something went wrong.")

        return True