from tkinter import *


def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)


def equal():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except ZeroDivisionError:
        equation_label.set("Arithmetic Error")
        equation_text = ""
    except SyntaxError:
        equation_label.set("Syntax Error")
        equation_text = ""


def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""


def create_buttons(button_text, row, column):
    calc_button = Button(
        frame,
        text=button_text,
        height=4,
        width=9,
        font=35,
        command=lambda: button_press(button_text)
    )
    calc_button.grid(row=row, column=column)


window = Tk()
window.title("Calculator Program")
window.geometry("500x500")

equation_text = ""

equation_label = StringVar()

label = Label(
    window,
    textvariable=equation_label,
    font=("concolas", 20),
    bg="#ffffff",
    width=24,
    height=2
)
label.pack()

frame = Frame(window)
frame.pack()
buttons = [
    [1, 0, 0],
    [2, 0, 1],
    [3, 0, 2],
    [4, 1, 0],
    [5, 1, 1],
    [6, 1, 2],
    [7, 2, 0],
    [8, 2, 1],
    [9, 2, 2],
    [0, 3, 0],
    ["+", 0, 3],
    ["-", 1, 3],
    ["*", 2, 3],
    ["/", 3, 3],
    [".", 3, 1]
]

for button in buttons:
    create_buttons(button[0], button[1], button[2])

equal_key = Button(frame, text="=", height=4, width=9, font=35, command=equal)
equal_key.grid(row=3, column=2)

clear_key = Button(frame, text="Clear", height=4, width=18, font=35, command=clear)
clear_key.grid(row=4, column=0, columnspan=2)

quit_key = Button(frame, text="Quit", height=4, width=18, font=35, command=quit)
quit_key.grid(row=4, column=2, columnspan=2)

window.mainloop()
