listaNumere = [2 * i + 1 for i in range(55)]
print(listaNumere)

listaNumereNormale = [i for i in range(25)]
listaNumerePare = [2*i for i in range(15)]

def isprime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in range(3,int(n**0.5) + 1,2):
        if n % x == 0:
            return False
    return True

if all(isprime(x) for x in listaNumere) : print("Lista numere prime")
if not all(isprime(x) for x in listaNumereNormale) : print("Lista de numere")
if any(not isprime(x) for x in listaNumerePare) : print("Lista de numere")