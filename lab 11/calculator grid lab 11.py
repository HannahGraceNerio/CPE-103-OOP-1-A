import tkinter as tk
from tkinter import messagebox

def click(value):
    if value == '=':
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            messagebox.showerror("Error", "Invalid Expression")
    elif value == 'C':
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, value)

root = tk.Tk()
root.title("Calculator")
root.geometry("500x600")
root.configure(bg="light blue")


entry = tk.Entry(root, font=("Arial", 24), bd=20, justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

# Buttons layout as in the picture
buttons = [
    ('C', 1, 0, 4),
    ('7', 2, 0, 1), ('8', 2, 1, 1), ('9', 2, 2, 1), ('/', 2, 3, 1),
    ('4', 3, 0, 1), ('5', 3, 1, 1), ('6', 3, 2, 1), ('*', 3, 3, 1),
    ('1', 4, 0, 1), ('2', 4, 1, 1), ('3', 4, 2, 1), ('-', 4, 3, 1),
    ('0', 5, 0, 2), ('.', 5, 2, 1), ('+', 5, 3, 1),
    ('=', 6, 0 , 4)
]

for (text, row, col, colspan) in buttons:
    tk.Button(root, text=text, font=("Arial", 18), width=5, height=2,
              command=lambda val=text: click(val), bg="white").grid(
              row=row, column=col, columnspan=colspan, padx=5, pady=5, sticky='nsew')

# Expand grid cells
for i in range(7):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()
