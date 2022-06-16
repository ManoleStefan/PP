x = {'a' : 1,'b' : 2}
y = {'b': 3,'c' : 4}
z = {**x,**y}

print(z)

valoriGradeF = {'t1' : -32,'t2' : -24,'t3' : -13,'t4' : 0}
valoriGradeC = {k : round((float(5)/9) * (v-32)) for (k,v) in valoriGradeF.items()}
print(valoriGradeC)

dict1 = {'e': 1,'f' : 2,'k' : 3,'p' : 4,'l': 5}

filtrareCuCond = {k:v for(k,v) in dict1.items() if v > 2}
print(filtrareCuCond)

filtrareCuCondDict = {k:v for(k,v) in dict1.items() if v > 2 if v % 2 == 0}
print(filtrareCuCondDict)

nestedDict = {'primul' : {'a' : 1},'aldoilea' : {'b' : 2}}
conversieFloatDict = {exterior_k : {float(interior_v) for (interior_k,interior_v) in exterior_v.items()} for(exterior_k,exterior_v) in nestedDict.items()}
print(conversieFloatDict)
