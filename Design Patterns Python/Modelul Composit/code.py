import abc
class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def draw(self,color): pass

class Triangle(Shape):
    def draw(self,color):
        print("Desenez un triunghi cu culoarea " + color)

class Circle(Shape):
    def draw(self,color):
        print("Desenez un cerc cu culoarea " + color)

class Drawing(Shape):
    def __init__(self):
        self.shapes = []

    def draw(self,color):
        for sh in self.shapes:
            sh.draw(color)

    def add(self,shape):
        self.shapes.append(shape)
        print("Adaugam figura {} in lista".format(shape.__class__.__name__))

    def remove(self,shape):
        self.shapes.remove(shape)
        print("Stergem figura {} din lista".format(shape.__class__.__name__))

    def clear(self):
        print("Stergem toate formele din lista")
        self.shapes = []

tri1 = Triangle()
tri2 = Triangle()

cir1 = Circle()

drawing = Drawing()
drawing.add(tri1)
drawing.add(tri2)

Maindrawing = Drawing()
Maindrawing.add(drawing)
Maindrawing.add(cir1)
Maindrawing.draw("verde")
