import json
import os

USERS_FILE = "users.json"

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

def add_user(username, email, password):
    users = load_users()
    if username in users:
        return False  # Username already exists
    users[username] = {"email": email, "password": password}
    save_users(users)
    return True

def validate_user(username, password):
    users = load_users()
    return username in users and users[username]["password"] == password
