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
YELLOW = (225,200,20)
PINK = (200,100,100)


def build_board(size):
    #
    unit = size/24
    PlayerColors = [RED,GREEN,BLUE,YELLOW]
    TileColors = [LIGHTGRAY,GRAY]
    c = 0
    board = []
    for i in range(4):
        for j in range(20):
            c += 1
            if i == 0:
                if j%2 == 1 and j not in [0,1]:
                    if j == 11:
                        board.append(Tile(Point(unit*j,unit),"fight",PINK,unit*2))
                    else:
                        board.append(Tile(Point(unit*j,unit),"neutral",TileColors[c%2],unit*2))
                    c += 1
                elif j == 0:
                    board.append(Tile(Point(0,0),"spawn",PlayerColors[i],unit*3))

            if i == 1:
                if j%2 == 1 and j not in [0,1]:
                    if j == 11:
                        board.append(Tile(Point(unit*j,unit*21),"fight",PINK,unit*2))
                    else:
                        board.append(Tile(Point(unit*j,unit*21),"neutral",TileColors[c%2-1],unit*2))
                    c += 1
                elif j == 0:
                    board.append(Tile(Point(unit*21,0),"spawn",PlayerColors[i],unit*3))
            if i == 2:
                if j%2 == 1 and j not in [0,1]:
                    if j == 11:
                        board.append(Tile(Point(unit,unit*j),"fight",PINK,unit*2))
                    else:
                        board.append(Tile(Point(unit,unit*j),"neutral",TileColors[c%2],unit*2))
                    c += 1
                elif j == 0:
                    board.append(Tile(Point(0,unit*21),"spawn",PlayerColors[i],unit*3))
            if i == 3:
                if j%2 == 1 and j not in [0,1]:
                    if j == 11:
                        board.append(Tile(Point(unit*21,unit*j),"fight",PINK,unit*2))
                    else:
                        board.append(Tile(Point(unit*21,unit*j),"neutral",TileColors[c%2-1],unit*2))
                    c += 1
                elif j == 0:
                    board.append(Tile(Point(unit*21,unit*21),"spawn",PlayerColors[i],unit*3))
    return board


# def build_board():
#     _board = []
#     for i in range(4):
#         _board.append(Tile(Point(0,0),"spawn",PlayerColors[i]))
#         for j in range(8):
#             if j == 4:
#                 _board.append(Tile(Point(0,0),"fight",PINK))
#             _board.append(Tile(Point(0,0),"neutral",GRAY))
#     return _board

def main():
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surface_sz = width = height = 400   # Desired physical surface size, in pixels.

    # Create surface of (width, height), and its window.
    main_surface = pygame.display.set_mode((surface_sz, surface_sz))

    # Set up some data to describe a small rectangle and its color
    # <rect> = (x, y, w, h)
    board = build_board(surface_sz)
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