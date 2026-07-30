# Cyber Kill Chain Model for Threat Investigation

# Dictionary containing attack events and Kill Chain stages
kill_chain = {
    "Email Phishing": "Weaponization / Delivery",
    "Malicious Attachment": "Delivery",
    "Malicious Link": "Delivery",
    "Exploit Executed": "Exploitation",
    "Malware Installed": "Installation",
    "Persistence Established": "Installation",
    "Command and Control Traffic": "Command and Control (C2)",
    "Data Exfiltration": "Actions on Objectives",
    "Privilege Escalation": "Installation",
    "Network Scanning": "Reconnaissance",
    "Information Gathering": "Reconnaissance",
    "Credential Theft": "Actions on Objectives"
}

print("========== Cyber Kill Chain Investigation ==========")

# Sample observed events
observed_events = [
    "Network Scanning",
    "Email Phishing",
    "Exploit Executed",
    "Malware Installed",
    "Command and Control Traffic",
    "Data Exfiltration"
]

print("\nObserved Threat Events:\n")

for event in observed_events:
    stage = kill_chain.get(event, "Unknown Stage - Requires Investigation")
    print(f"{event:30} --> {stage}")
