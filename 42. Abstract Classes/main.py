# Prevents users from creating an object of that class
# Compels a user to override abstract methods in a child class

# abstract class = A class which contains one or more abstract methods
# abstract method = a method that has a declaration but does not have an implementation

from abc import ABC, abstractmethod     # abc = abstract based class


class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass


class Car(Vehicle):
    def go(self):
        print("You are driving the car")


class Motorcycle(Vehicle):
    def go(self):
        print("You ride the motorcycle")


# vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

car.go()
motorcycle.go()
