def fabricaDeContoare():
    contorvar = 0
    def contor():
        nonlocal contorvar
        contorvar += 1
        return contorvar
    def valoareCurentaContor():
        nonlocal contorvar
        return contorvar
    return contor,valoareCurentaContor

contor,valoarecontor = fabricaDeContoare()
print(contor())
print(contor())
print(contor())
print(valoarecontor())

numarator2 ,num = fabricaDeContoare()
print(numarator2())
print(numarator2())
print(numarator2())