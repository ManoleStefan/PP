'''
class ornament(object):
    def __init__(self,f):
        print("sunt in constructorul decoratorului")
        f()

    def __call__(self):
        print("sunt in decorator")


@ornament
def functie1():
    print("Sunt in interiorul functiei decorate")

functie1()


'''


class ornament(object):
    def __init__(self,f):
        self.f = f
    def __call__(self):
        print("Intru in corp decorator ",self.f.__name__)
        self.f()
        print("Ies din corp decorator ",self.f.__name__)

@ornament
def functia1():
    print("sunt in functia1")



@ornament
def functia2():
    print("sunt in functia2")


functia1()
functia2()