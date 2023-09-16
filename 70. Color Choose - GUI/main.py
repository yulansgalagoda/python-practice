from tkinter import *
from tkinter import colorchooser    # submodule


def choose_color():
    # color_code = colorchooser.askcolor()
    # window.config(bg=str(color_code[1]))
    mycolor = colorchooser.askcolor()
    print(mycolor)
    window.config(bg=str(colorchooser.askcolor()[1]))


window = Tk()
window.geometry("420x420")

button = Button(window, text="Choose Color", command=choose_color)
button.pack()

window.mainloop()
