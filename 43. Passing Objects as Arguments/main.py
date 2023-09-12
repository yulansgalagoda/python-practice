class Car:
    color = None


class Motorcycle:
    color = None


def change_color(vehicle, color):
    vehicle.color = color


car_1 = Car()
car_2 = Car()
motorcycle_1 = Motorcycle()

change_color(car_1, "red")
change_color(car_2, "white")
change_color(motorcycle_1, "blue")

print(car_1.color)
print(car_2.color)
print(motorcycle_1.color)
