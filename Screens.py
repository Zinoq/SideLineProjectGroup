from Common import *

pygame.display.set_caption("Survivor")


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
            screen.blit(bg, (0, 0))

            # Start button
            if button1.Rect.collidepoint(mouse):
                button1.DrawButton(screen, BRIGHTGREEN)
                if pygame.mouse.get_pressed()[0]:
                    screen.blit(bg2, (0, 0))
                    switchScreen(title2())
            else:
                button1.DrawButton(screen, GREEN)

            # Exit button
            if button2.Rect.collidepoint(mouse):
                button2.DrawButton(screen, BRIGHTRED)
                if pygame.mouse.get_pressed()[0]:
                    exit()
            else:
                button2.DrawButton(screen, RED)

            # Instructions button
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

            screen.blit(bg2, (0, 0))
            button3.DrawButton(screen)
            button4.DrawButton(screen)
            button5.DrawButton(screen)  #
            button6.DrawButton(screen)  # Button 1 Player
            pygame.display.flip()

            # 1 Player forever alone
            if button3.Rect.collidepoint(mouse):
                button3.DrawButton(screen, PINK)
                if pygame.mouse.get_pressed()[0]:
                    numberOfPlayers = 2
                    switchScreen(game(),numberOfPlayers)
            else:
                button3.DrawButton(screen, RED)

            # 2 PLayers
            if button4.Rect.collidepoint(mouse):
                button4.DrawButton(screen, PINK)
                if pygame.mouse.get_pressed()[0]:
                    numberOfPlayers = 2
                    switchScreen(game(),numberOfPlayers)
            else:
                button4.DrawButton(screen, RED)

            # 3 Players
            if button5.Rect.collidepoint(mouse):
                button5.DrawButton(screen, PINK)
                if pygame.mouse.get_pressed()[0]:
                    numberOfPlayers = 3
                    switchScreen(game(),numberOfPlayers)
            else:
                button5.DrawButton(screen, RED)

            # 4 Players
            if button6.Rect.collidepoint(mouse):
                button6.DrawButton(screen, PINK)
                if pygame.mouse.get_pressed()[0]:
                    numberOfPlayers = 4
                    switchScreen(game(),numberOfPlayers)
            else:
                button6.DrawButton(screen, RED)

            pygame.display.flip()


class game:
    def run(self,numberOfPlayers):
        """ Set up the game and run the main game loop """
        pygame.init()  # Prepare the pygame module for use
        # Create surface of (width, height), and its window.
        main_surface = pygame.display.set_mode((width, height))

        # <rect> = (x, y, w, h)
        board, startTiles = build_board()
        players = playerInit(numberOfPlayers,startTiles)
        current_turn = 0

        def turn(current_turn):  # TODO further improvement once the board is fixed by mr. Lucas Pekelharing
            rolling_dice = True
            current_player = players[current_turn%4]
            if rolling_dice:
                if button8.Rect.collidepoint(mouse):
                    button8.DrawButton(main_surface, BRIGHTBLUE)
                    if pygame.mouse.get_pressed()[0]:
                        a = current_player.rollDice()
                        textColor = BLACK
                        textSurf, textRect = text_objects("You rolled: " + str(a), smallText, textColor)
                        textPosition = (10,600)
                        screen.blit(textSurf, textPosition)
                        current_player.moveToTile(findNewTile(current_player.Tile,board,a))
                        current_turn += 1
            return current_turn
                        # if current_turn >= 4:
                        #     current_turn = 0


        displayConfirmation = 0
        while True:
            mouse = pygame.mouse.get_pos()
            ev = pygame.event.poll()  # Look for any event
            if ev.type == pygame.QUIT:  # Window close button clicked?
                exit()  # ... leave game loop
            elif ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    switchScreen(title1())

            # Update your game objects and data structures here...
            current_turn = turn(current_turn)

            # We draw everything from scratch on each frame.
            # So first fill everything with the background color
            main_surface.fill(WHITE)

            button8.DrawButton(main_surface, BLUE)

            # Drawing the game's Tiles
            for tile in board:
                tile.draw(main_surface)
            # The big center "tile"
            main_surface.blit(Tile(Point(offset + unit * 2, unit * 2), "ring", None, unit * 12, 0).image,
                              (offset + unit * 2, unit * 2))

            # Drawing the players on their starting tiles
            for player in players:
                player.draw(screen)

            textColor = BLACK
            textSurf, textRect = text_objects("Current player is " + str(players[0].Name), smallText, textColor)
            textPosition = (10, 10)
            screen.blit(textSurf, textPosition)

            button7.DrawButton(main_surface)

            # EXIT BUTTON
            if button7.Rect.collidepoint(mouse):
                button7.DrawButton(main_surface, BRIGHTRED)
                if pygame.mouse.get_pressed()[0]:
                    displayConfirmation = 1
            else:
                button7.DrawButton(main_surface, RED)

            pygame.event.wait()  # fixes it immediately appearing for 0.1sec and then quitting
            # EXIT CONFIRMATION
            if displayConfirmation == 1 or displayConfirmation == 2:
                mouse = pygame.mouse.get_pos()
                button9.DrawButton(main_surface, WHITE)
                button10.DrawButton(main_surface, GREEN)
                button11.DrawButton(main_surface, RED)
                if button10.Rect.collidepoint(mouse):
                    button10.DrawButton(main_surface, BRIGHTGREEN)
                    if pygame.mouse.get_pressed(button10.Rect)[0]:
                        displayConfirmation = 0
                if button11.Rect.collidepoint(mouse):
                    button11.DrawButton(main_surface, BRIGHTRED)
                    if pygame.mouse.get_pressed(button11.Rect)[0]:
                        switchScreen(title1())
            pygame.display.flip()


