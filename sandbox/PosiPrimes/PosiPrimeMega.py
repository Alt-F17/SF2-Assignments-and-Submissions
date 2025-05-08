import numpy as np
import cupy as cp
from numba import cuda, njit, prange, int64
import math
import time
import os
import re
import concurrent.futures
import sympy
from pathlib import Path
import multiprocessing

FILE_PATH = r"c:\Users\felix\OneDrive - Dawson College\Class Files\SF2 - Coding\SF2-Assignments-and-Submissions\sandbox\PosiPrimes\position_primes_result.txt"
CHECKPOINT_PATH = r"c:\Users\felix\OneDrive - Dawson College\Class Files\SF2 - Coding\SF2-Assignments-and-Submissions\sandbox\PosiPrimes\checkpoint.npz"

LAST_POSITION = 96664044 # CHANGE THIS TO THE LAST POSITION FOUND
LAST_POSIPRIME = 1966640443 # CHANGE THIS TO THE LAST POSITION PRIME FOUND

CPU_CORES = max(1, multiprocessing.cpu_count() - 1)  # Leave one core free for system cuz I wanna play minecraft
GPU_MEM_LIMIT = 0.95  # Use 95% of available GPU memory
BATCH_SIZE_MAX = 100000000  # Maximum batch size, could make this bigger but it will slow down the system like hell
REPORT_INTERVAL = 100  # Report progress every 10 seconds

@njit(cache=True)
def is_position_prime(prime, position):
    return sympy.isprime(position)

@njit(cache=True, parallel=True)
def cpu_find_position_prime(start, step, candidates, positions, num_to_check):
    for i in prange(num_to_check):
        n = start + i * step
        if sympy.isprime(n):
            pos = positions[i]
            if is_position_prime(n, pos):
                return n, pos
    return -1, -1

@cuda.jit(device=True)
def is_prime_device(n):
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

@cuda.jit(device=True)
def is_position_prime_device(prime, position):
    return is_prime_device(position)

@cuda.jit
def find_position_primes_kernel(start, start_pos, step, results, positions):
    """GPU kernel to find both primes and check position in one pass"""
    idx = cuda.grid(1)
    stride = cuda.gridsize(1)
    
    for i in range(idx, results.size, stride):
        n = start + i * step
        pos = start_pos + i
        
        if is_prime_device(n):
            positions[i] = pos
            if is_position_prime_device(n, pos):
                results[i] = n
            else:
                results[i] = 0
        else:
            results[i] = 0 
            positions[i] = 0

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

def estimate_max_batch_size():
    """Estimate the maximum batch size based on available GPU memory"""
    try:
        free_mem, total_mem = cuda.current_context().get_memory_info()
        usable_mem = int(free_mem * GPU_MEM_LIMIT)
        bytes_per_candidate = 8 + 8
        max_batch = min(usable_mem // bytes_per_candidate, BATCH_SIZE_MAX)
        return max_batch
    except:
        return BATCH_SIZE_MAX // 2

def find_next_posiprime():
    current_num, current_position = load_checkpoint()
    
    if current_num % 2 == 0:
        current_num += 1
    
    block_size = 256 # Optimal for RTX 3070
    grid_size = 1024 # Optimal for RTX 3070
    
    batch_size = estimate_max_batch_size()
    print(f"Using batch size: {batch_size}")
    
    start_time = time.time()
    last_report_time = start_time
    primes_checked = 0
    
    cpu_pool = concurrent.futures.ThreadPoolExecutor(max_workers=CPU_CORES)
    
    print(f"Starting search from number {current_num}, position {current_position}")
    print(f"Using {CPU_CORES} CPU cores and GPU acceleration")
    
    try:
        while True:
            start_num = current_num
            start_pos = current_position + 1
            d_results = cuda.device_array(batch_size, dtype=np.int64)
            d_positions = cuda.device_array(batch_size, dtype=np.int64)
            find_position_primes_kernel[grid_size, block_size](
                start_num, start_pos, 2, d_results, d_positions
            )
            
            results = d_results.copy_to_host()
            positions = d_positions.copy_to_host()
            
            for i in range(batch_size):
                if results[i] > 0:  # Found a posiprime
                    prime = results[i]
                    position = positions[i]
                    print(f"\nFound position prime: Prime No {position}: {prime}")
                    append_posiprime_to_file(position, prime)
                    return prime, position
            
            primes_found = np.count_nonzero(positions)
            current_position += primes_found
            primes_checked += batch_size
            current_num += batch_size * 2
            
            now = time.time()
            if now - last_report_time > REPORT_INTERVAL:
                elapsed = now - start_time
                rate = primes_checked / elapsed
                print(f"Checked up to {current_num-2}, found {primes_found} primes in last batch")
                print(f"Current position: {current_position}, Processing speed: {rate:.2f} numbers/sec")
                last_report_time = now
                save_checkpoint(current_num, current_position)
    
    except KeyboardInterrupt:
        print("\nSearch stopped by user")
        save_checkpoint(current_num, current_position)
        return None, None

if __name__ == "__main__":
    try:
        import cupy
    except ImportError:
        print("Installing required packages...")
        import subprocess
        subprocess.call(["pip", "install", "cupy-cuda11x", "sympy", "numba"])
    
    overall_start_time = time.time()

    cuda.select_device(0)
    
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
    finally:
        cuda.close()

# Verify the results at https://t5k.org/nthprime/index.php#nth