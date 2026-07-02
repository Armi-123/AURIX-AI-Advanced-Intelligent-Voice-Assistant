import random


# ==========================================
# AURIX AI CHATBOT
# ==========================================

def chatbot_response(user_input):

    user_input = user_input.lower().strip()

    responses = {

        # ---------------------------------
        # Greetings
        # ---------------------------------
        "hello": [
            "Hello! How can I help you today?",
            "Hi there! Nice to meet you.",
            "Hello! I'm AURIX AI."
        ],

        "hi": [
            "Hi!",
            "Hello!",
            "Hey!"
        ],

        "good morning": [
            "Good Morning! Have a wonderful day.",
            "Good Morning! How may I assist you?"
        ],

        "good afternoon": [
            "Good Afternoon!",
            "Hope you're having a productive day."
        ],

        "good evening": [
            "Good Evening!",
            "Hope your day went well."
        ],

        # ---------------------------------
        # About Assistant
        # ---------------------------------
        "who are you": [
            "I am AURIX AI, your Advanced Intelligent Voice Assistant."
        ],

        "your name": [
            "My name is AURIX AI."
        ],

        "what can you do": [
            "I can answer questions, search Wikipedia, open applications, play music, set reminders, tell jokes, provide weather updates, and much more."
        ],

        # ---------------------------------
        # Health
        # ---------------------------------
        "how are you": [
            "I'm doing great!",
            "I'm functioning perfectly.",
            "All my systems are running smoothly."
        ],

        # ---------------------------------
        # AI
        # ---------------------------------
        "what is ai": [
            "Artificial Intelligence is the simulation of human intelligence by machines."
        ],

        "machine learning": [
            "Machine Learning is a branch of Artificial Intelligence that enables computers to learn from data."
        ],

        "deep learning": [
            "Deep Learning uses neural networks with multiple layers to solve complex problems."
        ],

        "python": [
            "Python is a popular programming language widely used in Artificial Intelligence, Data Science, Automation, and Web Development."
        ],

        # ---------------------------------
        # Courtesy
        # ---------------------------------
        "thank you": [
            "You're welcome!",
            "Happy to help!",
            "My pleasure!"
        ],

        "thanks": [
            "You're welcome!",
            "Anytime!"
        ],
        "thank":[
            "You're welcome!"
        ],
        # ---------------------------------
        # Fun
        # ---------------------------------
        "tell me something": [
            "Did you know? Python was released in 1991 by Guido van Rossum."
        ],

        "who created you": [
            "I was developed as the AURIX AI project using Python and Artificial Intelligence concepts."
        ],

        # ---------------------------------
        # Goodbye
        # ---------------------------------
        "bye": [
            "Goodbye!",
            "Take care!",
            "See you soon!"
        ]
    }

    # ---------------------------------
    # Search Matching Response
    # ---------------------------------

    for keyword, reply in responses.items():

        if keyword in user_input:
            return random.choice(reply)

    # ---------------------------------
    # Default Response
    # ---------------------------------

    default_responses = [

        "I'm still learning. Could you ask that differently?",

        "I don't have enough information about that yet.",

        "Sorry, I couldn't understand. Please try another question.",

        "That's an interesting question. I'm still improving my knowledge.",

        "Could you please rephrase your question?"
    ]

    return random.choice(default_responses)