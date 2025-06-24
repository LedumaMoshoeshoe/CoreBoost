import tkinter as tk
from tkinter import messagebox

class RegistrationScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        tk.Label(self, text="Register New User", font=("Arial", 18)).pack(pady=20)

        tk.Label(self, text="Username:").pack(anchor="w", padx=20)
        self.username_entry = tk.Entry(self)
        self.username_entry.pack(padx=20, fill="x")

        tk.Label(self, text="Email:").pack(anchor="w", padx=20, pady=(10,0))
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(padx=20, fill="x")

        tk.Label(self, text="Password:").pack(anchor="w", padx=20, pady=(10,0))
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack(padx=20, fill="x")

        tk.Label(self, text="Confirm Password:").pack(anchor="w", padx=20, pady=(10,0))
        self.confirm_password_entry = tk.Entry(self, show="*")
        self.confirm_password_entry.pack(padx=20, fill="x")

        tk.Button(self, text="Register", command=self.register_user).pack(pady=20)
        tk.Button(self, text="Back to Login", command=self.back_to_login).pack()

    def register_user(self):
        from utils import user_store
        username = self.username_entry.get().strip()
        email = self.email_entry.get().strip()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        # Basic validation example
        if not username or not email or not password:
            messagebox.showwarning("Input Error", "Please fill in all fields.")
            return

        if password != confirm_password:
            messagebox.showwarning("Password Error", "Passwords do not match.")
            return
        
        success = user_store.add_user(username, email, password)
        if not success:
            messagebox.showerror("Error", "Username already exists.")
            return
        
        messagebox.showinfo("Success", "User registered successfully!")

        from .login_screen import LoginScreen
        self.master.switch_frame(LoginScreen)

        # Placeholder for actual registration logic (e.g., save to DB)
        print(f"Registered user: {username}, {email}")

        messagebox.showinfo("Success", "User registered successfully!")

        # Delayed import to avoid circular import
        from .login_screen import LoginScreen
        self.master.switch_frame(LoginScreen)

    def back_to_login(self):
        from .login_screen import LoginScreen
        self.master.switch_frame(LoginScreen)
