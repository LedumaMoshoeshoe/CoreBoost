import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
from screens.base_screen import BaseScreen

class WorkoutScreen(BaseScreen):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        # Background image full screen (matching your app style)
        bg_path = os.path.join("assets", "background", "menucore.png")
        bg_image = Image.open(bg_path).resize((master.winfo_screenwidth(), master.winfo_screenheight()))
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = tk.Label(self, image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # White card container
        self.card = tk.Frame(self, bg="white", bd=0, highlightthickness=0, width=450, height=400)
        self.card.place(relx=0.5, rely=0.5, anchor="center")

        # Title
        tk.Label(self.card, text="Workout Selection", bg="white",
                 font=("Arial", 20, "bold"), fg="#2c3e50").pack(pady=(30, 20))

        # Form container
        form_frame = tk.Frame(self.card, bg="white")
        form_frame.pack(padx=40, fill="x")

        # Exercise Type
        tk.Label(form_frame, text="Choose Exercise Type:", bg="white",
                 fg="#34495e", font=("Arial", 12)).grid(row=0, column=0, sticky="w", pady=10)
        self.exercise_type = ttk.Combobox(form_frame, values=["Yoga", "Pilates", "Strength"], font=("Arial", 12), state="readonly")
        self.exercise_type.grid(row=0, column=1, sticky="ew", pady=10, padx=(15,0))
        self.exercise_type.current(0)

        # Intensity Level
        tk.Label(form_frame, text="Intensity Level:", bg="white",
                 fg="#34495e", font=("Arial", 12)).grid(row=1, column=0, sticky="w", pady=10)
        self.intensity = ttk.Combobox(form_frame, values=["Beginner", "Intermediate", "Advanced"], font=("Arial", 12), state="readonly")
        self.intensity.grid(row=1, column=1, sticky="ew", pady=10, padx=(15,0))
        self.intensity.current(0)

        # Select Time
        tk.Label(form_frame, text="Select Time (minutes):", bg="white",
                 fg="#34495e", font=("Arial", 12)).grid(row=2, column=0, sticky="w", pady=10)
        self.time_entry = tk.Entry(form_frame, font=("Arial", 12))
        self.time_entry.grid(row=2, column=1, sticky="ew", pady=10, padx=(15,0))

        form_frame.columnconfigure(1, weight=1)

        # Buttons frame
        btn_frame = tk.Frame(self.card, bg="white")
        btn_frame.pack(pady=20, padx=40, fill="x")

        btn_style = {
            "font": ("Arial", 12, "bold"),
            "bd": 0,
            "relief": "flat",
            "width": 15,
            "height": 1,
            "fg": "white",
        }

        save_btn = tk.Button(btn_frame, text="Save Workout", bg="#e67e22", command=self.save_workout, **btn_style)
        save_btn.grid(row=0, column=0, padx=10)

        back_btn = tk.Button(btn_frame, text="Back to Menu", bg="#3498db", command=self.back_to_menu, **btn_style)
        back_btn.grid(row=0, column=1, padx=10)

        btn_frame.columnconfigure((0,1), weight=1)

    def save_workout(self):
        # Placeholder: Save to database or file
        print("Workout saved:", self.exercise_type.get(), self.intensity.get(), self.time_entry.get())
        # Optionally add a messagebox or confirmation here

    def back_to_menu(self):
        # Use your master’s method to go back
        self.master.show_menu_screen()
