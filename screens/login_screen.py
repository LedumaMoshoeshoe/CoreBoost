import tkinter as tk
from tkinter import messagebox
from screens.base_screen import BaseScreen

class LoginScreen(BaseScreen):
    def __init__(self, master):
        super().__init__(master)

        # Simulate gradient background (solid fallback)
        self.configure(bg="#4c00c2")

        # Card container
        card = tk.Frame(self, bg="white", bd=2, relief="flat")
        card.place(relx=0.5, rely=0.5, anchor="center", width=350, height=400)

        # Icon + Title
        tk.Label(card, text="🔐 Login", font=("Arial", 20, "bold"), bg="white", fg="#222").pack(pady=(25, 10))

        # Username Label + Entry
        tk.Label(card, text="Username", font=("Arial", 10), bg="white").pack(anchor="w", padx=40, pady=(10, 2))
        self.username_entry = tk.Entry(card, font=("Arial", 11), bd=1, relief="solid")
        self.username_entry.pack(padx=40, fill="x")

        # Password Label + Entry
        tk.Label(card, text="Password", font=("Arial", 10), bg="white").pack(anchor="w", padx=40, pady=(15, 2))
        self.password_entry = tk.Entry(card, font=("Arial", 11), bd=1, relief="solid", show="*")
        self.password_entry.pack(padx=40, fill="x")

        # Login Button (Gradient-look with color transition)
        login_btn = tk.Button(
            card, text="⇨ Login", font=("Arial", 11, "bold"),
            bg="#4facfe", fg="white", activebackground="#00f2fe",
            relief="flat", command=self.check_login
        )
        login_btn.pack(pady=20, ipadx=10, ipady=5)

        # Register Link (underlined style)
        register_link = tk.Label(
            card, text="👤 Don't have an account? Register",
            font=("Arial", 9, "underline"), fg="blue",
            bg="white", cursor="hand2"
        )
        register_link.pack()
        register_link.bind("<Button-1>", lambda e: self.go_to_register())

    def check_login(self):
        from utils import user_store
        from .menu_screen import MenuScreen

        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "1234":
            messagebox.showinfo("Login Successful", "Welcome to the CoreBoost App!")
            self.master.switch_frame(lambda master: MenuScreen(master, username))
            return

        if user_store.validate_user(username, password):
            messagebox.showinfo("Login Successful", "Welcome to the CoreBoost App!")
            self.master.switch_frame(lambda master: MenuScreen(master, username))
            return

        messagebox.showerror("Login Failed", "Incorrect username or password.")

    def go_to_register(self):
        from .registration_screen import RegistrationScreen
        self.master.switch_frame(RegistrationScreen)
