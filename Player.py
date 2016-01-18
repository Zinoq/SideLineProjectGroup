class Player:
    def __init__(self, health, posX, posY):
        self.HP = health
        self.X = posX
        self.Y = posY

    def decreaseHealth(self, amount):
        self.HP = self.HP - amount

# this is a new comment