import tkinter as tk
import config

def show_text(entry_field, label):
    entered_text = entry_field.get()
    label.config(text=entered_text)

def clear_text(entry_field, label):
    entry_field.delete(0, tk.END)
    label.config(text="Text will appear here")

def save_text(entry_field):
    with open(config.SAVE_FILE, "w") as file:
        file.write(entry_field.get())

def load_text(entry_field):
    try:
        with open(config.SAVE_FILE, "r") as file:
            content = file.read()
            entry_field.delete(0, tk.END)
            entry_field.insert(0, content)
    except FileNotFoundError:
        pass
