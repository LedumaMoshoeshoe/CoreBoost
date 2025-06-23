import tkinter as tk

class MeditationScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        tk.Label(self, text="🧘 Stretch & Meditation", font=("Arial", 20)).pack(pady=20)
        tk.Label(self, text="Relax your body and mind.", font=("Arial", 12)).pack(pady=10)

        # TODO: Add meditation/stretching routines here

        tk.Button(self, text="← Back to Menu", command=self.go_back).pack(pady=20)

    def go_back(self):
        from screens.menu_screen import MenuScreen  # ✅ Local import to avoid circular import
        self.master.switch_frame(MenuScreen)
