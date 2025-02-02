import tkinter as tk

def show_text():
    entered_text = entry_field.get()
    label.config(text=entered_text)

# main window
window = tk.Tk()
window.title("Tkinter GUI")
window.geometry("300x200")

entry_field = tk.Entry(window, width=25)
entry_field.pack(pady=10)

button = tk.Button(window, text="Show", command=show_text)
button.pack()
label = tk.Label(window, text="Text will appear here", font=("Arial", 12))
label.pack(pady=10)

def clear_text():
    entry_field.delete(0, tk.END)  # Entry alanını temizle
    label.config(text="Text will appear here")  # Etiketi sıfırla

# Clear Button
clear_button = tk.Button(window, text="Clear", command=clear_text)
clear_button.pack(pady=5)



window.mainloop()
