from Common import *


class title1:
    def run(self):
        screen = pygame.display.set_mode(size)
        while True:
            ev = pygame.event.poll()
            if ev.type == pygame.QUIT:
                break

            button1.DrawButton(screen)
            button2.DrawButton(screen)
            screen.blit(bg,(0,0))


            #Start button
            if button1.Rect.collidepoint(mouse):
                button1.DrawButton(screen,BRIGHTGREEN)
                if pygame.mouse.get_pressed()[0]:
                    screen.blit(bg2,(0,0))
                    switchScreen(title2())
            else:
                button1.DrawButton(screen,GREEN)

            #Exit button
            if button2.Rect.collidepoint(mouse):
                button2.DrawButton(screen,BRIGHTRED)
                if pygame.mouse.get_pressed()[0]:
                    exit()
            else:
                button2.DrawButton(screen,RED)

            pygame.display.flip()

class title2:
    def run(self):
        while True:
            ev = pygame.event.poll()
            if ev.type == pygame.QUIT:
                exit()

            screen.blit(bg2,(0,0))
            button3.DrawButton(screen)
            button4.DrawButton(screen)
            button5.DrawButton(screen) #
            button6.DrawButton(screen) # Button 1 Player
            pygame.display.flip()
            Button.Color = WHITE

            #1 Player forever alone
            if button3.Rect.collidepoint(mouse):
                button3.DrawButton(screen,PINK)
                if pygame.mouse.get_pressed()[0]:
                    numberOfPlayers = 2
                    switchScreen(game())
            else:
                button3.DrawButton(screen,RED)

            #2 PLayer
            if button4.Rect.collidepoint(mouse):
                button4.DrawButton(screen,PINK)
                if pygame.mouse.get_pressed()[0]:
                    numberOfPlayers = 2
                    switchScreen(game())
            else:
                button4.DrawButton(screen,RED)

            #3 Player
            if button5.Rect.collidepoint(mouse):
                button5.DrawButton(screen,PINK)
                if pygame.mouse.get_pressed()[0]:
                    numberOfPlayers = 3
                    switchScreen(game())
            else:
                button5.DrawButton(screen,RED)

            #4 Players
            if button6.Rect.collidepoint(mouse):
                button6.DrawButton(screen,PINK)
                if pygame.mouse.get_pressed()[0]:
                    numberOfPlayers = 4
                    switchScreen(game())
            else:
                button6.DrawButton(screen,RED)

            pygame.display.flip()

class game:
    def run(self):
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

            button7.DrawButton(main_surface)
            pygame.event.get()

            if button7.Rect.collidepoint(mouse):
                button7.DrawButton(main_surface,BRIGHTRED)
                if pygame.mouse.get_pressed()[0]:
                    switchScreen(title1())
            else:
                button7.DrawButton(main_surface,RED)





            # Now the surface is ready, tell pygame to display it!
            pygame.display.flip()


        pygame.quit()     # Once we leave the loop, close the window.

title1().run()
