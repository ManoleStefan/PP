import socket
def afla_detalii_despre_masina_locala():
    nume_masina = socket.gethostname()
    adresa_ip = socket.gethostbyname(nume_masina)
    print("Numele sistemului local : {}".format(nume_masina))
    print("Adresa IP a sistemului local : {}".format(adresa_ip))

def afla_informatii_despre_masina_la_distanta(nume):
    try:
        print("Adresa IP a masinii cu numele {} : {}".format(nume,socket.gethostbyname(nume)))
    except socket.error as err_msg:
        print("{} : {}".format(nume,err_msg))

if __name__ == "__main__":
    afla_detalii_despre_masina_locala()
    afla_informatii_despre_masina_la_distanta("www.tuiasi.ro")