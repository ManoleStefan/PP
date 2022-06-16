import threading
import queue
import time
import random

class Producator(threading.Thread):
    def __init__(self,queue):
        super().__init__()
        self.queue = queue

    def run(self):
        for i in range(50):
            element = random.randint(0,256)
            self.queue.put(element)
            print("Mesaj de la producator : {} adaugat in coada".format(element))
            time.sleep(1)

class Consumator(threading.Thread):
    def __init__(self,queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            element = self.queue.get()
            print("Mesaj de la consumator : {} scos din coada de {}".format(element,self.name))
            self.queue.task_done()

if __name__ == "__main__":
    coada = queue.Queue()
    t1 = Producator(coada)
    t2 = Consumator(coada)
    t3 = Consumator(coada)
    t4 = Consumator(coada)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()