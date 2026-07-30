network_events = [
    "multiple failed login attempts",
    "high traffic volume",
    "malicious attachment detected",
    "fake email requesting credentials",
    "normal web browsing"
]

# Threat classification
for event in network_events:
    if "failed login" in event:
        threat = "Unauthorized Access"
    elif "high traffic" in event:
        threat = "Denial of Service (DoS)"
    elif "malicious attachment" in event:
        threat = "Malware"
    elif "fake email" in event:
        threat = "Phishing"
    else:
        threat = "Normal Traffic"

    print("Network Event:", event)
    print("Threat Category:", threat)
    print()


