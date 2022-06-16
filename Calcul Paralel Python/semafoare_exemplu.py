import threading
import time
import random

semafor = threading.Semaphore(0)

def consumator():
    print('Consumatorul in asteptare')
    semafor.acquire()
    print('Consumatorul a fost anuntat si a folosit {} elemente.'.format(element))

def producator():
    global element
    time.sleep(1)
    element = random.randint(0,1000)
    print('Producatorul a fost anuntat si a produs {} elemente.'.format(element))
    semafor.release()

if __name__ == "__main__":
    for i in range(5):
        t1 = threading.Thread(target=consumator)
        t2 = threading.Thread(target=producator)
        t1.start()
        t2.start()
        t1.join()
        t2.join()

