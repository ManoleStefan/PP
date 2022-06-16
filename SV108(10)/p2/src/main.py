from abc import ABC, abstractmethod


class Handler(ABC):
    @abstractmethod
    def set_next(self,handler):
        pass

    @abstractmethod
    def handle(self,tip,mesaj):
        pass

class AbstractHandler(Handler):

    next_handler = None

    def set_next(self,handler):
        self.next_handler = handler
        return handler

    @abstractmethod
    def handle(self,tip,mesaj):
        if self.next_handler:
            return self.next_handler.handle(tip,mesaj)

        return None

class Paznic(AbstractHandler):

    def handle(self, tip, mesaj):
        if tip == 5:
            return f"Paznic de muzeu am primit mesajul {mesaj}"
        else:
            return super().handle(tip,mesaj)


class Politie(AbstractHandler):

    def handle(self, tip, mesaj):
        if tip == 4:
            return f"Politie am primit mesajul {mesaj}"
        else:
            return super().handle(tip, mesaj)


class SRI(AbstractHandler):

    def handle(self, tip, mesaj):
        if tip == 3:
            return f"SRI am primit mesajul {mesaj}"
        else:
            return super().handle(tip, mesaj)


class SIE(AbstractHandler):

    def handle(self, tip, mesaj):
        if tip == 2:
            return f"SIE am primit mesajul {mesaj}"
        else:
            return super().handle(tip, mesaj)


class CSAT(AbstractHandler):

    def handle(self, tip, mesaj):
        if tip == 1:
            return f"CSAT am primit mesajul {mesaj}"
        else:
            return super().handle(tip, mesaj)


class NATO(AbstractHandler):

    def handle(self, tip, mesaj):
        if tip == 0:
            return f"NATO am primit mesajul {mesaj}"
        else:
            return super().handle(tip, mesaj)

if __name__ == '__main__':
    paznic = Paznic()
    politie = Politie()
    sri = SRI()
    sie = SIE()
    nato = NATO()
    csat = CSAT()

    nato.set_next(csat).set_next(sie).set_next(sri).set_next(politie).set_next(paznic)

    print(nato.handle(0,"Primul mesaj"))
    print(nato.handle(4,"Al doilea mesaj"))
    print(nato.handle(5,"Ultimul mesaj"))