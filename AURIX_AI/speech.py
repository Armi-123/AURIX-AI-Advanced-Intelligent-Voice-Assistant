import speech_recognition as sr
import pyttsx3
from config import VOICE_RATE, VOICE_VOLUME

# -----------------------------
# Text-to-Speech Engine
# -----------------------------
engine = pyttsx3.init()
engine.setProperty("rate", VOICE_RATE)
engine.setProperty("volume", VOICE_VOLUME)

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def speak(text):
    """Convert text to speech"""
    print(f"AURIX AI: {text}")
    engine.say(text)
    engine.runAndWait()


# -----------------------------
# Voice Recognition
# -----------------------------
def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\n🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(source, timeout=6, phrase_time_limit=6)
            command = recognizer.recognize_google(audio)
            print(f"You: {command}")
            return command.lower()

        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return ""

        except sr.RequestError:
            speak("Speech service is unavailable.")
            return ""

        except Exception:
            return ""