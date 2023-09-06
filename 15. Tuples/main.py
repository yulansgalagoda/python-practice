# collection which is ordered and unchangeable
# used to group together related data

student = ("Yulan", 20, "male")

print(student.count("Yulan"))
print(student.index("male"))

for value in student:
    print(value)

if "Yulan" in student:
    print("Available")
