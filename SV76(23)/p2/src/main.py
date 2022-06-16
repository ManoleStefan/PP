import abc

class DrawingAPI(metaclass=abc.ABCMeta):
    def draw(self,*args):
        pass

class DrawingTriangleAPI(DrawingAPI):
    def draw(self,coords,laturi):
        print(f"Triunghi cu coordonatele: {coords} si laturile {laturi}")


class DrawingCircleAPI(DrawingAPI):
    def draw(self, coords, raza):
        print(f"Cerc cu coordonatele: {coords} si raza {raza}")


class DrawingRectAPI(DrawingAPI):
    def draw(self, coords, laturi):
        print(f"Triunghi cu coordonatele: {coords} si laturile {laturi}")


class Shape(metaclass=abc.ABCMeta):
    def draw(self):
        pass

class Triangle(Shape):
    def __init__(self,coords,laturi,drawingAPI):
        self.coords = coords
        self.laturi = laturi
        self.drawingAPI = drawingAPI

    def draw(self):
        self.drawingAPI.draw(self.coords,self.laturi)


class Circle(Shape):
    def __init__(self, coords, raza, drawingAPI):
        self.coords = coords
        self.raza = raza
        self.drawingAPI = drawingAPI

    def draw(self):
        self.drawingAPI.draw(self.coords, self.raza)


class Rectangle(Shape):
    def __init__(self, coords, laturi, drawingAPI):
        self.coords = coords
        self.laturi = laturi
        self.drawingAPI = drawingAPI

    def draw(self):
        self.drawingAPI.draw(self.coords, self.laturi)

if __name__ == '__main__':

    circle = Circle((0,0),2,DrawingCircleAPI())

    rectangle = Rectangle([(0,0),(0,1),(1,0),(1,1)],[1,1],DrawingRectAPI())

    circle.draw()
    rectangle.draw()