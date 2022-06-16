listaValori = [('5','3','5','7','11'),('13','17','19','23','29'),('31','137','41','143','47'),('53','59','61','67','71'),('173','9','83','89','97'),('101','103','107','109','113'),('12','131','17','139','19'),('151','157','163','167','173'),('179','18','191','199','197'),('194','21','123','225','229')]

def flatten(list):
    t = []
    for i in list:
        t.extend(i)
    return t


#print(flatten(listaValori))



inregistrare = {'Nume ' : 'Bula','Locatia' : {'Oras' : 'Pocreaca','Tara' : 'Rom'},'hobi' : ['Manea','Bautura','Femei']}

def flatten_table(y):
    iesire = {}
    def flatten(x,nume = ''):
        if type(x) is dict:
            for a in x:
                flatten(x[a],nume + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a,nume + str(i) + '_')
                i += 1
        else :
            iesire[nume[:-1]] = x
    flatten(y)
    return iesire

print(flatten_table(inregistrare))