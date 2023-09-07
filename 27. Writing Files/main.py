text = "Hello world\nThis is another text file"

with open("C:\\Users\\ADMIN\\Desktop\\text-written.txt", "a") as file:
    file.write(text)
    # mode "w" will write a new file, if it already exists, it will overwrite the file
    # mode "a" will append the new content to the file
