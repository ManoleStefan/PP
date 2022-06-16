
class AbstractFactory:
    def create(self,*args):
        pass

class SquareFactory(AbstractFactory):
    def create(self,start,end,l):
        return Square(start,end,l)

class CircleFactory(AbstractFactory):
    def create(self,center,radius):
        return Circle(center,radius)

class RectangleFactory(AbstractFactory):
    def create(self,start,end,l1,l2):
        return Rectangle(start,end,l1,l2)

class Square:
    def __init__(self,start,end,l):
        self.start = start
        self.end = end
        self.l = l

    def __str__(self):
        return f"Patrat:\n -start: {self.start}\n -end: {self.end}\n -latura: {self.l}\n"
class Circle:
    def __init__(self,center,radius):
        self.center = center
        self.radius = radius

    def __str__(self):
        return f"Cerc:\n -centru: {self.center}\n -raza: {self.radius}\n"
class Rectangle:
    def __init__(self,start,end,l1,l2):
        self.start = start
        self.end = end
        self.l1 = l1
        self.l2 = l2

    def __str__(self):
        return f"Dreptunghi:\n -start: {self.start}\n -end: {self.end}\n -lungime: {self.l1}\n -latime: {self.l2}\n"

if __name__ == '__main__':
    sf = SquareFactory()
    cf = CircleFactory()
    rf = RectangleFactory()

    s = sf.create((1,1),(2,2),1)
    c = cf.create((2,3),3)
    r = rf.create((2,3),(4,3),3,4)

    print(s,c,r)