import concurrent.futures as cf
import time

lista_numere = list(range(1,10))

def numara(numar):
    i = 0
    for i in range(10**7):
        i += 1
    return i * numar

def evaluare(element):
    element_rezultat = numara(element)
    #print("Element %s  ---->   Rezultat %s"%(element,element_rezultat))

if __name__ == "__main__":
    #secvential
    start = time.time()
    for element in lista_numere:
        evaluare(element)
    print("\nExecutia secventiala a durat {}\n\n".format(time.time() - start))

    #threadpool
    start = time.time()
    with cf.ThreadPoolExecutor(max_workers=5) as executor:
        for element in lista_numere:
            executor.submit(evaluare,element)

    print("\nExecutia cu threadpool a durat {}\n\n".format(time.time() - start))

    #processpool
    start = time.time()
    with cf.ProcessPoolExecutor(max_workers=5) as executor:
        for element in lista_numere:
            executor.submit(evaluare,element)

    print("\nExecutia cu processpool a durat {}\n\n".format(time.time() - start))