import tkinter as tk
from src.config.config import APP_TITLE, WINDOW_SIZE

def create_gui():
    window = tk.Tk()
    window.title(APP_TITLE)
    window.geometry(WINDOW_SIZE)
    window.mainloop()
