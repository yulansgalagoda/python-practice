# used to give access to the methods of a parent class.
# Returns a temporary object of a parent class when used

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width


class Square(Rectangle):

    def __init__(self, length, width):
        super().__init__(length, width)

    def area(self):
        print("Area of the square is: " + str(self.length * self.width))


class Cube(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        print("Volume of the cube is: " + str(self.length * self.width * self.height))


square = Square(3, 3)
cube = Cube(3, 3, 3)

square.area()
cube.volume()
