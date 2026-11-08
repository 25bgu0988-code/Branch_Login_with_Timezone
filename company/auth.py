import time
from company.branches import EMPLOYEES

MAX_ATTEMPTS = 3
LOCKOUT_SECONDS = 5

def check_credentials(username, password):
    """Check whether the employee credentials are valid."""
    username = username.lower()

    if username in EMPLOYEES:
        return EMPLOYEES[username]["password"] == password

    return False

def login():
    """Handle employee login with a maximum of three attempts."""
    for attempt in range(MAX_ATTEMPTS):
        username = input("Username: ").strip().lower()
        password = input("Password: ")

        if check_credentials(username, password):
            return username

        attempts_left = MAX_ATTEMPTS - (attempt + 1)

        print(f"Invalid username or password. Attempts left: {attempts_left}")

    print("Too many failed attempts. Please wait 5 seconds.")
    time.sleep(LOCKOUT_SECONDS)

    return None
