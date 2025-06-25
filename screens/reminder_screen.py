import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
import sqlite3
from PIL import Image, ImageTk
import os

class ReminderScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        # Load and display background image (full screen)
        bg_path = os.path.join("assets", "background", "menucore.png")  # match your menu bg
        bg_image = Image.open(bg_path).resize((master.winfo_screenwidth(), master.winfo_screenheight()))
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = tk.Label(self, image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # White card container for form and list
        self.card = tk.Frame(self, bg="white", bd=0, highlightthickness=0, width=600, height=650)
        self.card.place(relx=0.5, rely=0.5, anchor="center")

        # Header label
        header = tk.Label(self.card, text="📅 Set a New Reminder", bg="white",
                          fg="#2c3e50", font=("Arial", 20, "bold"))
        header.pack(pady=(25, 20))

        # Form container frame
        form_frame = tk.Frame(self.card, bg="white")
        form_frame.pack(fill="x", padx=40)

        # Reminder Type Label + Combobox
        tk.Label(form_frame, text="Reminder Type:", bg="white", fg="#34495e",
                 font=("Arial", 12)).grid(row=0, column=0, sticky="w", pady=10)
        self.reminder_type = ttk.Combobox(form_frame, values=["Workout", "Meal", "Hydration", "Stretch"],
                                          state="readonly", font=("Arial", 12))
        self.reminder_type.grid(row=0, column=1, sticky="ew", pady=10, padx=(15,0))
        self.reminder_type.current(0)

        # Reminder Time Label + Entry
        tk.Label(form_frame, text="Reminder Time (YYYY-MM-DD HH:MM):", bg="white", fg="#34495e",
                 font=("Arial", 12)).grid(row=1, column=0, sticky="w", pady=10)
        self.reminder_time = tk.Entry(form_frame, font=("Arial", 12))
        self.reminder_time.grid(row=1, column=1, sticky="ew", pady=10, padx=(15,0))
        self.reminder_time.insert(0, datetime.now().strftime('%Y-%m-%d %H:%M'))

        form_frame.columnconfigure(1, weight=1)

        # Buttons Frame
        btn_frame = tk.Frame(self.card, bg="white")
        btn_frame.pack(fill="x", padx=40, pady=(15, 25))

        btn_style = {"font": ("Arial", 12, "bold"), "bd": 0, "relief": "flat", "width": 15, "height": 1}

        add_btn = tk.Button(btn_frame, text="Add Reminder", bg="#e67e22", fg="white", **btn_style, command=self.save_reminder)
        add_btn.grid(row=0, column=0, padx=10)

        del_btn = tk.Button(btn_frame, text="Delete Selected", bg="#e74c3c", fg="white", **btn_style, command=self.delete_reminder)
        del_btn.grid(row=0, column=1, padx=10)

        back_btn = tk.Button(btn_frame, text="← Back to Menu", bg="#3498db", fg="white", **btn_style, command=self.go_back)
        back_btn.grid(row=0, column=2, padx=10)

        # Upcoming Reminders Label
        tk.Label(self.card, text="Upcoming Reminders", bg="white", fg="#2c3e50",
                 font=("Arial", 16, "bold")).pack(pady=(10, 5))

        # Treeview container frame
        tree_frame = tk.Frame(self.card, bg="white")
        tree_frame.pack(fill="both", expand=True, padx=40, pady=(0, 30))

        # Treeview with columns
        self.tree = ttk.Treeview(tree_frame, columns=("Type", "Time"), show="headings", selectmode="browse")
        self.tree.heading("Type", text="Type")
        self.tree.heading("Time", text="Time")
        self.tree.column("Type", anchor="center", width=150)
        self.tree.column("Time", anchor="center", width=300)
        self.tree.pack(side="left", fill="both", expand=True)

        # Scrollbar
        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Create DB and load reminders
        self.create_table()
        self.load_reminders()

    def create_table(self):
        conn = sqlite3.connect('coreboost.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS reminders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                reminder_time TEXT,
                reminder_type TEXT,
                active INTEGER DEFAULT 1
            )
        ''')
        conn.commit()
        conn.close()

    def save_reminder(self):
        r_type = self.reminder_type.get()
        r_time = self.reminder_time.get()

        if not r_type or not r_time:
            messagebox.showerror("Missing Info", "Please enter both reminder type and time.")
            return

        try:
            datetime.strptime(r_time, '%Y-%m-%d %H:%M')
        except ValueError:
            messagebox.showerror("Invalid Format", "Use format YYYY-MM-DD HH:MM")
            return

        try:
            conn = sqlite3.connect('coreboost.db')
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO reminders (user_id, reminder_time, reminder_type, active)
                VALUES (?, ?, ?, 1)
            ''', (1, r_time + ":00", r_type))
            conn.commit()
            conn.close()
            messagebox.showinfo("Added", f"Reminder for {r_type} set at {r_time}")
            self.load_reminders()
        except Exception as e:
            messagebox.showerror("DB Error", str(e))

    def load_reminders(self):
        self.tree.delete(*self.tree.get_children())
        conn = sqlite3.connect('coreboost.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT id, reminder_type, reminder_time FROM reminders
            WHERE user_id = 1 AND active = 1
            ORDER BY reminder_time ASC
        ''')
        for row in cursor.fetchall():
            self.tree.insert('', 'end', iid=row[0], values=(row[1], row[2]))
        conn.close()

    def delete_reminder(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Select", "Please select a reminder to delete.")
            return

        reminder_id = selected[0]
        conn = sqlite3.connect('coreboost.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM reminders WHERE id = ?', (reminder_id,))
        conn.commit()
        conn.close()
        self.tree.delete(reminder_id)
        messagebox.showinfo("Deleted", "Reminder removed successfully.")

    def go_back(self):
        from screens.menu_screen import MenuScreen
        self.master.switch_frame(MenuScreen)
