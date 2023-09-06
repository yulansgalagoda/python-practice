while True:
    name = input("Your name: ")
    if name != "":
        break

phone_number = "123-456-7890"
for number in phone_number:
    if number == "-":
        continue
    print(number, end="")
print()

for i in range(1, 21):
    if i == 13:
        pass
    else:
        print(i)
