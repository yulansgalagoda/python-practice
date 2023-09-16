from tkinter import *
from tkinter import messagebox


def display_message():
    # messagebox.showinfo(title="This is an info message", message="You clicked the button.")

    # messagebox.showwarning(title="This is a warning", message="You have a virus.")

    # while True:
    #     messagebox.showwarning(title="This is a warning", message="You have a virus.")

    # messagebox.showerror(title="This is an error", message="Something went wrong")

    # if messagebox.askokcancel(title="Ask ok cancel", message="Want to do it?"):
    #     print("You did it")
    # else:
    #     print("You canceled it")

    # if messagebox.askretrycancel(title="Ask ok cancel", message="Want to retry it?"):
    #     print("You retried it")
    # else:
    #     print("You canceled it")

    # if messagebox.askyesno(title="Ask ok cancel", message="Want to retry it?"):
    #     print("You said yes to it")
    # else:
    #     print("You said no to it")

    # answer = messagebox.askquestion(title="Asking a question", message="Do you like pie?")
    # if answer == "yes":
    #     print("I like pie too!")
    # else:
    #     print("Why dont you like pie?")

    answer = messagebox.askyesnocancel(title="Yes, No and Cancel", message="Do you like coding?")
    print(answer)
    if answer:
        print("I like coding too!")
    elif answer is None:
        print("Huh?")
    else:
        print("Why? it is fun!")


window = Tk()

button = Button(window, text="Click here!", command=display_message)
button.pack()

window.mainloop()
