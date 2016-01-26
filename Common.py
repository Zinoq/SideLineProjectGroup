import pygame
import time
from Tile import *
from Player import *
from Button import *

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
    X = (width-height)/2
else:
    X = 0
unit = int(height/16)

#Background 1
unscaled_bg = pygame.image.load("assets\\title1.png")
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
BRIGHTRED = (255,0,0)
GREEN = (80,200,80)
BRIGHTGREEN = (0,255,0)
BLUE = (80,80,200)
YELLOW = (200,200,80)
PINK = (200,100,100)
BRIGHTBLUE = (51,153,255)

# Doorloopbare lijst aan kleuren voor spelerTiles en normale Tiles
PlayerColors = [RED,GREEN,BLUE,YELLOW]
TileColors = [LIGHTGRAY,GRAY]

# Spelerplaatjes in doorloopbare lijst
pimg = player_images = [
        pygame.transform.scale(pygame.image.load("assets\\player1.png"),(int(unit/2), int(unit/2))),
        pygame.transform.scale(pygame.image.load("assets\\player2.png"),(int(unit/2), int(unit/2))),
        pygame.transform.scale(pygame.image.load("assets\\player3.png"),(int(unit/2), int(unit/2))),
        pygame.transform.scale(pygame.image.load("assets\\player4.png"),(int(unit/2), int(unit/2)))
        ]

players = init_players = []
tiles = init_tiles = []

# Alle Buttons:
# TITLE SCREEN
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

# GAME SCREEN
# Exitbutton game
button7 = Button("EXIT", RED,(1020, 640, 250, 75), ((1020+125), (640+(75/2))))

# Roll dice
button8 = Button("Roll Dice", WHITE,(10,640,250,75),((10+125),(640+(75/2))))

#Instructions
button12 = Button("INSTRUCTIONS", PINK,(490, 550, 300, 75), ((490+150), (550+(75/2)))) #changed size


def build_board():
    # startwaardes voor het doorlopen van de kleurlijsten
    pc = xc = yc = 0
    board = []
    for j in range(int(height/unit)):
        for i in range(int(height/unit)):
            if (i == 0 and j == 0) or (i == 14 and j == 0) or (i == 0 and j == 14) or (i == 14 and j == 14):
                tiles.append(Tile(Point(X+unit*i,unit*j),"spawn",PlayerColors[pc],unit*2,0))
                players.append(Player(100, Point(X+unit*i+unit/1.4,unit*j+unit/1.4), 15, Point(X+unit*i+unit/1.4, unit*j+unit/1.4),pimg[pc], True))
                pc += 1
            elif (i == 7 and j == 1) or (i == 7 and j == 14) or (i == 1 and j == 7) or (i == 14 and j == 7):
                axis = 1 if j == 1 or j == 14 else 2
                tiles.append(Tile(Point(X+unit*i,unit*j),"fight",PINK,unit,axis))
            elif not (i == 8 and j == 1) or (i == 8 and j == 14) or (i == 1 and j == 8) or (i == 14 and j == 8):
                if 1<i<14 and (j == 1 or j == 14):
                    if 1<i<7:
                        tiles.append(Tile(Point(X+unit*i,unit*j),"neutral",TileColors[xc%2],unit,0))
                        xc += 1
                    elif 8<i<14:
                        tiles.append(Tile(Point(X+unit*i,unit*j),"neutral",TileColors[xc%2-1],unit,0))
                        xc += 1
                if 1<j<14 and (i == 1 or i == 14):
                    if i == 1:
                        if 1<j<7:
                            tiles.append(Tile(Point(X+unit*i,unit*j),"neutral",TileColors[yc%2],unit,0))
                        elif 8<j<14:
                            tiles.append(Tile(Point(X+unit*i,unit*j),"neutral",TileColors[yc%2-1],unit,0))
                    if i == 14:
                        if 1<j<7:
                            tiles.append(Tile(Point(X+unit*i,unit*j),"neutral",TileColors[yc%2],unit,0))
                        elif 8<j<14:
                            tiles.append(Tile(Point(X+unit*i,unit*j),"neutral",TileColors[yc%2-1],unit,0))
                        yc += 1
    for tile in tiles:
        board.append([(tile.Position.X,tile.Position.Y,tile.Width,tile.Height),tile.image])

    return board, players


def switchScreen(screen):
    screen.run()