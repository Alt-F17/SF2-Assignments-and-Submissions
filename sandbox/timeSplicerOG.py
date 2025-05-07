import time
import datetime
import sys
import threading

today = datetime.datetime.now()
end_time = datetime.datetime(today.year, today.month, today.day, 11, 30, 0)

start_time = datetime.datetime.now()
total_duration = (end_time - start_time).total_seconds()

total_tasks = 1
completed_tasks = 0

def get_user_input(completed_tasks):
    """Function to handle user input in a separate thread"""
    global total_tasks, end_time
    while True:
        try:
            user_input = input()
            if user_input.split()[0] == "-total":
                total_tasks = int(user_input.split()[1])
                print(f"Total tasks set to {total_tasks}")
            if user_input.split()[0] == "-end":
                end_time = datetime.datetime(today.year, today.month, today.day, int(user_input.split()[1]), int(user_input.split()[2]), 0)
                print(f"End time set to {end_time}")
            if user_input.strip():
                new_value = int(user_input)
                if 0 <= new_value <= total_tasks:
                    return new_value
        except ValueError:
            pass
        except Exception as e:
            pass
        except EOFError:
            return completed_tasks
def input_thread():
    global completed_tasks
    while True:
        try:
            new_value = get_user_input(completed_tasks)
            completed_tasks = new_value
        except:
            break

input_thread = threading.Thread(target=input_thread)
input_thread.daemon = True
input_thread.start()

try:
    while datetime.datetime.now() < end_time:
        now = datetime.datetime.now()
        remaining_seconds = (end_time - now).total_seconds()
        
        if remaining_seconds <= 0:
            break
        
        elapsed_seconds = (now - start_time).total_seconds()
        progress = elapsed_seconds / total_duration
        
        remaining_tasks = total_tasks - completed_tasks
        time_per_task = remaining_seconds / remaining_tasks if remaining_tasks > 0 else 0
        
        sys.stdout.write("\033[H\033[J") 
        
        hours, remainder = divmod(remaining_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        time_str = f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"
        
        print(f"Time remaining: {time_str}")
        
        filled_length = int(progress * 50)
        bar = '█' * filled_length + '-' * (50 - filled_length)
        print(f"[{bar}] {progress * 100:.2f}%")
        
        print(f"Tasks completed: {completed_tasks}/{total_tasks} ({completed_tasks / total_tasks * 100:.2f}%)")
        
        minutes_per_task, seconds_per_task = divmod(time_per_task, 60)
        print(f"Time per remaining task: {int(minutes_per_task):02d}:{int(seconds_per_task):02d}")
        print("")
        print("Enter number of completed tasks: ", end="", flush=True)
        
        time.sleep(1)
        
    sys.stdout.write("\033[H\033[J")
    print("Time's up! All tasks should be completed.")
    
except KeyboardInterrupt:
    print("\nTimer stopped.")