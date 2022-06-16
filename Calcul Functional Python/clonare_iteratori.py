import itertools as it
numere = [i for i in range(11)]
def calcul(lista):
    it0,it1 = it.tee(lista,2)
    s0 = sum(1 for x in it0)
    s1 = sum(x for x in it1)
    return s1/s0

print(calcul(numere))