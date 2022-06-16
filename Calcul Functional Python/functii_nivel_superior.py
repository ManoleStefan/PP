from functools import reduce
lista = [50,71,11,97,54,62,77]

rezultat = min(max(list(filter(lambda x : (x % 2 == 0),lista))), min(list(map(lambda x : (x*2),lista))), reduce((lambda x,y : x+y),lista))

print("Rezultatul unei functii de nivel superior : {}".format(rezultat))