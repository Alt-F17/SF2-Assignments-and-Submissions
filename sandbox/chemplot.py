import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons

def plot_wavelength_vs_scale(wavelengths, scales, degree=2):
    """
    Plot wavelengths vs scales with a toggleable trend line.
    
    Parameters:
    - wavelengths: list of wavelength values
    - scales: list of scale values (1-14)
    - degree: degree of polynomial fit for trend line
    """
    # Create the figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Plot the data points
    ax.scatter(scales, wavelengths, color='blue', label='Data Points')
    
    # Calculate the trend line using polynomial fit
    coeffs = np.polyfit(scales, wavelengths, degree)
    poly_func = np.poly1d(coeffs)
    
    # Generate x values for the trend line
    x_trend = np.linspace(min(scales), max(scales), 100)
    y_trend = poly_func(x_trend)
    
    # Plot the trend line (initially visible)
    trend_line, = ax.plot(x_trend, y_trend, 'r-', label=f'Trend (Degree {degree})')
    
    # Set up the checkbutton for toggling
    ax_check = plt.axes([0.02, 0.9, 0.15, 0.1])
    check_button = CheckButtons(ax_check, ['Show Trend Line'], [True])
    
    # Define the toggle function
    def toggle_trend_line(label):
        trend_line.set_visible(not trend_line.get_visible())
        fig.canvas.draw_idle()
    
    # Connect the toggle function to the checkbutton
    check_button.on_clicked(toggle_trend_line)
    
    # Add labels and title
    ax.set_xlabel('Scale Value')
    ax.set_ylabel('Wavelength')
    ax.set_title('Wavelength vs Scale with Toggleable Trend Line')
    ax.legend()
    ax.grid(True)
    
    plt.tight_layout()
    plt.show()

def main():
    # Sample data (can be replaced with user input)
    wavelengths = [706.5, 667.8, 587.6, 504.6, 501.6, 492.2, 471.3, 447.1, 438.8, 421.1, 402.6, 396.4]
    scales = list(range(1, 15))  # 1 through 14
    
    # Option to input data
    use_sample = input("Use sample data? (y/n): ").lower() == 'y'
    
    if not use_sample:
        print("Enter wavelength values (comma-separated):")
        wavelengths_input = input()
        wavelengths = [float(w.strip()) for w in wavelengths_input.split(',')]
        
        print("Enter scale values (comma-separated, must be between 1-14):")
        scales_input = input()
        scales = [float(s.strip()) for s in scales_input.split(',')]
        
        # Validate scales are between 1-14
        if any(s < 1 or s > 14 for s in scales):
            print("Error: Scale values must be between 1 and 14.")
            return
        
        # Check if both lists have the same length
        if len(wavelengths) != len(scales):
            print("Error: The number of wavelengths and scales must be the same.")
            return
    
    # Get polynomial degree for trend line
    try:
        degree = int(input("Enter polynomial degree for trend line (default: 2): ") or 2)
    except ValueError:
        degree = 2
    
    # Plot the data
    plot_wavelength_vs_scale(wavelengths, scales, degree)

if __name__ == "__main__":
    main()