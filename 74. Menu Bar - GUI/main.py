from tkinter import *


def print_name():
    print("Yulan")


window = Tk()

menubar = Menu(window)                                      # define menu
window.config(menu=menubar)                                 # add menu to window

file_menu = Menu(menubar, tearoff=0, font=("MV Boli", 15))                        # define a new menu section (file)
menubar.add_cascade(label="File", menu=file_menu)           # add the new menu to main menu
file_menu.add_command(label="Open", command=print_name)     # add options
file_menu.add_command(label="Save", command=print_name)
file_menu.add_separator()                                   # add separators
file_menu.add_command(label="Exit", command=quit)

edit_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=print_name)
edit_menu.add_command(label="Copy", command=print_name)
edit_menu.add_command(label="Paste", command=print_name)

window.mainloop()
