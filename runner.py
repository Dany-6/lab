import subprocess

scripts = [
    "p1.py", "p2.py", "p3.py", "p4.py", "p5.py",
    "p6.py", "p7.py", "p8.py", "p9.py", "p10.py",
]

error_summary = {}
timeout_seconds = 15  # Adjust this if your scripts need more time

for script in scripts:
    try:
        result = subprocess.run(
            ["python", script],
            capture_output=True,
            text=True,
            timeout=timeout_seconds
        )
        
        print(f"=== Output for {script} ===")
        print(result.stdout)
        
        if result.stderr or result.returncode != 0:
            error_summary[script] = result.stderr

    except subprocess.TimeoutExpired:
        print(f"=== Output for {script} ===")
        print(f"[!] Terminated: Script exceeded the {timeout_seconds}-second time limit.\n")
        error_summary[script] = f"TimeoutError: Script ran longer than {timeout_seconds} seconds and was killed."

if error_summary:
    print("\n" + "="*40)
    print("           ERROR SUMMARY")
    print("="*40)
    for failed_script, error_msg in error_summary.items():
        print(f"\n--- Errors encountered in {failed_script} ---")
        print(error_msg.strip())
else:
    print("\nAll scripts completed without any errors.")
