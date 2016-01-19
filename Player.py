class Player:
    def __init__(self, health, posX, posY, condition):
        self.HP = health
        self.X = posX
        self.Y = posY
        self.Condition = condition

    def decreaseHealth(self, amount):
        self.HP = self.HP - amount

