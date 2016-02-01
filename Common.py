import pygame
import time
from Tile import *
from Player import *
from Button import *
from Cards import *


pygame.init()

# surface_sz = width = height = 480   # Desired physical surface size, in pixels.
width = 1280
height = 720
size = width, height
screen = pygame.display.set_mode(size)
mouse = pygame.mouse.get_pos()
numberOfPlayers = 0

# Scherm opdelen in 16 stukken
if not width == height:
    offset = (width-height)/2
else:
    offset = 0
unit = int(height/16)

#Background 1
unscaled_bg = pygame.image.load("assets\\title3.png")
bg = pygame.transform.scale(unscaled_bg,size)

#Background 2
unscaled_bg2 = pygame.image.load("assets\\title2.png")
bg2 = pygame.transform.scale(unscaled_bg2,size)

# A color is a mix of (Red, Green, Blue)
# <color> = (r, g, b)
WHITE = (255,255,255)
BLACK = (0,0,0)
GRAY = (100,100,100)
LIGHTGRAY = (200,200,200)
RED = (200,80,80)
DARKRED = (160,80,80)
BRIGHTRED = (255,0,0)
GREEN = (80,200,80)
DARKGREEN = (80,160,80)
BRIGHTGREEN = (0,255,0)
BLUE = (80,80,200)
DARKBLUE = (80,80,160)
YELLOW = (200,200,80)
DARKYELLOW = (160,160,80)
PINK = (200,100,100)
BRIGHTBLUE = (51,153,255)

# Doorloopbare lijst aan kleuren voor spelerTiles en normale Tiles
PlayerColors = [RED,GREEN,BLUE,YELLOW]
PlayerColors2 = [DARKRED,DARKGREEN,DARKBLUE,DARKYELLOW]
TileColors = [LIGHTGRAY,GRAY]

# Spelerplaatjes in doorloopbare lijst
pimg = player_images = [
        pygame.transform.scale(pygame.image.load("assets\\player1.png"),(int(unit/2), int(unit/2))),
        pygame.transform.scale(pygame.image.load("assets\\player2.png"),(int(unit/2), int(unit/2))),
        pygame.transform.scale(pygame.image.load("assets\\player3.png"),(int(unit/2), int(unit/2))),
        pygame.transform.scale(pygame.image.load("assets\\player4.png"),(int(unit/2), int(unit/2)))
        ]


# Alle Buttons:
# TITLE SCREEN
#Start
button1 = Button("START!", GREEN, (180, 350, 250, 75),((180+125), (350+(75/2))))

#Exit
button2 = Button("EXIT", RED,(850, 350, 250, 75), ((850+125), (350+(75/2))))

#Instructions
button12 = Button("INSTRUCTIONS", PINK,(490, 350, 300, 75), ((490+150), (350+(75/2)))) #changed size

#Player amount selection screen
#1 Player
button3 = Button("1 PLAYER", WHITE, (180, 250, 250, 75),((180+125), (250+(75/2))))

#2 Players
button4 = Button("2 PLAYERS", WHITE, (515, 250, 250, 75),((515+125), (250+(75/2))))

#3 Players
button5 = Button("3 PLAYERS", WHITE, (850, 250, 250, 75),((850+125), (250+(75/2))))

#4 Players
button6 = Button("4 PLAYERS", WHITE, (515, 350, 250, 75), ((515+125), (350+(75/2))))

# GAME SCREEN
# Exitbutton game
button7 = Button("EXIT", RED,(1020, 640, 250, 75), ((1020+125), (640+(75/2))))

# Roll dice
button8 = Button("Roll Dice", BLUE,(10,640,250,75),((10+125),(640+(75/2))))

# Pop-up screen
button9 = Button("Are you sure you want to quit?", WHITE, (340, 235, 600, 250), ((340+300), (150+125)))

# Keep playing
button10 = Button("Keep playing", GREEN,(350,425,250,50),((350+125),(425+25)))

# Exit anyway
button11 = Button("Quit", RED,(680,425,250,50),((680+125),(425+25)))

#instructionscreen
#start
button13 = Button("START!", GREEN, (180, 550, 250, 75),((180+125), (550+(75/2))))

#back
button14 = Button("BACK", RED,(850, 550, 250, 75), ((850+125), (550+(75/2))))

