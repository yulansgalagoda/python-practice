from tkinter import *
from tkinter import filedialog


def open_files():
    file_path = filedialog.askopenfilename(
        initialdir="D:\\python practice",
        title="Open a file YO!",
        filetypes=(("text files", "*.txt"), ("all files", "*.*"))
    )
    file = open(file_path, "r")
    print(file.read())


window = Tk()

button = Button(window, text="Browse", command=open_files)
button.pack()

window.mainloop()
