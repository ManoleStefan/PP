class Bird:
    def fly(self): pass
    def makeEggs(self): pass
    def sing(self): pass

class Cioara(Bird):
    def fly(self):
        print("Cioara zboara")

    def makeEggs(self):
        print("Cioara face oua")

    def sing(self):
        print("Cioara face cra cra")


class Porumbel(Bird):
    def fly(self):
        print("Porumbelul zboara")

    def makeEggs(self):
        print("Porumbelul face oua")

    def sing(self):
        print("Porubelul face gru gru")


class ToyBird:
    def valability(self): pass
    def scartaie(self,):pass

class PorumbelDeJucarie(ToyBird):
    def __init__(self,pasare):
        self.pasare = pasare

    def valability(self):
        print("123 zile")

    def scartaie(self):
        print("Pasarea de jucarie ")
        self.pasare.sing()



cioara = Cioara()
cioara.sing()
porumbel = Porumbel()
porumbel.sing()
jucarie = PorumbelDeJucarie(porumbel)
jucarie.scartaie()


