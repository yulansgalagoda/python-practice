# grid() = geometry manager that organizes widgets in a table-like structure

from tkinter import *

window = Tk()

Label(window, text="Form", font=("Arial", 15)).grid(row=0, column=0, columnspan=2)

label_first_name = Label(window, text="First Name: ")
entry_first_name = Entry(window)
label_first_name.grid(row=1, column=0)
entry_first_name.grid(row=1, column=1)

label_last_name = Label(window, text="Last Name: ")
entry_last_name = Entry(window)
label_last_name.grid(row=2, column=0)
entry_last_name.grid(row=2, column=1)

label_email = Label(window, text="Email: ")
entry_email = Entry(window)
label_email.grid(row=3, column=0)
entry_email.grid(row=3, column=1)

button_submit = Button(window, text="Submit")
button_submit.grid(row=4, column=0, columnspan=2)

window.mainloop()
