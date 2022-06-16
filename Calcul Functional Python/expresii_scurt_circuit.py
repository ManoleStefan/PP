lista2 = [2,3,5,7,11,13,17,19,23,39,31,37,41,43,47,53,59,51,67,71,73,79,83,89,97,101,103]

val1 = lambda x : x in range(0,3)
val2 = lambda x : x in range(3,100)
val3 = lambda x : x > 100

f1 = lambda x : x * 2
f2 = lambda x : x + 2
f3 = lambda x : round(x/2)

eval = (lambda x,y : y if x == True else False)

scurtcircuit = lambda x : eval(val1(x),f1(x)) or eval(val2(x),f2(x)) or eval(val3(x),f3(x))

map1 = map(scurtcircuit,lista2)
print(list(map1))
