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
except Exception as e:
    print(f"WHOIS command failed or not found: {e}")

print("\n========== DNS Information ==========\n")
try:
    subprocess.run(["dig", domain])
except Exception as e:
    print(f"DIG command failed or not found: {e}")

print("\nThreat Intelligence Collection Completed.")
