class EuropeanSocketInterface:
    def earth(self): pass
    def neutral(self): pass
    def voltage(self): pass
    def live(self): pass

class Socket(EuropeanSocketInterface):
    def voltage(self): return 230
    def live(self): return 1
    def neutral(self): return -1
    def earth(self): return 0


class USASocketInterface:
    def voltage(self): pass
    def live(self): pass
    def neutral(self): pass

class Adaptor(USASocketInterface):
    _socket = None
    def __init__(self,socket):
        self._socket = socket

    def voltage(self): return 110
    def live(self): return self._socket.live()
    def neutral(self): return self._socket.neutral()


class ElectricKettlen:
    _power = None
    def __init__(self,power):
        self._power = power

    def boil(self):
        if self._power.voltage() > 110:
            print("Kettle on fire!")
        elif self._power.live() == 1 and self._power.neutral() == -1:
            print("Coffe time!")
        else:
            print("No power!")

socket = Socket()
adapter = Adaptor(socket)
EUkettle = ElectricKettlen(socket)
USkettle = ElectricKettlen(adapter)
print("EU Socket : ", end = "")
EUkettle.boil()
print("US Socket : ",end = "")
USkettle.boil()