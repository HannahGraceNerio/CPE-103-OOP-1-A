# Simple TUI Calculator

import tkinter as tk
from tkinter import messagebox
import math

def validate_input(value):
    try:
        return float(value)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number")
        return None

def add():
    num1 = validate_input(entry1.get())
    num2 = validate_input(entry2.get())
    if num1 is not None and num2 is not None:
        result.set(num1 + num2)
        update_history(f"{num1} + {num2} = {num1 + num2}")

def subtract():
    num1 = validate_input(entry1.get())
    num2 = validate_input(entry2.get())
    if num1 is not None and num2 is not None:
        result.set(num1 - num2)
        update_history(f"{num1} - {num2} = {num1 - num2}")

def multiply():
    num1 = validate_input(entry1.get())
    num2 = validate_input(entry2.get())
    if num1 is not None and num2 is not None:
        result.set(num1 * num2)
        update_history(f"{num1} × {num2} = {num1 * num2}")

def divide():
    num1 = validate_input(entry1.get())
    num2 = validate_input(entry2.get())
    if num1 is not None and num2 is not None:
        if num2 == 0:
            result.set("Error! Division by zero.")
            messagebox.showerror("Math Error", "Cannot divide by zero.")
        else:
            result.set(num1 / num2)
            update_history(f"{num1} ÷ {num2} = {num1 / num2}")

def power():
    num1 = validate_input(entry1.get())
    num2 = validate_input(entry2.get())
    if num1 is not None and num2 is not None:
        result.set(num1 ** num2)
        update_history(f"{num1} ^ {num2} = {num1 ** num2}")

def sqrt():
    num1 = validate_input(entry1.get())
    if num1 is not None:
        if num1 < 0:
            result.set("Error! Negative sqrt.")
            messagebox.showerror("Math Error", "Cannot calculate square root of a negative number.")
        else:
            result.set(math.sqrt(num1))
            update_history(f"√{num1} = {math.sqrt(num1)}")

def clear ():
    entry1.delete(0,'end')
    entry2.delete(0,'end')
    result.set("")

history = []

def update_history (operation):
    history.append(operation)
    history_Label.config(text="History:\n" + "\n" .join(history))


# Create the main window
root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("400x500")
root.configure(bg="silver")

result = tk.StringVar ()
font_style = ("Arial", 12)

# Create the layout
tk.Label(root, text="Enter first number:", bg="azure").grid(row=0, column=0),
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Enter second number:", bg="azure").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

# Buttons for operations
tk.Button(root, text="Add", command=add, bg="azure").grid(row=3, column=0)
tk.Button(root, text="Subtract", command=subtract, bg="azure").grid(row=3, column=1)
tk.Button(root, text="Multiply", command=multiply, bg="azure").grid(row=4, column=0)
tk.Button(root, text="Divide", command=divide, bg="azure").grid(row=4, column=1)
tk.Button(root, text='Clear', command=clear, bg="azure").grid(row=5, column=2)
tk.Button(root, text="power", command=power, bg="azure").grid(row=5, column=0)
tk.Button(root, text="sqrt", command=sqrt, bg="azure").grid(row=5, column=1)

# Label to show result
tk.Label(root, text="Result:", bg="azure").grid(row=6, column=0)
result_label = tk.Label(root, textvariable=result, width=20, height=1, bg="azure")
result_label.grid(row=7, column=1)


history_Label = tk.Label(root, text="History:\n", justify="left", bg="azure")
history_Label.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

# Start the main loop
root.mainloop()

