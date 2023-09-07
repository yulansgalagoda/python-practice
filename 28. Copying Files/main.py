# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata

import shutil

shutil.copyfile(
    "C:\\Users\\ADMIN\\Desktop\\text.txt",
    "C:\\Users\\ADMIN\\Desktop\\text-copy.txt"
)
