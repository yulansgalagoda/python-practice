# a block of code which only executes when invoked or called
# arguments which match for defined parameters are fed to a function
# return statement is used within functions to send values/objects back to the caller
# the values returned are known as return value


# defining functions


def hello(age):
    print("You are " + str(age) + " years old.")


hello(20)


# Return statement


def multiply(num1, num2):
    return num1 * num2


print(multiply(2, 4)) # positional arguments are used instead of keyword arguments


# keyword arguments


def say_hello(first, middle, last):
    print("Hello " + first + " " + middle + " " +last)


say_hello(middle="Senula", last="Galagoda", first="Yulan")


# nested function calls

num = 5
num = float(num)
num = abs(num)
num = round(num)
print(num)
# or it can be done with nested functions
print(round(abs(float(10))))
