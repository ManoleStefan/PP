'''
    True and print("and cu true")
    False and print("and cu false")
    1 and print("and cu unu")
    0 and print("and cu zero")
    True or print("or cu true")
    False or print("or cu false")
'''


def numere(n: int):
    for i in range(n):
        print(f"Generatorul genereaza {i}")
        yield i

def sumaPrimelorN(n : int):
    suma = 0
    for i in numere(n):
        if i == n:
            break
        suma += i
    return suma

def sumaPrimelorN1(n : int):
    suma = 0
    for i in range(n):
        suma += i
    return suma

def sumaPrimelorN2(n : int):
    suma   = 0
    i : int = 0
    while True:
        suma += i
        i += 1
        if i>=n:
            break
    return suma

x = 6
print("Sumare cu generator {}".format(sumaPrimelorN(x)))
print("Sumare cu range {}".format(sumaPrimelorN1(x)))
print("Sumare clasica {}".format(sumaPrimelorN2(x)))





