class Stock:
    def __init__(self,name):
        self.size = 0
        self.name = name

    def sell(self,destination):
        amount = 0
        if destination == "N":
            amount = 10
        if destination == "S":
            amount = 20
        if destination == "E":
            amount = 15
        if destination == "V":
            amount = 5

        if self.size - amount > 0:
            self.size -= 10
            print("STOCK {} : S-au vandut {} unitati spre {}.".format(self.name,amount,destination))
            self.status()
        else:
            print("STOCK {}: Comanda nu poate fi efectuata.Lipsesc {} unitati.".format(self.name,amount - self.size))

    def buy(self,quantity):
        self.size += quantity
        print("STOCK {}: S-au cumparat {} unitati.".format(self.name,quantity))
        self.status()


    def status(self):
        print("        >STOCK {}: {} unitati disponibile.".format(self.name,self.size))


class Order:
    def __init__(self,stock,commandname):
        self.commandname = commandname
        self.stock = stock

    def getType(self):pass


class BuyStock(Order):
    def __init__(self,stock,quantity,commandname = "buy"):
        super().__init__(stock,commandname)
        self.quantity = quantity

    def buy(self):
        self.stock.buy(self.quantity)

    def getType(self):
        return "buy"

class SellStock(Order):
    def __init__(self,stock,destination,commandname = "sell"):
        super().__init__(stock,commandname)
        self.destination = destination

    def sell(self):
        self.stock.sell(self.destination)

    def getType(self):
        return "sell"



class Broker:
    def __init__(self):
        self.commands = []

    def AddCommand(self,command):
        self.commands.append(command)

    def ExecuteQueries(self):
        for cmd in self.commands:
            if cmd.getType() == "sell":
                cmd.sell()
            elif cmd.getType() == "buy":
                cmd.buy()
            else:
                print("Invalid command")
        self.commands = []


fanta = Stock("fanta")
sprite = Stock("sprite")
cola = Stock("cola")

CocaColaCompany = Broker()
CocaColaCompany.AddCommand(BuyStock(fanta,10))
CocaColaCompany.AddCommand(BuyStock(fanta,14))
CocaColaCompany.AddCommand(BuyStock(fanta,18))
CocaColaCompany.AddCommand(BuyStock(cola,5))
CocaColaCompany.AddCommand(BuyStock(cola,15))
CocaColaCompany.AddCommand(BuyStock(sprite,30))
CocaColaCompany.AddCommand(BuyStock(sprite,100))

CocaColaCompany.AddCommand(SellStock(fanta,"N"))
CocaColaCompany.AddCommand(SellStock(fanta,"S"))
CocaColaCompany.AddCommand(SellStock(fanta,"V"))
CocaColaCompany.AddCommand(SellStock(cola,"E"))
CocaColaCompany.AddCommand(SellStock(cola,"S"))
CocaColaCompany.AddCommand(SellStock(sprite,"V"))
CocaColaCompany.AddCommand(SellStock(sprite,"N"))

CocaColaCompany.ExecuteQueries()


print("\n\n")
