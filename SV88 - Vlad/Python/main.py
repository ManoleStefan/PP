import abc
from abc import ABC
import tkinter as tk
import math


class IShape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def drawShape(self, xAxis, yAxis, canvas):
        pass


class IRoundedShape(IShape, ABC):
    def __init__(self, radius):
        self.radius = radius


class IRectangleShape(IShape, ABC):
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Circle(IRoundedShape):
    def __init__(self, radius):
        super().__init__(radius)

    def drawShape(self, xAxis, yAxis, canvas):
        print("Draw Circle of radius " + str(self.radius))
        if isinstance(canvas, tk.Canvas):
            canvas.create_oval(xAxis, yAxis,xAxis + 2*self.radius, yAxis + 2*self.radius, fill="red")


class Rectangle(IRectangleShape):
    def __init__(self, width, height):
        super().__init__(width, height)

    def drawShape(self, xAxis, yAxis, canvas):
        print("Draw Rectangle of width " + str(self.width) + " and height " + str(self.height))
        if isinstance(canvas, tk.Canvas):
            canvas.create_rectangle(xAxis, yAxis, xAxis + self.width, yAxis + self.height, fill="blue")


class Square(IRectangleShape):
    def __init__(self, length):
        super().__init__(length, length)

    def drawShape(self, xAxis, yAxis, canvas):
        print("Draw Square of length " + str(self.width))
        if isinstance(canvas, tk.Canvas):
            canvas.create_rectangle(xAxis, yAxis, xAxis + self.width, yAxis + self.width, fill="green")


class IFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def createShape(self, shapeType) -> IShape:
        pass


class RoundShapesFactory(IFactory):

    def __init__(self):
        self.radius = 10

    def createShape(self, shapeType) -> IShape:
        if shapeType == "Circle":
            return Circle(self.radius)
        raise Exception("Unknown object")

    @property
    def radius(self):
        return self.radius__

    @radius.setter
    def radius(self, radius):
        if radius <= 0:
            raise Exception("Radius must be positive!")
        self.radius__ = radius


class RectangleShapesFactory(IFactory):
    def __init__(self):
        self.width = 10
        self.height = 5

    def createShape(self, shapeType) -> IShape:
        if shapeType == "Rectangle":
            return Rectangle(self.width, self.height)
        if shapeType == "Square":
            return Square(self.width)
        raise Exception("Unknown object")

    @property
    def width(self):
        return self.width__

    @property
    def height(self):
        return self.height__

    @width.setter
    def width(self, width):
        if width <= 0:
            raise Exception("Width must be positive!")
        self.width__ = width

    @height.setter
    def height(self, height):
        if height <= 0:
            raise Exception("Height must be positive!")
        self.height__ = height


class IFactoryMaker(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def createFactory(self, factoryType) -> IFactory:
        pass


class ConcreteFactoryMaker(IFactoryMaker):
    def createFactory(self, factoryType) -> IFactory:
        if factoryType == "RoundShapesFactory":
            return RoundShapesFactory()
        if factoryType == "RectangleShapesFactory":
            return RectangleShapesFactory()


class Application(tk.Frame):
    def __init__(self, master):
        self.master = master
        self.createWidgets()

        self.factoryCreator = ConcreteFactoryMaker()

        self.roundedFactory = self.factoryCreator.createFactory("RoundShapesFactory")
        self.rectangleFactory = self.factoryCreator.createFactory("RectangleShapesFactory")

        self.itemNo = 0
        self.leftSpace = 5
        self.topSpace = 5

    def createWidgets(self):
        self.rightSideFrame = tk.Frame(self.master)
        self.rightSideFrame.pack(side=tk.RIGHT)

        self.drawCircleButton = tk.Button(self.rightSideFrame, text="Draw Circle", command=self.drawCircleCommand)
        self.drawRectangleButton = tk.Button(self.rightSideFrame, text="Draw Rectangle",
                                             command=self.drawRectangleCommand)
        self.drawSquareButton = tk.Button(self.rightSideFrame, text="Draw Square", command=self.drawSquareCommand)
        self.quitButton = tk.Button(self.rightSideFrame, text="Quit", command=self.quitCommand)

        self.drawCircleButton.pack(fill=tk.BOTH)
        self.drawRectangleButton.pack(fill=tk.BOTH)
        self.drawSquareButton.pack(fill=tk.BOTH)
        self.quitButton.pack(fill=tk.BOTH)

        self.canvas = tk.Canvas(self.master, width=200, height=200, borderwidth=2, bg="white")
        self.canvas.pack(side=tk.LEFT)

    def drawCircleCommand(self):
        self.roundedFactory.radius = 20
        circle = self.roundedFactory.createShape("Circle")
        circle.drawShape(self.leftSpace + 50 * math.fmod(self.itemNo, 4), self.topSpace + 50 * math.floor(self.itemNo / 4), self.canvas)
        self.itemNo += 1

    def drawRectangleCommand(self):
        self.rectangleFactory.width = 40
        self.rectangleFactory.height = 20
        rectangle = self.rectangleFactory.createShape("Rectangle")
        rectangle.drawShape(self.leftSpace + 50 * math.fmod(self.itemNo, 4), self.topSpace + 50 * math.floor(self.itemNo / 4), self.canvas)
        self.itemNo += 1

    def drawSquareCommand(self):
        self.rectangleFactory.width = 40
        square = self.rectangleFactory.createShape("Square")
        square.drawShape(self.leftSpace + 50 * math.fmod(self.itemNo, 4), self.topSpace + 50 * math.floor(self.itemNo / 4), self.canvas)
        self.itemNo += 1

    def quitCommand(self):
        exit(0)


if __name__ == '__main__':
    root = tk.Tk()

    app = Application(root)
    root.mainloop()
