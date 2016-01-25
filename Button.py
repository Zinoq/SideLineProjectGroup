import pygame
from Common import *


class Button:
    def __init__(self, text, color, size, center):
        self.Text = text
        self.Color = color
        self.Size = size
        self.Center = center
        self.Rect = pygame.Rect(self.Size)

    def DrawButton(self, color=None):
        if color is not None:
            self.Color = color
        pygame.draw.rect(screen, self.Color, self.Size)
        textSurf, textRect = text_objects(self.Text, largeText)
        textRect.center = (self.Center)
        screen.blit(textSurf, textRect)