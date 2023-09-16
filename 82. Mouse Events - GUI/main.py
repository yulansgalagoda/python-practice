from tkinter import *


def do_something(event):
    print("Mouse location: " + str(event.x) + ", " + str(event.y))


window = Tk()

# window.bind("<Button-1>", do_something)         # Button-1 is the left mouse button
# window.bind("<Button-2>", do_something)         # Button-1 is the pressing mouse wheel
# window.bind("<Button-3>", do_something)         # Button-1 is the right mouse button
# window.bind("<ButtonRelease>", do_something)         # when releasing any mouse button that has been clicked
# window.bind("<Enter>", do_something)         # mouse entered into the window (not the enter / return button
window.bind("<Motion>", do_something)         # where the mouse moved


window.mainloop()
