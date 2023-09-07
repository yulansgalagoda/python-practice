import os

source = "C:\\Users\\ADMIN\\Desktop\\text.txt"
destination = "C:\\Users\\ADMIN\\Desktop\\movedFile\\text.txt"

try:
    if os.path.exists(destination):
        print("There is a file there already")
    else:
        os.replace(source, destination)
        print(source + " was moved")
except FileNotFoundError as e:
    print(e)
