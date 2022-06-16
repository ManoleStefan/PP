from threading import *

sem = Semaphore()

class Command(Thread):
    def __init__(self,receiver):
        super().__init__()
        self.receiver = receiver

    def execute(self):
        pass

class Invoker:
    def __init__(self):
        self.commands = []

    def setCommands(self,command):
        self.commands.append(command)

    def executeCommands(self):
        for i in self.commands:
            t = Thread(target=i.execute)
            t.start()

class AddCommand(Command):
    def __init__(self,receiver):
        super().__init__(receiver)

    def execute(self):
        l = self.receiver
        global sem

        sem.acquire()

        for k, v in l.items():
            l[k] = v + 1

        self.receiver = l
        print(self.receiver)
        sem.release()

class SubCommand(Command):
    def __init__(self,receiver):
        super().__init__(receiver)

    def execute(self):
        l = self.receiver
        global sem

        sem.acquire()

        for k, v in l.items():
            l[k] = v - 2

        self.receiver = l
        print(self.receiver)
        sem.release()

class MulCommand(Command):
    def __init__(self,receiver):
        super().__init__(receiver)

    def execute(self):
        l = self.receiver
        global sem

        sem.acquire()

        for k, v in l.items():
            l[k] = v * 2

        self.receiver = l
        print(self.receiver)
        sem.release()

if __name__ == '__main__':
    inv = Invoker()

    hm = {1:11,2:20,3:33}

    inv.setCommands(AddCommand(hm))
    inv.setCommands(SubCommand(hm))
    inv.setCommands(MulCommand(hm))

    inv.executeCommands()
    


