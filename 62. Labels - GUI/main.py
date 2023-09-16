from tkinter import *

# label = an area widget that holds text and/or an image within a window

window = Tk()
window.title("Python Labels")

photo = PhotoImage(file="img.png")

label = Label(
    window,
    text="Hello World!",
    font=("Arial", 40, "bold"),
    fg="#00ff00",
    bg="black",
    relief=RAISED,
    bd=10,
    padx=20,
    pady=20,
    image=photo,
    compound="bottom"
)
label.pack()
# label.place(x=10, y=10)

window.mainloop()
