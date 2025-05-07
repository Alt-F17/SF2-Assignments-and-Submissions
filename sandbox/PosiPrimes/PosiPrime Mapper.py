import numpy as np
import re

import matplotlib.pyplot as plt

# Read the data from the file
try:
    with open(r"C:\Users\felix\OneDrive - Dawson College\Class Files\SF2 - Coding\SF2-Assignments-and-Submissions\sandbox\position_primes_result.txt", 'r') as f:
        content = f.read()

    # Extract position and prime pairs using regex
    pattern = r"Prime No (\d+): (\d+)"
    matches = re.findall(pattern, content)

    # Convert the extracted data to lists of integers
    positions = [int(pos) for pos, prime in matches]
    primes = [int(prime) for pos, prime in matches]

    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.scatter(positions, primes, color='blue', alpha=0.6, label='Prime Numbers')

    # Fit a degree 8 polynomial
    coefficients = np.polyfit(positions, primes, 8)
    polynomial = np.poly1d(coefficients)

    # Generate x values for the trend line
    x_range = np.linspace(min(positions), max(positions), 1000)
    y_values = polynomial(x_range)

    # Plot the trend line
    plt.plot(x_range, y_values, color='red', linewidth=2, label='Degree 8 Trend Line')

    # Add labels and title
    plt.xlabel('Position')
    plt.ylabel('Prime Value')
    plt.title('Prime Numbers vs. Position with Degree 8 Trend Line')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Format tick labels for readability
    plt.ticklabel_format(style='plain', useOffset=False)
    
    # Show the plot
    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print("Error: The file 'position_primes.txt' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")