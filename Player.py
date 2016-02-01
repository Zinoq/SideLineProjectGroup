import random

class Player:
    def __init__(self, health, position, condition, spawntile, texture, is_human, name,pnr):
        self.Health = health
        self.Condition = condition
        self.SpawnTile = spawntile #has to be a Point(x,y)
        self.Tile = self.SpawnTile
        self.image = texture
        self.IsHuman = is_human
        self.rect = self.image.get_rect()
        self.Position = position
        self.Pnr = pnr
        if self.IsHuman:
            self.Name = "[Human] " + name
        else:
            self.Name = "[CPU] " + name

    def draw(self,screen):
        screen.blit(self.image,(self.Tile.rect.centerx- self.rect.w/2, self.Tile.rect.centery- self.rect.h/2))

    def moveToTile(self,tile):
        self.Tile = tile

    def decreaseHealth(self, amount):           #tested, works.
        self.Health = self.Health - amount

    def resetLocation(self):
        self.Position = self.SpawnTile      #is a Point, tested and works

    def rollDice(self):                         #tested, works
        return random.randint(1,6)



