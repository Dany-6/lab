import hashlib
import os

s
KNOWN_MALWARE_HASHES = {
    "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f": "EICAR Anti-Virus Test File",
    "24d004a104d4d54034dbcffc2a4b19a11f39008a575aa614ea04703480b1022c": "WannaCry Ransomware"
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
        

    file_hash = calculate_hash(filename)

    print("\nFile:", filename)
    print("SHA-256 Hash:", file_hash)

    # Threat intelligence check
    if file_hash in KNOWN_MALWARE_HASHES:
        print("Result: MALWARE DETECTED")
        print(f"Threat Intelligence: Known malicious file ({KNOWN_MALWARE_HASHES[file_hash]})")
        return
        
  
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


filename = input("Enter the file name: ")
detect_malware(filename)
