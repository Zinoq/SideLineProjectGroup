
class Card:
    def __init__(self, name, val1, val2, val3, val4, val5, val6):
        self.Name = name
        self.dmg_table = [val1,val2,val3,val4,val5,val6]
        self.Dice = None
        self.Damage = None
    def calculateDamage(self):
        self.Damage = self.dmg_table[self.Dice-1]
