import abc


class Exceptia:
    def __init__(self, strategy):
        self._strategy = strategy

    def trateaza_exceptia(self):
        self._strategy.message_interface()


class Manager:
    def __init__(self):
        self.x = WarningStrategy()
        self.y = LightErrorStrategy()
        self.z = CriticalErrorStrategy()
        self.exception3 = Exceptia(self.z)
        self.exception2 = Exceptia(self.y)
        self.exception1 = Exceptia(self.x)

    def call(self, num):
        if num == 1:
            self.exception1.trateaza_exceptia()
        if num == 2:
            self.exception2.trateaza_exceptia()
        if num == 3:
            self.exception3.trateaza_exceptia()


class Strategy(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def message_interface(self):
        pass


class WarningStrategy(Strategy):
    def message_interface(self):
        f = open("warning.txt", "a+")
        f.write("The error is a warning level 2\n")


class LightErrorStrategy(Strategy):
    def message_interface(self):
        print("The error is a warning level 1")
        f = open("light_error.txt", "a+")
        f.write("The error is a warning level 1\n")


class CriticalErrorStrategy(Strategy):
    def message_interface(self):
        f = open("critical_error.txt", "a+")
        f.write("The error is critical level 0\n")
        print("Program stopped")


def main():
    manager = Manager()
    manager.call(3)


if __name__ == "__main__":
    main()
