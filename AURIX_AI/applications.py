import os
import subprocess


# ==========================================
# OPEN DESKTOP APPLICATIONS
# ==========================================

def open_app(app_name):

    app_name = app_name.lower().strip()

    try:

        # ---------------- NOTEPAD ----------------
        if app_name in [
            "note",
            "notes",
            "notepad"
        ]:
            os.system("start notepad")
            return "Opening Notepad"

        # ---------------- CALCULATOR ----------------
        elif app_name in [
            "calc",
            "calculator"
        ]:
            os.system("start calc")
            return "Opening Calculator"

        # ---------------- PAINT ----------------
        elif app_name in [
            "paint",
            "mspaint"
        ]:
            os.system("start mspaint")
            return "Opening Paint"

        # ---------------- COMMAND PROMPT ----------------
        elif app_name in [
            "cmd",
            "command prompt"
        ]:
            os.system("start cmd")
            return "Opening Command Prompt"

        # ---------------- POWERSHELL ----------------
        elif app_name in [
            "powershell"
        ]:
            os.system("start powershell")
            return "Opening PowerShell"

        # ---------------- FILE EXPLORER ----------------
        elif app_name in [
            "explorer",
            "file explorer",
            "files"
        ]:
            os.system("start explorer")
            return "Opening File Explorer"

        # ---------------- CHROME ----------------
        elif app_name in [
            "chrome",
            "google chrome"
        ]:
            subprocess.Popen("start chrome", shell=True)
            return "Opening Google Chrome"

        # ---------------- EDGE ----------------
        elif app_name in [
            "edge",
            "microsoft edge"
        ]:
            subprocess.Popen("start msedge", shell=True)
            return "Opening Microsoft Edge"

        # ---------------- VS CODE ----------------
        elif app_name in [
            "code",
            "vs code",
            "visual studio code",
            "vscode"
        ]:
            subprocess.Popen("code", shell=True)
            return "Opening Visual Studio Code"

        # ---------------- WORD ----------------
        elif app_name in [
            "word",
            "ms word",
            "microsoft word"
        ]:
            subprocess.Popen("start winword", shell=True)
            return "Opening Microsoft Word"

        # ---------------- EXCEL ----------------
        elif app_name in [
            "excel",
            "ms excel"
        ]:
            subprocess.Popen("start excel", shell=True)
            return "Opening Microsoft Excel"

        # ---------------- POWERPOINT ----------------
        elif app_name in [
            "powerpoint",
            "ppt"
        ]:
            subprocess.Popen("start powerpnt", shell=True)
            return "Opening PowerPoint"

        else:
            return f"Sorry, I don't know how to open '{app_name}'."

    except Exception as e:
        return f"Failed to open application: {e}"
