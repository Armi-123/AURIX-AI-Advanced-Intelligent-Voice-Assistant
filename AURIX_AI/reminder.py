import json
import os
from datetime import datetime

REMINDER_FILE = "reminders.json"


# -----------------------------
# LOAD REMINDERS
# -----------------------------
def load_reminders():

    if not os.path.exists(REMINDER_FILE):
        return []

    with open(REMINDER_FILE, "r") as f:
        return json.load(f)


# -----------------------------
# SAVE REMINDERS
# -----------------------------
def save_reminders(data):

    with open(REMINDER_FILE, "w") as f:
        json.dump(data, f, indent=4)


# -----------------------------
# ADD REMINDER
# -----------------------------
def add_reminder(task, time_str):

    reminders = load_reminders()

    reminder = {
        "task": task,
        "time": time_str,
        "status": "pending"
    }

    reminders.append(reminder)
    save_reminders(reminders)

    return f"Reminder set for {time_str} to {task}"


# -----------------------------
# GET PENDING REMINDERS
# -----------------------------
def get_pending_reminders():

    reminders = load_reminders()

    return [r for r in reminders if r["status"] == "pending"]


# -----------------------------
# MARK COMPLETED
# -----------------------------
def mark_done(task):

    reminders = load_reminders()

    for r in reminders:
        if r["task"] == task:
            r["status"] = "done"

    save_reminders(reminders)