import threading

def printf(name,message):
    print("({})   :   {}".format(name,message))

def thread_cu_with(statement):
    with statement:
        printf(statement,"achizionat cu with.")

def thread_fara_with(statement):
    statement.acquire()
    try:
        printf(statement,"achizitionat direct.")
    finally:
        statement.release()

if __name__ == "__main__":
    lock = threading.Lock()
    rlock = threading.RLock()
    conditie = threading.Condition()
    mutex = threading.Semaphore(1)
    threading_sync_list = [lock,rlock,conditie,mutex]
    for statement in threading_sync_list:
        t1 = threading.Thread(target=thread_cu_with,args=(statement,))
        t2 = threading.Thread(target=thread_fara_with,args=(statement,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()