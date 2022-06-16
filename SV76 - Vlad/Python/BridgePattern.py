import abc


class IShape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def DrawShape(self):
        pass


class IColor(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def GetColor(self) -> str:
        pass


class Circle(IShape):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def DrawShape(self):
        print("Draw circle or radius " + str(self.radius) + " and color " + self.color.GetColor())


class Triangle(IShape):
    def __init__(self, length1, length2, length3, color):
        self.length1 = length1
        self.length2 = length2
        self.length3 = length3
        self.color = color

    def DrawShape(self):
        lenghts = [self.length1, self.length2, self.length3]
        print("Draw triangle or lengths " + str(lenghts) + " and color " + self.color.GetColor())


class Rectangle(IShape):
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

    def DrawShape(self):
        print("Draw rectangle or width " + str(self.width) + " and height " + str(
            self.height) + " and color " + self.color.GetColor())


class Red(IColor):
    def GetColor(self) -> str:
        return "Red"


class Blue(IColor):
    def GetColor(self) -> str:
        return "Blue"


if __name__ == '__main__':
    circle = Circle(3, Red())
    triangle = Triangle(4, 5, 6, Blue())
    rectangle = Rectangle(5, 6, Red())

    circle.DrawShape()
    triangle.DrawShape()
    rectangle.DrawShape()
