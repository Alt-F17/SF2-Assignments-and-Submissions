import numpy as np
import math
import time
import os
import re
import concurrent.futures
import sympy
from pathlib import Path
import multiprocessing

# Use platform-independent paths
FILE_PATH = Path("position_primes_result.txt")
CHECKPOINT_PATH = Path("checkpoint.npz")

LAST_POSITION = 96664044  # CHANGE THIS TO THE LAST POSITION FOUND
LAST_POSIPRIME = 1966640443  # CHANGE THIS TO THE LAST POSITION PRIME FOUND

CPU_CORES = max(1, multiprocessing.cpu_count() - 1)  # Leave one core free for system
BATCH_SIZE = 1000000  # Batch size for processing
REPORT_INTERVAL = 10  # Report progress every 10 seconds

def is_position_prime(prime, position):
    """Check if position is contained in prime number"""
    return str(position) in str(prime)

def is_prime(n):
    """Fast prime check for larger numbers"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    return True

def process_batch(start_num, start_pos, batch_size, step=2):
    """Process a batch of numbers to find position primes"""
    results = []
    
    for i in range(batch_size):
        n = start_num + i * step
        if is_prime(n):
            pos = start_pos + len(results)
            if is_position_prime(n, pos):
                return n, pos, i+1
            results.append(n)
    
    return None, None, len(results)

def save_checkpoint(current_num, current_position):
    """Save checkpoint to resume from later"""
    np.savez(CHECKPOINT_PATH, 
             current_num=current_num,
             current_position=current_position)
    print(f"Checkpoint saved: number={current_num}, position={current_position}")

def load_checkpoint():
    """Load checkpoint if available"""
    if os.path.exists(CHECKPOINT_PATH):
        data = np.load(CHECKPOINT_PATH)
        return int(data['current_num']), int(data['current_position'])
    else:
        return LAST_POSIPRIME + 2, LAST_POSITION

def append_posiprime_to_file(position, prime):
    """Append a new position prime to the file"""
    try:
        with open(FILE_PATH, 'a') as file:
            file.write(f"Prime No {position}: {prime}\n")
    except Exception as e:
        print(f"Error writing to file: {e}")

def find_next_posiprime():
    current_num, current_position = load_checkpoint()
    
    if current_num % 2 == 0:
        current_num += 1
    
    start_time = time.time()
    last_report_time = start_time
    numbers_checked = 0
    
    print(f"Starting search from number {current_num}, position {current_position}")
    print(f"Using {CPU_CORES} CPU cores")
    
    with concurrent.futures.ProcessPoolExecutor(max_workers=CPU_CORES) as executor:
        try:
            while True:
                batch_futures = []
                
                # Submit multiple batches to the process pool
                for i in range(CPU_CORES):
                    start_batch = current_num + i * BATCH_SIZE * 2
                    batch_futures.append(executor.submit(
                        process_batch, start_batch, current_position, BATCH_SIZE
                    ))
                
                # Process results as they complete
                for future in concurrent.futures.as_completed(batch_futures):
                    prime, position, primes_found = future.result()
                    numbers_checked += BATCH_SIZE * 2
                    
                    if prime is not None:  # Found a posiprime
                        print(f"\nFound position prime: Prime No {position}: {prime}")
                        append_posiprime_to_file(position, prime)
                        return prime, position
                    
                    current_position += primes_found
                
                current_num += CPU_CORES * BATCH_SIZE * 2
                
                now = time.time()
                if now - last_report_time > REPORT_INTERVAL:
                    elapsed = now - start_time
                    rate = numbers_checked / elapsed
                    print(f"Checked up to {current_num-2}, position: {current_position}")
                    print(f"Processing speed: {rate:.2f} numbers/sec")
                    last_report_time = now
                    save_checkpoint(current_num, current_position)
        
        except KeyboardInterrupt:
            print("\nSearch stopped by user")
            save_checkpoint(current_num, current_position)
            return None, None

if __name__ == "__main__":
    try:
        import sympy
    except ImportError:
        print("Installing required packages...")
        import subprocess
        subprocess.call(["pip", "install", "sympy", "numpy"])
    
    overall_start_time = time.time()
    
    try:
        prime, position = find_next_posiprime()
        
        if prime is not None:
            elapsed = time.time() - overall_start_time
            print(f"\nSuccess! Position prime found and saved to file")
            print(f"Prime No {position}: {prime}")
            print(f"Total running time: {elapsed:.2f} seconds")
    
    except Exception as e:
        print(f"\nError occurred: {e}")
        raise

# Verify the results at https://t5k.org/nthprime/index.php#nth