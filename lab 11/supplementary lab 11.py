import tkinter as tk
from tkinter import messagebox
import math

def click(value):
    current = entry.get()
    if value == '=':
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            messagebox.showerror("Error", "Invalid Expression")
    elif value == 'C':
        entry.delete(0, tk.END)
    elif value == 'DEL':
        entry.delete(len(current)-1, tk.END)
    elif value == 'sin':
        try:
            result = math.sin(math.radians(float(current)))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            messagebox.showerror("Error", "Invalid input for sin()")
    elif value == 'cos':
        try:
            result = math.cos(math.radians(float(current)))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            messagebox.showerror("Error", "Invalid input for cos()")
    elif value == 'tan':
        try:
            result = math.tan(math.radians(float(current)))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            messagebox.showerror("Error", "Invalid input for tan()")
    elif value == '^':
        entry.insert(tk.END, '**')
    elif value == '√':
        try:
            result = math.sqrt(float(current))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            messagebox.showerror("Error", "Invalid input for sqrt()")
    elif value == '±':
        if current:
            if current.startswith('-'):
                entry.delete(0, 1)
            else:
                entry.insert(0, '-')
    else:
        entry.insert(tk.END, value)

root = tk.Tk()
root.title("Scientific Calculator")
root.configure(bg="lightblue")

entry = tk.Entry(root, font=("Arial", 24, "bold"), bd=5, relief=tk.RIDGE, justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

buttons = [
    ('sin', 1, 0), ('cos', 1, 1), ('tan', 1, 2), ('√', 1, 3),
    ('(', 2, 0), (')', 2, 1), ('^', 2, 2), ('%', 2, 3),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('+', 3, 3),
    ('4', 4, 0), ('5', 4, 1), ('6', 4, 2), ('-', 4, 3),
    ('1', 5, 0), ('2', 5, 1), ('3', 5, 2), ('*', 5, 3),
    ('C', 6, 0), ('0', 6, 1), ('.', 6, 2), ('/', 6, 3),
    ('DEL', 7, 0), ('±', 7, 1), ('=', 7, 2, 2),
]

for btn in buttons:
    text = btn[0]
    row = btn[1]
    col = btn[2]
    colspan = btn[3] if len(btn) == 4 else 1

    bg_color = "azure"
    fg_color = "black"

    if text == 'C':
        bg_color = "azure"
        fg_color = "black"
    elif text == '=':
        bg_color = "light blue"
        fg_color = "black"
    elif text in ['+', '-', '*', '/', '^', '√', '%']:
        bg_color = "azure"
        fg_color = "black"
    elif text in ['sin', 'cos', 'tan', '(', ')']:
        bg_color = "azure"
        fg_color = "black"
    elif text in ['DEL', '±']:
        bg_color = "azure"
        fg_color = "black"

    btn_widget = tk.Button(root, text=text, font=("Arial", 18, "bold"),
                           bg=bg_color, fg=fg_color,
                           command=lambda val=text: click(val))
    btn_widget.grid(row=row, column=col, columnspan=colspan, padx=5, pady=5, sticky="nsew")

for i in range(8):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()