class ChatRoom(object):
    def display_message(self,user,message):
        print("[{} zice ] : {}".format(user,message))


class User(object):
    def __init__(self,name):
        self.name = name
        self.chat_room = ChatRoom()

    def say(self,message):
        self.chat_room.display_message(self,message)

    def __str__(self):
        return self.name



vasile = User('Vasile')
tica = User('Tica2')
altul = User('Altul')

vasile.say("Echipa adunarea la ora 3 dupa amiaza!")
tica.say("Da sefu pot sa astept pana atunci in fata usii?")
altul.say("Dar eu pot>")