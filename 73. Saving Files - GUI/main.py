from tkinter import *
from tkinter import filedialog


def save_file():
    file = filedialog.asksaveasfile(
        defaultextension=".txt",
        filetypes=[
            ("text file", ".txt"),
            ("html", ".html")
        ],
        initialdir="D:\\python practice"
    )
    if file is None:        # avoid throwing errors when closing the file dialog
        return
    file.write(str(text.get(1.0, END)))


window = Tk()

Button(window, text="save", command=save_file).pack()
text = (Text(window, width=50, height=10))
text.pack()

window.mainloop()
