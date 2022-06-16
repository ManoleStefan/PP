import abc
from abc import ABC


class MyException(Exception):
    def __init__(self, message, type):
        super(MyException, self).__init__(message)
        self.message = message
        self.type = type

    def getType(self):
        return self.type

    def getMessage(self):
        return self.message


class IStrategy(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def treat(self, message):
        pass


class ErrorStrategy(IStrategy):
    def treat(self, message):
        f = open("common_errors.txt", "a")
        f.write("Error: " + message)
        print("Error: " + message)


class WarningStrategy(IStrategy):
    def treat(self, message):
        f = open("warnings.txt", "a")
        f.write("Warning: " + message)


class CriticalStrategy(IStrategy):
    def treat(self, message):
        f = open("critical_errors.txt", "a")
        f.write("Critical: " + message)
        exit(-1)


class UnknownStrategy(IStrategy):
    def treat(self, message):
        print("Unknown: " + message)


class IExceptionClassManager(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def createTreatStrategy(self, customException) -> IStrategy:
        pass

    @abc.abstractmethod
    def resolveException(self):
        pass


class MyExceptionManager(IExceptionClassManager):
    def __init__(self):
        self.myStrategy = UnknownStrategy()
        self.message = ""

    def createTreatStrategy(self, customException):
        #print("Create Strategy")
        if isinstance(customException, MyException):
            #print("Exceptia mea boss")
            self.message = customException.getMessage()
            typeNumber = customException.getType()
            if typeNumber == 2:
                self.myStrategy = WarningStrategy()
                return
            if typeNumber == 1:
                self.myStrategy = ErrorStrategy()
                return
            if typeNumber == 0:
                self.myStrategy = CriticalStrategy()
                return
            self.myStrategy = UnknownStrategy()
        else:
            self.myStrategy = UnknownStrategy()

    def resolveException(self):
        self.myStrategy.treat(self.message)


if __name__ == '__main__':
    case = 0
    exceptionManager = MyExceptionManager()

    try:
        if case == 2:
            raise MyException("MyWarning Message", 2)

        if case == 1:
            raise MyException("MyError Message", 1)

        if case == 0:
            raise MyException("MyCritical Message", 0)
    except MyException as e:
        exceptionManager.createTreatStrategy(e)
        exceptionManager.resolveException()

