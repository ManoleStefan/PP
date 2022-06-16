from itertool import *

sinus = cycle([1,-1])
print(list(next(sinus) for _ in range(6)))

ceva = cycle([3,1,0,-1,-3])
print(list(next(ceva) for _ in range(9)))

sir = cycle(['a','b','c'])
print(list(next(sir) for _ in range(6)))