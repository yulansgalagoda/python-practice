import os

path = "C:\\Users\\ADMIN\\Desktop\\text.txt"

# check if a location exists or not
if os.path.exists(path):
    print("File location exists")
else:
    print("File lcoation does not exist")

# check if it is a file or a directory
if os.path.isfile(path):
    print("This is a file")
elif os.path.isdir(path):
    print("This is a directory")