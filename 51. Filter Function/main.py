# creates a collection of elements from an iterable for which a function returns true
# filter(function, iterable)

friends = [
    ("Rachel", 19),
    ("Monica", 18),
    ("Phoebe", 17),
    ("Joey", 16),
    ("Chandler", 21),
    ("Ross", 20)
]

check_age = lambda data: data[1] >= 18

adult_friends = list(filter(check_age, friends))
print(adult_friends)

