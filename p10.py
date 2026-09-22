import hashlib
import os

# Small threat intelligence database
# These are example hashes for demonstration.
KNOWN_MALWARE_HASHES = {
    "44d88612fea8a8f36de82e1278abb02f": "Example Malware"
}

def calculate_hash(filename):
    sha256 = hashlib.sha256()

    with open(filename, "rb") as file:
        while True:
            data = file.read(4096)

            if not data:
                break

            sha256.update(data)
    return sha256.hexdigest()
def detect_malware(filename):
    # Check whether file exists
    if not os.path.exists(filename):
        print("File not found!")
        return
    # Calculate SHA-256 hash
    file_hash = calculate_hash(filename)

    print("\nFile:", filename)
    print("SHA-256 Hash:", file_hash)

    # Threat intelligence check
    if file_hash in KNOWN_MALWARE_HASHES:
        print("Result: MALWARE DETECTED")
        print("Threat Intelligence: Known malicious file")
        return
    # Basic suspicious file check
    suspicious_extensions = [
        ".exe", ".bat", ".cmd", ".vbs", ".scr"
    ]
    extension = os.path.splitext(filename)[1].lower()
    if extension in suspicious_extensions:
        print("Result: SUSPICIOUS FILE")
        print("Reason: Executable or script file")
    else:
        print("Result: SAFE")
        print("Threat Intelligence: No known malicious hash found")

# Main program
filename = input("Enter the file name: ")
detect_malware(filename)
