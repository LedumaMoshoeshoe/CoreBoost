import tkinter as tk
from tkinter import messagebox
from screens.base_screen import BaseScreen

class HelpScreen(BaseScreen):
    def __init__(self, master):
        super().__init__(master)

        # 🧾 Content box
        content = tk.Frame(self, bg="#ffffff", bd=2, relief="ridge")
        content.place(relx=0.5, rely=0.5, anchor="center", width=600, height=500)

        # 🧠 Header
        tk.Label(content, text="📞 Contact Us / Help", font=("Helvetica", 22, "bold"),
                 bg="#ffffff", fg="#333333").pack(pady=(20, 10))

        # 💬 Info
        tk.Label(content, text="Need help or have questions about CoreBoost?",
                 font=("Helvetica", 12), bg="#ffffff", fg="#666").pack()
        tk.Label(content, text="Fill out the form below or contact us:", font=("Helvetica", 11),
                 bg="#ffffff", fg="#666").pack(pady=(0, 10))

        tk.Label(content, text="📧 support@coreboostapp.com", font=("Helvetica", 10),
                 bg="#ffffff", fg="#444").pack()
        tk.Label(content, text="📱 +27 61 234 5678", font=("Helvetica", 10),
                 bg="#ffffff", fg="#444").pack(pady=(0, 20))

        # 🎯 Form variables
        self.name_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.message_text = tk.Text(content, height=5, width=50, font=("Helvetica", 10), relief="solid", bd=1)

        # 📝 Form Layout
        self._build_form(content)

        # 📩 Submit Button
        tk.Button(content, text="✉️ Submit", width=20, bg="#4CAF50", fg="white", font=("Helvetica", 10, "bold"),
                  relief="flat", command=self.submit_form).pack(pady=(10, 5))

        # 🔙 Back
        tk.Button(content, text="← Back to Menu", bg="#2196F3", fg="white", relief="flat",
                  command=self.go_back).pack()

    def _build_form(self, parent):
        form_padding = {"padx": 30, "anchor": "w", "bg": "#ffffff", "font": ("Helvetica", 10, "bold")}

        tk.Label(parent, text="Your Name:", **form_padding).pack()
        tk.Entry(parent, textvariable=self.name_var, font=("Helvetica", 10), relief="solid", bd=1).pack(padx=30, fill="x")

        tk.Label(parent, text="Your Email:", **form_padding).pack(pady=(10, 0))
        tk.Entry(parent, textvariable=self.email_var, font=("Helvetica", 10), relief="solid", bd=1).pack(padx=30, fill="x")

        tk.Label(parent, text="Your Message:", **form_padding).pack(pady=(10, 0))
        self.message_text.pack(padx=30, pady=(0, 10))

    def submit_form(self):
        name = self.name_var.get()
        email = self.email_var.get()
        message = self.message_text.get("1.0", "end").strip()

        if not name or not email or not message:
            messagebox.showwarning("⚠️ Incomplete Form", "Please fill in all fields.")
            return

        print(f"[HELP FORM SUBMITTED]\nName: {name}\nEmail: {email}\nMessage: {message}")
        messagebox.showinfo("✅ Submitted", "Thanks for reaching out. We'll respond shortly!")
        self.clear_form()

    def clear_form(self):
        self.name_var.set("")
        self.email_var.set("")
        self.message_text.delete("1.0", "end")

    def go_back(self):
        from .menu_screen import MenuScreen
        self.master.switch_frame(lambda master: MenuScreen(master, ""))
