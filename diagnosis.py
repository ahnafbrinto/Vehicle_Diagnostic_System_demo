#!/usr/bin/env python3


# another_script.py

import random

# Generate random diagnostic codes and statuses
def generate_diagnostic_codes_and_statuses(num):
    diagnostic_codes = []
    for _ in range(num):
        code = random.randint(100000, 108000)
        status = get_status(code)
        location = get_location()
        diagnostic_codes.append(f"Diagnostic Code: {code} ~ Status: {status} : {location}")
    return diagnostic_codes

# Get status based on diagnostic code range
def get_status(code):
    if 100000 <= code < 103000:
        return "GOOD     # Working Well    "
    elif 103000 <= code < 104000:
        return "FAIR     # Service Due soon"
    elif 104000 <= code < 105000:
        return "POOR     # Service Needed  "
    elif 105000 <= code < 106000:
        return "BAD      # Service Urgent  "
    elif 106000 <= code < 107000:
        return "CRITICAL # Problem Detected"
    elif 107000 <= code <= 108000:
        return "NUCLEAR  # Replace Part    "

# Get random location from the specified list
def get_location():
    locations = [
        "Hood", "Engine", "Front Wheels", "Left Front Door", "Right Front Door",
        "Left Rear Door", "Right Rear Door", "Trunk Hood", "Rear Wheels",
        "Back Window", "Cabin", "Center Console"
    ]
    return random.choice(locations)

# Generate 12 random diagnostic codes and statuses with locations
random_diagnostic_codes = generate_diagnostic_codes_and_statuses(12)

# Print the generated diagnostic codes and statuses
for code in random_diagnostic_codes:
    print(code)
