def fabricaDeFunctii(x):
    def contine(lst):
        return x in lst
    return contine

amProcent100 = fabricaDeFunctii(100)
print(amProcent100)
print(amProcent100([1,2,30,50,40]))
print(amProcent100([1,2,3,50,42,100]))
print(amProcent100(range(1,200)))