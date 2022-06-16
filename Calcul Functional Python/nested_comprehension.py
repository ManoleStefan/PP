numarLinii = 5
numarColoane = 5
matrice = [[1 if elementMatrice == linie else 0 for elementMatrice in range(0,numarColoane)] for linie in range(0,numarLinii)]
for i in range(0,numarLinii):
    print(matrice[i])
