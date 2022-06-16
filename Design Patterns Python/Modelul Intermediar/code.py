class SensitiveInfo:
    def __init__(self):
        self.users = ['bula','strula','bugs','mike']

    def read(self):
        print(f"Sunt {len(self.users)} utilizatori : {' '.join(self.users)}")

    def add(self,user):
        self.users.append(user)
        print(f'Adauga loser {user}')

class Info:
    def __init__(self):
        self.protected = SensitiveInfo()
        self.secret = '0xdeadbeef'

    def read(self):
        self.protected.read()

    def add(self,user):
        sec = input("Dati parola ? > ")
        self.protected.add(user) if sec == self.secret else print("Mai incearca !")


info = Info()
while True:
    print('1. Afiseaza lista | == | 2. Adauga loser | == | 3. Iesire')
    key = input("Alegeti optiune : ")
    if key == '1':
        info.read()
    elif key == '2':
        name = input('Dati numele utilizatorului: ')
        info.add(name)
    elif key == "3":
        exit()
    else:
        print("Optiune invalida")