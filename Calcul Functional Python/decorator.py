def ornament(oFunctie):
    def impachetezFunctia():
        print("blocul predecesor al apelului functiei originale")
        oFunctie()
        print("blocul succesor al apelului functiei originale")
    return impachetezFunctia


@ornament
def functie1():
    print("se executa functia originala din decorator")

ornament(functie1())
functie1()

