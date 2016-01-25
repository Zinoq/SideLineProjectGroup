import pygame
from Tile import *
from Player import *
from Common import *
from Button import *

# Exitbutton
button7 = Button("EXIT", RED,(850, 550, 250, 75), ((850+125), (550+(75/2))))


def game():
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    # Create surface of (width, height), and its window.
    main_surface = pygame.display.set_mode((width, height))

    # <rect> = (x, y, w, h)
    board, players = build_board()

    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            exit()                   #   ... leave game loop
        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE: break

        # Update your game objects and data structures here...

        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        main_surface.fill(WHITE)

        # Drawing the game's Tiles
        for tile in board:
            main_surface.fill(tile[1], tile[0])
        # The big center "tile"
        main_surface.blit(Tile(Point(X+unit*2,unit*2),"ring",None,unit*12,0).image,(X+unit*2,unit*2))

        # Drawing the players on their starting tiles
        for player in players:
            main_surface.blit(player.image,(player.Position.X,player.Position.Y))
        button7.DrawButton()



        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()


    pygame.quit()     # Once we leave the loop, close the window.
