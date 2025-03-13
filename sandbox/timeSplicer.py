# Time Splicer - A visual timer application
import pygame
import datetime
import math
import sys
import os

# Check if pygame_gui is installed, provide helpful message if not
try:
    import pygame_gui
except ImportError:
    print("Error: pygame_gui module not found.")
    print("Please install it using: pip install pygame_gui")
    sys.exit(1)

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 150, 0)
GRAY = (100, 100, 100)
WHITE = (255, 255, 255)

class TimerApp:
    def __init__(self):
        # Set up display
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Time Splicer")
        icon = pygame.Surface((32, 32))
        icon.fill(GREEN)
        pygame.display.set_icon(icon)
        
        # Initialize clock and UI manager
        self.clock = pygame.time.Clock()
        self.manager = pygame_gui.UIManager((WIDTH, HEIGHT), os.path.join(os.path.dirname(__file__), 'theme.json') if os.path.exists(os.path.join(os.path.dirname(__file__), 'theme.json')) else None)
        
        # Timer variables
        self.start_time = None
        self.end_time = None
        self.total_duration = 0
        self.total_tasks = 5
        self.completed_tasks = 0
        self.paused = False
        self.pause_start_time = None
        self.pause_duration = 0
        
        # App state
        self.state = "setup"  # "setup" or "timer"
        
        # Initialize fonts (fallback to default if Consolas isn't available)
        try:
            self.title_font = pygame.font.SysFont('consolas', 36)
            self.font = pygame.font.SysFont('consolas', 24)
            self.small_font = pygame.font.SysFont('consolas', 18)
        except:
            self.title_font = pygame.font.Font(None, 36)
            self.font = pygame.font.Font(None, 24)
            self.small_font = pygame.font.Font(None, 18)
        
        # Create UI for setup screen
        self.selected_date = datetime.datetime.now().date()
        self.date_picker = None
        self.create_setup_ui()
    
    def create_setup_ui(self):
        # Date picker button
        self.date_picker_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((300, 120), (200, 40)),
            text='Select Date',
            manager=self.manager
        )
        
        # Time inputs (hours, minutes, seconds)
        self.hour_input = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((300, 180), (60, 40)),
            manager=self.manager
        )
        self.hour_input.set_text("00")
        
        self.minute_input = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((370, 180), (60, 40)),
            manager=self.manager
        )
        self.minute_input.set_text("00")
        
        self.second_input = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((440, 180), (60, 40)),
            manager=self.manager
        )
        self.second_input.set_text("00")
        
        # Task count input
        self.task_input = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((300, 240), (200, 40)),
            manager=self.manager
        )
        self.task_input.set_text("5")
        
        # Start button
        self.start_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((300, 300), (200, 50)),
            text='Start Timer',
            manager=self.manager
        )
    
    def create_timer_ui(self):
        # Timer control buttons
        self.pause_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((WIDTH - 220, HEIGHT - 60), (100, 40)),
            text='Pause' if not self.paused else 'Resume',
            manager=self.manager
        )
        
        self.end_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((WIDTH - 110, HEIGHT - 60), (100, 40)),
            text='End Timer',
            manager=self.manager
        )
        
        # Task completion buttons
        self.task_up_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((WIDTH - 220, 150), (100, 40)),
            text='Task +',
            manager=self.manager
        )
        
        self.task_down_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((WIDTH - 110, 150), (100, 40)),
            text='Task -',
            manager=self.manager
        )
    
    def start_timer(self):
        try:
            # Set start time to now
            self.start_time = datetime.datetime.now()
            
            # Parse end time from inputs
            hour = min(max(0, int(self.hour_input.get_text())), 23)
            minute = min(max(0, int(self.minute_input.get_text())), 59)
            second = min(max(0, int(self.second_input.get_text())), 59)
            
            # Set end time using the selected date
            self.end_time = datetime.datetime.combine(
                self.selected_date,
                datetime.time(hour, minute, second)
            )
            
            # If end time is in the past, move to the next day
            if self.end_time < self.start_time:
                self.end_time += datetime.timedelta(days=1)
            
            # Calculate total duration
            self.total_duration = (self.end_time - self.start_time).total_seconds()
            
            # Set tasks
            self.total_tasks = max(1, int(self.task_input.get_text()))
            self.completed_tasks = 0
            
            # Reset pause variables
            self.paused = False
            self.pause_start_time = None
            self.pause_duration = 0
            
            # Change state
            self.state = "timer"
            
            # Clear UI and create timer UI
            self.manager.clear_and_reset()
            self.create_timer_ui()
            return True
        except ValueError:
            print("Invalid input values. Please check your entries.")
            return False
    
    def draw_round_timer(self):
        # Draw circular timer
        center_x, center_y = WIDTH // 3, HEIGHT // 2
        radius = 150
        
        # Calculate remaining time
        now = datetime.datetime.now()
        if self.paused:
            effective_now = self.pause_start_time
        else:
            effective_now = now
            
        elapsed_seconds = (effective_now - self.start_time).total_seconds() - self.pause_duration
        remaining_seconds = max(0, self.total_duration - elapsed_seconds)
        
        # Calculate progress (0.0 to 1.0)
        progress = min(1.0, elapsed_seconds / self.total_duration) if self.total_duration > 0 else 1.0
        
        # Draw background circle
        pygame.draw.circle(self.screen, GRAY, (center_x, center_y), radius)
        
        if progress > 0:
            # Draw progress arc using polygon approach
            points = [(center_x, center_y)]  # Center point
            angle_start = -90  # Start at top (12 o'clock position)
            angle_end = angle_start + (360 * progress)
            
            # Add arc points
            for angle in range(int(angle_start), int(angle_end) + 1, 2):  # Step by 2 degrees for smoother arc
                rad_angle = math.radians(angle)
                x = center_x + radius * math.cos(rad_angle)
                y = center_y + radius * math.sin(rad_angle)
                points.append((x, y))
            
            # Draw the arc if we have enough points
            if len(points) > 2:
                # Add final point if needed for precision
                if angle_end - int(angle_end) > 0:
                    final_angle = math.radians(angle_end)
                    x = center_x + radius * math.cos(final_angle)
                    y = center_y + radius * math.sin(final_angle)
                    points.append((x, y))
                
                pygame.draw.polygon(self.screen, GREEN, points)
        
        # Display time remaining
        hours, remainder = divmod(remaining_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        time_str = f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"
        
        time_text = self.font.render(time_str, True, WHITE)
        self.screen.blit(time_text, (center_x - time_text.get_width() // 2, center_y - time_text.get_height() // 2))
        
        # Return remaining time info for other displays
        return remaining_seconds, progress
    
    def draw_timer_screen(self):
        # Draw timer components
        remaining_seconds, progress = self.draw_round_timer()
        
        # Calculate time per remaining task (handle division by zero)
        remaining_tasks = max(1, self.total_tasks - self.completed_tasks)
        time_per_task = remaining_seconds / remaining_tasks
        
        # Progress bar at bottom
        bar_width = WIDTH - 200
        bar_height = 30
        pygame.draw.rect(self.screen, GRAY, (50, HEIGHT - 100, bar_width, bar_height))
        pygame.draw.rect(self.screen, GREEN, (50, HEIGHT - 100, bar_width * progress, bar_height))
        
        progress_text = self.small_font.render(f"{progress * 100:.1f}%", True, GREEN)
        self.screen.blit(progress_text, (bar_width + 60, HEIGHT - 100))
        
        # Task completion counter
        task_percentage = (self.completed_tasks / self.total_tasks * 100) if self.total_tasks > 0 else 0
        task_text = self.font.render(
            f"Tasks: {self.completed_tasks}/{self.total_tasks} ({task_percentage:.1f}%)",
            True, GREEN)
        self.screen.blit(task_text, (50, 150))
        
        # Time per task
        minutes_per_task, seconds_per_task = divmod(time_per_task, 60)
        time_per_task_text = self.font.render(
            f"Time per task: {int(minutes_per_task):02d}:{int(seconds_per_task):02d}",
            True, GREEN)
        self.screen.blit(time_per_task_text, (50, 190))
        
        # End time
        end_time_text = self.font.render(
            f"End time: {self.end_time.strftime('%H:%M:%S')}",
            True, GREEN)
        self.screen.blit(end_time_text, (50, 230))
    
    def draw_setup_screen(self):
        # Draw setup screen UI
        title = self.title_font.render("Time Splicer Setup", True, GREEN)
        self.screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 50))
        
        date_label = self.font.render("Date:", True, GREEN)
        self.screen.blit(date_label, (150, 130))
        
        time_label = self.font.render("Time (HH:MM:SS):", True, GREEN)
        self.screen.blit(time_label, (100, 190))
        
        tasks_label = self.font.render("Number of tasks:", True, GREEN)
        self.screen.blit(tasks_label, (120, 250))
        
        # Show selected date
        date_text = self.font.render(
            f"Selected: {self.selected_date.strftime('%Y-%m-%d')}",
            True, GREEN)
        self.screen.blit(date_text, (530, 130))
    
    def run(self):
        running = True
        
        while running:
            time_delta = self.clock.tick(60) / 1000.0
            
            # Process events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                # Pass events to UI manager
                self.manager.process_events(event)
                
                # Handle UI interactions based on current state
                if self.state == "setup":
                    if event.type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == self.date_picker_button:
                            # Create calendar picker
                            try:
                                self.date_picker = pygame_gui.windows.UICalendarWindow(
                                    rect=pygame.Rect((300, 120), (300, 300)),
                                    manager=self.manager
                                )
                            except Exception as e:
                                # Fallback if calendar window fails (older pygame_gui versions)
                                print(f"Calendar window error: {e}")
                                self.selected_date = datetime.datetime.now().date()
                        
                        elif event.ui_element == self.start_button:
                            self.start_timer()
                    
                    # Handle calendar date selection
                    elif event.type == pygame_gui.UI_WINDOW_CLOSE:
                        if hasattr(self, 'date_picker') and self.date_picker and event.ui_element == self.date_picker:
                            self.date_picker = None
                    
                    elif event.type == pygame_gui.UI_CALENDAR_DATE_CHANGED:
                        self.selected_date = event.date
                
                elif self.state == "timer":
                    if event.type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == self.pause_button:
                            # Toggle pause/resume
                            self.paused = not self.paused
                            self.pause_button.set_text('Resume' if self.paused else 'Pause')
                            
                            if self.paused:
                                self.pause_start_time = datetime.datetime.now()
                            else:
                                # Calculate and add pause duration
                                pause_time = (datetime.datetime.now() - self.pause_start_time).total_seconds()
                                self.pause_duration += pause_time
                        
                        elif event.ui_element == self.end_button:
                            # Return to setup screen
                            self.state = "setup"
                            self.manager.clear_and_reset()
                            self.create_setup_ui()
                        
                        elif event.ui_element == self.task_up_button:
                            # Increment completed tasks
                            self.completed_tasks = min(self.completed_tasks + 1, self.total_tasks)
                        
                        elif event.ui_element == self.task_down_button:
                            # Decrement completed tasks
                            self.completed_tasks = max(self.completed_tasks - 1, 0)
            
            # Update UI manager
            self.manager.update(time_delta)
            
            # Draw background
            self.screen.fill(BLACK)
            
            # Draw content based on current state
            if self.state == "setup":
                self.draw_setup_screen()
            
            elif self.state == "timer":
                # Check if timer has ended
                now = datetime.datetime.now()
                effective_now = now if not self.paused else self.pause_start_time
                elapsed_with_pause = (effective_now - self.start_time).total_seconds() - self.pause_duration
                
                if not self.paused and elapsed_with_pause >= self.total_duration:
                    # Timer completed
                    completion_text = self.title_font.render("Time's up!", True, GREEN)
                    self.screen.blit(completion_text, (WIDTH // 2 - completion_text.get_width() // 2, 50))
                    
                    # Show final stats
                    self.draw_timer_screen()
                else:
                    # Timer running
                    timer_text = self.title_font.render("Time Remaining", True, GREEN)
                    self.screen.blit(timer_text, (WIDTH // 2 - timer_text.get_width() // 2, 50))
                    self.draw_timer_screen()
            
            # Draw UI elements
            self.manager.draw_ui(self.screen)
            
            # Update display
            pygame.display.update()
        
        pygame.quit()

# Start the application when script is run directly
if __name__ == "__main__":
    try:
        app = TimerApp()
        app.run()
    except Exception as e:
        print(f"Error running application: {e}")
        import traceback
        traceback.print_exc()
        pygame.quit()
        sys.exit(1)