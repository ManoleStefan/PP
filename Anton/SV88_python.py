class Shape:
    def draw(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def draw(self):
        import turtle
        circ = turtle.Turtle()
        circ.circle(self.radius)
        circ.clear()


class Square(Shape):
    def __init__(self, latura):
        self.latura = latura

    def draw(self):
        import turtle
        t = turtle.Turtle()
        t.forward(self.latura)
        t.left(90)
        t.forward(self.latura)
        t.left(90)
        t.forward(self.latura)
        t.left(90)
        t.forward(self.latura)
        t.left(90)
        t.clear()


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self):
        import turtle
        t = turtle.Turtle()
        t.forward(self.width)
        t.left(90)
        t.forward(self.height)
        t.left(90)
        t.forward(self.width)
        t.left(90)
        t.forward(self.height)
        t.left(90)
        turtle.clear()


class FactoryOfFactories:
    @staticmethod
    def createCircleFactory():
        return CircleFactory()

    @staticmethod
    def createSquareFactory():
        return SquareFactory()

    @staticmethod
    def createRectangleFactory():
        return RectangleFactory()


class CircleFactory(FactoryOfFactories):
    @staticmethod
    def createCircle(radius):
        return Circle(radius)


class SquareFactory(FactoryOfFactories):
    @staticmethod
    def createSquare(latura):
        return Square(latura)


class RectangleFactory(FactoryOfFactories):
    @staticmethod
    def createRectangle(width, height):
        return Rectangle(width, height)


if __name__ == "__main__":
    factoryFactory = FactoryOfFactories()
    circleFactory = factoryFactory.createCircleFactory()
    circle = circleFactory.createCircle(100)
    circle.draw()

    squareFactory = factoryFactory.createSquareFactory()
    square = squareFactory.createSquare(100)
    square.draw()

    rectangleFactory = factoryFactory.createRectangleFactory()
    rectangle = rectangleFactory.createRectangle(100, 50)
    rectangle.draw()
