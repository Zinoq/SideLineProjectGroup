__author__ = 'Tristan & Zino'
import pygame
import time
from Game import game
from Button import Button
from Common import *

numberOfPlayers = 0



pygame.init()

#Start
button1 = Button("START!", GREEN, (180, 550, 250, 75),((180+125), (550+(75/2))))

#Exit
button2 = Button("EXIT", RED,(850, 550, 250, 75), ((850+125), (550+(75/2))))

#1 Player
button3 = Button("1 PLAYER", WHITE, (180, 250, 250, 75),((180+125), (250+(75/2))))

#2 Players
button4 = Button("2 PLAYERS", WHITE, (515, 250, 250, 75),((515+125), (250+(75/2))))

#3 Players
button5 = Button("3 PLAYERS", WHITE, (850, 250, 250, 75),((850+125), (250+(75/2))))

#4 Players
button6 = Button("4 PLAYERS", WHITE, (515, 350, 250, 75), ((515+125), (350+(75/2))))


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
            button1.DrawButton(BRIGHTGREEN)
            if pygame.mouse.get_pressed()[0]:
                screen.blit(bg2,(0,0))
                drawScreen2()
        else:
            button1.DrawButton(GREEN)

        #Exit button
        if button2.Rect.collidepoint(mouse):
            button2.DrawButton(BRIGHTRED)
            if pygame.mouse.get_pressed()[0]:
                exit()
        else:
            button2.DrawButton(RED)

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
        Button.Color = WHITE

        #1 Player forever alone
        if button3.Rect.collidepoint(mouse):
            button3.DrawButton(PINK)
            if pygame.mouse.get_pressed()[0]:
                numberOfPlayers = 2
                game()
        else:
            button3.DrawButton(RED)

        #2 PLayer
        if button4.Rect.collidepoint(mouse):
            button4.DrawButton(PINK)
            if pygame.mouse.get_pressed()[0]:
                numberOfPlayers = 2
                game()
        else:
            button4.DrawButton(RED)

        #3 Player
        if button5.Rect.collidepoint(mouse):
            button5.DrawButton(PINK)
            if pygame.mouse.get_pressed()[0]:
                numberOfPlayers = 3
                game()
        else:
            button5.DrawButton(RED)

        #4 Players
        if button6.Rect.collidepoint(mouse):
            button6.DrawButton(PINK)
            if pygame.mouse.get_pressed()[0]:
                numberOfPlayers = 4
                game()
        else:
            button6.DrawButton(RED)

        pygame.display.flip()

main()
