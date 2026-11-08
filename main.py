import time
from company import auth, timeconvert
from company.branches import EMPLOYEES, get_branch, get_branch_codes

def format_utc_offset(offset):
    """Format a UTC offset in hours and minutes."""
    sign = "+" if offset >= 0 else "-"

    total_minutes = int(round(abs(offset) * 60))
    hours, minutes = divmod(total_minutes, 60)

    if minutes == 0:
        return f"UTC{sign}{hours}"

    return f"UTC{sign}{hours}:{minutes:02d}"


def show_all_branch_times():
    """Display the current time at every company branch."""
    print("\n--- Current time at all branches ---")

    for code in get_branch_codes():
        branch = get_branch(code)
        current_time = timeconvert.get_branch_time(code)

        city = branch["city"]
        tz = branch["tz"]
        offset = branch["offset"]

        offset_text = format_utc_offset(offset)

        print(f"{city} ({tz}, {offset_text}): {current_time}")


def read_time():
    """Read and validate a meeting time in HH:MM format."""
    entered_time = input("Enter a time in 24-hour format (HH:MM): ").strip()

    if len(entered_time) != 5 or entered_time[2] != ":":
        return None

    hour_text, minute_text = entered_time.split(":")

    if not hour_text.isdigit() or not minute_text.isdigit():
        return None

    hour = int(hour_text)
    minute = int(minute_text)

    if hour > 23 or minute > 59:
        return None

    return hour, minute

def convert_meeting_time(my_code):
    """Convert a meeting time to the other company branches."""
    meeting_time = read_time()

    if meeting_time is None:
        print("Invalid time. Use HH:MM, for example 09:30 or 17:45.")
        return

    hour, minute = meeting_time
    my_branch = get_branch(my_code)

    print(f"\n{hour:02d}:{minute:02d} in {my_branch['city']} is:")

    for code in get_branch_codes():
        if code == my_code:
            continue

        new_hour, new_minute, day_change = timeconvert.convert_time(
            hour, minute, my_code, code
        )

        branch = get_branch(code)
        difference = timeconvert.hour_difference(my_code, code)
        day_description = timeconvert.describe_day_change(day_change)

        print(
            f"  {new_hour:02d}:{new_minute:02d} in {branch['city']} "
            f"{day_description} [{difference:+d} h]"
        )

def employee_menu(username):
    """Display the employee menu until the user logs out."""
    employee = EMPLOYEES[username]
    my_code = employee["branch"]
    branch = get_branch(my_code)

    start = time.time()

    print(f"\nWelcome, {employee['name']}! ({branch['city']}, {branch['country']} branch)")
    print(f"Logged in at {timeconvert.get_branch_time(my_code)} {branch['tz']}")

    while True:
        print("\n[1] Show all branch times")
        print("[2] Convert a meeting time")
        print("[3] Logout")

        choice = input("Choose: ").strip()

        if choice == "1":
            show_all_branch_times()

        elif choice == "2":
            convert_meeting_time(my_code)

        elif choice == "3":
            minutes, seconds = divmod(int(time.time() - start), 60)

            print(
                f"Goodbye, {employee['name']}. "
                f"Session length: {minutes} min {seconds} sec."
            )
            return

        else:
            print("Invalid choice.")

def main():
    """Start the company login system."""
    print("=" * 45)
    print("  GLOBALTECH SOLUTIONS - EMPLOYEE LOGIN")
    print("=" * 45)

    while True:
        username = auth.login()

        if username is not None:
            employee_menu(username)

        again = input("\nLog in again? (y/n): ").strip().lower()

        if again != "y":
            print("System closed.")
            break

if __name__ == "__main__":
    main()
