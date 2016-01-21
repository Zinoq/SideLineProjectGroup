import pygame
from Tile import *

# A color is a mix of (Red, Green, Blue)
# <color> = (r, g, b)
WHITE = (255,255,255)
BLACK = (0,0,0)
GRAY = (100,100,100)
LIGHTGRAY = (200,200,200)
RED = (200,0,0)
GREEN = (20,200,10)
BLUE = (0,0,200)
LIGHTBLUE = (100,100,200)
YELLOW = (225,200,20)
PINK = (200,100,100)


def build_board(width,height):
    if not width == height:
        X = (width-height)/2
    else:
        X = 0
    unit = int(height/16)
    PlayerColors = [RED,GREEN,BLUE,YELLOW]
    TileColors = [LIGHTGRAY,GRAY]
    pc = 0
    xc = 0
    yc = 0
    board = []
    for j in range(int(height/unit)):
        for i in range(int(height/unit)):
            if (i == 0 and j == 0) or (i == 14 and j == 0) or (i == 0 and j == 14) or (i == 14 and j == 14):
                board.append(Tile(Point(X+unit*i,unit*j),"spawn",PlayerColors[pc],unit*2,0))
                pc += 1
            elif (i == 7 and j == 1) or (i == 7 and j == 14) or (i == 1 and j == 7) or (i == 14 and j == 7):
                axis = 1 if j == 1 or j == 14 else 2
                board.append(Tile(Point(X+unit*i,unit*j),"fight",PINK,unit,axis))
            elif i == 2 and j == 2:
                board.append(Tile(Point(X+unit*i,unit*j),"ring",BLUE,unit,0))
            elif not (i == 8 and j == 1) or (i == 8 and j == 14) or (i == 1 and j == 8) or (i == 14 and j == 8):
                if 1<i<14 and (j == 1 or j == 14):
                    if 1<i<7:
                        board.append(Tile(Point(X+unit*i,unit*j),"neutral",TileColors[xc%2],unit,0))
                        xc += 1
                    elif 8<i<14:
                        board.append(Tile(Point(X+unit*i,unit*j),"neutral",TileColors[xc%2-1],unit,0))
                        xc += 1
                if 1<j<14 and (i == 1 or i == 14):
                    if i == 1:
                        if 1<j<7:
                            board.append(Tile(Point(X+unit*i,unit*j),"neutral",TileColors[yc%2],unit,0))
                        elif 8<j<14:
                            board.append(Tile(Point(X+unit*i,unit*j),"neutral",TileColors[yc%2-1],unit,0))
                    if i == 14:
                        if 1<j<7:
                            board.append(Tile(Point(X+unit*i,unit*j),"neutral",TileColors[yc%2],unit,0))
                        elif 8<j<14:
                            board.append(Tile(Point(X+unit*i,unit*j),"neutral",TileColors[yc%2-1],unit,0))
                        yc += 1
    return board


def main():
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    # surface_sz = width = height = 480   # Desired physical surface size, in pixels.
    width = 1280
    height = 720
    # Create surface of (width, height), and its window.
    main_surface = pygame.display.set_mode((width, height))

    # Set up some data to describe a small rectangle and its color
    # <rect> = (x, y, w, h)
    board = build_board(width,height)
    tiles = []
    for tile in board:
        _tile = [(tile.Position.X,tile.Position.Y,tile.Width,tile.Height),tile.Color]
        tiles.append(_tile)

    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop

        # Update your game objects and data structures here...

        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        main_surface.fill(WHITE)

        # Overpaint a smaller rectangle on the main surface
        for tile in tiles:
            main_surface.fill(tile[1], tile[0])

        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()

    pygame.quit()     # Once we leave the loop, close the window.

main()