# PlayerOrder screen
button15 = Button("", PlayerColors[0],(width/12*2,height/5,width/12*2,250),((width/12*3)+175,(height/3*2)+125))
button16 = Button("", PlayerColors[1],(width/12*4,height/5,width/12*2,250),((width/12*5)+175,(height/3*2)+125))
button17 = Button("", PlayerColors[2],(width/12*6,height/5,width/12*2,250),((width/12*7)+175,(height/3*2)+125))
button18 = Button("", PlayerColors[3],(width/12*8,height/5,width/12*2,250),((width/12*9)+175,(height/3*2)+125))
button19 = Button("START!", GREEN,(width/12*7,height/5*4,250,75),((width/12*7)+125,(height/5*4)+37))

#CARDS, SuperFighters
card1 = Card("Agua Man", 12, 15, 9, 7, 7, 13)
card2 = Card("Bruce Hee", 20, 15, 5, 7, 8, 26)
card3 = Card("Chack Norris", 15, 28, 27, 25, 29, 30)
card4 = Card("Dexter", 9, 8, 7, 15, 13, 9)
card5 = Card("Ernold Schwarzenegger", 25, 25, 20, 15, 15, 10)
card6 = Card("Jackie Chen", 12, 10, 15, 9, 10, 25)
card7 = Card("James Bend", 25, 15, 15, 7, 20, 25)
card8 = Card("Jason Statham", 15, 17, 19, 21, 23, 26)
card9 = Card("Jet Ri", 10, 30, 12, 25, 14, 23)
card10 = Card("John Cena", 10, 6, 25, 7, 8, 11)
card11 = Card("Pariz Hilten", 12, 8, 7, 15, 13, 9)
card13 = Card("Steve Seagal", 10, 15, 12, 11, 25, 20)
card14 = Card("Super Merio", 10, 10, 30, 30, 15, 15)
card15 = Card("Terry Crews", 10, 15, 25, 20, 15, 10)
card16 = Card("The Roch", 13, 28, 30, 17, 10, 7)
card17 = Card("Vin Dieser", 20, 25, 30, 25, 20, 15)
card18 = Card("Wesley Sniper", 10, 12, 14, 16, 14, 12)




def build_board():
    board = []
    startTiles = []
    pc = 0
    tc = 1
    for j in range(16):
        for i in range(16):
            if (0<=j<=2 or 13<=j<=14) and (0<=i<=2 or 13<=i<=14):
                if (j == 0 and i == 0) or (j == 0 and i == 14) or (j == 14 and i == 0) or (j == 14 and i == 14):
                    board.append(Tile(Point(i,j),"spawn",PlayerColors[pc],unit,offset))
                    startTiles.append(Tile(Point(i,j),"spawn",PlayerColors[pc],unit,offset))
                    pc += 1
                elif (j == 1 and i == 2) or (j == 2 and i == 1):
                    board.append(Tile(Point(i,j),"spawn2", PlayerColors2[0],unit,offset))
                elif (j == 13 and i == 1) or (j == 14 and i == 2):
                    board.append(Tile(Point(i,j),"spawn2", PlayerColors2[2],unit,offset))
                elif (j == 1 and i == 13) or (j == 2 and i == 14):
                    board.append(Tile(Point(i,j),"spawn2", PlayerColors2[1],unit,offset))
                elif (j == 13 and i == 14) or (j == 14 and i == 13):
                    board.append(Tile(Point(i,j),"spawn2", PlayerColors2[3],unit,offset))
            elif (j == 1 and i == 7) or (j == 14 and i == 7):
                board.append(Tile(Point(i,j),"fight",PINK,unit,offset,0))
            elif (j == 7 and i == 1) or (j == 7 and i == 14):
                board.append(Tile(Point(i,j),"fight",PINK,unit,offset,1))
            elif j == 1:
                if 1<i<7:
                    board.append(Tile(Point(i,j),"neutral",TileColors[tc%2-1],unit,offset))
                elif 8<i<14:
                    board.append(Tile(Point(i,j),"neutral",TileColors[tc%2-1],unit,offset))
                tc += 1
            elif j == 14:
                if 1<i<7:
                    board.append(Tile(Point(i,j),"neutral",TileColors[tc%2],unit,offset))
                elif 8<i<14:
                    board.append(Tile(Point(i,j),"neutral",TileColors[tc%2],unit,offset))
                tc += 1
            elif i == 1:
                if 1<j<7:
                    board.append(Tile(Point(i,j),"neutral",TileColors[tc%2],unit,offset))
                elif 8<j<14:
                    board.append(Tile(Point(i,j),"neutral",TileColors[tc%2],unit,offset))
            elif i == 14:
                if 1<j<7:
                    board.append(Tile(Point(i,j),"neutral",TileColors[tc%2],unit,offset))
                elif 8<j<14:
                    board.append(Tile(Point(i,j),"neutral",TileColors[tc%2],unit,offset))
                tc += 1
    return board, startTiles


