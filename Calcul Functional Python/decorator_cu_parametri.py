class ornamentcuparametri(object):
    def __init__(self,par1,par2,par3):
        self.par1 = par1
        self.par2 = par2
        self.par3 = par3

    def __call__(self,f):
        def functieimpachetata(*args):
            print("Argumentele decoratorului : ", self.par1,self.par2,self.par3)
            f(*args)
        return functieimpachetata

@ornamentcuparametri("vreau","sa merg",42)
def sayHello(a1,a2,a3,a4):
    print("{} {} {} {}".format(a1,a2,a3,a4))


sayHello("ma","duc","la","bere")
