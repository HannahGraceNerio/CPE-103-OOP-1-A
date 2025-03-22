import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showinfo

# Creating tkinter window and set dimensions
window = tk.Tk()
window.title('Combobox')
window.geometry('500x250')
window.configure(bg="azure")


def choice(event):
    month = event.widget.get()
    print("Your birth month", month)

def choice(event):
    day = event.widget.get()
    print("Your birth date", day)

def choice(event):
    year = event.widget.get()
    print("Your birth year", year)

ttk.Label(window, text="Choose your birth day",
          background='light pink', foreground="black",
          font=("Times New Roman", 15)).grid(row=0, column=1)

# Set label
ttk.Label(window, text="Select the month of your birth :",
          font=("Times New Roman", 12)).grid(column=0,
                                             row=5, padx=5, pady=25)

ttk.Label(window, text="Select the day of your birth :",
          font=("Times New Roman", 12)).grid(column=0,
                                             row=6, padx=5, pady=25)

ttk.Label(window, text="Select the year of your birth :",
          font=("Times New Roman", 12)).grid(column=0,
                                             row=7, padx=5, pady=25)

# Create Combobox
n = tk.StringVar()
m = tk.StringVar()
o = tk.StringVar()

month = ttk.Combobox(window, width=27, textvariable=n)
day = ttk.Combobox(window, width=27, textvariable=m)
year = ttk.Combobox(window, width=27, textvariable=o)

# Adding combobox drop down list
month['values'] = (' January',
                     ' February',
                     ' March',
                     ' April',
                     ' May',
                     ' June',
                     ' July',
                     ' August',
                     'September',
                     'October',
                     'November',
                     'December')
day ['values'] = ('1','2','3','4','5','6','7','8','9','10',
                  '11','12','13','14','15','16','17','18','19','20',
                  '21','22','23','24','25','26','27','28','29','30')

year['values'] = ('2000','2001', '2002','2003','2004','2005','2006','2007',
                  '2008','2009','2010','2011','2012','2013','2014','2015',
                  '2016','2017','2018','2019','2020','2021','2022','2023')

month.grid(column=1, row=5)
month.current()

day.grid(column=1, row=6)
day.current()

year.grid(column=1, row=7)
year.current()

gender_label = ttk.Label(window, text="Select your gender:", font=("Times New Roman", 12))
gender_label.grid(row=8, column=0, padx=5, pady=25, sticky="w")

gender_var = tk.StringVar() # Default value
male_radio = ttk.Radiobutton(window, text="Male", variable=gender_var, value="Male")
female_radio = ttk.Radiobutton(window, text="Female", variable=gender_var, value="Female")
other_radio = ttk.Radiobutton(window, text="Other", variable=gender_var, value="Other")

male_radio.grid(row=8, column=1, padx=5, sticky="w")
female_radio.grid(row=8, column=2, padx=5, sticky="w")
other_radio.grid(row=8, column=3, padx=5, sticky="w")

# Listbox for selecting favorite colors
color_label = ttk.Label(window, text="Select your favorite color(s):", font=("Times New Roman", 12))
color_label.grid(row=12, column=0, padx=5, pady=25, sticky="w")

color_listbox = tk.Listbox(window, selectmode=tk.MULTIPLE, height=5, width=27)
color_listbox.insert(1, "Red")
color_listbox.insert(2, "Blue")
color_listbox.insert(3, "Green")
color_listbox.insert(4, "Yellow")
color_listbox.insert(5, "Purple")
color_listbox.grid(row=12, column=1)

# Check Button for accepting terms and conditions
terms_var = tk.BooleanVar()
terms_check = ttk.Checkbutton(window, text="I accept the terms and conditions", variable=terms_var)
terms_check.grid(row=13, column=1, padx=5, pady=25, sticky="w")


def show_choice():
    selected_month = n.get()
    selected_day = m.get()
    selected_year = o.get()
    selected_gender = gender_var.get()

    selected_colors = [color_listbox.get(i) for i in color_listbox.curselection()]
    terms_accepted = "Accepted" if terms_var.get() else "Not Accepted"

    message = (f'You selected: {selected_month} {selected_day}, {selected_year}\n'
               f'Gender: {selected_gender}\n'
               f'Favorite Color(s): {", ".join(selected_colors) if selected_colors else "None"}\n'
               f'Terms and Conditions: {terms_accepted}')

    showinfo(title="Selection", message=message)


# Button to confirm the selection
ttk.Button(window, text="Confirm Selection", command=show_choice).grid(row=14, column=1, pady=20)
window.mainloop()