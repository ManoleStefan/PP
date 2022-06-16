import time
class CoffeeMachine:
    def __init__(self):
        self.beans = 0
        self.water = 0
        self.state = Off(self)
        self.running = False

    def turnOff(self):
        self.state.turnOff()
    def turnOn(self):
        self.state.turnOn()
    def fillBeans(self,quantity):
        self.state.fillBeans(quantity)
    def fillWater(self,quantity):
        self.state.fillWater(quantity)
    def makeCoffee(self):
        self.state.makeCoffee()
    def changeState(self,stare):
        self.state = stare


class CoffeMachineState:
    def __init__(self,coffemachine):
        self.machine = coffemachine

    def turnOff(self) : print("Not supported in this state")
    def turnOn(self) : print("Not supported in this state")
    def fillBeans(self,quantity) : print("Not supported in this state")
    def fillWater(self,quantity) : print("Not supported in this state")
    def makeCoffee(self) : print("Not supported in this state")



class Off(CoffeMachineState):
    def __init__(self,coffemachine):
        super().__init__(coffemachine)

    def turnOn(self):
        print("MACHINE STATUS : POWERED ON.")
        self.machine.running = True
        self.machine.changeState(NoIngredients(self.machine))

class NoIngredients(CoffeMachineState):
    def __init__(self,coffemachine):
        super().__init__(coffemachine)

    def fillBeans(self,quantity):
        if self.machine.beans + quantity < 100:
            self.machine.beans += quantity
            print("MACHINE STATUS : {} BEANS ADDED.".format(quantity))
        else:
            print("MACHINE STATUS : TOO MUCH BEANS")

        #if(self.machine.beans > 0):
            #self.machine.changeState(MakeCoffe(self.machine))

    def fillWater(self,quantity):
        if self.machine.water + quantity < 100:
            self.machine.water += quantity
            print("MACHINE STATUS : {} g OF WATER ADDED.".format(quantity))
        else:
            print("MACHINE STATUS : TOO MUCH WATER")

        if(self.machine.water > 0):
            self.machine.changeState(MakeCoffe(self.machine))

class MakeCoffe(CoffeMachineState):
    def __init__(self,coffemachine):
        super().__init__(coffemachine)

    def makeCoffee(self):
        #assert self.machine.running is True, "MACHINE STATUS : POWER UP FIRST"
        print("MACHINE STATUS : STARTED MAKING COFFEE")
        #assert self.machine.beans > 0 is True,"MACHINE STATUS : NO MORE BEANS"
        self.machine.beans -= 1
        #assert self.machine.water > 0 is True,"MACHINE STATUS : NO MORE WATER"
        self.machine.water -= 1
        print("MACHINE STATUS : MAKING COFFEE..........")
        time.sleep(5)
        print("MACHINE STATUS : COFFEE READY ! TAKE IT!")


machine = CoffeeMachine()
machine.turnOn()
machine.fillBeans(10)
machine.fillWater(10)
machine.makeCoffee()
