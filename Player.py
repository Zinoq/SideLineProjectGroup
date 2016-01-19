from Tile import *

class Player:
    def __init__(self, health, posX, posY, condition, spawnlocation):
        self.HP = health
        self.X = posX
        self.Y = posY
        self.Condition = condition
        self.Spawnlocation = spawnlocation #has to be a Point(x,y)

    def decreaseHealth(self, amount):
        self.HP = self.HP - amount

