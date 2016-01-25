import pygame
from Tile import Tile,Point
from Player import Player

pygame.init()
# surface_sz = width = height = 480   # Desired physical surface size, in pixels.
width = 1280
height = 720
size = width, height
smallText = pygame.font.Font(None, 25)
largeText = pygame.font.Font(None, 50)

# Scherm opdelen in 16 stukken
if not width == height:
    X = (width-height)/2
else:
    X = 0
unit = int(height/16)

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

# Doorloopbare lijst aan kleuren voor spelerTiles en normale Tiles
PlayerColors = [RED,GREEN,BLUE,YELLOW]
TileColors = [LIGHTGRAY,GRAY]


pimg = player_images = [
        pygame.transform.scale(pygame.image.load("assets\\player1.png"),(int(unit/2), int(unit/2))),
        pygame.transform.scale(pygame.image.load("assets\\player2.png"),(int(unit/2), int(unit/2))),
        pygame.transform.scale(pygame.image.load("assets\\player3.png"),(int(unit/2), int(unit/2))),
        pygame.transform.scale(pygame.image.load("assets\\player4.png"),(int(unit/2), int(unit/2)))
        ]

players = init_players = []
tiles = init_tiles = []


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


def text_objects(text,font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()