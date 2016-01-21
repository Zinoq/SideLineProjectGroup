import pygame

class Point:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def __str__(self):
        return str(self.X) + "," + str(self.Y) #if we want to print the location of a player


class Tile:
    def __init__(self, position, type, texture, size, axis):
        self.Position = position
        self.Width = size
        self.Height = self.Width
        self.Size = size

        self.image = texture
        self.Type = type
        if self.Type not in ["neutral","fight","spawn","ring"]:
            raise Exception("Invalid Type, use \'neutral\', \'fight\' or \'spawn\'")
        else:
            self.Type = type
            if type == "spawn":
                self.Width = self.Height =  self.Size
                self.rect = pygame.Rect(self.Position.X,self.Position.Y,self.Width,self.Height)
            elif type == "fight":
                if axis == 1: # 0: does not apply, 1: along X, 2: along Y
                    self.Width = size*2
                    self.Height = size
                    self.rect = pygame.Rect(self.Position.X,self.Position.Y,self.Width,self.Height)
                elif axis == 2:
                    self.Width = size
                    self.Height = size*2
                    self.rect = pygame.Rect(self.Position.X,self.Position.Y,self.Width,self.Height)
            elif type == "ring":
                self.image = pygame.transform.scale(pygame.image.load("assets\\boxring.png"),(self.Width,self.Height))
                self.rect = self.image.get_rect()

    def __str__(self):
        return self.Position






