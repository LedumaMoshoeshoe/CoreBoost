import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

class LiveTrainersScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # 🌄 Background image
        bg_path = os.path.join("assets", "background", "coreboostlogo.png")
        bg_image = Image.open(bg_path).resize((master.winfo_screenwidth(), master.winfo_screenheight()))
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        tk.Label(self, image=self.bg_photo).place(x=0, y=0, relwidth=1, relheight=1)

        # 🧾 Content wrapper
        content = tk.Frame(self, bg="#ffffff", bd=2, relief="ridge")
        content.place(relx=0.5, rely=0.5, anchor="center", width=700, height=550)

        # 📢 Header
        tk.Label(content, text="💪 Live Trainers", font=("Helvetica", 22, "bold"), bg="#ffffff", fg="#333").pack(pady=20)

        # 🧍 Trainer Data
        self.trainers = [
            {"name": "Zinhle M.", "specialty": "Yoga", "status": "Online", "image": "zinhle.jpg"},
            {"name": "Tumi K.", "specialty": "Strength", "status": "Offline", "image": "tumi.jpg"},
            {"name": "Chris D.", "specialty": "Cardio", "status": "Online", "image": "chris.jpg"},
        ]

        self.image_refs = []
        self.container = tk.Frame(content, bg="#ffffff")
        self.container.pack(fill="both", expand=True, padx=20)

        for trainer in self.trainers:
            self.display_trainer(trainer)

        tk.Button(content, text="← Back to Menu", font=("Helvetica", 10, "bold"), bg="#2196F3", fg="white",
                  relief="flat", command=self.go_back).pack(pady=15)

    def display_trainer(self, trainer):
        frame = tk.Frame(self.container, bg="#f7f7f7", bd=1, relief="solid", padx=10, pady=10)
        frame.pack(fill="x", pady=8)

        # 📷 Trainer Image
        image_path = os.path.join("assets", "trainers", trainer["image"])
        try:
            img = Image.open(image_path).resize((70, 70))
            photo = ImageTk.PhotoImage(img)
            self.image_refs.append(photo)
            img_label = tk.Label(frame, image=photo, bg="#f7f7f7")
            img_label.pack(side="left", padx=10)
        except Exception:
            tk.Label(frame, text="🧍", font=("Helvetica", 36), bg="#f7f7f7").pack(side="left", padx=10)

        # 📄 Info Section
        info = tk.Frame(frame, bg="#f7f7f7")
        info.pack(side="left", fill="x", expand=True)

        name = f"{trainer['name']} ({trainer['specialty']})"
        status = trainer["status"]
        status_color = "#4CAF50" if status == "Online" else "#9E9E9E"

        tk.Label(info, text=name, font=("Helvetica", 14, "bold"), bg="#f7f7f7", fg="#333").pack(anchor="w")
        tk.Label(info, text=f"● {status}", fg=status_color, font=("Helvetica", 10, "bold"), bg="#f7f7f7").pack(anchor="w")

        # 🔗 Join Button
        if status == "Online":
            tk.Button(frame, text="Join Session", font=("Helvetica", 10), bg="#4CAF50", fg="white",
                      relief="flat", command=lambda: self.join_session(trainer["name"])).pack(side="right", padx=10)

    def join_session(self, trainer_name):
        messagebox.showinfo("Joining", f"You are joining {trainer_name}'s live session...")

    def go_back(self):
        from .menu_screen import MenuScreen
        self.master.switch_frame(lambda master: MenuScreen(master, ""))
