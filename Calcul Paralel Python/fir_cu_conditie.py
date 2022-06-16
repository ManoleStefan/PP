import threading
import time

elemente = []

conditie = threading.Condition()

class Cosumator(threading.Thread):
    def __init__(self):
        super().__init__()

    def consumator(self):
        global conditie
        global elemente
        conditie.acquire()
        if len(elemente) == 0:
            conditie.wait()
            print('mesaj de la consumator : nu am nimic disponibil')
        elemente.pop()
        print('mesaj de la consumator : am utilizat un element')
        print('mesaj de la consumator : mai am {} elemente disponibile'.format(len(elemente)))
        conditie.notify()
        conditie.release()

    def run(self):
        for i in range(5):
            self.consumator()

class Producator(threading.Thread):
    def __init__(self):
        super().__init__()

    def producator(self):
        global conditie
        global elemente
        conditie.acquire()
        if(len(elemente) == 10):
            conditie.wait()
            print('mesaj de la producator : am disponibile {} elemente.'.format(len(elemente)))
            print('mesaj de la producator : am oprit productia')
        elemente.append(1)
        print('mesaj de la producator : am produs {} elemente'.format(len(elemente)))
        conditie.notify()
        conditie.release()

    def run(self):
        for i in range(5):
            self.producator()

if __name__ == "__main__":
    producator = Producator()
    consumator = Cosumator()
    producator.start()
    consumator.start()
    producator.join()
    consumator.join()