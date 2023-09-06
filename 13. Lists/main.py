# store multilpe values in a single variable

vehicles = ["car", "bike", "train", "bus"]

print(vehicles)
print(vehicles[1])
print(vehicles[-1])

for vehicle in vehicles:
    print(vehicle)

vehicles[1] = "cycle"
print(vehicles[1])

vehicles.append("Airplane")
print(vehicles)

vehicles.pop()
print(vehicles)

vehicles.remove("cycle")
print(vehicles)

vehicles.insert(1, "van")
print(vehicles)

vehicles.sort()
print(vehicles)

vehicles.clear()
print(vehicles)
