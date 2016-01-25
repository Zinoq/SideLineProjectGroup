__author__ = 'Tristan & Zino'
import pygame
import time
from Game import game
from Common import *




pygame.init()
size = width, height
smallText = pygame.font.Font(None, 25)
largeText = pygame.font.Font(None, 50)
screen = pygame.display.set_mode(size)

class Button:
    def __init__(self, text, color, size, center):
        self.Text = text
        self.Color = color
        self.Size = size
        self.Center = center

    def DrawButton(self):
        pygame.draw.rect(screen, self.Color, self.Size)
        textSurf, textRect = text_objects(self.Text, largeText)
        textRect.center = (self.Center)
        screen.blit(textSurf, textRect)


#Start
button1 = Button("START!", GREEN, (180, 550, 250, 75),((180+125), (550+(75/2))))

#Exit
button2 = Button("EXIT", RED,(850, 550, 250, 75), ((850+125), (550+(75/2))))

#Background 1
unscaled_bg = pygame.image.load("assets\\title1.png")
bg = pygame.transform.scale(unscaled_bg,size)

#Background 2
unscaled_bg2 = pygame.image.load("assets\\title2.png")
bg2 = pygame.transform.scale(unscaled_bg2,size)

def main():
    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break

        # pygame.display.flip()
        screen.blit(bg,(0,0))
        mouse = pygame.mouse.get_pos()
        button1.DrawButton()
        button2.DrawButton()

        #Start button
        if 180+250 > mouse[0] > 180 and 550+75 > mouse [1] > 550:
            pygame.draw.rect(screen, BRIGHTGREEN,(180, 550, 250, 75))
            if pygame.mouse.get_pressed()[0]:
                screen.blit(bg2,(0,0))
                pygame.display.flip()
                time.sleep(2)
                game()
        else:
            pygame.draw.rect(screen, GREEN,(180, 550, 250, 75))
        textSurf, textRect = text_objects("START!", largeText)
        textRect.center = ((180+125), (550+(75/2)))
        screen.blit(textSurf, textRect)


        #Exit button
        if 850+250 > mouse[0] > 850 and 550+75 > mouse[1] > 550:
            pygame.draw.rect(screen, BRIGHTRED,(850, 550, 250, 75))
            if pygame.mouse.get_pressed()[0]:
                exit()
        else:
            pygame.draw.rect(screen, RED,(850, 550, 250, 75))
        textSurf, textRect = text_objects("EXIT", largeText)
        textRect.center = ((850+125), (550+(75/2)))
        screen.blit(textSurf, textRect)

        pygame.display.flip()

main()
