# Web Application Attack Vector Analysis

web_events = [
    "SQL query with user input",
    "script tag detected in input field",
    "multiple failed login attempts",
    "file upload without validation",
    "normal page request"
]

for event in web_events:
    if "SQL query" in event:
        threat = "SQL Injection Vulnerability"
    elif "script tag" in event:
        threat = "Cross Site Scripting (XSS)"
    elif "failed login" in event:
        threat = "Brute Force Attack"
    elif "file upload" in event:
        threat = "Unrestricted File Upload Vulnerability"
    else:
        threat = "No Threat Detected"

    print("Event:", event)
    print("Threat Identified:", threat)
    print("-----------------------------")
