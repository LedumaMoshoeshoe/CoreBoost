import tkinter as tk

class DietScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        tk.Label(self, text="🍎 Diet Plan", font=("Arial", 20)).pack(pady=20)
        tk.Label(self, text="Here you will find your personalized meal plans.", font=("Arial", 12)).pack(pady=10)

        # 🔙 Back Button with delayed import
        tk.Button(self, text="← Back to Menu", command=self.go_back).pack(pady=20)

    def go_back(self):
        from screens.menu_screen import MenuScreen  # ✅ Local import
        self.master.switch_frame(MenuScreen)