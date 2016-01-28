from Common import *


class title1:
    def run(self):
        screen = pygame.display.set_mode(size)
        while True:
            ev = pygame.event.poll()
            if ev.type == pygame.QUIT:
                exit()
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    exit()
            mouse = pygame.mouse.get_pos()

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

            #Instructions button
            if button12.Rect.collidepoint(mouse):
                button12.DrawButton(screen, BRIGHTBLUE)
                if pygame.mouse.get_pressed()[0]:
                    switchScreen(Instructions())
            else:
                button12.DrawButton(screen, BLUE)

            pygame.display.flip()

class title2:
    def run(self):
        while True:
            ev = pygame.event.poll()
            if ev.type == pygame.QUIT:
                exit()
            elif ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    switchScreen(title1())


            mouse = pygame.mouse.get_pos()

            screen.blit(bg2,(0,0))
            button3.DrawButton(screen)
            button4.DrawButton(screen)
            button5.DrawButton(screen) #
            button6.DrawButton(screen) # Button 1 Player
            pygame.display.flip()

            #1 Player forever alone
            if button3.Rect.collidepoint(mouse):
                button3.DrawButton(screen,PINK)
                if pygame.mouse.get_pressed()[0]:
                    numberOfPlayers = 2
                    switchScreen(game())
            else:
                button3.DrawButton(screen,RED)

            #2 PLayers
            if button4.Rect.collidepoint(mouse):
                button4.DrawButton(screen,PINK)
                if pygame.mouse.get_pressed()[0]:
                    numberOfPlayers = 2
                    switchScreen(game())
            else:
                button4.DrawButton(screen,RED)

            #3 Players
            if button5.Rect.collidepoint(mouse):
                button5.DrawButton(screen,PINK)
                if pygame.mouse.get_pressed()[0]:
                    numberOfPlayers = 3
                    switchScreen(game())
            else:
                button5.DrawButton(screen,RED)

            #4 Playerss
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
        board, tiles, players = build_board()

        rolling_dice = False
        current_turn = 0
        current_player = players[0]

        while True:
            ev = pygame.event.poll()    # Look for any event
            if ev.type == pygame.QUIT:  # Window close button clicked?
                exit()                 #   ... leave game loop
            elif ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    switchScreen(title1())

            # Update your game objects and data structures here...
            if rolling_dice:
                current_tile = tiles[current_player.CurrentTile]
                new_tile = tiles.index(current_tile) + current_player.rollDice()
                if new_tile > 47:
                    new_tile -= 47
                elif new_tile < 0:
                    new_tile += 47
                current_player.moveToTile(tiles[new_tile])

                rolling_dice = False
                current_turn += 1
                current_player = players[current_turn%4]


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
                pnr = player
                main_surface.blit(players[pnr].image,(players[pnr].Position.X,players[pnr].Position.Y))

            # button7.DrawButton(main_surface)
            # button8.DrawButton(main_surface)
            #
            # if button7.Rect.collidepoint(mouse):
            #     button7.DrawButton(main_surface,BRIGHTRED)
            #     if pygame.mouse.get_pressed()[0]:
            #         displayConfirmation = True
            #
            #         if displayConfirmation:
            #             button9.DrawButton(main_surface, WHITE)
            #             button10.DrawButton(main_surface, GREEN)
            #             if button10.Rect.collidepoint(mouse):
            #                 button10.DrawButton(main_surface,BRIGHTGREEN)
            #                 if pygame.mouse.get_pressed()[0]:
            #                     button11.DrawButton(main_surface, RED)
            #             #switchScreen(title1())
            # else:
            #     button7.DrawButton(main_surface,RED)
            #
            # if button8.Rect.collidepoint(mouse):
            #     button8.DrawButton(main_surface,WHITE)
            #     if pygame.mouse.get_pressed()[0]:
            #         rolling_dice = True

            pygame.display.flip()
            # time.sleep(5)
            # displayit= False

class Instructions:
    def run(self):
        screen = pygame.display.set_mode(size)
        while True:
            ev = pygame.event.poll()
            if ev.type == pygame.QUIT:
                break
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    exit()
            mouse = pygame.mouse.get_pos()

            pygame.Surface.fill(screen, WHITE)

            # Display some text
            textColor = BLUE
            text = "Kappa123"
            textSurf, textRect = text_objects(text, largeText,textColor)
            textPosition = ((100), (100))
            screen.blit(textSurf, textPosition)

            # Now the surface is ready, tell pygame to display it!
            pygame.display.flip()


        pygame.quit()     # Once we leave the loop, close the window.

title1().run()
