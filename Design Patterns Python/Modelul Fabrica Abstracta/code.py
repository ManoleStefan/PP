import abc

class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def draw(self):
        pass


class Color(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def fill(self):
        pass

class Square(Shape):
    def draw(self):
        print("Drawing a Square")

class Circle(Shape):
    def draw(self):
        print("Drawing a Circle")

class Rectangle(Shape):
    def draw(self):
        print("Drawing a Rectangle")

class Green(Color):
    def fill(self):
        print("Filling with Green")

class Blue(Color):
    def fill(self):
        print("Filling with Blue")

class Red(Color):
    def fill(self):
        print("Filiing with Red")


class AbstractFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def getcolor(self,choice):
        pass

    @abc.abstractmethod
    def getshape(self,choice):
        pass

class ShapeFactory(AbstractFactory):
    def getcolor(self,choice):
        print("This factory creates only shapes.")

    def getshape(self,choice):
        if choice == "Rectangle":
            return Rectangle()
        elif choice == "Square":
            return Square()
        elif choice == "Circle":
            return Circle()
        return None

class ColorFactory(AbstractFactory):
    def getshape(self,choice):
        print("This factory creates only colors.")

    def getcolor(self,choice):
        if choice == "Red":
            return Red()
        elif choice == "Green":
            return Green()
        elif choice == "Blue":
            return Blue()
        return None


class FactoryProducer:
    @staticmethod
    def get_factory(choice):
        if choice == "SHAPE":
            return ShapeFactory()
        elif choice == "COLOR":
            return ColorFactory()
        return None

if __name__ == '__main__':
    shape_factory = FactoryProducer.get_factory("SHAPE")
    color_factory = FactoryProducer.get_factory("COLOR")

    shape = [ shape_factory.getshape("Circle"),
              shape_factory.getshape("Rectangle"),
              shape_factory.getshape("Square") ]

    color = [ color_factory.getcolor("Red"),
              color_factory.getcolor("Green"),
              color_factory.getcolor("Blue") ]

    for shp in shape:
        shp.draw()

    for clr in color:
        clr.fill()

