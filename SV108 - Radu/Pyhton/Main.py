from abc import abstractmethod


class AbstractSecurity:
    MUSEUM_GUARDIAN = 5
    POLICE = 4
    SRI = 3
    SIE = 2
    CSAT = 1
    NATO = 0

    _next = None
    _level: int

    def set_next_in_chain(self, next_in_chain):
        self._next = next_in_chain

    def process_message(self, level, message):
        if self._level <= level:
            self.process(message)
        else:
            self._next.process_message(level, message)

    @abstractmethod
    def process(self, message):
        pass


class MuseumGuardian(AbstractSecurity):

    def __init__(self, level):
        self._level = level

    def process(self, message):
        print("I'm the guardian and I can do that: " + message)


class Police(AbstractSecurity):

    def process(self, message):
        print("The police wil solve that: " + message)

    def __init__(self, level):
        self._level = level


class SRI(AbstractSecurity):

    def __init__(self, level):
        self._level = level

    def process(self, message):
        print("We are the SRI, we take that: " + message)


class SIE(AbstractSecurity):

    def __init__(self, level):
        self._level = level

    def process(self, message):
        print("This is SIE: " + message)


class CSAT(AbstractSecurity):

    def __init__(self, level):
        self._level = level

    def process(self, message):
        print("CSAT: " + message)


class NATO(AbstractSecurity):

    def __init__(self, level):
        self._level = level

    def process(self, message):
        print("NATO: " + message)


class SecurityChain:

    @staticmethod
    def get_security_chain() -> AbstractSecurity:
        guardian = MuseumGuardian(AbstractSecurity.MUSEUM_GUARDIAN)
        police = Police(AbstractSecurity.POLICE)
        sri = SRI(AbstractSecurity.SRI)
        sie = SIE(AbstractSecurity.SIE)
        csat = CSAT(AbstractSecurity.CSAT)
        nato = NATO(AbstractSecurity.NATO)

        guardian.set_next_in_chain(police)
        police.set_next_in_chain(sri)
        sri.set_next_in_chain(sie)
        sie.set_next_in_chain(csat)
        csat.set_next_in_chain(nato)

        return guardian


if __name__ == '__main__':
    security_chain = SecurityChain.get_security_chain()

    security_chain.process_message(4, "Get the thief!")
    security_chain.process_message(5, "Close the museum!")
    security_chain.process_message(1, "Someone has stolen a statue!")
    security_chain.process_message(3, "Someone robbed the bank!")
    security_chain.process_message(2, "Someone has a gun!")
    security_chain.process_message(0, "There is a murder!")
