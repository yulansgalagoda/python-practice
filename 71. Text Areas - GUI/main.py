# text widget = functions like a text area where multiple lines of text can be entered
from tkinter import *


def submit():
    user_input = text.get("1.0", END)
    print(user_input)


window = Tk()

text = Text(
    window,
    bg="light yellow",
    fg="purple",
    font=("Ink Free", 20),
    height=5,
    width=15,
    padx=20,
    pady=20
)
text.pack()

button = Button(window, text="Submit", command=submit)
button.pack()

window.mainloop()
