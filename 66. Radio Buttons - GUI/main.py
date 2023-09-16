from tkinter import *

food = ["Pizza", "Hamburger", "Hotdog"]


def order():
    if x.get() == 0:
        print("Ordered Pizza")
    elif x.get() == 1:
        print("Ordered a hamburger")
    elif x.get() == 2:
        print("Ordered hotdog")
    else:
        print("Huh?")


window = Tk()

x = IntVar()

for index in range(len(food)):
    radio_button = Radiobutton(
        window,
        text=food[index],
        variable=x,
        value=index,
        indicatoron=False,
        width=15,
        padx=25,
        pady=10,
        command=order
    )
    radio_button.config(font=("Impact", 30))
    radio_button.pack(anchor=W)

window.mainloop()
