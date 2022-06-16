lista1 = list(range(11,17))
f1 = lambda x : x*2
f2 = lambda x : x+2
f3 = lambda x : round(x/2)
tabelFunctii = [f1,f2,f3]

compunereFunctii = lambda tabelFunctii, *args,: [list(map(functie,*args)) for functie in tabelFunctii]
lista = compunereFunctii([f1,f2,f3],lista1)
print(lista)

