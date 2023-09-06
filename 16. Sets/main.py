# collection which is unordered, un-indexed
# does not support duplicate values

utensils = {"fork", "spoon", "knife", "knife"}
dishes = {"bowl", "plate", "knife", "cup"}
dinner_table = utensils.union(dishes)

for item in utensils:
    print(item)

utensils.add("napkin")
print(utensils)

utensils.remove("napkin")
print(utensils)

utensils.update(dishes)
print(utensils)

print(dinner_table)

print(utensils.difference(dishes))

print(utensils.intersection(dishes))
