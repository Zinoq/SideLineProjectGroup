class Player:
    def __init__(self, health, posX, posY, condition, damage):
        self.HP = health
        self.X = posX
        self.Y = posY
        self.Condition = condition
        self.Damage = damage

    def decreaseHealth(self, amount):
        self.HP = self.HP - amount

