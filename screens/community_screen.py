import tkinter as tk

class CommunityScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        tk.Label(self, text="🌍 Join the Community", font=("Arial", 20)).pack(pady=20)
        tk.Label(self, text="Connect, share, and grow with others!", font=("Arial", 12)).pack(pady=10)

        # TODO: Add social features, chat links, or community forum integrations

        tk.Button(self, text="← Back to Menu", command=self.go_back).pack(pady=20)

    def go_back(self):
        from screens.menu_screen import MenuScreen  # ✅ Local import to avoid circular import
        self.master.switch_frame(MenuScreen)
