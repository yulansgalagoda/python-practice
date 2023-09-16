from tkinter import *


def display():
    if x.get() == 1:
        print("Agree")
    else:
        print("You do not agree")


window = Tk()

x = IntVar()        # StringVar() and BooleanVar() can be used depending on the data type of 'onvalue' and 'offvalue'

image = PhotoImage(file="img.png")

check_button = Checkbutton(
    window,
    text="I agree to it",
    variable=x,
    onvalue=1,
    offvalue=0,
    command=display,
    font=("Arial", 20),
    fg="#00ff00",
    bg="#000000",
    activeforeground="#00ff00",
    activebackground="#252525",
    padx=25,
    pady=10,
    image=image,
    compound="left"
)
check_button.pack()

window.mainloop()
