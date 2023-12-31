from tkinter import *

# entry widget = textbox that accepts a single line of user input


def submit():
    username = entry.get()
    print("hello", username)
    entry.config(state=DISABLED)


def delete():
    entry.delete(0, END)


def backspace():
    entry.delete(len(entry.get())-1, END)


window = Tk()

entry = Entry(window, font=("Arial", 50), fg="#00ff00", bg="#000000", show="*")
entry.pack(side=LEFT)
entry.insert(0, "Spongebob")

submit_button = Button(window, text="Submit", command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window, text="Delete", command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window, text="Backspace", command=backspace)
backspace_button.pack(side=RIGHT)

window.mainloop()
