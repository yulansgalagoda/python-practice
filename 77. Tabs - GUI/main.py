from tkinter import *
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window)     # a widget that manages a collection of windows / displays

tab1 = Frame(notebook)              # new frame for tab1
tab2 = Frame(notebook)

notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")
notebook.pack(expand=True, fill="both")

Label(tab1, text="Hello, this is tab 1").pack()
Label(tab2, text="Bye, this is tab 2").pack()

window.mainloop()
