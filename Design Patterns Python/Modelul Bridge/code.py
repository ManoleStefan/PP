class DrawAPI:
    def drawCircle(self,x,y,radius) : pass

class DrawAPIOne(DrawAPI):
    def drawCircle(self,x,y,radius):
        print("API 1 deseneaza un cerc de coordonate ({},{}) cu raza {}.".format(x,y,radius))

class DrawAPITwo(DrawAPI):
    def drawCircle(self,x,y,radius):
        print("API 1 deseneaza un cerc de coordonate ({},{}) cu raza {}.".format(x,y,radius))

class Circle:
    def __init__(self,x,y,radius,DrawingAPI):
        self.x = x
        self.y = y
        self.radius = radius
        self.API = DrawingAPI

    def draw(self):
        self.API.drawCircle(self.x,self.y,self.radius)


FirstAPI = DrawAPIOne()
SecondAPI = DrawAPITwo()
c1 = Circle(2,3,4,FirstAPI)
c2 = Circle(5,6,7,SecondAPI)
c1.draw()
c2.draw()