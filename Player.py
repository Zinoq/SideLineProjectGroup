from Tile import *
import random

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

    def rollDice(self):
        return random.randint(1,6)


player = Player(100,Point(2,5),100,Point(0,0)) #testing purposes
print(player.rollDice())



