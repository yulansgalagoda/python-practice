from tkinter import *
from tkinter.ttk import *
import time


def start():
    tasks = 10
    completed_tasks = 0
    while completed_tasks < tasks:
        bar["value"] += 10

        time.sleep(1)
        completed_tasks += 1

        percent.set(str((completed_tasks/tasks)*100) + "%")

        text.set(str(completed_tasks) + "/" + str(tasks) + " tasks completed")

        window.update_idletasks()       # update realtime progress bar


window = Tk()

percent = StringVar()
text = StringVar()

bar = Progressbar(window, orient=HORIZONTAL, length=300)
bar.pack(pady=10)

label_percent = Label(window, textvariable=percent)
label_percent.pack()

task_percent = Label(window, textvariable=text)
task_percent.pack()

button = Button(window, text="download", command=start)
button.pack()

window.mainloop()
