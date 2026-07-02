import time
from datetime import datetime
from speech import speak
from reminder import load_reminders, save_reminders


# -----------------------------
# CHECK REMINDERS LOOP
# -----------------------------
def start_scheduler():

    print("Scheduler started...")

    while True:

        now = datetime.now().strftime("%H:%M")

        reminders = load_reminders()

        for r in reminders:

            if r["status"] == "pending" and r["time"] == now:

                speak(f"Reminder: {r['task']}")

                r["status"] = "done"

                save_reminders(reminders)

        time.sleep(30)