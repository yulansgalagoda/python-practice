# a listing of selectable text items within its own container

from tkinter import *


def submit():
    # print(listbox.get(listbox.curselection()))      # display current selection, Only works if there's one selection
    food = []
    for element in listbox.curselection():
        food.insert(element, listbox.get(element))
    for element in food:
        print(element)
    print(food)


def add():
    listbox.insert(listbox.size(), entry_box.get())      # insert items
    adjust_size()


def delete():
    # listbox.delete(listbox.curselection())      # delete items, only for 1 item
    for element in reversed(listbox.curselection()):  # reverse function because when one is deleted, indexes changes
        listbox.delete(element)

    adjust_size()


def adjust_size():
    listbox.config(height=listbox.size())      # adjust size


window = Tk()

# defining listbox
listbox = Listbox(
    window,
    bg="#f7ffde",
    font=("Constantia", 14),
    width=12,
    selectmode=MULTIPLE
)
listbox.pack()

# entering values into the listbox
foodlist = ["Pizza", "Pasta", "Garlic Bread", "Soup", "Salad"]
for index in range(len(foodlist)):
    listbox.insert(index+1, foodlist[index])

adjust_size()

#  defining an entry box, buttons (submit button, add button and delete button)
entry_box = Entry(window)
entry_box.pack()

submit_button = Button(window, text="Submit", command=submit)
submit_button.pack()

add_button = Button(window, text="Add", command=add)
add_button.pack()

delete_button = Button(window, text="Delete", command=delete)
delete_button.pack()

# running the window
window.mainloop()
