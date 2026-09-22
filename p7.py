import os, hashlib, re

TARGET = "suspicious_sample.bin"
LOG_FILE = "static_analysis_report.txt"

# 1. Create a mock file if it does not exist
if not os.path.exists(TARGET):
    with open(TARGET, "w") as f:
        f.write("MZ Header\nIP: 192.168.1.105\nURL: malicious-cnc.com\nAPI: VirtualAlloc")

# 2. Read the file bytes and check size
with open(TARGET, "rb") as f:
    data = f.read()

# 3. Calculate MD5 and SHA-256 hashes
md5_h = hashlib.md5(data).hexdigest()
sha_h = hashlib.sha256(data).hexdigest()

# 4. Extract readable text strings (4 or more printable characters)
strings = [s.decode() for s in re.findall(b"[ -~]{4,}", data)]

# 5. Save everything to the report file
print(f"[*] Analyzing {TARGET}... Saving report to {LOG_FILE}")
with open(LOG_FILE, "w") as r:
    r.write(f"File Size: {len(data)} bytes\nMD5: {md5_h}\nSHA256: {sha_h}\n\n[Strings Found]\n")
    r.write("\n".join(f" -> {s}" for s in strings))
