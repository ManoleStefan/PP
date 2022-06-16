class Subject(object):
    def __init__(self):
        self._observers = []

    def attach(self,observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self,observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            print("Observer not in this list.")

    def notify(self,modifier = None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)

class Data(Subject):
    def __init__(self,name=""):
        Subject.__init__(self)
        self.name = name
        self._data = 0

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self,value):
        self._data = value
        self.notify()

class HexViewer:
    def update(self,subject):
        print(u'Format Hexa : Subiectul %s are valoarea 0x%x'%(subject.name,subject.data))

class DecimalViewer:
    def update(self,subject):
        print(u'Format Zecimal : Subiectul %s are valoarea %d'%(subject.name,subject.data))



data1 = Data('Data 1')
data2 = Data('Data 2')

view1 = DecimalViewer()
view2 = HexViewer()

data1.attach(view1)
data1.attach(view2)
data2.attach(view1)
data2.attach(view2)

print(u"Stabilim valoarea 11 = 10")
data1.data = 10

print(u"Stabilim valoarea 12 = 15")
data2.data = 15

print(u"Stabilim valoarea 11 = 3")
data1.data = 3

print(u"Stabilim valoarea 12 = 5")
data2.data = 5

print(u"Nu mai utilizam afisarea Hexa pentru data1 si data2")

data1.detach(view2)
data2.detach(view2)

print(u"Stabilim valoarea 11 = 10")
data1.data = 10

print(u"Stabilim valoarea 12 = 15")
data2.data = 15

