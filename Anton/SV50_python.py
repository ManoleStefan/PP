from abc import ABC, abstractmethod
from datetime import datetime


class RecalculatorPret(ABC):

    @abstractmethod
    def recalculare_pret(self, user, password, pret) -> None:
        pass


class RealRecalculatorPret(RecalculatorPret):

    def recalculare_pret(self, user, password, pret) -> None:
        print("Real Calculator: Handling request cu recalculare cu pretul " + str(pret))


class Logger(RecalculatorPret):

    def __init__(self, subiect: RealRecalculatorPret) -> None:
        self._real_subject = subiect

    def recalculare_pret(self, user, password, pret) -> None:
        if self.check_access(user, password):
            self._real_subject.recalculare_pret(user, password, pret)
            self.log_access(user, pret)

    @staticmethod
    def check_access(user, password) -> bool:
        if user == "unu" and password == "doi":
            print("Proxy: Verific accesul utilizatorului")
            return True
        return False

    @staticmethod
    def log_access(user, pret) -> None:
        f = open("log.txt", "a+")
        f.write(user + " a schimbat pretul la " + str(pret) + " la data " + str(datetime.now()) + "\n")


def client_code(subject: RecalculatorPret, user, password, pret) -> None:
    subject.recalculare_pret(user, password, pret)


if __name__ == "__main__":
    real_subject = RealRecalculatorPret()
    proxy = Logger(real_subject)
    client_code(proxy, "unu", "doi", 14)
