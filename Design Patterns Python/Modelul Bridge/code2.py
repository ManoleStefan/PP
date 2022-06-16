class Construire:
    def __init__(self,name):
        self.name = name
    def construire(self,lungime,latime):
        print("{} realizeaza obiectul de {} L si {} l.".format(self.name,lungime,latime))


class Asamblare:
    def __init__(self,name):
        self.name = name
    def asamblare(self,culoare):
        print("{} impacheteaza obiectul {}.".format(self.name,culoare))


class Vehicle:
    def __init__(self,tip,lungime,latime,culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare
        self.tip = tip

    def build(self,builder):
        print("{} : ".format(self.tip),end="")
        builder.construire(self.lungime,self.latime)

    def assemble(self,assembler):
        print("{} : ".format(self.tip),end="")
        assembler.asamblare(self.culoare)


Toyota = Construire("Toyota")
Apple = Asamblare("Apple")
masina = Vehicle("masina",200,100,"rosie")
masina.build(Toyota)
masina.assemble(Apple)


