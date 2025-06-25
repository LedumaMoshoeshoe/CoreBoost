import tkinter as tk
from tkinter import messagebox
import os
from PIL import Image, ImageTk

class RegistrationScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        # Load and display background image
        bg_path = os.path.join("assets", "background", "CoreBoostLogoo.png")
        bg_image = Image.open(bg_path).resize((master.winfo_screenwidth(), master.winfo_screenheight()))
        self.bg_photo = ImageTk.PhotoImage(bg_image)

        bg_label = tk.Label(self, image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # White card frame centered with fixed size
        self.card = tk.Frame(self, bg="white", bd=0, highlightthickness=0, width=400, height=450)
        self.card.place(relx=0.5, rely=0.5, anchor="center")

        # Title label
        tk.Label(self.card, text="Register New User", font=("Arial", 18, "bold"), bg="white").pack(pady=(20, 15))

        # Username
        tk.Label(self.card, text="Username:", bg="white", anchor="w", font=("Arial", 10)).pack(fill="x", padx=30)
        self.username_entry = tk.Entry(self.card, font=("Arial", 10))
        self.username_entry.pack(padx=30, fill="x", pady=(0, 10))

        # Email
        tk.Label(self.card, text="Email:", bg="white", anchor="w", font=("Arial", 10)).pack(fill="x", padx=30)
        self.email_entry = tk.Entry(self.card, font=("Arial", 10))
        self.email_entry.pack(padx=30, fill="x", pady=(0, 10))

        # Password
        tk.Label(self.card, text="Password:", bg="white", anchor="w", font=("Arial", 10)).pack(fill="x", padx=30)
        self.password_entry = tk.Entry(self.card, show="*", font=("Arial", 10))
        self.password_entry.pack(padx=30, fill="x", pady=(0, 10))

        # Confirm Password
        tk.Label(self.card, text="Confirm Password:", bg="white", anchor="w", font=("Arial", 10)).pack(fill="x", padx=30)
        self.confirm_password_entry = tk.Entry(self.card, show="*", font=("Arial", 10))
        self.confirm_password_entry.pack(padx=30, fill="x", pady=(0, 20))

        # Register button
        tk.Button(self.card, text="Register", font=("Arial", 11, "bold"), bg="#4CAF50", fg="white",
                  relief="flat", command=self.register_user).pack(pady=(0, 10), ipadx=10, ipady=5)

        # Back to login button
        tk.Button(self.card, text="Back to Login", font=("Arial", 10), bg="#f0f0f0", fg="#333",
                  relief="flat", command=self.back_to_login).pack(ipadx=10, ipady=5)

    def register_user(self):
        from utils import user_store
        username = self.username_entry.get().strip()
        email = self.email_entry.get().strip()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

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

    def back_to_login(self):
        from .login_screen import LoginScreen
        self.master.switch_frame(LoginScreen)
