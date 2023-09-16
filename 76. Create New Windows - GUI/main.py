from tkinter import *


def create_window():
    # new_window = Toplevel()     # new window on top of other windows and linked to a bottom window
    new_window = Tk()           # new independent window

    window.destroy()            # destroys the old window


window = Tk()

Button(window, text="Create new window", command=create_window).pack()

window.mainloop()