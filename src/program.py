import tkinter as tk

def show_text():
    entered_text = entry_field.get()
    label.config(text=entered_text)

def clear_text():
    entry_field.delete(0, tk.END)  # Clear the entry field
    label.config(text="Text will appear here")  # Reset label

# Create main window
window = tk.Tk()
window.title("Tkinter GUI")
window.configure(bg="#f0f0f0")  # Set background color

# Window size
window_width = 300
window_height = 250

# Get screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate position (center of screen)
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

# Set window size and position
window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Entry field with default text
entry_field = tk.Entry(window, width=25, fg="gray")
entry_field.insert(0, "Enter text here...")  # Default text
entry_field.pack(pady=10)

# Show Button
button = tk.Button(window, text="Show", command=show_text, bg="#4CAF50", fg="white")
button.pack(pady=5)

# Clear Button
clear_button = tk.Button(window, text="Clear", command=clear_text, bg="#f44336", fg="white")
clear_button.pack(pady=5)

# Label
label = tk.Label(window, text="Text will appear here", font=("Arial", 12), bg="#f0f0f0")
label.pack(pady=10)

# Run the window
window.mainloop()
