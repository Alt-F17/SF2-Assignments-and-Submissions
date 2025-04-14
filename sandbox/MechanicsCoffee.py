import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import CheckButtons

def simulate_coffee_filter_drop(initial_height, mass_multiplier=1, time_values=None, t_final=2.0):
    """
    Simulate a coffee filter drop using Euler's method
    
    Args:
        initial_height (float): Initial height in meters
        mass_multiplier (int): Multiplier for the base mass (0.88g)
        time_values (list, optional): Specific time points to calculate positions for
        t_final (float): Final simulation time if time_values not provided
        
    Returns:
        tuple: (time_values, position_values)
    """
    # Constants
    g = 9.81  # m/s^2
    m = (0.88/1000) * mass_multiplier  # kg # Per coffee filter * multiplier
    c = 1.1109991310477379  # drag coefficient
    A = 141.591/10000  # m^2
    rho = 1.2  # kg/m^3
    h = 0.0001  # s - time step
    
    # Initial conditions
    t_start = 0
    v = 0  # m/s - initial velocity
    y = initial_height  # m - initial height
    
    # Use provided time values or generate time sequence
    if time_values is None:
        # Initialize lists to store values
        t_values = [t_start]
        v_values = [v]
        y_values = [y]
        
        # Euler's method with fixed time steps
        while t_values[-1] < t_final:
            v = v - h*g + h*(rho*c*A*v**2)/(2*m)
            y = y + h*v
            # Break the loop if y becomes negative
            if y < 0:
                break
            t_values.append(t_values[-1] + h)
            v_values.append(v)
            y_values.append(y)
    else:
        # Calculate y values for specified time points
        t_values = []
        y_values = []
        
        current_t = t_start
        current_v = v
        current_y = y
        
        for target_t in time_values:
            while current_t < target_t:
                current_v = current_v - h*g + h*(rho*c*A*current_v**2)/(2*m)
                current_y = current_y + h*current_v
                current_t += h
                
                # Break if hitting the ground
                if current_y < 0:
                    break
            
            t_values.append(target_t)
            y_values.append(max(0, current_y))  # Don't go below ground
    
    return t_values, y_values

