# applies a function to each item in an iterable
# map(function, iterable)

store = [
    ("shirts", 20.00),
    ("pants", 25.00),
    ("jackets", 50.00),
    ("socks", 10.00)
]

to_euro = lambda data: (data[0], data[1]*0.82)
to_dollars = lambda data: (data[0], data[1]/0.82)

store_euro = list(map(to_euro, store))
store_dollars = list(map(to_dollars, store_euro))

print(store_euro)
print(store_dollars)
