def exemplu(a,b,c,**kwargs): return a*b

print(type(exemplu))
print(exemplu.__code__.co_varnames)
print(exemplu.__code__.co_argcount)