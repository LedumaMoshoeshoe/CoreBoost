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
        tk.Button(self, text="Register", command=self.go_to_register).pack()

    def check_login(self):
        from utils import user_store
        from .menu_screen import MenuScreen

        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check if user is admin (hardcoded login)
        if username == "admin" and password == "1234":
            messagebox.showinfo("Login Successful", "Welcome to the CoreBoost App!")
            self.master.switch_frame(lambda master: MenuScreen(master, username))
            return

        # Check if user is in JSON store
        if user_store.validate_user(username, password):
            messagebox.showinfo("Login Successful", "Welcome to the CoreBoost App!")
            self.master.switch_frame(lambda master: MenuScreen(master, username))
            return

        # If both checks fail
        messagebox.showerror("Login Failed", "Incorrect username or password.")

    def go_to_register(self):
        from .registration_screen import RegistrationScreen
        self.master.switch_frame(RegistrationScreen)
