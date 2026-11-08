
import time
from company.branches import BRANCHES, get_branch

TIME_FORMAT = "%A, %d %B %Y %I:%M:%S %p"


def get_local_time(offset):
    """Return the current time at the given UTC offset."""
    return time.gmtime(time.time() + offset * 3600)

def format_time(t):
    """Format a time structure into readable text."""
    return time.strftime(TIME_FORMAT, t)

def get_branch_time(code):
    """Return the current formatted time of a branch."""
    branch = get_branch(code)
    return format_time(get_local_time(branch["offset"]))

def hour_difference(from_code, to_code):
    """Return the hour difference between two branches."""
    from_branch = BRANCHES[from_code]
    to_branch = BRANCHES[to_code]

    return to_branch["offset"] - from_branch["offset"]


def convert_time(hour, minute, from_code, to_code):
    """Convert meeting time and track the day change."""
    difference = hour_difference(from_code, to_code)

    difference_minutes = int(round(difference * 60))

    total = hour * 60 + minute + difference_minutes

    day_change = total // 1440

    total = total % 1440

    new_hour = total // 60
    new_minute = total % 60

    return new_hour, new_minute, day_change


def describe_day_change(day_change):
    """Describe whether the converted time changes the day."""
    if day_change > 0:
        return "(next day)"
    elif day_change < 0:
        return "(previous day)"
    else:
        return "(same day)"
