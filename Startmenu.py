__author__ = 'Tristan & Zino'
import pygame
import time
from Game import game
from Common import *

numberOfPlayers = 0



pygame.init()
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

#2 Players
button3 = Button("2 PLAYERS", WHITE, (180, 550, 250, 75),((180+125), (550+(75/2))))

#3 Players
button4 = Button("3 PLAYERS", WHITE, (515, 550, 250, 75),((180+125), (550+(75/2))))

#4 Player
button5 = Button("4 PLAYERS", WHITE, (850, 550, 250, 75),((180+125), (550+(75/2))))

#Background 1
unscaled_bg = pygame.image.load("assets\\title1.png")
bg = pygame.transform.scale(unscaled_bg,size)

#Background 2
unscaled_bg2 = pygame.image.load("assets\\title2.png")
bg2 = pygame.transform.scale(unscaled_bg2,size)



def main():
    screen1 = True
    screen2 = False
    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break

        mouse = pygame.mouse.get_pos()

        if screen2:
                screen.blit(bg2,(0,0))
                button3.DrawButton()
                button4.DrawButton()
                button5.DrawButton()
                pygame.display.flip()
                if 180+350 > mouse[0] > 180 and 550+75 > mouse[1] > 550:
                    pygame.draw.rect(screen, BRIGHTGREEN,(180, 550, 350, 75))
                    if pygame.mouse.get_pressed()[0]:
                        numberOfPlayers = 2
                        game()
                elif 515+350 > mouse[0] > 515 and 550+75 > mouse[1] > 550:
                    pygame.draw.rect(screen, BRIGHTGREEN,(515, 550, 350, 75))
                    if pygame.mouse.get_pressed()[0]:
                        numberOfPlayers = 3
                        game()
                elif 850+350 > mouse[0] > 850 and 550+75 > mouse[1] > 550:
                    pygame.draw.rect(screen, BRIGHTGREEN,(180, 550, 350, 75))
                    if pygame.mouse.get_pressed()[0]:
                        numberOfPlayers = 4
                        game()


        if screen1:
            button1.DrawButton()
            button2.DrawButton()
            screen.blit(bg,(0,0))
            pygame.display.flip()

            #Start button
            if 180+250 > mouse[0] > 180 and 550+75 > mouse [1] > 550:
                pygame.draw.rect(screen, BRIGHTGREEN,(180, 550, 250, 75))
                if pygame.mouse.get_pressed()[0]:
                    screen.blit(bg2,(0,0))
                    screen1= False
                    screen2 = True
                    # time.sleep(2)
                    # game()
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