def playerInit(humans,startTiles,names = None): #give names as a list, in order of players
    players = []
    pnr = 0
    if names is None:
        while pnr < 4:
            if pnr < humans:
                if pnr == 2:
                    players.append(Player(100,startTiles[3],15,startTiles[3],pimg[3],True,"Player %s" % (3),3))
                elif pnr == 3:
                    players.append(Player(100,startTiles[2],15,startTiles[2],pimg[2],True,"Player %s" % (4),4))
                else:
                    players.append(Player(100,startTiles[pnr],15,startTiles[pnr],pimg[pnr],True,"Player %s" % (pnr+1),pnr+1))
            else:
                if pnr == 2:
                    players.append(Player(100,startTiles[3],15,startTiles[3],pimg[3],False,"Player %s" % (3),3))
                elif pnr == 3:
                    players.append(Player(100,startTiles[2],15,startTiles[2],pimg[2],False,"Player %s" % (4),4))
                else:
                    players.append(Player(100,startTiles[pnr],15,startTiles[pnr],pimg[pnr],False,"Player %s" % (pnr+1),pnr+1))
            pnr += 1
    else:
        while pnr < 4:
            if names[pnr] == "":
                names[pnr] = "Player %s" % (pnr+1)
            if pnr < humans:
                if pnr == 2:
                    players.append(Player(100,startTiles[3],15,startTiles[3],pimg[3],True,names[3],3))
                elif pnr == 3:
                    players.append(Player(100,startTiles[2],15,startTiles[2],pimg[2],True,names[2],4))
                else:
                    players.append(Player(100,startTiles[pnr],15,startTiles[pnr],pimg[pnr],True,names[pnr],pnr+1))
            else:
                if pnr == 2:
                    players.append(Player(100,startTiles[3],15,startTiles[3],pimg[3],False,names[3],3))
                elif pnr == 3:
                    players.append(Player(100,startTiles[2],15,startTiles[2],pimg[2],False,names[2],4))
                else:
                    players.append(Player(100,startTiles[pnr],15,startTiles[pnr],pimg[pnr],False,names[pnr],pnr+1))
            pnr += 1
    return players


def findNewTile(current,board,n):
    X1 = current.Position.X - 1
    Y1 = current.Position.Y - 1
    if n > 0:
        if Y1 == 0: # upper line
            if X1+n >= 13: # hit upper-right corner, moving right then down
                X2 = 13
                Y2 = n - (13 - X1)
            else: # moving right
                X2 = X1+n
                Y2 = Y1
        elif Y1 == 13: # lower line
            if X1-n <= 0:  # hit lower-left corner, moving left then up
                X2 = 0
                Y2 = 13 - (n-X1)
            else: # moving left
                X2 = X1-n
                Y2 = Y1
        elif 0<Y1<13: # sides
            if X1 == 0: # left side
                if Y1-n <= 0: # hit upper-left corner, moving up then right
                    Y2 = 0
                    X2 = n-Y1
                else: # moving up
                    Y2 = Y1-n
                    X2 = X1
            elif X1 == 13: # right side
                if Y1+n >= 13: # hit lower-right corner, moving down then left
                    Y2 = 13
                    X2 = 13 - (n - (13-Y1))
                else:
                    Y2 = Y1+n
                    X2 = X1
    else: # if user somehow gets a 0 roll
        X2,Y2 = X1,Y1
    if X2 != 7: # fight tiles zijn 2 lang, spelers kunnen alleen op de eerste van de 2 coordinaten staan
        X2 += 1
    if Y2 != 7: # same here
        Y2 += 1
    for tile in board:
        if tile.Position.X == X2 and tile.Position.Y == Y2:
            return tile


def switchScreen(screen,optArg1 = None,optArg2 = None):
    if optArg1 is None:
        screen.run()
    else:
        if optArg2 is None:
            screen.run(optArg1)
        else:
            screen.run(optArg1,optArg2)