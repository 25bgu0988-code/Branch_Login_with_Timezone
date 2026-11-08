

BRANCHES = {
    "MNL": {"city": "Manila", "country": "Philippines", "tz": "PHT", "offset": 8},
    "TYO": {"city": "Tokyo", "country": "Japan", "tz": "JST", "offset": 9},
    "DXB": {"city": "Dubai", "country": "United Arab Emirates", "tz": "GST", "offset": 4},
    "MUM": {"city": "Mumbai", "country": "India", "tz": "IST", "offset": 5.5}
}

EMPLOYEES = {
    "juan": {
        "password": "mnl123",
        "name": "Juan Dela Cruz",
        "branch": "MNL"
    },
    "yuki": {
        "password": "tyo123",
        "name": "Yuki Tanaka",
        "branch": "TYO"
    },
    "omar": {
        "password": "dxb123",
        "name": "Omar Haddad",
        "branch": "DXB"
    }
}

def get_branch(code):
    """Return branch information using its code."""
    return BRANCHES.get(code)


def get_branch_codes():
    """Return a list of all branch codes."""
    return list(BRANCHES.keys())
