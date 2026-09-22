import os, subprocess, time, psutil

TARGET = "suspicious_payload.exe"
LOG_FILE = "sandbox_report.txt"
DURATION = 5

def run_sandbox():
    print(f"[*] Initializing sandbox for {TARGET}...")
    if not os.path.exists(TARGET):
        with open(TARGET, "w") as f: f.write("@echo off\ncalc.exe") # Create mock that spawns Calculator
        
    baseline = {p.pid for p in psutil.process_iter()}
    print(f"[*] Baseline: {len(baseline)} processes. Detonating...")
    
    proc = subprocess.Popen(TARGET, shell=True)
    start, detected = time.time(), set()
    
    while time.time() - start < DURATION:
        for p in psutil.process_iter(['name']):
            if p.pid not in baseline: detected.add(p.info['name'])
        time.sleep(0.5)
        
    proc.terminate()
    print("[*] Monitoring complete. Saving findings...")
    
    with open(LOG_FILE, "w") as r:
        r.write(f"SANDBOX REPORT FOR: {TARGET}\n" + "="*30 + "\n")
        r.write("\n".join(f" -> Spawned Process: {name}" for name in detected if name))

if __name__ == "__main__":
    run_sandbox()
