import random
def pfactorsr(x):
    def factor_n(x,n):
        if n * n > x:
            yield x
            return
        if x % n == 0:
            yield n
            if x // n > 1:
                yield from factor_n(x // n,n)
            else:
                yield from factor_n(x,n+2)
        if x // 2 > 1:
            yield from pfactorsr(x//2)
        return
    yield from factor_n(x,3)

def recursiv(n):
    def impar(n):
        print(n)
        if n < 10:
            return
        else:
            val = random.randint(1,5)
            yield from recursiv(n // val)

    def par(n):
        print(n)
        if n < 10:
            return
        else:
            val = random.randint(5,10)
            yield from recursiv(n // val)

    if n % 2 == 0:
        yield n
        yield from par(n)
    else:
        yield n
        yield from impar(n)



print(list(recursiv(129878)))

print(list(pfactorsr(1455560)))