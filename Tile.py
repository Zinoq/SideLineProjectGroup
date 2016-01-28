import pygame

class Point:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def __str__(self):
        return str(self.X) + "," + str(self.Y) #if we want to print the location of a player


class Tile:
    def __init__(self, position, type, image, size, offset, axis = None):
        self.Position = position
        self.Width = size
        self.Height = self.Width
        self.Size = size
        self.Offset = offset
        self.image = image
        self.Type = type

        if type == "spawn":
            self.Width = self.Height = self.Size*2
            self.rect = pygame.Rect(offset+self.Position.X*self.Size,self.Position.Y*self.Size,self.Width,self.Height)
            if self.Position.X == 0:
                self.Position.X += 1
            if self.Position.Y == 0:
                self.Position.Y += 1
        elif type == "fight":
            if axis == 0: # 0: along X, 1: along Y
                self.Width = size*2
                self.Height = size
                self.rect = pygame.Rect(offset+self.Position.X*self.Size,self.Position.Y*self.Size,self.Width,self.Height)
            elif axis == 1:
                self.Width = size
                self.Height = size*2
                self.rect = pygame.Rect(self.Offset+self.Position.X*self.Size,self.Position.Y*self.Size,self.Width,self.Height)
        elif type == "neutral":
            self.rect = pygame.Rect(self.Offset+self.Position.X*self.Size,self.Position.Y*self.Size,self.Width,self.Height)
        elif type == "ring":
            self.image = pygame.transform.scale(pygame.image.load("assets\\boxring.png"),(self.Width,self.Height))
            self.rect = self.image.get_rect()
        else:
            self.Height = 2/3*self.Width
            self.image = pygame.Rect(self.Position.X,self.Position.Y,self.Width,self.Height)

    def draw(self,screen):
        screen.fill(self.image, self.rect)

    def __str__(self):
        return self.Position






