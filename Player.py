from Tile import *
import random

class Player:
    def __init__(self, health, position, condition, spawnlocation):
        self.Health = health
        self.Position = position
        self.Condition = condition
        self.Spawnlocation = spawnlocation #has to be a Point(x,y)

    def decreaseHealth(self, amount):
        self.Health = self.Health - amount

    def resetLocation(self):
        self.Position = self.Spawnlocation #is a Point

    def rollDice(self):
        return random.randint(1,6)


# player = Player(100,Point(2,5),100,Point(0,0)) #testing purposes
# print(player.rollDice())

#Later we should add a function where we can decide how much player we want, and with that we decide how many players we
#iniate
Player1 = Player(100, Point(0,0), 15, Point(0,0))
Player2 = Player(100, Point(260, 0), 15, Point(260,0))
Player3 = Player(100, Point(0,260), 15, Point(0,260))
Player4 = Player(100, Point(260,260), 15, Point(260, 260))

# print(Player4.Health)
#
# Player4.decreaseHealth(40)
#
# print(Player4.Health)  Testing purposes


