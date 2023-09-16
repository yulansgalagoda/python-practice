from tkinter import *


def pressed(event):
    # print("You pressed " + event.keysym)
    label.config(text=event.keysym)


window = Tk()

window.bind("<Key>", pressed)

label = Label(window, font=("Helvetica", 20))
label.pack()

window.mainloop()
