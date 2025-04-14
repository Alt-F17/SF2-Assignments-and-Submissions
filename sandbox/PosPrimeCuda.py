import numpy as np
import os
import time
# Set PTX version constraint before importing CUDA
os.environ["NUMBA_CUDA_MAX_PTX_VERSION"] = "8.4"  # For CUDA 8.4
from numba import cuda
# If cupy is not installed, run: pip install cupy-cuda11x (replace with your CUDA version)
try:
    import cupy as cp
except ImportError:
    raise ImportError("Please install cupy. Run: pip install cupy-cuda11x (replace with your CUDA version)")
import math

# File path for results
try:
    # For script execution
    result_file = os.path.join(os.path.dirname(__file__), 'position_primes_result.txt')
except NameError:
    # For interactive environments like Jupyter
    result_file = os.path.join(os.getcwd(), 'position_primes_result.txt')

# Initialize variables from previous run or start new
if os.path.exists(result_file):
    with open(result_file, 'r') as f:
        lines = f.readlines()
    
    if len(lines) > 1:
        last_line = lines[-1].strip()
        position = int(last_line.split("Prime No ")[1].split(":")[0])
        last_prime = int(last_line.split(": ")[1])
        count = len(lines) - 1 
        num = last_prime + 1 
        print(f"Resuming from result file: {count} position primes found, last prime at position {position}, checking from number {num}")
    else:
        count = 0
        position = 0
        num = 2
else:
    count = 0
    position = 0
    num = 2
    with open(result_file, 'w') as f:
        f.write(f"Position primes:\n")

# CUDA kernel for sieve of Eratosthenes
@cuda.jit
def sieve_kernel(sieve, limit):
    # Get the thread ID within the grid
    idx = cuda.grid(1)
    stride = cuda.gridsize(1)
    
    # Start at 2 (first prime)
    for i in range(2 + idx, int(math.sqrt(limit)) + 1, stride):
        if sieve[i]:
            # Mark all multiples of i as non-prime
            for j in range(i*i, limit, i):
                sieve[j] = False

# CUDA kernel to check if position is in prime
@cuda.jit
def check_position_prime_kernel(primes, positions, results):
    idx = cuda.grid(1)
    if idx < len(primes):
        prime = primes[idx]
        position = positions[idx]
        
        # Convert to strings and check
        prime_str = str(prime)
        pos_str = str(position)
        
        results[idx] = pos_str in prime_str

def find_primes_in_range_cuda(start, end, block_size=512):
    """Find all primes in given range using CUDA-accelerated sieve"""
    if start < 2:
        start = 2
    
    # Create boolean array, initially all True (all are potential primes)
    sieve_size = end
    sieve = cp.ones(sieve_size, dtype=cp.bool_)
    sieve[0] = False
    sieve[1] = False
    
    # Configure the grid and launch the kernel
    threads_per_block = block_size
    blocks_per_grid = (sieve_size + threads_per_block - 1) // threads_per_block
    sieve_kernel[blocks_per_grid, threads_per_block](sieve, sieve_size)
    
    # Get the prime numbers in our range
    all_primes = cp.arange(start, end)[sieve[start:end]]
    return cp.asnumpy(all_primes)

def check_position_primes_cuda(primes, start_position, block_size=512):
    """Check which primes are position primes using CUDA"""
    if len(primes) == 0:
        return []
    
    # Create array of positions
    positions = np.arange(start_position, start_position + len(primes), dtype=np.int64)
    results = np.zeros(len(primes), dtype=np.bool_)
    
    # Move data to device
    d_primes = cuda.to_device(primes)
    d_positions = cuda.to_device(positions)
    d_results = cuda.to_device(results)
    
    # Configure grid
    threads_per_block = block_size
    blocks_per_grid = (len(primes) + threads_per_block - 1) // threads_per_block
    
    # Launch kernel
    check_position_prime_kernel[blocks_per_grid, threads_per_block](d_primes, d_positions, d_results)
    
    # Get results
    d_results.copy_to_host(results)
    
    # Return matching position primes
    return [(positions[i], primes[i]) for i in range(len(primes)) if results[i]]

def main():
    global num, position, count
    
    # Set GPU parameters for maximum performance
    os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
    os.environ["CUDA_VISIBLE_DEVICES"] = "0"  # Use first GPU
    # Get device info
    device = cp.cuda.Device(0)
    properties = cp.cuda.runtime.getDeviceProperties(0)
    print(f"Using GPU: {properties['name'].decode()}")
    total_memory = device.mem_info[1]
    print(f"Total GPU memory: {total_memory/1024**3:.2f} GB")
    
    # Use larger chunks for GPU efficiency
    chunk_size = 10000000  # 10 million numbers per batch
    last_report_time = time.time()
    batch_times = []
    
    try:
        while True:
            batch_start = time.time()
            
            # Find all primes in the current chunk using CUDA sieve
            print(f"Finding primes between {num} and {num + chunk_size}...")
            primes = find_primes_in_range_cuda(num, num + chunk_size)
            print(f"Found {len(primes)} primes")
            
            # Current primes start at position+1
            current_pos = position + 1
            
            # Check if any are position primes
            new_position_primes = check_position_primes_cuda(primes, current_pos)
            
            # Update position counter and next start number
            position = current_pos + len(primes) - 1
            num = num + chunk_size
            
            # Save results
            if new_position_primes:
                with open(result_file, 'a') as f:
                    for pos, prime in new_position_primes:
                        f.write(f"Prime No {pos}: {prime}\n")
                        print(f"Prime No {pos}: {prime}")
                count += len(new_position_primes)
            
            # Calculate performance metrics
            batch_end = time.time()
            batch_time = batch_end - batch_start
            batch_times.append(batch_time)
            if len(batch_times) > 5:
                batch_times.pop(0)
            avg_batch_time = sum(batch_times) / len(batch_times)
            
            # Show progress report
            current_time = time.time()
            if current_time - last_report_time > 2:
                primes_per_second = len(primes) / batch_time
                print(f"Checked up to: {num}, Found: {count} position primes, Last Prime Position: {position}")
                print(f"Performance: {primes_per_second:.0f} primes/second, Avg batch time: {avg_batch_time:.2f}s")
                last_report_time = current_time
                
                # Force CUDA sync to clear memory
                cp.cuda.Stream.null.synchronize()
    
    except KeyboardInterrupt:
        print(f"\nStopped! Found {count} position primes so far. Results saved to {result_file}")
        print(f"Will resume from number {num} when restarted.")
    except Exception as e:
        print(f"Error: {e}")
        print(f"Will resume from number {num} when restarted.")

if __name__ == "__main__":
    main()