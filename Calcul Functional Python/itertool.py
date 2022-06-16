from itertools import *

numar = count(start = 1,step = 1)
numere = [next(numar) for _ in range(10)]

def grupareOptimizata(lista,numarTuple):
    iteratori = [iter(lista)] * numarTuple
    return zip(*iteratori)

print(list(grupareOptimizata(numere,2)))
print(list(grupareOptimizata(numere,4)))

def grupareOptimizataCuPadding(lista,numarTuble,valoareCompletare = None):
    iteratori = [iter(lista)] * numarTuble
    return zip_longest(*iteratori,fillvalue=valoareCompletare)

print(list(grupareOptimizataCuPadding(numere,4,1231313114131)))


print(list(combinations(numere,3)))

seturicusuma12 = []
for i in range(1,len(numere) + 1):
    for combinatie in combinations(numere,i):
        if sum(combinatie) == 12:
            seturicusuma12.append(combinatie)
seturicusuma12.append((2,10))
print(seturicusuma12)

seturiUniceCuSuma12 = set(seturicusuma12)
print(seturiUniceCuSuma12)

seturicusuma12SiInlocuire = []
for i in range(1,len(numere) + 1):
    for combinatie in combinations_with_replacement(numere,i):
        if sum(combinatie) == 12:
            seturicusuma12SiInlocuire.append(combinatie)

print(seturicusuma12SiInlocuire)