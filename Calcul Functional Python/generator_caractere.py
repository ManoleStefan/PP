def combinare(ADTiterabil,index=0,lungime=1):
    it = iter(ADTiterabil)
    for contor in range(index):
        yield next(it)
    combinata = next(it)
    for count in range(lungime-1):
        combinata += next(it)
    yield combinata
    for element in it:
        yield element

l1 = ['11','22','3','4']
print(list(combinare(l1,0,len(l1))))
