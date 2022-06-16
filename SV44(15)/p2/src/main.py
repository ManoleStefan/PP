
class Camera:
    def __init__(self,numar:int,nr_paturi:int,status:str,pret:int):
        self.numar = numar
        self.nr_paturi =nr_paturi
        self.status = status
        self.pret = pret

    def ocupaCamera(self):
        self.status = "OCUPAT"

    def elibereazaCamera(self):
        self.status = "LIBER"

def price_decorator(f):
    def wrapper(*args):
        if args[0].camere[args[1]].pret >100:
            args[0].camere[args[1]].pret += 50
        return f(*args)
    return wrapper

class Hostel:
    def __init__(self,camere):
        self.camere = camere

    def rezerva(self):
        for i in self.camere:
            if i.status == "LIBER":
                i.ocupaCamera()
                break

    def rezerva(self,nr):
        self.camere[nr].ocupaCamera()


    @price_decorator
    def elibereaza(self,nr):
        self.camere[nr].elibereazaCamera()

def price_calc(camera):
    if(camera.pret > 100):
        camera.pret += 50
    return camera

if __name__ == '__main__':
    camere = []
    camere.append(Camera(1,2,"LIBER",90))
    camere.append(Camera(2,3,"LIBER",100))
    camere.append(Camera(3,3,"LIBER",110))
    camere.append(Camera(4,2,"LIBER",120))
    camere.append(Camera(5,2,"LIBER",100))

    hostel = Hostel(camere)


    hostel.elibereaza(2)

    print(hostel.camere[2].pret)


