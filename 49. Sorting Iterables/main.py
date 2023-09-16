# sort() method = used with lists
# sort() function = used with iterables

# students = ["Oggy", "Jack", "Joey", "Olivia", "Bob"]
#
# students.sort()
# for student in students:
#     print(student)
# print()
#
# students.sort(reverse=True)
# for student in students:
#     print(student)
# print()
#
# new_students = ("Oggy", "Jack", "Joey", "Olivia", "Bob")
# sorted_students = sorted(new_students)
#
# for student in sorted_students:
#     print(student)

# students = [
#     ("Oggy", "F", 60),
#     ("Jack", "A", 33),
#     ("Joey", "D", 36),
#     ("Olivia", "B", 20),
#     ("Bob", "C", 78)
# ]
#
grade = lambda grades: grades[1]
# students.sort(key=grade)
# print(students)


students = (
    ("Oggy", "F", 60),
    ("Jack", "A", 33),
    ("Joey", "D", 36),
    ("Olivia", "B", 20),
    ("Bob", "C", 78)
)

sorted_students = sorted(students, key=grade)
print(sorted_students)
