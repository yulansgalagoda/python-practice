# an optional method for strings which gives users more control when displaying output
# it use format fields {}

animal = "cow"
item = "moon"

print("The "+animal+" jumped over the "+item)

print("The {} jumped over the {}".format(animal, item))
print("The {1} jumped over the {0}".format(item, animal))  # positional argument
print("The {animal} jumped over the {item}".format(animal="cow", item="moon"))  # keyword argument

text = "The {} jumped over the {}"
print(text.format(animal, item))

name = "Yulan"

print("Hello, my name is {}".format(name))
print("Hello, my name is {:10}".format(name))  # adds padding after
print("Hello, my name is {:>10}".format(name))  # adds padding before
print("Hello, my name is {:<10}".format(name))  # adds padding after (default)

number = 3.14159
print("The number pi is {}".format(number))
print("The number pi is {:.2f}".format(number))  # 2 is for number of characters and f is for float
print("The number pi is {:,}".format(1000))  # add, for 1000 places
print("The number pi is {:b}".format(10))  # display binary
print("The number pi is {:0}".format(10))  # display octal
print("The number pi is {:x}".format(10))  # display hexa
print("The number pi is {:e}".format(10))  # display scientific
