# gui.py
import tkinter as tk
import config
import functions

def create_gui():
    # Create main window
    window = tk.Tk()
    window.title("Advanced Tkinter App")
    window.configure(bg=config.BG_COLOR)

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_position = (screen_width - config.WINDOW_WIDTH) // 2
    y_position = (screen_height - config.WINDOW_HEIGHT) // 2
    window.geometry(f"{config.WINDOW_WIDTH}x{config.WINDOW_HEIGHT}+{x_position}+{y_position}")

    entry_field = tk.Entry(window, width=40, fg="black")
    entry_field.pack(pady=10)

    button_show = tk.Button(window, text="Show", command=lambda: functions.show_text(entry_field, label), bg="#4CAF50", fg="white")
    button_show.pack(pady=5)

    button_clear = tk.Button(window, text="Clear", command=lambda: functions.clear_text(entry_field, label), bg="#f44336", fg="white")
    button_clear.pack(pady=5)

    button_save = tk.Button(window, text="Save", command=lambda: functions.save_text(entry_field), bg="#008CBA", fg="white")
    button_save.pack(pady=5)

    button_load = tk.Button(window, text="Load", command=lambda: functions.load_text(entry_field), bg="#FF9800", fg="white")
    button_load.pack(pady=5)

    label = tk.Label(window, text="Text will appear here", font=("Arial", 12), bg=config.BG_COLOR)
    label.pack(pady=10)

    # run window
    window.mainloop()
