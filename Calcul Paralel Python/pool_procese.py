import multiprocessing
import time
import signal as sig
import sys
def la_patrat(data):
    return data * data

def signal_handler(signal,frame):
    print("A aparut o operatie externa  -->  {}".format(signal))
    pool.terminate()
    pool.join()
    print("Am terminat fortat procesul")
    sys.exit(0)

if __name__ == "__main__":
    intrari = list(range(10))
    pool = multiprocessing.Pool(processes=4)
    sig.signal(sig.SIGINT,signal_handler)
    calcul_pool = pool.map(la_patrat,intrari)
    pool.close()
    pool.join()
    print("Pool : {}".format(calcul_pool))
