import time
import threading
import random

elemente = []
eveniment = threading.Event()

class Consumator(threading.Thread):
    def __init__(self,elemente,event):
        super().__init__()
        self.elemente = elemente
        self.eveniment = event

    def run(self):
        for i in range(5):
            self.eveniment.wait()
            try:
                item = self.elemente.pop()
            except IndexError:
                print("Nu pot scoate dintr-o coada goala!")
            print("\nMesaj de la consumator : %d a fost generat de %s"%(item,self.name))

class Producator(threading.Thread):
    def __init__(self,elemente,event):
        super().__init__()
        self.elemente = elemente
        self.eveniment = event

    def run(self):
        for i in range(5):
            item = random.randint(0,256)
            self.elemente.append(item)
            print("\nMesaj de la producator : %d a fost adaugat de %s"%(item,self.name))
            self.eveniment.set()
            print("Mesaj de la producator : evenimentul a fost anulat de %s"%self.name)
            self.eveniment.clear()

if __name__ == "__main__":
    t1 = Producator(elemente,eveniment)
    t2 = Consumator(elemente,eveniment)
    t1.start()
    t2.start()
    t1.join()
    t2.join()