import tkinter as tk

def display_text():
    enter_text=.get()
    ticket.config(text=enter_text)

window=tk.Tk();
window.title("Interface")
window.geometry("300x200")

# Buton
buton = tk.Button(window, text="Göster", command=display_text)
buton.pack()

# Etiket
tag = tk.Label(window, text="Burada gözükecek", font=("Arial", 12))
tag.pack(pady=10)

window.mainloop()