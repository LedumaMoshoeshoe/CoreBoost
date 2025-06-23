import tkinter as tk
from tkinter import messagebox

class LoginScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        tk.Label(self, text="CoreBoost Login", font=("Arial", 24)).pack(pady=20)

        tk.Label(self, text="Username").pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        tk.Label(self, text="Password").pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        tk.Button(self, text="Login", command=self.check_login).pack(pady=10)

    def check_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        from screens.menu_screen import MenuScreen
        self.master.switch_frame(MenuScreen)
        
        if username == "admin" and password == "1234":
            self.master.switch_frame(MenuScreen)
        else:
            messagebox.showerror("Login Failed", "Incorrect username or password.")
