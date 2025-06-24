import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Requires `pillow` package
import os

class LiveTrainersScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        tk.Label(self, text="💪 Live Trainers", font=("Arial", 20)).pack(pady=20)

        # Example trainer data
        self.trainers = [
            {"name": "Zinhle M.", "specialty": "Yoga", "status": "Online", "image": "zinhle.jpg"},
            {"name": "Tumi K.", "specialty": "Strength", "status": "Offline", "image": "tumi.jpg"},
            {"name": "Chris D.", "specialty": "Cardio", "status": "Online", "image": "chris.jpg"},
        ]

        # Container frame (for potential scroll support later)
        self.container = tk.Frame(self)
        self.container.pack(padx=10, pady=10)

        self.image_refs = []  # Keep references to prevent image garbage collection

        for trainer in self.trainers:
            self.display_trainer(trainer)

        tk.Button(self, text="Back to Menu", command=self.go_back).pack(pady=20)

    def display_trainer(self, trainer):
        frame = tk.Frame(self.container, bd=2, relief="groove", padx=10, pady=10)
        frame.pack(fill="x", pady=8)

        # Load image
        image_path = os.path.join("assets", "trainers", trainer["image"])
        try:
            img = Image.open(image_path).resize((80, 80))
            photo = ImageTk.PhotoImage(img)
            self.image_refs.append(photo)  # Prevent garbage collection

            img_label = tk.Label(frame, image=photo)
            img_label.pack(side="left", padx=10)
        except Exception as e:
            tk.Label(frame, text="🧍", font=("Arial", 30)).pack(side="left", padx=10)

        # Textual info
        info = tk.Frame(frame)
        info.pack(side="left", fill="x", expand=True)

        name = f"{trainer['name']} ({trainer['specialty']})"
        status = trainer["status"]

        tk.Label(info, text=name, font=("Arial", 14, "bold")).pack(anchor="w")
        tk.Label(info, text=f"Status: {status}", fg="green" if status == "Online" else "gray").pack(anchor="w")

        # Join button (only if online)
        if status == "Online":
            tk.Button(frame, text="Join Session", command=lambda: self.join_session(trainer["name"])).pack(side="right", padx=10)

    def join_session(self, trainer_name):
        messagebox.showinfo("Joining", f"You are joining {trainer_name}'s live session...")

    def go_back(self):
        from .menu_screen import MenuScreen
        self.master.switch_frame(lambda master: MenuScreen(master, ""))
