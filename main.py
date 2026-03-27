import tkinter as tk
from tkinter import font
from tkinter import ttk
from dataframe import spendings, generate, initialize, categories


class Field:
    def __init__(self, window, texto, row, options=None):
        self.label = tk.Label(window, text=texto)
        self.label.grid(row=row, column=0, padx=10, pady=10)

        if options:
            self.input = ttk.Combobox(window, values=options)
        else:
            self.input = tk.Entry(window)

        self.input.grid(row=row, column=1, padx=10, pady=10)

initialize()


root = tk.Tk()
root.title("Spending Table")
root.geometry("1000x600")
root.resizable(False, False)

font.Font(family="Helvetica", size=25)
root.option_add("*Font", "Helvetica 25")
root.configure(bg="#f0f0f0")

style = ttk.Style()
style.theme_use("clam")
style.configure("TButton",relief="flat" ,background="#4CAF50", foreground="white", font="Helvetica 25", padding=6)

style.configure("TLabel", font="Helvetica 25")
style.configure("TEntry", font="Helvetica 25")

Category = Field(root, "Category", 0, options=categories)
Category.label.grid(row=0, column=0, padx=10, pady=10)
Category.input.grid(row=0, column=1, padx=10, pady=10)

Description = Field(root, "Description", 1)
Description.label.grid(row=1, column=0, padx=10, pady=10)
Description.input.grid(row=1, column=1, padx=10, pady=10)

Value = Field(root, "Value", 2)
Value.label.grid(row=2, column=0, padx=10, pady=10)
Value.input.grid(row=2, column=1, padx=10, pady=10)

Add = tk.Button(
    root,
    text="Add",
    command=lambda: spendings(
        Value.input,
        Category.input,
        Description.input
    )
)

Generate = tk.Button(root, text="Generate Data", command=generate)

Add.grid(row=3, column=0, padx=10, pady=10)
Generate.grid(row=3, column=1, padx=10, pady=10)

root.mainloop()



