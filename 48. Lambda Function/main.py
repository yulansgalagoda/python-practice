# written in 1 line using lambda keyword
# accepts any number of arguments, but only has one expression
# useful if needed for a short period of time

# lambda parameters: expression


# def double(x):
#    return x*2


# print(double(5))

double = lambda x: x * 2
multiply = lambda x, y: x*y

age_check = lambda age: True if age>= 18 else False

print(double(4))
print(multiply(5, 6))
print(age_check(22))
