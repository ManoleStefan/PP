import random
class Logger:
    def __init__(self,type):
        self.type = type
        self.next : Logger = 0

    def handle_request(self,type,message):
        if self.type == type:
            self.write(message)
        else:
            self.next.handle_request(type,message)

    def write(self,message) : pass

    def set_next(self,nextt):
        self.next = nextt

class Console(Logger):
    def __init__(self,type):
        super().__init__(type)

    def write(self,message):
        print("Console message : {}".format(message))

class File(Logger):
    def __init__(self,type):
        super().__init__(type)

    def write(self,message):
        print("File message : {}".format(message))

class ErrorLogger(Logger):
    def __init__(self,type):
        super().__init__(type)

    def write(self,message):
        print("Error message : {}".format(message))


consola = Console("console")
error = ErrorLogger("error")
file = File("file")

error.set_next(file)
consola.set_next(error)

options = ["file","console","error"]

for i in range(10):
    value = random.randint(0,2)
    print("message type : {}".format(options[value]))
    consola.handle_request(options[value],"mesajul {}".format(i))