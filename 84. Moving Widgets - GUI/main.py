from tkinter import *


def move_up(event):
    label_car.place(x=label_car.winfo_x(), y=label_car.winfo_y()-10)


def move_down(event):
    label_car.place(x=label_car.winfo_x(), y=label_car.winfo_y()+10)


def move_left(event):
    label_car.place(x=label_car.winfo_x()-10, y=label_car.winfo_y())


def move_right(event):
    label_car.place(x=label_car.winfo_x()+10, y=label_car.winfo_y())


window = Tk()
window.geometry("500x500")

window.bind("<w>", move_up)
window.bind("<a>", move_left)
window.bind("<s>", move_down)
window.bind("<d>", move_right)

image_car = PhotoImage(file="car.png")
label_car = Label(window, image=image_car)
label_car.place(x=10, y=10)

window.mainloop()