def analyze_coffee_filter_data(csv_file):
    """
    Analyze coffee filter drop data from CSV and compare to theoretical model
    
    Args:
        csv_file (str): Path to the CSV file with experimental data
    """
    # Read the CSV file
    df = pd.read_csv(csv_file)
    
    # Process each run in the data
    runs = []
    max_time = 0
    
    # Find all runs in the dataframe
    for col in df.columns:
        if 'Time (s) Run' in col:
            run_num = int(col.split('#')[1])
            time_col = col
            pos_col = f'Position (m) Run #{run_num}'
            
            # Filter out NaN values
            run_data = df[[time_col, pos_col]].dropna()
            
            if not run_data.empty:
                times = run_data[time_col].values
                positions = run_data[pos_col].values
                initial_height = positions[0]
                
                # Mass multiplier depends on run number (Run #1 = 10, Run #2 = 9, etc.)
                mass_multiplier = 11 - run_num if run_num <= 10 else 1
                
                # Add to collection
                runs.append({
                    'run_num': run_num,
                    'times': times,
                    'positions': positions,
                    'initial_height': initial_height,
                    'mass_multiplier': mass_multiplier
                })
                
                # Track maximum time
                if len(times) > 0 and times[-1] > max_time:
                    max_time = times[-1]
    
    # Create figure with main plot area
    fig = plt.figure(figsize=(14, 8))
    
    # Create the main plot (using most of the figure width)
    ax = fig.add_axes([0.1, 0.1, 0.7, 0.8])
    
    # Plot lines and store them
    colors = plt.cm.tab10(np.linspace(0, 1, len(runs)))
    lines = []  # Store all line objects for toggling visibility
    check_labels = []  # Labels for checkboxes
    
    for i, run in enumerate(runs):
        run_color = colors[i]
        label = f"Run #{run['run_num']}"
        check_labels.append(label)
        
        # Get positions and times
        positions = run['positions'].copy()
        times = run['times'].copy()
        plot_initial_height = run['initial_height']
        
        # Plot experimental data
        exp_line, = ax.plot(times, positions, 'o-', alpha=0.6, 
                            label=f"{label} (Exp)", markersize=4, 
                            color=run_color)
        
        # Generate theoretical data at experimental time points
        theory_times, theory_positions = simulate_coffee_filter_drop(
            plot_initial_height, 
            mass_multiplier=run['mass_multiplier'],
            time_values=times
        )
        
        # Plot the theoretical model for this run (matches experimental color)
        theory_line, = ax.plot(theory_times, theory_positions, '--', alpha=0.3, 
                              linewidth=1.5, color=run_color,
                              label=f"{label} (Theory)")
        
        # Generate dense theoretical data for same mass/height
        dense_times = np.linspace(0, max(times) * 1.1, 200)
        dense_theory_times, dense_theory_positions = simulate_coffee_filter_drop(
            plot_initial_height,
            mass_multiplier=run['mass_multiplier'],
            time_values=dense_times
        )
        
        # Plot detailed theoretical curve 
        dense_theory_line, = ax.plot(dense_theory_times, dense_theory_positions, '-', 
                                    linewidth=1.5, color=run_color, alpha=0.5)
        
        # Store all lines for this run to toggle visibility
        lines.append([exp_line, theory_line, dense_theory_line])
    
    # Add labels and title
    ax.set_xlabel('Time (s)', fontsize=12)
    ax.set_ylabel('Position (m)', fontsize=12)
    ax.set_title('Coffee Filter Drop: Experimental vs Theoretical', fontsize=14)
    ax.grid(True, alpha=0.3)
    
    # Create checkboxes for runs (on the right side)
    runs_checkbox_ax = fig.add_axes([0.85, 0.4, 0.12, 0.5], frameon=True)
    runs_checkbox = CheckButtons(
        runs_checkbox_ax, 
        check_labels, 
        [True] * len(check_labels)
    )
    
    # Adjust appearance of checkboxes (compatible with older matplotlib)
    for label in runs_checkbox.labels:
        label.set_fontsize(10)
    
    # Define checkbox callback function
    def update_visibility(label):
        idx = check_labels.index(label)
        for line in lines[idx]:
            line.set_visible(not line.get_visible())
        fig.canvas.draw_idle()
    
    # Connect callback to widget
    runs_checkbox.on_clicked(update_visibility)
    # Create second checkbox for data types (experimental/theoretical)
    type_checkbox_ax = fig.add_axes([0.85, 0.2, 0.12, 0.15], frameon=True)
    type_labels = ['Experimental', 'Theoretical']
    type_checkbox = CheckButtons(
        type_checkbox_ax, 
        type_labels, 
        [True, True]
    )
    
    # Adjust appearance of checkboxes (compatible with older matplotlib)
    for label in type_checkbox.labels:
        label.set_fontsize(12)
    
    # Define type checkbox callback
    def update_type_visibility(label):
        idx = type_labels.index(label)
        for i in range(len(lines)):
            if idx == 0:  # Experimental data (first line in each group)
                lines[i][0].set_visible(not lines[i][0].get_visible())
            else:  # Theoretical data (second and third lines in each group)
                lines[i][1].set_visible(not lines[i][1].get_visible())
                lines[i][2].set_visible(not lines[i][2].get_visible())
        fig.canvas.draw_idle()
    
    # Connect callback to widget
    type_checkbox.on_clicked(update_type_visibility)
    
    # Add title to the controls area
    fig.text(0.85, 0.95, "Graph Controls", fontsize=14, 
             horizontalalignment='center', verticalalignment='top')
    
    plt.show()

# Execute the analysis
if __name__ == "__main__":
    analyze_coffee_filter_data(r"C:\Users\felix\OneDrive - Dawson College\Class Files\SF2 - Coding\SF2-Assignments-and-Submissions\sandbox\clean_data_multiple_filter_j6.csv")
