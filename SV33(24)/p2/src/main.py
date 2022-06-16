import time
import datetime

class Furnica:
    def __init__(self,nume):
        self.__nume = nume

    def getNume(self):
        return self.__nume

    def send(self,msg):
        Mediator.showMessage(self,msg)

class Mediator:
    @staticmethod
    def showMessage(f:Furnica,msg:str):
        print(f"{datetime.datetime.now()} {f.getNume()}: {msg}")

if __name__ == '__main__':
    f1 = Furnica("Bobi")
    f2 = Furnica("Cody")

    f1.send("Am terminat treaba")
    f2.send("Ma duc sa mananc")