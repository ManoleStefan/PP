import multiprocessing
import time
import datetime as dt

def test_bariera(barrier,lock):
    name = multiprocessing.current_process().name
    barrier.wait()
    now = time.time()
    with lock:
        print("Procesul {}   -----> {}".format(name,dt.datetime.fromtimestamp(now)))

def test_fara_bariera():
    name = multiprocessing.current_process().name
    now = time.time()
    print("Procesul {} -----> {}".format(name,dt.datetime.fromtimestamp(now)))


if __name__ == "__main__":
    barrier = multiprocessing.Barrier(2)
    lock = multiprocessing.Lock()
    multiprocessing.Process(name="p1-test_cu_bariera",target=test_bariera,args=(barrier,lock)).start()
    multiprocessing.Process(name="p2-test_cu_bariera",target=test_bariera,args=(barrier,lock)).start()
    multiprocessing.Process(name="p3-test_fara_bariera",target=test_fara_bariera).start()
    multiprocessing.Process(name="p4-test_fara_bariera",target=test_fara_bariera).start()