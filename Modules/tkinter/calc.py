import tkinter as tk

def add():
    a = float(first.get())
    b = float(second.get())

    result.config(text=f"Result: {a + b}")


root = tk.Tk()

root.title("Calculator")

tk.Label(root, text="First Number").grid(
    row=0,
    column=0,
    padx=10,
    pady=10
)

first = tk.Entry(root)
first.grid(row=0, column=1)

tk.Label(root, text="Second Number").grid(
    row=1,
    column=0,
    padx=10,
    pady=10
)

second = tk.Entry(root)
second.grid(row=1, column=1)

tk.Button(
    root,
    text="Add",
    command=add
).grid(
    row=2,
    column=0,
    columnspan=2
)

result = tk.Label(root, text="Result:")
result.grid(
    row=3,
    column=0,
    columnspan=2
)

root.mainloop()