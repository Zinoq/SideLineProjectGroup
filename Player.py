import random

class Player:
    def __init__(self, health, position, condition, spawntile, texture, is_human, name, pnr):
        self.Health = health
        self.Condition = condition
        self.SpawnTile = spawntile #has to be a Point(x,y)
        self.Tile = self.SpawnTile
        self.image = texture
        self.IsHuman = is_human
        self.rect = self.image.get_rect()
        self.Position = position
        self.Pnr = pnr
        self.Name = name
        self.Damage = 0

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

    def calculateDamage(self, number): #number is result of rolling the dice
        #id 1 = Mike Tysen, 2 = Badr Heri, 3 = Rocky Belboa, 4 = Menny Pecquiao
        selected = random.randint(1,3) #TODO maak dit een keuze ipv random
        if self.Condition > 0:
            if self.Pnr is 1:
                choice = {
                    #ontleden van de aankomende code gaat als volgt:
                    #het eerste nummer is het nummer dat je dobbelt, en dan kan je 1 van de drie keuzes
                    #maken die een bepaalde schade doen en conditie afnemen, dit staan in de lijst er achter
                    1: {1:[3, -1], 2:[9, -2], 3:[19, -3]},
                    2: {1:[5, -2], 2:[11, -3], 3:[15, -5]},
                    3: {1:[7, -2], 2:[12, -3], 3:[16, -4]},
                    4: {1:[2, -1], 2:[4, -2], 3:[6, -3]},
                    5: {1:[10, -2], 2:[20, -5], 3:[30, -8]},
                    6: {1:[8, -3], 2:[13, -4], 3:[17, -5]}
                    }
                # self.Condition += choice[number][*][1]
                if self.Condition > 0:
                     if self.Condition + choice[number][selected][1] > 0:
                         self.Condition = self.Condition + choice[number][selected][1]
                         return choice[number][selected][0] #select damage of selected
                     else:
                         return 0 #je kunt deze aanval niet uitvoeren
                else:
                    return 0

            elif self.Pnr is 2:
                choice = {
                    1: {1:[5, -2], 2:[11, -3], 3:[15, -5]},
                    2: {1:[3, -1], 2:[9, -2], 3:[19, -3]},
                    3: {1:[2, -1], 2:[4, -2], 3:[6, -3]},
                    4: {1:[7, -2], 2:[12, -3], 3:[16, -4]},
                    5: {1:[8, -3], 2:[13, -4], 3:[17,-5]},
                    6: {1:[10, -2], 2:[20, -5], 3:[30, -8]}
                    }
                # self.Condition += choice[number][*][1]
                if self.Condition > 0:
                    if self.Condition + choice[number][selected][1] > 0:
                        self.Condition = self.Condition + choice[number][selected][1]
                        return choice[number][selected][0] #select damage of selected
                    else:
                        return 0
                else:
                    return 0

            elif self.Pnr is 3:
                choice = {
                    1: {1:[10, -2], 2:[20, -5], 3:[30, -8]},
                    2: {1:[8, -3], 2:[13, -4], 3:[17, -5]},
                    3: {1:[3, -1], 2:[9, -2], 3:[19, -3]},
                    4: {1:[5, -2], 2:[11, -3], 3:[15, -4]},
                    5: {1:[7, -2], 2:[12, -3], 3:[16,-4]},
                    6: {1:[2, -1], 2:[4, -2], 3:[6, -3]}
                    }
                # self.Condition += choice[number][*][1]
                if self.Condition > 0:
                    if self.Condition + choice[number][selected][1] > 0:
                        self.Condition = self.Condition + choice[number][selected][1]
                        return choice[number][selected][0] #select damage of selected
                    else:
                        return 0
                else:
                    return 0

            elif self.Pnr is 4:
                choice = {
                    1: {1:[8, -3], 2:[13, -4], 3:[17, -5]},
                    2: {1:[10, -2], 2:[20, -5], 3:[30, -8]},
                    3: {1:[5, -2], 2:[11, -3], 3:[15, -5]},
                    4: {1:[3, -1], 2:[9, -2], 3:[19, -3]},
                    5: {1:[2, -1], 2:[4, -2], 3:[6, -3]},
                    6: {1:[7, -2], 2:[12, -3], 3:[16, -4]}
                    }
                # self.Condition += choice[number][*][1]
                if self.Condition > 0:
                    if self.Condition + choice[number][selected][1] >= 0:
                        self.Condition = self.Condition + choice[number][selected][1]
                        return choice[number][selected][0] #select damage of selected
                    else:
                        return 0
                else:
                    return 0
        else:
            return 0









