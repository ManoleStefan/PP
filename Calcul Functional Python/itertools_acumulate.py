import operator as op
import itertool as it

print(list(it.accumulate([1,2,3,4,5],op.add)))
print(list(it.accumulate([1,2,3,4,5],op.mul)))
print(list(it.accumulate([1,2,3,4,5],lambda x,y:(x+y)/2)))
print(list(it.accumulate([1,2,3,4,5],lambda x,y:(x-y))))
print(list(it.accumulate([1,2,3,4,5],lambda x,y:(y-x))))

def generareSecventa(p,q,valoareInitiala):
    return it.accumulate(it.repeat(valoareInitiala),lambda s,_ : p * s + q)
pare = generareSecventa(1,2,0)
primeleOpt = list(next(pare) for _ in range(8))
print(primeleOpt)