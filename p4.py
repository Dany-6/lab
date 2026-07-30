# Threat Intelligence Collection using OSINT
# Kali Linux

import subprocess

print("=======================================")
print(" OSINT Threat Intelligence Collection")
print("=======================================\n")

domain = input("Enter Target Domain: ")

print("\n========== WHOIS Information ==========\n")

try:
    subprocess.run(["whois", domain])
except:
    print("WHOIS command not found.")

print("\n========== DNS Information ==========\n")

try:
    subprocess.run(["dig", domain])
except:
    print("DIG command not found.")

print("\nThreat Intelligence Collection Completed.")


