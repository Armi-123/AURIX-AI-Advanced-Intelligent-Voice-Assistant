import json
import os

MEMORY_FILE = "memory.json"
HISTORY_FILE = "history.json"


# -------------------------
# Load Memory
# -------------------------
def load_memory():

    if not os.path.exists(MEMORY_FILE):
        return {}

    with open(MEMORY_FILE, "r") as f:
        return json.load(f)


# -------------------------
# Save Memory
# -------------------------
def save_memory(data):

    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=4)


# -------------------------
# Store User Name
# -------------------------
def set_user_name(name):

    data = load_memory()
    data["name"] = name
    save_memory(data)


# -------------------------
# Get User Name
# -------------------------
def get_user_name():

    data = load_memory()
    return data.get("name", None)


# -------------------------
# Add Chat History
# -------------------------
def add_history(user, assistant):

    if not os.path.exists(HISTORY_FILE):
        history = []
    else:
        with open(HISTORY_FILE, "r") as f:
            history = json.load(f)

    history.append({
        "user": user,
        "assistant": assistant
    })

    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)


# -------------------------
# Get Last Conversations
# -------------------------
def get_history(limit=5):

    if not os.path.exists(HISTORY_FILE):
        return []

    with open(HISTORY_FILE, "r") as f:
        history = json.load(f)

    return history[-limit:]