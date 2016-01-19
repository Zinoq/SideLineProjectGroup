from Tile import *

class Player:
    def __init__(self, health, position, condition, spawnlocation):
        self.HP = health
        self.Position = position
        self.Condition = condition
        self.Spawnlocation = spawnlocation #has to be a Point(x,y)

    def decreaseHealth(self, amount):
        self.HP = self.HP - amount

    def resetLocation(self):
        self.Position = self.Spawnlocation #is a Point

