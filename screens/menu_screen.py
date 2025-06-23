import tkinter as tk
from screens.workout_screen import WorkoutScreen
from screens.diet_screen import DietScreen
from screens.meditation_screen import MeditationScreen
from screens.community_screen import CommunityScreen
from screens.reminder_screen import ReminderScreen

class MenuScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        tk.Label(self, text="Welcome to CoreBoost!", font=("Arial", 20)).pack(pady=20)

        tk.Button(self, text="Select Workout", width=30, command=lambda: master.switch_frame(WorkoutScreen)).pack(pady=5)
        tk.Button(self, text="Diet Plan", width=30, command=lambda: master.switch_frame(DietScreen)).pack(pady=5)
        tk.Button(self, text="Stretch & Meditation", width=30, command=lambda: master.switch_frame(MeditationScreen)).pack(pady=5)
        tk.Button(self, text="Set Reminders", width=30, command=lambda: master.switch_frame(ReminderScreen)).pack(pady=5)
        tk.Button(self, text="Join Community", width=30, command=lambda: master.switch_frame(CommunityScreen)).pack(pady=5)
        tk.Button(self, text="Live Trainers", width=30).pack(pady=5)

        tk.Button(self, text="Logout", width=30, command=self.logout).pack(pady=20)

    def logout(self):
        from screens.login_screen import LoginScreen  # ✅ Local import to prevent circular import
        self.master.switch_frame(LoginScreen)
