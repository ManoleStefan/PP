from threading import Thread
from threading import Lock
import time


class Command(Thread):

    def __init__(self, hm):
        super().__init__()
        self._hm = hm
        self._sem = Lock()
        self._is_running = False

    def execute(self):
        if not self._is_running:
            self.start()
            self._is_running = True
        else:
            self.run()


class HashMapProcess:

    def __init__(self, h):
        self.__adder = HashMapAdd(h)
        self.__sub = HashMapSub(h)
        self.__mul = HashMapMul(h)

    def add(self):
        self.__adder.execute()

    def sub(self):
        self.__sub.execute()

    def mul(self):
        self.__mul.execute()


class HashMapAdd(Command):

    def __init__(self, h):
        super().__init__(h)

    def run(self) -> None:
        self._sem.acquire()
        s = 0
        for i in self._hm:
            if self._hm[i] <= pow(2, 16) - 1:
                s += self._hm[i]
            else:
                raise Exception("Error! Number is too big!")
        print("Sum: " + str(s))
        print("Now sleeping...")
        print()
        time.sleep(1)
        self._sem.release()


class HashMapSub(Command):

    def __init__(self, h):
        super().__init__(h)

    def run(self) -> None:
        self._sem.acquire()
        s = 0
        for i in self._hm:
            if self._hm[i] <= pow(2, 16) - 1:
                s -= self._hm[i]
            else:
                raise Exception("Error! Number is too big!")
        print("Sub: " + str(s))
        print("Now sleeping...")
        print()
        time.sleep(1)
        self._sem.release()


class HashMapMul(Command):

    def __init__(self, h):
        super().__init__(h)

    def run(self) -> None:
        self._sem.acquire()
        p = 1
        for i in self._hm:
            if self._hm[i] <= pow(2, 16) - 1:
                p *= self._hm[i]
            else:
                raise Exception("Error! Number is too big!")
        print("Mul: " + str(p))
        print("Now sleeping...")
        print()
        time.sleep(1)
        self._sem.release()


if __name__ == "__main__":
    my_dict = {0: 10, 1: 20, 2: 30, 3: 40, 4: 50}
    hp = HashMapProcess(my_dict)

    hp.add()
    hp.add()
    hp.mul()
    hp.sub()
    hp.add()
    hp.mul()
    hp.add()
    hp.add()
    hp.sub()
