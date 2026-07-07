"""
==========================================================
        AURIX AI - Advanced Intelligent Voice Assistant
==========================================================
Configuration File

This file contains all configurable settings used by the
AURIX AI application.

Author  : Armi Sherathiya
Version : 1.0
==========================================================
"""

# ==========================================================
# Assistant Information
# ==========================================================

ASSISTANT_NAME = "AURIX"
VERSION = "1.0"
AUTHOR = "Armi Sherathiya"

# ==========================================================
# Voice Settings
# ==========================================================

VOICE_RATE = 175          # Speech Speed
VOICE_VOLUME = 1.0        # Range: 0.0 to 1.0

# ==========================================================
# Greeting Messages
# ==========================================================

WELCOME_MESSAGE = f"""
Hello!

I am {ASSISTANT_NAME},
your Advanced Intelligent Voice Assistant.

How may I help you today?
"""

GOODBYE_MESSAGE = """
Goodbye!

Have a wonderful day.
"""

# ==========================================================
# Browser URLs
# ==========================================================

GOOGLE_URL = "https://www.google.com"
YOUTUBE_URL = "https://www.youtube.com"
GITHUB_URL = "https://github.com"
CHATGPT_URL = "https://chat.openai.com"

# ==========================================================
# Wikipedia Settings
# ==========================================================

WIKI_SENTENCES = 2

# ==========================================================
# Weather API Configuration
# ==========================================================

WEATHER_API_KEY = "3b040c790118481eaea554faa493e438"

WEATHER_BASE_URL = (
    "https://api.openweathermap.org/data/2.5/weather"
)

WEATHER_UNIT = "metric"

# ==========================================================
# Application Settings
# ==========================================================

DEFAULT_LANGUAGE = "en"

LISTEN_TIMEOUT = 5

PHRASE_TIME_LIMIT = 7

# ==========================================================
# Memory & Database Files
# ==========================================================

MEMORY_FILE = "memory.json"

HISTORY_FILE = "history.json"

REMINDER_FILE = "reminders.json"

SETTINGS_FILE = "settings.json"

# ==========================================================
# Log File
# ==========================================================

LOG_FILE = "logs/assistant.log"

# ==========================================================
# Supported Exit Commands
# ==========================================================

# Supported Exit Commands

EXIT_COMMANDS = [
    "exit",
    "quit",
    "stop",
    "bye",
    "goodbye",
    "bye bye",
    "bye-bye",
    "see you",
    "see you later",
    "good night",
    "close assistant",
    "close aurix",
    "shutdown assistant",
    "shutdown aurix",
    "terminate",
    "end",
    "end session"
]