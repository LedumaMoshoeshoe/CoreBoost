import tkinter as tk
from tkinter import messagebox
from screens.base_screen import BaseScreen
from PIL import Image, ImageTk
import sqlite3
import os

class DietScreen(BaseScreen):
    def __init__(self, master):
        super().__init__(master)
        self.conn = sqlite3.connect("coreboost.db")
        self.create_table()

        # 🌄 Background Image
        bg_path = os.path.join("assets", "background", "coreboostlogo.png")
        bg_image = Image.open(bg_path).resize((master.winfo_screenwidth(), master.winfo_screenheight()))
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = tk.Label(self, image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # 📦 Content Panel
        content = tk.Frame(self, bg="#ffffff", bd=2, relief="ridge")
        content.place(relx=0.5, rely=0.5, anchor="center", width=700, height=600)

        # 🧾 Header
        tk.Label(content, text="🍎 Diet Plan", font=("Helvetica", 22, "bold"), bg="#ffffff", fg="#333").pack(pady=(20, 5))
        tk.Label(content, text="Here you will find your personalized meal plans.",
                 font=("Helvetica", 12), bg="#ffffff", fg="#666").pack(pady=(0, 10))

        # 🍽️ Static placeholder
        tk.Label(content,
                 text="Breakfast: Oats with banana\nLunch: Grilled chicken salad\nDinner: Steamed fish & veggies",
                 font=("Helvetica", 11), justify="left", bg="#ffffff").pack(pady=10)

        # ➕ Add/Edit Meals
        tk.Label(content, text="➕ Add or Edit Your Meal", font=("Helvetica", 13, "bold"), bg="#ffffff", fg="#444").pack(pady=(10, 4))

        # 🧾 Form Frame for Meal Name & Calories (Aligned with grid)
        form_frame = tk.Frame(content, bg="#ffffff")
        form_frame.pack(pady=(0, 10))

        # Meal Name
        tk.Label(form_frame, text="Meal Name:", font=("Helvetica", 10, "bold"), bg="#ffffff").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.meal_entry = tk.Entry(form_frame, font=("Helvetica", 10), width=30)
        self.meal_entry.grid(row=0, column=1, padx=10, pady=5, ipady=3)

        # Calories
        tk.Label(form_frame, text="Calories (kcal):", font=("Helvetica", 10, "bold"), bg="#ffffff").grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.cal_entry = tk.Entry(form_frame, font=("Helvetica", 10), width=30)
        self.cal_entry.grid(row=1, column=1, padx=10, pady=5, ipady=3)

        # 💾 Save Button
        tk.Button(content, text="💾 Save Meal", command=self.add_or_update_meal,
                  bg="#4CAF50", fg="white", relief="flat", padx=10).pack(pady=6)

        # 📝 Meals List
        self.meal_listbox = tk.Listbox(content, width=50, height=8, font=("Helvetica", 10), bg="#f7f7f7", relief="flat")
        self.meal_listbox.pack(pady=10)
        self.meal_listbox.bind("<<ListboxSelect>>", self.load_selected_meal)

        # 🗑️ Delete Meal
        tk.Button(content, text="🗑️ Delete Selected Meal", command=self.delete_meal,
                  bg="#e53935", fg="white", relief="flat", padx=10).pack(pady=4)

        # 🔥 Total Calories
        self.total_label = tk.Label(content, text="", font=("Helvetica", 12, "bold"), bg="#ffffff", fg="#444")
        self.total_label.pack(pady=8)

        # 🔙 Back Button
        tk.Button(content, text="← Back to Menu", command=self.go_back,
                  bg="#2196F3", fg="white", activebackground="#1976D2", relief="flat", padx=12).pack(pady=10)

        # Init state
        self.selected_meal_id = None
        self.refresh_meals()

    def create_table(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS meals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                meal TEXT,
                calories INTEGER
            )
        """)
        self.conn.commit()

    def add_or_update_meal(self):
        meal = self.meal_entry.get()
        calories = self.cal_entry.get()

        if not meal or not calories.isdigit():
            messagebox.showwarning("Invalid Input", "Please enter a valid meal and numeric calories.")
            return

        if self.selected_meal_id:  # Update
            self.conn.execute("UPDATE meals SET meal = ?, calories = ? WHERE id = ?",
                              (meal, int(calories), self.selected_meal_id))
        else:  # Insert
            self.conn.execute("INSERT INTO meals (meal, calories) VALUES (?, ?)", (meal, int(calories)))

        self.conn.commit()
        self.clear_entries()
        self.refresh_meals()

    def delete_meal(self):
        if self.selected_meal_id:
            self.conn.execute("DELETE FROM meals WHERE id = ?", (self.selected_meal_id,))
            self.conn.commit()
            self.clear_entries()
            self.refresh_meals()
        else:
            messagebox.showinfo("Select a Meal", "Please select a meal to delete.")

    def load_selected_meal(self, event):
        selection = self.meal_listbox.curselection()
        if selection:
            index = selection[0]
            meal_id, meal, calories = self.meals_data[index]
            self.selected_meal_id = meal_id
            self.meal_entry.delete(0, tk.END)
            self.meal_entry.insert(0, meal)
            self.cal_entry.delete(0, tk.END)
            self.cal_entry.insert(0, str(calories))

    def clear_entries(self):
        self.selected_meal_id = None
        self.meal_entry.delete(0, tk.END)
        self.cal_entry.delete(0, tk.END)

    def refresh_meals(self):
        self.meal_listbox.delete(0, tk.END)
        self.meals_data = []
        total_cal = 0

        cursor = self.conn.execute("SELECT id, meal, calories FROM meals")
        for row in cursor:
            meal_id, meal, calories = row
            self.meal_listbox.insert(tk.END, f"{meal} - {calories} cal")
            self.meals_data.append((meal_id, meal, calories))
            total_cal += calories

        self.total_label.config(text=f"🔥 Total Daily Calories: {total_cal} cal")

    def go_back(self):
        from screens.menu_screen import MenuScreen
        self.master.switch_frame(MenuScreen)
