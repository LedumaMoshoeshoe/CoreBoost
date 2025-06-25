import tkinter as tk
from PIL import Image, ImageTk
import pygame
import sqlite3
import os

class MeditationScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # 🌄 Background Image
        bg_path = os.path.join("assets", "background", "coreboostlogo.png")
        bg_image = Image.open(bg_path).resize((master.winfo_screenwidth(), master.winfo_screenheight()))
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        tk.Label(self, image=self.bg_photo).place(x=0, y=0, relwidth=1, relheight=1)

        # 🎵 Init pygame mixer
        pygame.mixer.init()
        self.conn = sqlite3.connect("coreboost.db")
        self.create_table()
        self.currently_playing = None

        # 📦 Content Panel
        content = tk.Frame(self, bg="#ffffff", bd=2, relief="ridge")
        content.place(relx=0.5, rely=0.5, anchor="center", width=700, height=620)

        # 🧘 Header
        tk.Label(content, text="🧘 Stretch & Meditation", font=("Helvetica", 22, "bold"), bg="#ffffff", fg="#333").pack(pady=10)
        tk.Label(content, text="Relax your body and mind with guided audio routines.",
                 font=("Helvetica", 12), bg="#ffffff", fg="#666").pack(pady=5)

        # 🔊 Routine List
        self.routines = [
            ("Morning breathing meditation - 5 min", "assets/audio/breathing.mp3"),
            ("Upper body stretch (shoulders & arms) - 7 min", "assets/audio/stretch.mp3"),
            ("Guided mindful cooldown - 10 min", "assets/audio/cooldown.mp3"),
        ]

        for routine_text, audio_path in self.routines:
            tk.Button(content, text=f"▶ {routine_text}", width=45, anchor="w",
                      font=("Helvetica", 10), bg="#4CAF50", fg="white",
                      command=lambda path=audio_path, name=routine_text: self.play_audio(path, name)).pack(pady=2)

            tk.Button(content, text="💾 Save to My Routines", font=("Helvetica", 9),
                      bg="#eeeeee", relief="flat", command=lambda name=routine_text: self.save_routine(name)).pack(pady=(0, 5))

        # 🎵 Now Playing Info
        self.now_playing_label = tk.Label(content, text="🎵 Now Playing: None", font=("Helvetica", 10, "italic"),
                                          bg="#ffffff", fg="blue")
        self.now_playing_label.pack(pady=(5, 5))

        # ⏯ Controls
        controls = tk.Frame(content, bg="#ffffff")
        controls.pack(pady=4)
        tk.Button(controls, text="⏸ Pause", width=10, bg="#FF9800", fg="white", relief="flat",
                  command=self.pause_audio).pack(side="left", padx=5)
        tk.Button(controls, text="⏹ Stop", width=10, bg="#e53935", fg="white", relief="flat",
                  command=self.stop_audio).pack(side="left", padx=5)

        # 🔉 Volume Control
        tk.Label(content, text="🔊 Volume", bg="#ffffff", font=("Helvetica", 10, "bold")).pack(pady=(10, 2))
        self.volume_slider = tk.Scale(content, from_=0, to=100, orient="horizontal",
                                      command=self.set_volume, bg="#ffffff")
        self.volume_slider.set(70)
        self.volume_slider.pack(pady=5)
        pygame.mixer.music.set_volume(0.7)

        # ⭐ Saved Routines
        tk.Label(content, text="⭐ My Saved Routines", font=("Helvetica", 12, "bold"), bg="#ffffff", fg="#333").pack(pady=(10, 2))
        self.saved_list = tk.Text(content, height=5, width=50, font=("Helvetica", 10), bg="#f7f7f7", relief="flat")
        self.saved_list.pack(pady=5)
        self.load_saved_routines()

        # 🔙 Back to Menu
        tk.Button(content, text="← Back to Menu", command=self.go_back,
                  bg="#2196F3", fg="white", relief="flat", padx=12).pack(pady=12)

    def create_table(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS meditation_routines (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT
            )
        """)
        self.conn.commit()

    def save_routine(self, name):
        self.conn.execute("INSERT INTO meditation_routines (name) VALUES (?)", (name,))
        self.conn.commit()
        self.load_saved_routines()

    def load_saved_routines(self):
        self.saved_list.delete("1.0", tk.END)
        cursor = self.conn.execute("SELECT name FROM meditation_routines")
        for row in cursor:
            self.saved_list.insert(tk.END, f"✔ {row[0]}\n")

    def play_audio(self, path, name):
        if os.path.exists(path):
            pygame.mixer.music.load(path)
            pygame.mixer.music.play(-1)
            self.currently_playing = name
            self.now_playing_label.config(text=f"🎵 Now Playing: {name}")
        else:
            tk.messagebox.showerror("Audio Error", f"File not found:\n{path}")

    def pause_audio(self):
        pygame.mixer.music.pause()
        self.now_playing_label.config(text="⏸ Paused")

    def stop_audio(self):
        pygame.mixer.music.stop()
        self.now_playing_label.config(text="⏹ Stopped")

    def set_volume(self, value):
        volume = int(value) / 100
        pygame.mixer.music.set_volume(volume)

    def go_back(self):
        from screens.menu_screen import MenuScreen
        self.master.switch_frame(MenuScreen)
