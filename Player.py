from Tile import *
import random

class Player:
    def __init__(self, health, position, condition, spawntile, texture, is_human):
        self.Health = health
        self.Condition = condition
        self.SpawnTile = spawntile #has to be a Point(x,y)
        self.CurrentTile = self.SpawnTile
        self.image = texture
        self.IsHuman = is_human
        self.rect = self.image.get_rect()
        self.Position = position

    def moveToTile(self,tile):
        self.Position = Point(tile.rect.centerx,tile.rect.centery)

    def decreaseHealth(self, amount):           #tested, works.
        self.Health = self.Health - amount

    def resetLocation(self):
        self.Position = self.SpawnTile      #is a Point, tested and works

    def rollDice(self):                         #tested, works
        return random.randint(1,6)




