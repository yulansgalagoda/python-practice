from tkinter import *

# widgets = GUI elements: buttons, text boxes, labels and images
# windows = serves as a container to hold or contain these widgets

window = Tk()       # instantiate an instance of a window
window.geometry("420x420")
window.title("My First GUI Program")

icon = PhotoImage(file='gui-icon.png')
window.iconphoto(True, icon)

window.config(background="#5cfcff")

window.mainloop()   # place window on computer screen and listen for events
