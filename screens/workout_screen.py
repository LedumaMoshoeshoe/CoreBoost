import tkinter as tk

class WorkoutScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="Workout Selection", font=("Arial", 18)).pack(pady=20)

        tk.Label(self, text="Choose Exercise Type").pack()
        self.exercise_type = tk.StringVar()
        tk.OptionMenu(self, self.exercise_type, "Yoga", "Pilates", "Strength").pack()

        tk.Label(self, text="Intensity Level").pack()
        self.intensity = tk.StringVar()
        tk.OptionMenu(self, self.intensity, "Beginner", "Intermediate", "Advanced").pack()

        tk.Label(self, text="Select Time").pack()
        self.time_entry = tk.Entry(self)
        self.time_entry.pack()

        tk.Button(self, text="Save Workout", command=self.save_workout).pack(pady=10)

        # Back button to return to menu screen
        tk.Button(self, text="Back to Menu", command=self.back_to_menu).pack(pady=10)

    def save_workout(self):
        # Placeholder: Save to database or file
        print("Workout saved:", self.exercise_type.get(), self.intensity.get(), self.time_entry.get())

    def back_to_menu(self):
        # Call method on master to show the menu screen
        self.master.show_menu_screen()
