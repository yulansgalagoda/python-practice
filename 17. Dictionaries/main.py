# changeable unordered collection of unique key value pairs.
# they are fast since they use hashing

capitals = {
    "USA": "Washington DC",
    "England": "London",
    "India": "New Dehli",
    "China": "Beijing"
}

print(capitals["England"])

print(capitals.get("Germany"))
print(capitals.get("India"))

print(capitals.keys())
print(capitals.values())
print(capitals.items())

for key, value in capitals.items():
    print(key, value)

capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Las Vegas"})
print(capitals.get("Germany"))
print(capitals.get("USA"))

capitals.pop("USA")
print(capitals)

capitals.clear()
print(capitals)
