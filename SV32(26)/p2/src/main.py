from itertools import *

def fabricaDeContoare():
    contorvar = 0
    def contor():
        nonlocal contorvar
        contorvar += 1
        #return contorvar
    def valoareCurentaContor():
        nonlocal contorvar
        return contorvar
    return contor,valoareCurentaContor

def FileReturn(s1,s2,index=0):
    return f"{s1}-index-{s2}.tmp"

def generateFiles(s1,s2,nr):
    contor,valoareContor = fabricaDeContoare()
    l = []

    for i in range(0,nr):
        l.append((s1,s2,valoareContor()))
        contor()

    print(l)
    print((list)(starmap(FileReturn,(l))))

if __name__ == '__main__':
    nr = 10

    generateFiles("f1","f2",nr)

