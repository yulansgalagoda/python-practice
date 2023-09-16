# a way to create a new list with less syntax
# can mimic certain lambda function
# more readability

# list = [expression for item in iterable]

# squares = []
# for number in range(1, 11):
#     squares.append(number*number)
# print(squares)
#
# squares_list = [number*number for number in range(1, 11)]
# print(squares_list)

students = [100, 0, 90, 80, 70, 60, 50, 40, 30, 0]
passed_students = list(filter(lambda x: x>=60, students))
print(passed_students)

# list = [expression for item in iterable if conditional]
passed_list = [mark for mark in students if mark>=60]
print(passed_list)

# list = [expression (if/else) for item in iterable]
passed_students_1 = [mark if mark>=60 else "FAILED" for mark in students]
print(passed_students_1)
