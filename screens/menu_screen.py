import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw
import os

from screens.workout_screen import WorkoutScreen
from screens.diet_screen import DietScreen
from screens.meditation_screen import MeditationScreen
from screens.community_screen import CommunityScreen
from screens.reminder_screen import ReminderScreen

class MenuScreen(tk.Frame):
    def __init__(self, master, username=""):
        super().__init__(master)
        self.master = master
        self.username = username

        # Load and display background image
        bg_path = os.path.join("assets", "background", "menucore.png")
        bg_image = Image.open(bg_path).resize((master.winfo_screenwidth(), master.winfo_screenheight()))
        self.bg_photo = ImageTk.PhotoImage(bg_image)

        bg_label = tk.Label(self, image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Replace canvas and oval shadow with a single centered white Frame
        self.card = tk.Frame(self, bg="white", bd=0, highlightthickness=0, width=420, height=520)
        self.card.place(relx=0.5, rely=0.5, anchor="center")


        # Welcome message
        tk.Label(self.card, text=f"Welcome, {self.username} to CoreBoost!", font=("Arial", 16, "bold"),
                 bg="white").pack(pady=(20, 5))
        tk.Label(self.card, text="This is your main dashboard", bg="white", font=("Arial", 10)).pack(pady=(0, 15))

        # Load icons
        self.icons = {}
        icon_names = ["workout", "diet", "meditation", "reminder", "community", "live", "help"]
        for name in icon_names:
            path = os.path.join("assets", "icons", f"{name}.png")
            try:
                img = Image.open(path).resize((24, 24))
                self.icons[name] = ImageTk.PhotoImage(img)
            except:
                self.icons[name] = None

        # Menu buttons
        self.create_menu_button(" Select Workout", self.icons["workout"], lambda: master.switch_frame(WorkoutScreen))
        self.create_menu_button(" Diet Plan", self.icons["diet"], lambda: master.switch_frame(DietScreen))
        self.create_menu_button(" Stretch & Meditation", self.icons["meditation"], lambda: master.switch_frame(MeditationScreen))
        self.create_menu_button(" Set Reminders", self.icons["reminder"], lambda: master.switch_frame(ReminderScreen))
        self.create_menu_button(" Join Community", self.icons["community"], lambda: master.switch_frame(CommunityScreen))
        self.create_menu_button(" Live Trainers", self.icons["live"], self.show_live_trainers)
        self.create_menu_button(" Help / Contact Us", self.icons["help"], self.go_to_help)

        # Logout button
        tk.Button(self.card, text="Logout", width=20, font=("Arial", 10, "bold"),
                  bg="#ff4d4d", fg="white", relief="flat", command=self.logout).pack(pady=15)

    def create_menu_button(self, text, icon, command):
        """Helper method to create styled menu buttons"""
        btn = tk.Button(
            self.card, text=text, image=icon, compound="left", anchor="w",
            width=220, padx=10, font=("Arial", 10),
            bg="#f0f0f0", fg="#222", relief="flat", command=command
        )
        btn.pack(pady=4)

    def logout(self):
        from screens.login_screen import LoginScreen
        self.master.switch_frame(LoginScreen)

    def show_live_trainers(self):
        from screens.live_trainers_screen import LiveTrainersScreen
        self.master.switch_frame(lambda master: LiveTrainersScreen(master))

    def go_to_help(self):
        from .help_screen import HelpScreen
        self.master.switch_frame(HelpScreen)
