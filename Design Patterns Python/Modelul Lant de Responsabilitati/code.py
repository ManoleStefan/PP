import abc

class Handler(metaclass=abc.ABCMeta):
    def __init__(self,succesor = None):
        self.succesor = succesor

    def handle(self,request):
        res = self.check_range(request)
        if not res and self.succesor:
            self.succesor.handle(request)

    @abc.abstractmethod
    def check_range(self,request):
        """compara valoarea primita cu un interval predefinit"""

class ConcreteHandler0(Handler):
    @staticmethod
    def check_range(request):
        if 0 <= request < 10:
            print("cererea {} tratata in gestionarul 0".format(request))
            return True

class ConcreteHandler1(Handler):
    start,end = 10,20
    def check_range(self,request):
        if self.start <= request < self.end:
            print("cererea {} tratata in gestionarul 1".format(request))
            return True

class ConcreteHandler2(Handler):
    def check_range(self,request):
        start,end = self.get_interval_from_db()
        if start <= request < end:
            print("cererea {} tratata in gestionarul 2".format(request))
            return True

    @staticmethod
    def get_interval_from_db():
        return (20,30)

class FallBackHandler(Handler):
    @staticmethod
    def check_range(request):
        print("am terminat de parcurs lantul - nu exista tratare pentru cazul {}".format(request))
        return False

h0 = ConcreteHandler0()
h1 = ConcreteHandler1()
h2 = ConcreteHandler2()
h3 = FallBackHandler()
h0.succesor = h1
h1.succesor = h2
h2.succesor = h3
requests = [2,5,14,22,18,3,35,27,20]
for request in requests:
    h0.handle(request)