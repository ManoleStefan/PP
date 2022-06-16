numere = [1,2,3,4,5]

def doiX(x):
    return x * 2

def laPatrat(x):
    return x ** 2

listaProcesata = []
for i in numere:
    listaProcesata = listaProcesata + list(map(lambda x : x(i),(doiX,laPatrat)))
print(listaProcesata)

listaProcesata1 = []
for i in numere:
    listaProcesata1 = listaProcesata1 + list(map(lambda x : x(i),(lambda x : x + x , lambda x : x ** 2)))

print(listaProcesata1)