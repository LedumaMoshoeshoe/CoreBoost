import tkinter as tk

class DietScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        tk.Label(self, text="🍎 Diet Plan", font=("Arial", 20, "bold")).pack(pady=20)
        tk.Label(self, text="Here you will find your personalized meal plans.", font=("Arial", 12)).pack(pady=10)

        # Sample placeholder for meal plan UI (can be replaced with dynamic meal data)
        tk.Label(self, text="Breakfast: Oats with banana\nLunch: Grilled chicken salad\nDinner: Steamed fish & veggies",
                 font=("Arial", 11), justify="left").pack(pady=15)

        # 🔙 Back Button
        tk.Button(self, text="← Back to Menu", command=self.go_back).pack(pady=20)

    def go_back(self):
        from screens.menu_screen import MenuScreen  # ✅ Delayed import avoids circular dependencies
        self.master.switch_frame(MenuScreen)
