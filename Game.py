import pygame
from Tile import *

# A color is a mix of (Red, Green, Blue)
# <color> = (r, g, b)
WHITE = (255,255,255)
BLACK = (0,0,0)
GRAY = (100,100,100)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
PINK = (255,100,100)

PlayerColors = [RED,GREEN,BLUE,YELLOW]

# replace below with function or loop to build board
# every other neutral tile is colored a different shade of gray

board = [
    # Neutral Tiles

    # Top
    Tile(Point(60,20),"neutral",GRAY),
    Tile(Point(80,20),"neutral",GRAY),
    Tile(Point(100,20),"neutral",GRAY),
    Tile(Point(120,20),"neutral",GRAY),
    Tile(Point(180,20),"neutral",GRAY),
    Tile(Point(200,20),"neutral",GRAY),
    Tile(Point(220,20),"neutral",GRAY),
    Tile(Point(240,20),"neutral",GRAY),

    # Bottom
    Tile(Point(60,260),"neutral",GRAY),
    Tile(Point(80,260),"neutral",GRAY),
    Tile(Point(100,260),"neutral",GRAY),
    Tile(Point(120,260),"neutral",GRAY),
    Tile(Point(180,260),"neutral",GRAY),
    Tile(Point(200,260),"neutral",GRAY),
    Tile(Point(220,260),"neutral",GRAY),
    Tile(Point(240,260),"neutral",GRAY),

    # Left
    Tile(Point(20,60),"neutral",GRAY),
    Tile(Point(20,80),"neutral",GRAY),
    Tile(Point(20,100),"neutral",GRAY),
    Tile(Point(20,120),"neutral",GRAY),
    Tile(Point(20,180),"neutral",GRAY),
    Tile(Point(20,200),"neutral",GRAY),
    Tile(Point(20,220),"neutral",GRAY),
    Tile(Point(20,240),"neutral",GRAY),

    # Right
    Tile(Point(260,60),"neutral",GRAY),
    Tile(Point(260,80),"neutral",GRAY),
    Tile(Point(260,100),"neutral",GRAY),
    Tile(Point(260,120),"neutral",GRAY),
    Tile(Point(260,180),"neutral",GRAY),
    Tile(Point(260,200),"neutral",GRAY),
    Tile(Point(260,220),"neutral",GRAY),
    Tile(Point(260,240),"neutral",GRAY),

    # Fight Tiles
    Tile(Point(140,20),"fight",PINK),
    Tile(Point(20,140),"fight",PINK),
    Tile(Point(260,140),"fight",PINK),
    Tile(Point(140,260),"fight",PINK),

    # Players Tiles
    Tile(Point(0,0),"spawn",PlayerColors[0]),
    Tile(Point(260,0),"spawn",PlayerColors[1]),
    Tile(Point(0,260),"spawn",PlayerColors[2]),
    Tile(Point(260,260),"spawn",PlayerColors[3])
]

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
    surface_sz = width = height = 320  # Desired physical surface size, in pixels.

    # Create surface of (width, height), and its window.
    main_surface = pygame.display.set_mode((surface_sz, surface_sz))

    # Set up some data to describe a small rectangle and its color
    # <rect> = (x, y, w, h)
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