import copy

listaNumere = [2 * i + 1 for i in range(28)]

listaNumereNormale = [i for i in range(28)]
fermoar = zip(listaNumereNormale,listaNumere)

fermoar1 = copy.deepcopy(fermoar)
print(list(fermoar))

stanga = (x[0] for x in fermoar1)
dreapta = (x[1] for x in fermoar1)

print(list(stanga))
print(list(dreapta))