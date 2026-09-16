import tkinter as tk

root = tk.Tk()

def hello():
    print("Button clicked")

button = tk.Button(
    root,
    text="Click Me",
    command=hello
)

button.pack()

root.mainloop() 