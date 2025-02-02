import tkinter as tk

def show_text():
    entered_text = entry_field.get()
    label.config(text=entered_text)

# Create main window
window = tk.Tk()
window.title("Tkinter GUI")
window.geometry("300x200")

# Entry field
entry_field = tk.Entry(window, width=25)
entry_field.pack(pady=10)

# Button
button = tk.Button(window, text="Show", command=show_text)
button.pack()

# Label
label = tk.Label(window, text="Text will appear here", font=("Arial", 12))
label.pack(pady=10)

# Run the window
window.mainloop()
