class Obstacle:
    def action(self):
        pass

class Character:
    def interactWith(self,obstacle):
        pass

class Kitty(Character):
    def interactWith(self,obstacle):
        print("Kitty has encountered a",obstacle.action())

class KungFuGuy(Character):
    def interactWith(self,obstacle):
        print("Kung Fu Guy now battles a",obstacle.action())

class Puzzle(Obstacle):
    def action(self):
        return "Puzzle"

class NastyWeapon(Obstacle):
    def action(self):
        return "Nasty Weapon"

class GameElementFactory:
    def makeCharacter(self):pass
    def makeObstacle(self):pass

class KittiesAndPuzzles(GameElementFactory):
    def makeCharacter(self):
        k = Kitty()
        return k
    def makeObstacle(self):
        p = Puzzle()
        return p

class KillandDissembler(GameElementFactory):
    def makeCharacter(self):
        kfg = KungFuGuy()
        return kfg
    def makeObstacle(self):
        nw = NastyWeapon()
        return nw

class GameEnvironment:
    def __init__(self,factory):
        self.factory = factory
        self.p = self.factory.makeCharacter()
        self.ob = self.factory.makeObstacle()

    def play(self):
        self.p.interactWith(self.ob)


f1 = KittiesAndPuzzles()
f2 = KillandDissembler()
g1 = GameEnvironment(f1)
g2 = GameEnvironment(f2)

g1.play()
g2.play()

