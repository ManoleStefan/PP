import random
class ShapeFactory:
    @staticmethod
    def factory(type):
        if type == "Circle":
            return Circle()
        if type == "Square":
            return Square()
        assert 0,"Bad shape creation : " + type

class Shape:
    def draw(self): pass
    def erase(self): pass


class Circle(Shape):
    def draw(self):
        print("Circle draw")
    def erase(self):
        print("Circle erase")

class Square(Shape):
    def draw(self):
        print("Square draw")
    def erase(self):
        print("Square erase")

def ShapeNameGen(n):
    types = Shape.__subclasses__()
    for i in range(n):
        yield random.choice(types).__name__

shapes = [ShapeFactory.factory(i) for i in ShapeNameGen(7)]
for shape in shapes:
    shape.draw()
    shape.erase()
    print("\n\n")
    shape = ShapeFactory.factory("Circle")
    shape.draw()
    shape.erase()