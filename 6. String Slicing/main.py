name = "Yulan Galagoda"

first_name = name[:5]
last_name = name[6:]

print(first_name)
print(last_name)

funny_name = name[3:7]
print(funny_name)

funny_name = name[::2]
print(funny_name)

# reverse
reversed_name = name[::-1]
print(reversed_name)

# ----slicing----

website = "https://google.com"

sliced = slice(8, -4)
print(website[sliced])
