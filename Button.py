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
        self.Color = color
        self.Size = size
        self.Center = center
        self.Rect = pygame.Rect(self.Size)

    def DrawButton(self,screen, color=None,textColor=(0,0,0)):
        if color is not None:
            self.Color = color
        pygame.draw.rect(screen, self.Color, self.Size)
        textSurf, textRect = text_objects(self.Text, largeText,textColor)
        textRect.center = (self.Center)
        screen.blit(textSurf, textRect)