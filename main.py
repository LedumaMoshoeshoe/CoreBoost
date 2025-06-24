import tkinter as tk
from screens.login_screen import LoginScreen
from screens.menu_screen import MenuScreen     # Import your MenuScreen
from screens.workout_screen import WorkoutScreen  # Import WorkoutScreen
from screens.registration_screen import RegistrationScreen
import threading
from reminders.reminder_timer import check_reminders  # Background reminder checker

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CoreBoost")
        self.geometry("400x600")
        self._frame = None

        # Start the reminder system in the background
        self.start_reminder_checker()

        # Show login screen first
        self.switch_frame(LoginScreen)

    def switch_frame(self, frame_class):
        """Destroy current frame and replace it with a new one."""
        new_frame = frame_class(self) if not callable(frame_class) else frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(fill="both", expand=True)

    # Helper methods to switch to specific screens
    def show_menu_screen(self):
        self.switch_frame(MenuScreen)

    def show_workout_screen(self):
        self.switch_frame(WorkoutScreen)

    def start_reminder_checker(self):
        """Runs the reminder checker in a separate thread."""
        thread = threading.Thread(target=check_reminders, daemon=True)
        thread.start()

    def show_registration_screen(self):
        self.switch_frame(RegistrationScreen)


if __name__ == "__main__":
    app = App()
    app.mainloop()
