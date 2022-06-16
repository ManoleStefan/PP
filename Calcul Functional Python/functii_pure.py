import copy
from functools import reduce
x = int(input("Numar = "))

calculNumereMersenne = lambda x : 2**x - 1
print("Tipul variabile calculNumereMersenne este {}".format(type(calculNumereMersenne)))

print("mersenne({}) = {}".format(x,calculNumereMersenne(x)))

lista = [50,71,11,97,54,62,77]


rezultat = list(filter(lambda x : (x % 2 == 0),lista))
print(rezultat)

rezultat = list(map(lambda x : (x * 2),lista))
print(rezultat)

suma = reduce((lambda x,y : x + y),lista)

print("Sume elementelor din lista este : {}".format(suma))