import os

project_name = "AURIX_AI"

folders = [
    "logs",
    "assets",
    "screenshots",
    "models",
    "data"
]

files = [
    "main.py",
    "assistant.py",
    "speech.py",
    "nlp.py",
    "memory.py",
    "reminder.py",
    "weather.py",
    "wikipedia_search.py",
    "calculator.py",
    "sentiment.py",
    "applications.py",
    "browser.py",
    "chatbot.py",
    "scheduler.py",
    "utils.py",
    "config.py",
    "requirements.txt",
    "README.md",
    "LICENSE",
    ".gitignore",
    "memory.json",
    "reminders.json",
    "history.json",
    "settings.json",
    "logs/assistant.log",
    "assets/logo.png",
    "assets/microphone.png",
    "assets/assistant_icon.ico",
    "screenshots/home.png",
    "screenshots/voice_input.png",
    "screenshots/reminder.png",
    "screenshots/weather.png",
    "screenshots/chatbot.png",
    "models/intent_model.pkl",
    "data/intents.json",
    "data/greetings.json",
    "data/knowledge_base.json"
]

os.makedirs(project_name, exist_ok=True)

for folder in folders:
    os.makedirs(os.path.join(project_name, folder), exist_ok=True)

for file in files:
    path = os.path.join(project_name, file)

    folder = os.path.dirname(path)

    if folder:
        os.makedirs(folder, exist_ok=True)

    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:

            if file.endswith(".json"):
                f.write("{}")

            elif file == "README.md":
                f.write("# AURIX AI\n")

            elif file == "requirements.txt":
                f.write("")

            elif file == ".gitignore":
                f.write("__pycache__/\n*.pyc\n.env\n")

            elif file == "LICENSE":
                f.write("MIT License")

print("\nProject Created Successfully!")
print(f"\nLocation : {os.path.abspath(project_name)}")