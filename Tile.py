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
        self.Color = texture

        self.Width = size
        self.Height = self.Width
        self.Size = size
        if type is not "neutral" and type is not "fight" and type is not "spawn" and type is not "ring":
            raise Exception("Invalid Type, use \'neutral\', \'fight\' or \'spawn\'")
        else:
            self.Type = type
            if type == "spawn":
                self.Width = size
                self.Height = size
            elif type == "fight":
                if axis == 1: # 0: does not apply, 1: along X, 2: along Y
                    self.Width = size*2
                    self.Height = size
                elif axis == 2:
                    self.Width = size
                    self.Height = size*2
            elif type == "ring":
                self.image = pygame.transform.scale(pygame.image.load("assets\\Boxring.png"),(self.Width,self.Height))

    def __str__(self):
        return self.Position






