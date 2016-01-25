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
        self.Rect = pygame.Rect(self.Size)

    def DrawButton(self):
        pygame.draw.rect(screen, self.Color, self.Size)
        textSurf, textRect = text_objects(self.Text, largeText)
        textRect.center = (self.Center)
        screen.blit(textSurf, textRect)


#Start
button1 = Button("START!", GREEN, (180, 550, 250, 75),((180+125), (550+(75/2))))

#Exit
button2 = Button("EXIT", RED,(850, 550, 250, 75), ((850+125), (550+(75/2))))

#1 Player
button3 = Button("1 PLAYERS", WHITE, (180, 250, 250, 75),((180+125), (250+(75/2))))

#2 Players
button4 = Button("2 PLAYERS", WHITE, (515, 250, 250, 75),((515+125), (250+(75/2))))

#3 Players
button5 = Button("3 PLAYERS", WHITE, (850, 250, 250, 75),((850+125), (250+(75/2))))

#4 Players
button6 = Button("4 PLAYER", WHITE, (515, 350, 250, 75), ((515+125), (350+(75/2))))


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

        mouse = pygame.mouse.get_pos()

        button1.DrawButton()
        button2.DrawButton()
        screen.blit(bg,(0,0))
        pygame.display.flip()

        #Start button
        if button1.Rect.collidepoint(mouse):
            pygame.draw.rect(screen, BRIGHTGREEN, button1.Size)
            if pygame.mouse.get_pressed()[0]:
                screen.blit(bg2,(0,0))
                drawScreen2()
        else:
            pygame.draw.rect(screen, GREEN, button1.Size)
        textSurf, textRect = text_objects("START!", largeText)
        textRect.center = ((180+125), (550+(75/2)))
        screen.blit(textSurf, textRect)


        #Exit button
        if button2.Rect.collidepoint(mouse):
            pygame.draw.rect(screen, BRIGHTRED, button2.Size)
            if pygame.mouse.get_pressed()[0]:
                exit()
        else:
            pygame.draw.rect(screen, RED, button2.Size)
        textSurf, textRect = text_objects("EXIT", largeText)
        textRect.center = ((850+125), (550+(75/2)))
        screen.blit(textSurf, textRect)

        pygame.display.flip()


def drawScreen2():
    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            exit()


        mouse = pygame.mouse.get_pos()

        screen.blit(bg2,(0,0))
        button3.DrawButton()
        button4.DrawButton()
        button5.DrawButton() #
        button6.DrawButton() # Button 1 Player
        pygame.display.flip()


        #1 Player forever alone
        if button3.Rect.collidepoint(mouse):
            button3.Color = BLUE
            button3.DrawButton()
            if pygame.mouse.get_pressed()[0]:
                numberOfPlayers = 2
                game()

        #2 PLayer
        if button4.Rect.collidepoint(mouse):
            button3.Color = BLUE
            pygame.draw.rect(screen, BLUE, button4.Size)
            if pygame.mouse.get_pressed()[0]:
                numberOfPlayers = 2
                game()

        #3 Player
        if button5.Rect.collidepoint(mouse):
            button3.Color = BLUE
            pygame.draw.rect(screen, BLUE, button5.Size)
            if pygame.mouse.get_pressed()[0]:
                numberOfPlayers = 3
                game()

        #4 Players
        if button6.Rect.collidepoint(mouse):
            button3.Color = BLUE
            pygame.draw.rect(screen, BLUE,button6.Size)
            if pygame.mouse.get_pressed()[0]:
                numberOfPlayers = 4
                game()

        pygame.display.flip()

main()
