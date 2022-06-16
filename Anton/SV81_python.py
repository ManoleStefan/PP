from __future__ import annotations
from abc import ABC, abstractmethod
from numpy import random


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


class SimpleCommand(Command):
    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(f"Studentul zice: "f"({self._payload})")


class ComplexCommand(Command):
    def __init__(self, receiver: Colega, a: str, b: str) -> None:
        self._receiver = receiver
        self._a = a
        self._b = b

    def execute(self) -> None:
        if random.randint(2) == 1:
            self._receiver.raspunde_bine(self._a)
        else:
            self._receiver.raspunde_rau(self._b)


class Colega:
    @staticmethod
    def raspunde_bine(a: str) -> None:
        print(f"\nColega: Raspund bine la ({a}.)", end="")
        Student.state = "fericit"

    @staticmethod
    def raspunde_rau(b: str) -> None:
        print(f"\nColega: Raspund rau la ({b}.)", end="")
        Student.state = "anxios"


class Student:
    _on_start = None
    _on_finish = None
    state = "neutru"

    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def reactioneaza_la_ce_a_zis_colega(self) -> None:
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        if isinstance(self._on_finish, Command):
            self._on_finish.execute()


if __name__ == "__main__":
    invoker = Student()
    invoker.set_on_start(SimpleCommand("Buna"))
    print("\n" + invoker.state)
    receiver = Colega()
    invoker.set_on_finish(ComplexCommand(receiver, "Buna", "Salutari"))
    invoker.reactioneaza_la_ce_a_zis_colega()
    print("\n" + invoker.state)
