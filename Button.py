import pygame
pygame.init()

smallText = pygame.font.Font(None, 25)
largeText = pygame.font.Font(None, 50)


def text_objects(text,font,color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


class Button:
    def __init__(self, text, color, size, center):
        self.Text = text
        self.Color = self.initColor = color
        self.Size = size
        self.Center = center
        self.Rect = pygame.Rect(self.Size)

    def lighten(self):
        red = self.Color[0]
        lightred = red+20 if red + 20 <= 255 else 255
        green = self.Color[1]
        lightgreen = green + 20 if green + 20 <= 255 else 255
        blue = self.Color[2]
        lightblue = blue + 20 if blue + 20 <= 255 else 255
        lightColor = (lightred,lightgreen,lightblue)
        return lightColor

    def DrawButton(self,screen, color=None, textColor=(0,0,0)):
        if color is None:
            pygame.draw.rect(screen, self.Color, self.Size)
        else:
            pygame.draw.rect(screen, color, self.Size)
        textSurf, textRect = text_objects(self.Text, largeText,textColor)
        textRect.center = (self.Center)
        screen.blit(textSurf, textRect)