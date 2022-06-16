import multiprocessing
def worker(dictionary,cheie,element,contor):
    lock = multiprocessing.Lock()
    with lock:
        contor[0] += 1
    dictionary[cheie] = element
    print("Cheie : {}, valoare : {}, sunt la al {} - lea apel".format(cheie,element,contor[0]))

if __name__ == "__main__":
    manager = multiprocessing.Manager()
    dictionary = manager.dict()
    contor = manager.list([0])
    contor[0] = 0
    sarcini = [multiprocessing.Process(target=worker,args=(dictionary,i,i*2,contor)) for i in range(5)]
    for treaba in sarcini:
        treaba.start()
    for treaba in sarcini:
        treaba.join()
    print("Rezultate : ",dictionary)