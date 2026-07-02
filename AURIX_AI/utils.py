"""
=========================================
        Utility Functions
=========================================
"""

import datetime
import random
import logging
import os

from config import LOG_FILE


# -----------------------------
# Create Log Folder
# -----------------------------

os.makedirs("logs", exist_ok=True)

logging.basicConfig(

    filename=LOG_FILE,

    level=logging.INFO,

    format="%(asctime)s | %(levelname)s | %(message)s"

)


# -----------------------------
# Write Log
# -----------------------------

def write_log(message):

    logging.info(message)


# -----------------------------
# Current Time
# -----------------------------

def current_time():

    return datetime.datetime.now().strftime("%I:%M %p")


# -----------------------------
# Current Date
# -----------------------------

def current_date():

    return datetime.datetime.now().strftime("%d %B %Y")


# -----------------------------
# Greeting
# -----------------------------

def greeting():

    hour = datetime.datetime.now().hour

    if hour < 12:

        return "Good Morning"

    elif hour < 17:

        return "Good Afternoon"

    else:

        return "Good Evening"


# -----------------------------
# Random Joke
# -----------------------------

def random_joke():

    jokes = [

        "Why do programmers prefer dark mode? Because light attracts bugs.",

        "Why did Python break up with Java? Because it found someone less complicated.",

        "Artificial Intelligence never sleeps because it has no dreams.",

        "I am an AI, but I still can't find your missing socks."

    ]

    return random.choice(jokes)


# -----------------------------
# Motivational Quote
# -----------------------------

def motivational_quote():

    quotes = [

        "Success is the sum of small efforts repeated every day.",

        "Believe in yourself.",

        "Every expert was once a beginner.",

        "Dream big and dare to fail."

    ]

    return random.choice(quotes)


# -----------------------------
# Banner
# -----------------------------

def banner():

    print("=" * 60)

    print("          A U R I X    A I")

    print(" Advanced Intelligent Voice Assistant")

    print("=" * 60)


# -----------------------------
# Clean Command
# -----------------------------

def clean_command(command):

    command = command.lower()

    command = command.strip()

    return command


# -----------------------------
# Exit Check
# -----------------------------

def should_exit(command):

    exits = [

        "exit",

        "quit",

        "stop",

        "bye",

        "goodbye"

    ]

    return command in exits