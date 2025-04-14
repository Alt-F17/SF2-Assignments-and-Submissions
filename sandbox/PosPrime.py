import sympy
import os
import multiprocessing as mp
import time

result_file = os.path.join(os.path.dirname(__file__), 'position_primes_result.txt')

with open(result_file, 'r') as f:
    lines = f.readlines()

last_line = lines[-1].strip()
position = int(last_line.split("Prime No ")[1].split(":")[0])
last_prime = int(last_line.split(": ")[1])
count = len(lines) - 1 
num = last_prime + 1 
print(f"Resuming from result file: {count} position primes found, last prime at position {position}, checking from number {num}")

def find_primes_in_range(start, end):
    """Find all primes in the given range"""
    return [n for n in range(start, end) if sympy.isprime(n)]

def check_range(start, end, start_position):
    """Check a range of numbers for position primes"""
    primes_in_range = find_primes_in_range(start, end)
    results = []
    
    for i, prime in enumerate(primes_in_range):
        current_position = start_position + i + 1
        if str(current_position) in str(prime):
            results.append((current_position, prime))
    
    return results, len(primes_in_range)

def main():
    global num, position, count

    num_processes = mp.cpu_count()
    print(f"Using {num_processes} CPU cores for parallel processing")
    
    chunk_size = 100000
    results_buffer = []
    last_report_time = time.time()
    
    try:
        while True:
            chunks = []
            current_start = num
            
            for _ in range(num_processes):
                chunks.append((current_start, current_start + chunk_size))
                current_start += chunk_size
            
            all_primes = []
            with mp.Pool(processes=num_processes) as pool:
                for chunk_start, chunk_end in chunks:
                    primes = find_primes_in_range(chunk_start, chunk_end)
                    all_primes.extend(primes)
            
            all_primes.sort()
            
            new_position_primes = []
            current_pos = position
            
            for prime in all_primes:
                current_pos += 1
                if str(current_pos) in str(prime):
                    new_position_primes.append((current_pos, prime))

            position = current_pos
            num = chunks[-1][1]
            
            if new_position_primes:
                with open(result_file, 'a') as f:
                    for pos, prime in new_position_primes:
                        f.write(f"Prime No {pos}: {prime}\n")
                        print(f"Prime No {pos}: {prime}")
                
                count += len(new_position_primes)
            
            current_time = time.time()
            if current_time - last_report_time > 2:
                print(f"Checked up to: {num}, Found: {count}, Last Prime Position: {position}")
                last_report_time = current_time
    
    except KeyboardInterrupt:
        print(f"\nStopped! Found {count} position primes so far. Results saved to {result_file}")
        print(f"Will resume from number {num} when restarted.")

if __name__ == "__main__":
    main()
