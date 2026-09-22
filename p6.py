malware_database = {
    "WannaCry": "Ransomware",
    "Zeus": "Banking Trojan",
    "ILOVEYOU": "Worm",
    "Emotet": "Trojan",
    "Stuxnet": "Worm",
    "Conficker": "Worm",
    "CryptoLocker": "Ransomware",
    "DarkComet": "Remote Access Trojan (RAT)",
    "Mirai": "Botnet Malware",
    "Pegasus": "Spyware"
}

print("========== Malware Analysis Report ==========\n")

# Sample malware collected for analysis
samples = [
    "WannaCry",
    "Zeus",
    "Mirai",
    "Pegasus",
    "UnknownSample"
]

# Analyze each malware sample
for sample in samples:
    category = malware_database.get(
        sample,
        "Unknown Malware - Requires Further Analysis"
    )
    print(f"{sample:20} --> {category}")
