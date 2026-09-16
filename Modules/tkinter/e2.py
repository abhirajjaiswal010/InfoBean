import tkinter as tk

root = tk.Tk()

# label = tk.Label(root, text="Hello Abhiraj")
label = tk.Label(
    root,
    text="Hello",
    font=("Arial", 20),
    fg="blue"
)

label.pack()

root.mainloop()