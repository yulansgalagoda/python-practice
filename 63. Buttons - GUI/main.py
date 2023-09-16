from tkinter import *

count = 0


def click():
    global count
    count += 1
    print(count)


window = Tk()

photo = PhotoImage(file="img.png")

button = Button(
    window,
    text="Click me!",
    command=click,
    font=("Comic Sans", 30),
    fg="#00ff00",
    bg="#000000",
    activeforeground="#00ff00",
    activebackground="#909090",
    state=ACTIVE,
    image=photo,
    compound="bottom"
)
button.pack()

window.mainloop()
