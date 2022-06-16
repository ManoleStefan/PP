from abc import ABC, abstractmethod


class Memento(ABC):
    @abstractmethod
    def get_state(self):
        pass


class Originator:
    _state = None

    def __init__(self, state):
        self._state = state

    def f1(self):
        self._state = list(map(lambda x: x + 1 if x % 2 == 0 else x, self._state))

    def f2(self):
        self._state = list(map(lambda x: (3 * x * x) - (2 * x) + 1, self._state))

    def f3(self):
        self._state = list(map(lambda x, y: x + y, self._state, self._state))

    def save(self) -> Memento:
        return ConcreteMemento(self._state)

    def restore(self, memento: Memento):
        self._state = memento.get_state()

    def get_list(self) -> list:
        return self._state


class ConcreteMemento(Memento, ABC):

    def __init__(self, state):
        self._state = state

    def get_state(self) -> list:
        return self._state


class Caretaker:

    def __init__(self, originator: Originator):
        self._mementos = []
        self._originator = originator

    def backup(self):
        print("Saving state...")
        self._mementos.append(self._originator.save())

    def undo(self):
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        print("Restoring state...")
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()


if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    o = Originator(my_list)
    caretaker = Caretaker(o)

    caretaker.backup()
    print(o.get_list())

    o.f1()
    print(o.get_list())

    caretaker.undo()
    print(o.get_list())
    caretaker.backup()

    o.f2()
    print(o.get_list())

    caretaker.undo()
    print(o.get_list())
    caretaker.backup()

    o.f3()
    print(o.get_list())

    caretaker.undo()
    print(o.get_list())
