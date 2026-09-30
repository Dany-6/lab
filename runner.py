import subprocess
import re
import sys

def parse_selection(user_input):
    """Parses user input like 'p1 and 3', '1-5', or 'all' into a list of script names."""
    user_input = user_input.strip().lower()
    
    # 1. Handle "all" or specific ranges
    if user_input in ["all", "1 to 10", "p1 to p10", "p1 to 10", "1-10", "p1-p10"]:
        return [f"p{i}.py" for i in range(1, 11)]
    
    # 2. Handle hyphenated ranges like "2-5"
    range_match = re.match(r'^p?(\d+)\s*(?:-|to)\s*p?(\d+)$', user_input)
    if range_match:
        start, end = int(range_match.group(1)), int(range_match.group(2))
        step = 1 if start <= end else -1
        return [f"p{i}.py" for i in range(start, end + step, step)]
    
    # 3. Extract any specific numbers mentioned in the text
    numbers = re.findall(r'\b\d+\b', user_input)
    if numbers:
        return [f"p{num}.py" for num in numbers]
    
    return []

# --- Main Runner Logic ---
print("===========================================")
print("          PYTHON SCRIPT RUNNER             ")
print("===========================================")
print("Which programs would you like to run?")
print("Options:")
print("  - Type 'all' to run everything (p1 through p10)")
print("  - Type a range like '1-5'")
print("  - Type any combination like 'p2 and p8', '1, 4, 7', or 'run 3 and 10'")
print("===========================================")
user_choice = input("\nEnter your choice: ")

scripts_to_run = parse_selection(user_choice)

if not scripts_to_run:
    print("No valid scripts selected. Exiting.")
    sys.exit()

print(f"\nRunning the following scripts: {', '.join(scripts_to_run)}\n")

error_summary = {}
timeout_seconds = 15

for script in scripts_to_run:
    try:
        # Check which script is running and provide the correct automated input
        if script == "p10.py":
            script_input = "document1.txt\n"
        elif script == "p4.py":
            script_input = "google.com\n"
        else:
            script_input = None

        result = subprocess.run(
            ["python", script],
            capture_output=True,
            text=True,
            input=script_input,  # Passes the specific string based on the if-statement above
            timeout=timeout_seconds
        )
        
        print(f"=== Output for {script} ===")
        print(result.stdout)
        
        if result.stderr or result.returncode != 0:
            error_summary[script] = result.stderr

    except subprocess.TimeoutExpired:
        print(f"=== Output for {script} ===")
        print(f"[!] Terminated: Script exceeded the {timeout_seconds}-second time limit.\n")
        error_summary[script] = f"TimeoutError: Script ran longer than {timeout_seconds} seconds."

# --- Print Summary ---
if error_summary:
    print("\n" + "="*40)
    print("           ERROR SUMMARY")
    print("="*40)
    for failed_script, error_msg in error_summary.items():
        print(f"\n--- Errors encountered in {failed_script} ---")
        if error_msg:
            print(error_msg.strip())
else:
    print("\nAll selected scripts completed without any errors.")
