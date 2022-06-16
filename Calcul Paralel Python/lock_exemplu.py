import threading

contor_cu_lock = 0
contor_fara_lock = 0
COUNT = 1000000
lock_contor = threading.Lock()

def safe_inc():
    global contor_cu_lock
    for _ in range(COUNT):
        lock_contor.acquire()
        contor_cu_lock += 1
        lock_contor.release()

def safe_dec():
    global contor_cu_lock
    for _ in range(COUNT):
        lock_contor.acquire()
        contor_cu_lock -= 1
        lock_contor.release()

def unsafe_inc():
    global contor_fara_lock
    for _ in range(COUNT):
        contor_fara_lock += 1

def unsafe_dec():
    global contor_fara_lock
    for _ in range(COUNT):
        contor_fara_lock -= 1


if __name__ == "__main__":
    t1 = threading.Thread(target = safe_inc)
    t2 = threading.Thread(target= safe_dec)
    t3 = threading.Thread(target = unsafe_inc)
    t4 = threading.Thread(target= unsafe_dec)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

    print("Variabila comuna gestionata cu lock",contor_cu_lock)
    print("Variabila comuna gestionata fara lock",contor_fara_lock)
