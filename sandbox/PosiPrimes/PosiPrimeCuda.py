import numpy as np
from numba import cuda, njit, int64
import math
import time
import os
import re

# File path for storing position primes
FILE_PATH = r"c:\Users\felix\OneDrive - Dawson College\Class Files\SF2 - Coding\SF2-Assignments-and-Submissions\sandbox\PosiPrimes\position_primes_result.txt"

# Global variables for last known position prime
last_posiprime = 0
last_position = 0

def read_last_posiprime():
    """Read the last position prime from the file"""
    global last_posiprime, last_position
    
    # Default values
    last_posiprime = 17
    last_position = 7
    
    try:
        with open(FILE_PATH, 'r') as file:
            content = file.read()
            # Find the last entry using regex
            matches = re.findall(r'Prime No (\d+): (\d+)', content)
            if matches:
                last_match = matches[-1]
                last_position = int(last_match[0])
                last_posiprime = int(last_match[1])
                print(f"Loaded last position prime: Prime No {last_position}: {last_posiprime}")
    except Exception as e:
        print(f"Error reading file: {e}")
        print(f"Starting with default values: Prime No {last_position}: {last_posiprime}")

def append_posiprime_to_file(position, prime):
    """Append a new position prime to the file"""
    try:
        with open(FILE_PATH, 'a') as file:
            file.write(f"Prime No {position}: {prime}\n")
    except Exception as e:
        print(f"Error writing to file: {e}")

@cuda.jit(device=True)
def is_prime_device(n):
    """Device function to check primality using trial division"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    limit = int(math.sqrt(n)) + 1
    for i in range(5, limit, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    
    return True

@cuda.jit
def find_primes_kernel(start, num_to_check, step, results):
    """Kernel to find primes in a range"""
    idx = cuda.grid(1)
    stride = cuda.gridsize(1)
    
    for i in range(idx, num_to_check, stride):
        n = start + i * step
        results[i] = is_prime_device(n)

def find_next_posiprime():
    global last_posiprime, last_position
    
    # Start from the last posiprime (odd numbers only)
    current_num = last_posiprime + 2
    current_position = last_position
    
    # CUDA configuration optimized for RTX 3070 laptop
    block_size = 256
    grid_size = 1024
    
    # Process numbers in batches
    batch_size = 10000000
    
    print(f"Starting search from {current_num}...")
    
    while True:
        # Generate batch of candidates (odd numbers only)
        candidates = np.arange(current_num, current_num + batch_size * 2, 2, dtype=np.int64)
        d_results = cuda.device_array(len(candidates), dtype=np.bool_)
        
        # Launch kernel to find primes in batch
        find_primes_kernel[grid_size, block_size](current_num, len(candidates), 2, d_results)
        
        # Get results back to host
        results = d_results.copy_to_host()
        
        # Process results
        primes_found = 0
        for i, is_prime in enumerate(results):
            if is_prime:
                primes_found += 1
                current_position += 1
                prime = candidates[i]
                
                # Check if this is a position prime
                if str(current_position) in str(prime):
                    print(f"Found position prime: Prime No {current_position}: {prime}")
                    last_posiprime = prime
                    last_position = current_position
                    return prime, current_position
        
        # Move to next batch
        current_num += batch_size * 2
        print(f"Checked up to {current_num-2}, found {primes_found} primes in this batch")
        print(f"Current position: {current_position}")

if __name__ == "__main__":
    start_time = time.time()
    
    # Read the last position prime from file
    read_last_posiprime()
    
    cuda.select_device(0)  # Select the fastest GPU
    
    # Warm up CUDA
    dummy = cuda.device_array(1)
    
    try:
        while True:
            # Find the next position prime
            next_prime, position = find_next_posiprime()
            
            # Append to file
            append_posiprime_to_file(position, next_prime)
            
            elapsed = time.time() - start_time
            print(f"\nResult: Position prime found and saved to file")
            print(f"Prime No {position}: {next_prime}")
            print(f"Running time: {elapsed:.2f} seconds")
            #alert the user through a popup message
            os.system(f"powershell -Command \"& {{Add-Type -AssemblyName PresentationFramework; [System.Windows.MessageBox]::Show('Position prime found: Prime No {position}: {next_prime}', 'Position Prime Found')}}")
            
    except KeyboardInterrupt:
        print("\nSearch stopped by user")
        elapsed = time.time() - start_time
        print(f"Total runtime: {elapsed:.2f} seconds")
        print(f"Last position prime found: Prime No {last_position}: {last_posiprime}")

# Verify the results here: https://t5k.org/nthprime/