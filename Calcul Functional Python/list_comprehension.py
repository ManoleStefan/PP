oLista = (1,"4",9,"a",0,4)
for i in oLista:
    print(type(i))

listaIntreg = [i**2 for i in oLista if i.__class__.__name__ == 'int']
print(listaIntreg)
print("Lista filtrata {}".format(''.join(map(str,listaIntreg))))

rezultat = map(lambda el : el ** 2, filter(lambda el : el.__class__.__name__ == 'int',oLista))
print(list(rezultat))


