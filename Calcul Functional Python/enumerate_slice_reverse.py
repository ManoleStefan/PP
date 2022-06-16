listaSimpla = ['5','3','5','7','11','13','17','19','23','29','31','137','41','143','47','53','61','71','173','9','83','89','97','101','103']

student = ('mananca','doarme','femei')
n = len(listaSimpla)

listaSliced = zip((listaSimpla[2*i::n] for i in range(round(n/2))),(listaSimpla[2*i+1::n] for i in range(round(n/2))))
print(list(listaSliced))

print(list(enumerate(student)))