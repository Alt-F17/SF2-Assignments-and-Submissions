import time
import datetime
import sys
from tqdm import tqdm
import threading
import math

# Hardcoded end time (adjust as needed)
# Set it to a specific time
# Set end time to tomorrow at 5:50 AM
today = datetime.datetime.now()
end_time = datetime.datetime(today.year, today.month, today.day, 11, 10, 0)

# Set start time to when the script starts
start_time = datetime.datetime.now()
total_duration = (end_time - start_time).total_seconds()

# Initialize variables
total_tasks = 1
completed_tasks = 0

def get_user_input(completed_tasks):
    """Function to handle user input in a separate thread"""
    while True:
        try:
            user_input = input()
            if user_input.split()[0] == "-total":
                total_tasks = int(user_input.split()[1])
                print(f"Total tasks set to {total_tasks}")
            if user_input.split()[0] == "-end":
                end_time = datetime.datetime(today.year, today.month, today.day, user_input.split()[1], user_input.split()[2], 0)
                print(f"End time set to {end_time}")
            if user_input.strip():
                new_value = int(user_input)
                if 0 <= new_value <= total_tasks:
                    return new_value
        except ValueError:
            pass
        except any as e:
            pass
        except EOFError:
            return completed_tasks

# Start a thread to handle user input
def input_thread():
    global completed_tasks
    while True:
        try:
            new_value = get_user_input(completed_tasks)
            completed_tasks = new_value
        except:
            break

# Start input thread
input_thread = threading.Thread(target=input_thread)
input_thread.daemon = True
input_thread.start()

# Main loop
try:
    while datetime.datetime.now() < end_time:
        now = datetime.datetime.now()
        remaining_seconds = (end_time - now).total_seconds()
        
        if remaining_seconds <= 0:
            break
        
        # Calculate progress percentage using the start time
        elapsed_seconds = (now - start_time).total_seconds()
        progress = elapsed_seconds / total_duration
        
        # Calculate time per remaining task
        remaining_tasks = total_tasks - completed_tasks
        time_per_task = remaining_seconds / remaining_tasks if remaining_tasks > 0 else 0
        
        # Clear terminal
        sys.stdout.write("\033[H\033[J")
        
        # Format remaining time as HH:MM:SS
        hours, remainder = divmod(remaining_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        time_str = f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"
        
        # Display timer
        print(f"Time remaining: {time_str}")
        
        # Display progress bar
        bar_length = 50
        filled_length = int(progress * bar_length)
        bar = '█' * filled_length + '-' * (bar_length - filled_length)
        print(f"[{bar}] {progress * 100:.2f}%")
        
        # Display task counter and time per task
        print(f"Tasks completed: {completed_tasks}/{total_tasks} ({completed_tasks / total_tasks * 100:.2f}%)")
        
        minutes_per_task, seconds_per_task = divmod(time_per_task, 60)
        print(f"Time per remaining task: {int(minutes_per_task):02d}:{int(seconds_per_task):02d}")
        print("")
        print("Enter number of completed tasks: ", end="", flush=True)
        
        time.sleep(1)  # Update every second
        
    # Timer has ended
    sys.stdout.write("\033[H\033[J")
    print("Time's up! All tasks should be completed.")
    
except KeyboardInterrupt:
    print("\nTimer stopped.")