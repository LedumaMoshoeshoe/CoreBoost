import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
import sqlite3

class ReminderScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack(padx=20, pady=10)
        self.create_widgets()
        self.load_reminders()

    def create_widgets(self):
        tk.Label(self, text="📅 Set a New Reminder", font=("Arial", 16, "bold")).pack(pady=10)

        # Type
        tk.Label(self, text="Reminder Type:").pack(anchor='w')
        self.reminder_type = ttk.Combobox(self, values=["Workout", "Meal", "Hydration", "Stretch"])
        self.reminder_type.pack(fill='x')

        # Date/Time
        tk.Label(self, text="Reminder Time (YYYY-MM-DD HH:MM):").pack(anchor='w', pady=(10, 0))
        self.reminder_time = tk.Entry(self)
        self.reminder_time.insert(0, datetime.now().strftime('%Y-%m-%d %H:%M'))
        self.reminder_time.pack(fill='x')

        tk.Button(self, text="Add Reminder", command=self.save_reminder).pack(pady=10)

        # 📋 List of Reminders
        tk.Label(self, text="Upcoming Reminders", font=("Arial", 14)).pack(pady=10)

        self.tree = ttk.Treeview(self, columns=("Type", "Time"), show='headings')
        self.tree.heading("Type", text="Type")
        self.tree.heading("Time", text="Time")
        self.tree.pack(fill='both', expand=True, pady=10)

        # Delete Button
        tk.Button(self, text="Delete Selected", command=self.delete_reminder).pack(pady=5)

        # 🔙 Back Button
        tk.Button(self, text="← Back to Menu", command=self.go_back).pack(pady=10)

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
