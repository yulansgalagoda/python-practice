from tkinter import *


def submit():
    print("The temperature is:", scale.get(), "degrees C")


window = Tk()

scale = Scale(
    window,
    from_=0,
    to=100,
    length=600,
    orient=HORIZONTAL,
    font=("Consolas", 16),
    tickinterval=10,
    showvalue=False,  # hides current value
    troughcolor="#909090",
    fg="#cccccc",
    bg="#505050"
)
scale.set(50)
scale.pack()

button = Button(window, text="Submit", command=submit)
button.pack()

window.mainloop()
