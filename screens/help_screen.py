import tkinter as tk
from tkinter import messagebox

class HelpScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        tk.Label(self, text="📞 Contact Us / Help", font=("Arial", 20, "bold")).pack(pady=20)

        # Info
        tk.Label(self, text="Need help or have questions about CoreBoost?\nFill out the form below or contact us:", justify="center").pack(pady=10)
        tk.Label(self, text="Email: support@coreboostapp.com").pack()
        tk.Label(self, text="Phone: +27 61 234 5678").pack(pady=(0, 20))

        # Feedback Form
        self.name_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.message_text = tk.Text(self, height=5, width=40)

        self._build_form()

        tk.Button(self, text="Submit", command=self.submit_form).pack(pady=10)
        tk.Button(self, text="Back to Menu", command=self.go_back).pack(pady=5)

    def _build_form(self):
        tk.Label(self, text="Your Name:").pack(anchor="w", padx=40)
        tk.Entry(self, textvariable=self.name_var).pack(padx=40, fill="x")

        tk.Label(self, text="Your Email:").pack(anchor="w", padx=40, pady=(10, 0))
        tk.Entry(self, textvariable=self.email_var).pack(padx=40, fill="x")

        tk.Label(self, text="Your Message:").pack(anchor="w", padx=40, pady=(10, 0))
        self.message_text.pack(padx=40, pady=(0, 10))

    def submit_form(self):
        name = self.name_var.get()
        email = self.email_var.get()
        message = self.message_text.get("1.0", "end").strip()

        if not name or not email or not message:
            messagebox.showwarning("Incomplete Form", "Please fill in all fields.")
            return

        # Placeholder for email sending logic
        print(f"[HELP FORM SUBMITTED]\nName: {name}\nEmail: {email}\nMessage: {message}")
        messagebox.showinfo("Submitted", "Thank you for contacting us. We'll get back to you soon!")
        self.clear_form()

    def clear_form(self):
        self.name_var.set("")
        self.email_var.set("")
        self.message_text.delete("1.0", "end")

    def go_back(self):
        from .menu_screen import MenuScreen
        self.master.switch_frame(lambda master: MenuScreen(master, ""))
