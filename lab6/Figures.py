from Vector import *

def check_numerical(size):
    for i, v in enumerate(size):
        size[i] = float(v)
    return size


class Figure:
    colours = {'black', 'white', 'red', 'green', 'blue', 'cyan', 'magenta', 'yellow'}

    def __init__(self, *size):
        self.center = Vector(0, 0)
        self.border_colour = "black"
        self.background_colour = "white"
        self.size = check_numerical(list(size))

    def __str__(self):
        return "center: " + str(self.center) + "\nsize: " + str(self.size) + "\nbackground colour: " + \
               str(self.background_colour) + "\nborder colour: " + str(self.border_colour) + "\n\n"

    def move(self, x, y):
        self.center += Vector(x, y)

    def scale(self, ratio):
        if float(ratio) == 0:
            raise ValueError("Ratio cannot be zero")
        else:
            self.size = list(map(lambda x: x * float(ratio), self.size))

    def set_border_colour(self, colour):
        if colour in Figure.colours:
            self.border_colour = colour
        else:
            raise ValueError("Unknown colour")

    def set_background_colour(self, colour):
        if colour in Figure.colours:
            self.background_colour = colour
        else:
            raise ValueError("Unknown colour")


class Circle(Figure):
    def __init__(self, *size):
        if len(size) != 1:
            raise ValueError("Incorrect size")
        super().__init__(*size)

    def __str__(self):
        return "Circle:\n" + super().__str__()


class Polygon(Figure):
    def __init__(self, *size):
        super().__init__(*size)
        self.angle = 0

    def rotate(self, angle):
        self.angle = (self.angle + int(angle)) % 360

    def __str__(self):
        return super().__str__()[0:-1] + "rotation: " + str(self.angle)


class Square(Polygon):
    def __init__(self, *size):
        if len(size) != 1:
            raise ValueError("Incorrect size")
        super().__init__(*size)

    def __str__(self):
        return "Square:\n" + super().__str__() + "\n\n"


class Rectangle(Polygon):
    def __init__(self, *size):
        if len(size) != 2:
            raise ValueError("Incorrect size")
        super().__init__(*size)

    def __str__(self):
        return "Rectangle:\n" + super().__str__() + "\n\n"


class Triangle(Polygon):
    def __init__(self, *size):
        if len(size) != 3:
            raise ValueError("Incorrect size")
        super().__init__(*size)
        if sum(self.size) - max(self.size) <= max(self.size):
            raise ValueError("Triangle inequality isn\'t satisfied")

    def __str__(self):
        return "Triangle:\n" + super().__str__() + "\n\n"
