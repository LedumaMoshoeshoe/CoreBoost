import tkinter as tk
from PIL import Image, ImageTk
import os

class BaseScreen(tk.Frame):
    def __init__(self, master, bg_path="assets/background/coreboostlogo.png"):
        super().__init__(master)
        self.master = master

        # Load and display the background image
        bg_image = Image.open(bg_path)
        bg_image = bg_image.resize((master.winfo_screenwidth(), master.winfo_screenheight()))
        self.bg_photo = ImageTk.PhotoImage(bg_image)

        self.bg_label = tk.Label(self, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
