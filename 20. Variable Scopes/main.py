# scope is the region that a variable is recognized
# variable is only available in the region it is created
# LEGB rule - Local > Enclosing > Global > Built-in

name = "Galagoda"


def display_name():
    name = "Yulan"
    print(name)  # can only be referred within the scope of the function (local scope)


display_name()
print(name)  # refers to the global scope of the variable
