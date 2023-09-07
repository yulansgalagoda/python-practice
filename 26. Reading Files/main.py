try:
    with open("C:\\Users\\ADMIN\\Desktop\\text.txt") as file:
        print(file.read())
except FileNotFoundError as e:
    print(e)

# with open command closes the file automatically just after the action is completed
