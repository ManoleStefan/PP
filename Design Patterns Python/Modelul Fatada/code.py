class _IgnitionSystem(object):
    @staticmethod
    def produce_spark():
        return True

class _Engine(object):
    def __init__(self):
        self.revs_per_minute = 0
    def turnon(self):
        self.revs_per_minute = 2000
    def turnoff(self):
        self.revs_per_minute = 0

class _FuelTank(object):
    def __init__(self,level=30):
        self.levels = level
    @property
    def level(self):
        return self.levels
    @level.setter
    def level(self,level):
        self.levels = level

class _DashBoardLight(object):
    def __init__(self,is_on = False):
        self._is_on = is_on
    def __str__(self):
        return self.__class__.__name__
    @property
    def is_on(self):
        return self._is_on
    @is_on.setter
    def is_on(self,status):
        self._is_on = status
    def status_check(self):
        if self._is_on:
            print("{}: Pornit".format(str(self)))
        else:
            print("{}: Oprit".format(str(self)))

class _HandBrakeLight(_DashBoardLight):
    pass

class _FogLampLight(_DashBoardLight):
    pass


class _Dashboard(object):
    def __init__(self):
        self.lights = {"Frana de mana": _HandBrakeLight(),"ceata": _FogLampLight()}

    def show(self):
        for light in self.lights.values():
            light.status_check()



class Car(object):
    def __init__(self):
        self.ignition_system = _IgnitionSystem()
        self.engine = _Engine()
        self.fuel_tank = _FuelTank()
        self.dashboard = _Dashboard()

    @property
    def km_per_litre(self):
        return 17.0
    def consume_fuel(self,km):
        self.fuel_tank.level -= min(self.fuel_tank.level,km/self.km_per_litre)
    def start(self):
        print("\nPornire..")
        self.dashboard.show()
        if self.ignition_system.produce_spark():
            self.engine.turnon()
        else:
            print("Nu pot porni. Eroare la sistemul de aprindere")
    def has_enough_fuel(self,km,km_per_litre):
        litres_needed = km/km_per_litre
        if self.fuel_tank.level > litres_needed:
            return True
        return False
    def drive(self,km=100):
        print("\n")
        if self.engine.revs_per_minute > 0:
            while self.has_enough_fuel(km,self.km_per_litre):
                self.consume_fuel(km)
                print("S-au condus {} km.".format(km))
                print("Au mai ramas {:.2f} litri de combustibil".format(self.fuel_tank.level))
        else:
            print("Nu se poate merge. Motorul este oprit.")

    def park(self):
        print("/Parcare..")
        self.dashboard.lights["Frana de mana"].is_on = True
        self.dashboard.show()
        self.engine.turnoff()

    def switch_fog_lights(self,status):
        print("\nPornire {} lumini de ceata..".format(status))
        self.dashboard.lights["ceata"].is_on = True if status == "ON" else False
        self.dashboard.show()

    def fill_up_tank(self):
        print("\nRezervorul a fost umplut")
        self.fuel_tank.level = 100

car  = Car()
car.start()
car.drive()
car.switch_fog_lights("ON")
car.switch_fog_lights("OFF")
car.park()
car.fill_up_tank()
car.drive()
car.start()
car.drive()
