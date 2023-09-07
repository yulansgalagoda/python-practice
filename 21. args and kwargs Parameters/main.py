# args is a parameter that will pack all arguments in to a tuple
# its useful so that a function can accept a varying amount of arguments
# if a argument passed in needs to be changed, it should be converted to a list first. list()
# since tuples cannot be changed, there is no other option to change a value passed

# kwargs is a parameter that packs all arguments in to a dictionary
# unlike args which packs positional arguments to a tuple
# kwargs pack keyword arguments to a dictionary


def add(*args):
    sum = 0
    args_list = list(args)
    args_list[0] = 20
    for arg in args:
        sum += 1
    return sum


print(add(1, 4, 2, 5, 7, 2))


def hello(**kwargs):
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")


hello(first="Yulan", second="Senula", last="Galagoda")
