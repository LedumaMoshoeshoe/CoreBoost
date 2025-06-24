import tkinter as tk
from tkinter import messagebox
from screens.workout_screen import WorkoutScreen
from screens.diet_screen import DietScreen
from screens.meditation_screen import MeditationScreen
from screens.community_screen import CommunityScreen
from screens.reminder_screen import ReminderScreen
from PIL import Image, ImageTk
import os

class MenuScreen(tk.Frame):
    def __init__(self, master, username=""):
        super().__init__(master)
        self.master = master
        self.username = username

        self.icons = {}
        icon_names = ["workout", "diet", "meditation", "reminder", "community", "live", "help"]
        for name in icon_names:
            path = os.path.join("assets", "icons", f"{name}.png")
            try:
                img = Image.open(path).resize((24, 24))
                self.icons[name] = ImageTk.PhotoImage(img)
            except:
                self.icons[name] = None  # fallback in case image is missing


        tk.Label(self, text=f"Welcome, {self.username} to CoreBoost!", font=("Arial", 24, "bold")).pack(pady=20)
        tk.Label(self, text="This is the main menu").pack()

        tk.Button(self, text=" Select Workout", image=self.icons["workout"], compound="left",
          width=200, anchor="w", command=lambda: master.switch_frame(WorkoutScreen)).pack(pady=5)

        tk.Button(self, text=" Diet Plan", image=self.icons["diet"], compound="left",
          width=200, anchor="w", command=lambda: master.switch_frame(DietScreen)).pack(pady=5)

        tk.Button(self, text=" Stretch & Meditation", image=self.icons["meditation"], compound="left",
          width=200, anchor="w", command=lambda: master.switch_frame(MeditationScreen)).pack(pady=5)

        tk.Button(self, text=" Set Reminders", image=self.icons["reminder"], compound="left",
          width=200, anchor="w", command=lambda: master.switch_frame(ReminderScreen)).pack(pady=5)

        tk.Button(self, text=" Join Community", image=self.icons["community"], compound="left",
          width=200, anchor="w", command=lambda: master.switch_frame(CommunityScreen)).pack(pady=5)

        tk.Button(self, text=" Live Trainers", image=self.icons["live"], compound="left",
          width=200, anchor="w", command=self.show_live_trainers).pack(pady=5)

        tk.Button(self, text=" Help / Contact Us", image=self.icons["help"], compound="left",
          width=200, anchor="w", command=self.go_to_help).pack(pady=5)
        
        tk.Button(self, text="Logout", width=30, command=self.logout).pack(pady=20)

    def logout(self):
        from screens.login_screen import LoginScreen
        self.master.switch_frame(LoginScreen)

    def show_live_trainers(self):
        from screens.live_trainers_screen import LiveTrainersScreen  # ✅ Actual screen import
        self.master.switch_frame(lambda master: LiveTrainersScreen(master))

    def go_to_help(self):
        from .help_screen import HelpScreen
        self.master.switch_frame(HelpScreen)
