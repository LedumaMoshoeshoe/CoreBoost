import tkinter as tk
from screens.login_screen import LoginScreen
import threading
from reminders.reminder_timer import check_reminders  # ✅ Background reminder checker

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CoreBoost")
        self.geometry("400x600")
        self._frame = None

        # ✅ Start the reminder system in the background
        self.start_reminder_checker()

        # Show login screen first
        self.switch_frame(LoginScreen)

    def switch_frame(self, frame_class):
        """Destroy current frame and replace it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(fill="both", expand=True)

    def start_reminder_checker(self):
        """Runs the reminder checker in a separate thread."""
        thread = threading.Thread(target=check_reminders, daemon=True)
        thread.start()

if __name__ == "__main__":
    app = App()
    app.mainloop()
