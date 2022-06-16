import time
nrIteratii = 20000000

def f(k):
    return 2 * k

def benchmark(functie,numefunctie):
    start = time.time()
    functie()
    stop = time.time()
    print("Calculul a durat {} secunde pentru {}".format(stop - start,numefunctie))

def listaA():
    listaA = []
    for i in range(nrIteratii):
        listaA.append(f(i))

def listaB():
    listaB = [f(i) for i in range(nrIteratii)]

def listaC():
    listaC = list(map(f,range(nrIteratii)))

benchmark(listaA,"structurata")
benchmark(listaB,"functional")
benchmark(listaC,"operator dedicat")

