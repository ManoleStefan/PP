
import tkinter as tk
from tkinter import ttk

def getText(window):
    input =
window = tk.Tk()

window.title("Python Tkinter Text Box")
window.minsize(600, 400)


label = ttk.Label(window, text="Companie")
label.grid(column=0, row=0)

name = tk.StringVar()
nameEntered = ttk.Entry(window, width=15, textvariable=name)
nameEntered.grid(column=0, row=1)

label = ttk.Label(window, text="Departament")
label.grid(column=1, row=0)

name = tk.StringVar()
nameEntered = ttk.Entry(window, width=15, textvariable=name)
nameEntered.grid(column=1, row=1)

label = ttk.Label(window, text="Nume")
label.grid(column=2, row=0)

name = tk.StringVar()
nameEntered = ttk.Entry(window, width=15, textvariable=name)
nameEntered.grid(column=2, row=1)

label = ttk.Label(window, text="Ziua nasterii")
label.grid(column=3, row=0)

name = [i for i in range(1,32)]
nameEntered = ttk.Combobox(window, width=15, values=name)
nameEntered.grid(column=3, row=1)

label = ttk.Label(window, text="Luna nasterii")
label.grid(column=4, row=0)

name = ["Jan","Feb","Mar","Apr","May","Jun","July","Aug","Sept","Oct","Nov","Dec"]
nameEntered = ttk.Combobox(window, width=15, values=name)
nameEntered.grid(column=4, row=1)


label = ttk.Label(window, text="Anul nasterii")
label.grid(column=5, row=0)

name = [i for i in range(1900,2010)]
nameEntered = ttk.Combobox(window, width=15, values=name)
nameEntered.grid(column=5, row=1)

label = ttk.Label(window, text="Functie")
label.grid(column=6, row=0)

name = tk.StringVar()
nameEntered = ttk.Entry(window, width=15, textvariable=name)
nameEntered.grid(column=6, row=1)

label = ttk.Label(window, text="Salariu")
label.grid(column=7, row=0)

name = tk.StringVar()
nameEntered = ttk.Entry(window, width=15, textvariable=name)
nameEntered.grid(column=7, row=1)


window.mainloop()