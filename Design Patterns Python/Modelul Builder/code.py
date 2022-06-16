import abc
class Car:
    def __init__(self):
        self.color = None

    def get_color(self):
        return self.color

    def set_color(self,color):
        self.color = color

    def __str__(self):
        return "Car[color = {}]".format(self.color)

class CarBuilder(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def set_color(self,color): pass

    @abc.abstractmethod
    def get_result(self): pass

class ConcreteClassBuilder(CarBuilder):
    def __init__(self,name):
        self.name = name
        self.car = Car()

    def set_color(self,color):
        self.car.set_color(color)

    def get_result(self):
        return self.car

Audi = ConcreteClassBuilder("Audi")
Audi.set_color("Blue")
print(Audi.get_result())