class Instructions:
    def run(self):
        screen = pygame.display.set_mode(size)
        text = [
            "Diegene die het hoogst gooit begint met het spel.",
            "Elke speler heeft zijn eigen hoek (3 vakjes) en start vanaf die hoek met de klok mee.",
            "Elke speler begint met 100 Levenspunten en 15 Conditiepunten.",
            "Elke speler heeft een Scorekaart van zijn Character en een bijpassende pion",
            "Er wordt gedobbeld om voort te bewegen over het bordspel.",
            "Wanneer een speler op een vakje ‘Fight’ terechtkomt moet deze vechten tegen de Superfighter ongeacht of er een speler ook op dat vakje staat.",
            "De Superfighter wordt bepaald door een Superfighter-kaart van de stapel op het bordspel te pakken. Leg deze hierna weer onderaan de stapel.",
            "Dobbelen geeft, aan de hand van de Scorekaart, een schade aan met de bijbehorende Conditiepunten.",
            "Wanneer men geen Conditiepunten meer heeft kan er géén schade aan de tegenstander worden gedaan!",
            "Wanneer er gevochten moet worden en beide spelers geen Conditiepunten hebben ontvangt de verdediger 15 schade.",
            "De hoogste schade - de laagste schade = schade aan de speler met de laagste schade.",
            "Wanneer 2 spelers op hetzelfde vak komen wordt er tegen elkaar gevochten.",
            "Meer dan 2 spelers op één vak? Dan kiest de diegene die als laatste op het vak terecht is gekomen een tegenstander die ook op het vak staat.",
            "Wanneer je beide op een ‘Fight!’ vak terechtkomt wordt er alleen gevochten met de Superfighter en niet met elkaar.",
            "Je ontvangt 15 Conditiepunten als je langs je eigen hoek komt(max = 15 Conditiepunten).",
            "Je ontvangt 10 Levenspunten als je op je eigen hoek komt.",
            "Wanneer een hoek leeg is wordt er -10 Levenspunten gerekend. Met 2 of 3 spelers heb je dus een lege hoek.",
            "Ook wanneer iemand af is heb je een lege hoek.",
            "Verwijder je pion wanneer je geen Levenspunten meer hebt. Je hebt verloren."
        ]
        while True:
            ev = pygame.event.poll()
            if ev.type == pygame.QUIT:
                exit()
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    switchScreen(title1())
            mouse = pygame.mouse.get_pos()

            pygame.Surface.fill(screen, WHITE)

            # Display some text
            textColor = BLACK

            for i in range(0, len(text)):  # this prints out the tekst list in a readable order
                textSurf, textRect = text_objects(text[i], smallText, textColor)
                textPosition = ((10), (30 + (20 * i)))
                screen.blit(textSurf, textPosition)

            button13.DrawButton(screen, GREEN)
            button14.DrawButton(screen, RED)

            if button13.Rect.collidepoint(mouse):
                button13.DrawButton(screen, BRIGHTGREEN)
                if pygame.mouse.get_pressed()[0]:
                    switchScreen(title2())

            if button14.Rect.collidepoint(mouse):
                button14.DrawButton(screen, BRIGHTRED)
                if pygame.mouse.get_pressed()[0]:
                    switchScreen(title1())

            # Now the surface is ready, tell pygame to display it!
            pygame.display.flip()

        pygame.quit()  # Once we leave the loop, close the window.


title1().run()
