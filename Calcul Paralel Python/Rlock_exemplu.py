import threading
import time

class Cutiechibrituri(object):
    lock = threading.RLock()
    def __init__(self):
        self.total_chibrituri = 0

    def execute(self,n):
        Cutiechibrituri.lock.acquire()
        self.total_chibrituri += n
        Cutiechibrituri.lock.release()

    def pun(self):
        #Cutiechibrituri.lock.acquire()
        self.execute(1)
        #Cutiechibrituri.lock.release()

    def scot(self):
        #Cutiechibrituri.lock.acquire()
        self.execute(-1)
        #Cutiechibrituri.lock.release()

def pune(Cutiechibrituri,chibrituri):
    while(chibrituri > 0):
        print("Pun un chibrit in cutie.\n")
        Cutiechibrituri.pun()
        time.sleep(1)
        chibrituri -= 1

def scoate(Cutiechibrituri,chibrituri):
    while(chibrituri > 0):
        print("Scot un chibrit din cutie.\n")
        Cutiechibrituri.scot()
        time.sleep(1)
        chibrituri -= 1


if __name__ == "__main__":
    chibrituri = 5
    cutie = Cutiechibrituri()
    print("Operam cu {} chibrituri.".format(chibrituri))
    t2 = threading.Thread(target=scoate,args=(cutie,chibrituri))
    t1 = threading.Thread(target=pune,args=(cutie,chibrituri))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Mai sunt {} chibrituri in cutie".format(cutie.total_chibrituri))