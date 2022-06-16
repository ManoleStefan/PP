from __future__ import annotations
from abc import ABC


class Mediator(ABC):
    def notify(self, sender: object, event: str) -> None:
        pass


class ConcreteMediator(Mediator):
    def __init__(self, component1: Furnica1, component2: Furnica2) -> None:
        self.furnica1 = component1
        self.furnica1.mediator = self
        self.furnica2 = component2
        self.furnica2.mediator = self

    def notify(self, sender: object, event: str) -> None:
        if event == "mancare":
            print("Anunt furnicile ca e mancare la locatia furnicii curente")
            self.furnica2.ajutor()
        elif event == "ajutor":
            print("Daca o furnica cere ajutor:")
            self.furnica1.pericol()
            self.furnica2.drum_bun()


class BaseFurnica:
    def __init__(self, mediator: Mediator = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator


class Furnica1(BaseFurnica):
    def gasit_mancare(self) -> None:
        print("Furnica 1 a gasit mancare.")
        self.mediator.notify(self, "mancare")

    def pericol(self) -> None:
        print("Furnica 1 anunta pericol.")
        self.mediator.notify(self, "pericol")


class Furnica2(BaseFurnica):
    def drum_bun(self) -> None:
        print("Furnica 2 anunta drum bun.")
        self.mediator.notify(self, "drum_bun")

    def ajutor(self) -> None:
        print("Furnica 2 anunta ajutor.")
        self.mediator.notify(self, "ajutor")


if __name__ == "__main__":
    '''
    Ca side note putem elabora exemplul asta si mai mult, facand o clasa Swarm care sa aibe un vector de furnici.
    Cand una dintre furnici anunta ceva putem alege un subset de n furnici dedicate sa raspunda la call.
    Fiecare furnica poate avea caracteristici asemanatoarea unui thread si anume sa fie busy sau free.
    '''
    f1 = Furnica1()
    f2 = Furnica2()
    mediator = ConcreteMediator(f1, f2)
    f1.gasit_mancare()
    print("\n", end="")
    f2.ajutor()
