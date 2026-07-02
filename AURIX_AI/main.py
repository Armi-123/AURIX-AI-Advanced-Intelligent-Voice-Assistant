from speech import speak, listen
from assistant import process_command
from utils import banner, greeting, write_log
from config import WELCOME_MESSAGE

# -----------------------------
# MAIN APPLICATION
# -----------------------------
def main():

    banner()
    speak(WELCOME_MESSAGE)

    speak(greeting())

    running = True

    while running:

        command = listen()

        if not command:
            continue

        write_log(f"User: {command}")

        running = process_command(command)

        write_log("Assistant responded")


# -----------------------------
# START PROGRAM
# -----------------------------
if __name__ == "__main__":
    main()