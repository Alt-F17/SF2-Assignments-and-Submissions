import numpy as np
import os
from datetime import datetime

# File path for checkpoint
CHECKPOINT_PATH = r"c:\Users\felix\OneDrive - Dawson College\Class Files\SF2 - Coding\SF2-Assignments-and-Submissions\sandbox\PosiPrimes\checkpoint.npz"

def load_current_checkpoint():
    """Load and display current checkpoint values"""
    if os.path.exists(CHECKPOINT_PATH):
        data = np.load(CHECKPOINT_PATH)
        current_num = int(data['current_num'])
        current_position = int(data['current_position'])
        print(f"Current checkpoint values:")
        print(f"  Number to start from: {current_num:,}")
        print(f"  Current prime position: {current_position:,}")
        return current_num, current_position
    else:
        print("No checkpoint file found.")
        return None, None

def backup_checkpoint():
    """Create a backup of the current checkpoint file"""
    if os.path.exists(CHECKPOINT_PATH):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = CHECKPOINT_PATH.replace('.npz', f'_backup_{timestamp}.npz')
        import shutil
        shutil.copy2(CHECKPOINT_PATH, backup_path)
        print(f"Backup created: {os.path.basename(backup_path)}")

def save_checkpoint(current_num, current_position):
    """Save new checkpoint values"""
    np.savez(CHECKPOINT_PATH, 
             current_num=current_num,
             current_position=current_position)
    print(f"Checkpoint saved successfully.")
    print(f"  New starting number: {current_num:,}")
    print(f"  New prime position: {current_position:,}")

def set_manual_checkpoint():
    """Set checkpoint values manually"""
    print("\n=== Position Prime Finder - Checkpoint Manager ===\n")
    
    # Load and display current values
    current_num, current_position = load_current_checkpoint()
    
    # Get new values from user
    print("\nEnter new checkpoint values (or press Enter to keep current):")
    
    # Starting number
    new_num_str = input(f"New starting number [{current_num:,}]: ")
    if new_num_str.strip():
        try:
            new_num = int(new_num_str.replace(',', ''))
            # Ensure it's odd (if not 2)
            if new_num > 2 and new_num % 2 == 0:
                new_num += 1
                print(f"Adjusted to next odd number: {new_num:,}")
        except ValueError:
            print("Invalid input. Using current value.")
            new_num = current_num
    else:
        new_num = current_num
    
    # Current position
    new_pos_str = input(f"New prime position [{current_position:,}]: ")
    if new_pos_str.strip():
        try:
            new_pos = int(new_pos_str.replace(',', ''))
        except ValueError:
            print("Invalid input. Using current value.")
            new_pos = current_position
    else:
        new_pos = current_position
    
    # Confirm changes
    print("\nReview new checkpoint values:")
    print(f"  Starting number: {new_num:,}")
    print(f"  Prime position: {new_pos:,}")
    
    confirm = input("\nSave these changes? (y/n): ")
    if confirm.lower() in ['y', 'yes']:
        # Backup existing checkpoint
        backup_checkpoint()
        # Save new checkpoint
        save_checkpoint(new_num, new_pos)
    else:
        print("Changes discarded.")

if __name__ == "__main__":
    try:
        set_manual_checkpoint()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"Error: {e}")
    
    input("\nPress Enter to exit...")