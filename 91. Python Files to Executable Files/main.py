# nagivate to the project folder
# enter the command pyinstaller -F -w -i icon.ico filename
            # -F = make one file
            # -w = Remove terminal
            # -i = Add an icon. must be followed by icon in the .ico format
            # filename = enter the name of the .py file (main.py)

from tkinter import *
from time import *


def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    window.after(1000, update)


window = Tk()

time_label = Label(window, font=("Arial", 50), fg="#00ff00", bg="#303030")
time_label.pack()

day_label = Label(window, font=("Arial", 25))
day_label.pack()

date_label = Label(window, font=("Arial", 30))
date_label.pack()

update()

window.mainloop()
