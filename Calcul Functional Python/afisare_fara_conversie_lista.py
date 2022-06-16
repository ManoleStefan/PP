def printIterator(it):
    s = ''
    for x in it:
        s = s+' '+str(x)
    print(s)
    print()

l1 = [1,2,3,4]
t1 = (5,6,7,8,9,10)
m = map(lambda x,y : x * y,l1,t1)
printIterator(m)
print(list(m))