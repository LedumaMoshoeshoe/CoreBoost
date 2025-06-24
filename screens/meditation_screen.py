import tkinter as tk

class MeditationScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        tk.Label(self, text="🧘 Stretch & Meditation", font=("Arial", 20, "bold")).pack(pady=20)
        tk.Label(self, text="Relax your body and mind.", font=("Arial", 12)).pack(pady=10)

        # Placeholder section for routines
        routine_list = [
            "1. Morning breathing meditation - 5 min",
            "2. Upper body stretch (shoulders & arms) - 7 min",
            "3. Guided mindful cooldown - 10 min"
        ]

        for routine in routine_list:
            tk.Label(self, text=routine, font=("Arial", 11), anchor="w", justify="left").pack(pady=2)

        # 🔙 Back Button
        tk.Button(self, text="← Back to Menu", command=self.go_back).pack(pady=20)

    def go_back(self):
        from screens.menu_screen import MenuScreen  # ✅ Local import to avoid circular import
        self.master.switch_frame(MenuScreen)
