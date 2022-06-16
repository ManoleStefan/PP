import multiprocessing
import random
import time

class Producator(multiprocessing.Process):
    def __init__(self,queue):
        super().__init__()
        self.queue = queue

    def run(self):
        for _ in range(10):
            element = random.randint(0,256)
            self.queue.put(element)
            print("P : {} adaugat in coada".format(element))
            print("Dim. coada : {}".format(self.queue.qsize()))

class Consumator(multiprocessing.Process):
    def __init__(self,queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            element = self.queue.get()
            print("C : {} scos din coada.".format(element))


if __name__ == "__main__":
    queue = multiprocessing.Queue()
    prod = Producator(queue)
    cons = Consumator(queue)
    prod.start()
    time.sleep(0.01)
    cons.start()
    prod.join()
    cons.join()