import tkinter as tk
from tkinter import messagebox, scrolledtext
import sqlite3
import datetime
import random
from screens.base_screen import BaseScreen
from PIL import Image, ImageTk
import os

class CommunityScreen(BaseScreen):
    def __init__(self, master, username="Guest"):
        super().__init__(master)
        self.username = username
        self.conn = sqlite3.connect("coreboost.db")
        self.create_tables()

        # 🔲 Background image
        bg_path = os.path.join("assets", "background", "coreboostlogo.png")
        bg_image = Image.open(bg_path).resize((master.winfo_screenwidth(), master.winfo_screenheight()))
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = tk.Label(self, image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # 🔳 Content panel
        content = tk.Frame(self, bg="#ffffff", bd=2, relief="ridge")
        content.place(relx=0.5, rely=0.5, anchor="center", width=800, height=580)

        # 🔤 Header
        tk.Label(content, text="🌍 CoreBoost Community", font=("Helvetica", 22, "bold"), bg="#ffffff", fg="#333").pack(pady=(20, 5))
        tk.Label(content, text=f"Welcome, {self.username} | Chat with others!", font=("Helvetica", 12), bg="#ffffff", fg="#666").pack(pady=(0, 15))

        # 💬 Chat display
        self.chat_display = scrolledtext.ScrolledText(content, width=70, height=12, state='disabled', wrap='word', bg="#f9f9f9", relief="flat")
        self.chat_display.pack(pady=(0, 10))

        # 📝 Message input
        entry_frame = tk.Frame(content, bg="#ffffff")
        entry_frame.pack(pady=5)

        self.message_entry = tk.Entry(entry_frame, width=50, font=("Helvetica", 10))
        self.message_entry.pack(side="left", padx=(0, 10), ipady=4)
        tk.Button(entry_frame, text="📨 Send", command=self.send_message,
                  bg="#4CAF50", fg="white", activebackground="#45A049", relief="flat", padx=10).pack(side="left")

        # 🧍 Moderation + online section
        right_frame = tk.Frame(content, bg="#ffffff")
        right_frame.pack(pady=10)

        if self.username.lower() == "admin":
            tk.Button(right_frame, text="🧹 Clear Chat History", command=self.clear_messages,
                      bg="#ff4444", fg="white", relief="flat", padx=10).pack(pady=5)

        tk.Label(right_frame, text="🟢 Online Users", font=("Helvetica", 11, "bold"), bg="#ffffff").pack()
        self.online_list = tk.Text(right_frame, height=4, width=25, bg="#f1f1f1", relief="flat", font=("Helvetica", 10))
        self.online_list.pack()
        self.online_list.config(state="disabled")

        self.update_online_users()

        # 🔙 Back Button
        tk.Button(content, text="← Back to Menu", command=self.go_back,
                  bg="#2196F3", fg="white", activebackground="#1976D2", relief="flat", padx=12).pack(pady=15)

        # 🗂️ Load messages
        self.load_messages()

    def create_tables(self):
        try:
            self.conn.execute("SELECT username FROM chat_messages LIMIT 1")
        except sqlite3.OperationalError:
            print("🛠 Rebuilding chat_messages table with username column...")
            self.conn.execute("DROP TABLE IF EXISTS chat_messages")
            self.conn.execute("""
                CREATE TABLE chat_messages (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT,
                    message TEXT,
                    timestamp TEXT
                )
            """)
            self.conn.commit()

    def send_message(self):
        msg = self.message_entry.get().strip()
        if msg:
            timestamp = datetime.datetime.now().strftime("%H:%M")
            self.conn.execute(
                "INSERT INTO chat_messages (username, message, timestamp) VALUES (?, ?, ?)",
                (self.username, msg, timestamp)
            )
            self.conn.commit()
            self.message_entry.delete(0, tk.END)
            self.load_messages()
        else:
            messagebox.showwarning("Empty Message", "Please type something before sending.")

    def load_messages(self):
        self.chat_display.config(state="normal")
        self.chat_display.delete("1.0", tk.END)

        cursor = self.conn.execute("SELECT username, message, timestamp FROM chat_messages ORDER BY id DESC LIMIT 50")
        messages = cursor.fetchall()[::-1]

        for username, message, timestamp in messages:
            self.chat_display.insert(tk.END, f"[{timestamp}] {username}: {message}\n")

        self.chat_display.config(state="disabled")
        self.chat_display.yview(tk.END)

    def clear_messages(self):
        confirm = messagebox.askyesno("Confirm Clear", "Are you sure you want to clear all messages?")
        if confirm:
            self.conn.execute("DELETE FROM chat_messages")
            self.conn.commit()
            self.load_messages()

    def update_online_users(self):
        sample_users = ["testinguser", "TlotlisoM", "Chad", "LeratoM", "Mpumi", "admin"]
        if self.username not in sample_users:
            sample_users.append(self.username)
        random.shuffle(sample_users)

        self.online_list.config(state="normal")
        self.online_list.delete("1.0", tk.END)
        for name in sample_users[:5]:
            self.online_list.insert(tk.END, f"🟢 {name}\n")
        self.online_list.config(state="disabled")

    def go_back(self):
        from screens.menu_screen import MenuScreen
        self.master.switch_frame(MenuScreen)
