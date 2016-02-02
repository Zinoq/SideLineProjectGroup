from Common import *

pygame.display.set_caption("Super Fight Punch")



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

            screen.blit(bg, (0, 0))
            button3.DrawButton(screen)
            button4.DrawButton(screen)
            button5.DrawButton(screen)  #
            button6.DrawButton(screen)  # Button 1 Player

            # 1 Player forever alone
            if button3.Rect.collidepoint(mouse):
                button3.DrawButton(screen, PINK)
                if pygame.mouse.get_pressed()[0]:
                    numberOfPlayers = 1
                    # switchScreen(game(),numberOfPlayers)
                    switchScreen(whostarts(),numberOfPlayers)
            else:
                button3.DrawButton(screen, RED)

            # 2 PLayers
            if button4.Rect.collidepoint(mouse):
                button4.DrawButton(screen, PINK)
                if pygame.mouse.get_pressed()[0]:
                    numberOfPlayers = 2
                    # switchScreen(game(),numberOfPlayers)
                    switchScreen(whostarts(),numberOfPlayers)
            else:
                button4.DrawButton(screen, RED)

            # 3 Players
            if button5.Rect.collidepoint(mouse):
                button5.DrawButton(screen, PINK)
                if pygame.mouse.get_pressed()[0]:
                    numberOfPlayers = 3
                    # switchScreen(game(),numberOfPlayers)
                    switchScreen(whostarts(),numberOfPlayers)
            else:
                button5.DrawButton(screen, RED)

            # 4 Players
            if button6.Rect.collidepoint(mouse):
                button6.DrawButton(screen, PINK)
                if pygame.mouse.get_pressed()[0]:
                    numberOfPlayers = 4
                    # switchScreen(game(),numberOfPlayers)
                    switchScreen(whostarts(),numberOfPlayers)
            else:
                button6.DrawButton(screen, RED)

            pygame.display.flip()


class whostarts:
    def run(self,numberOfPlayers):
        pygame.init()
        screen = pygame.display.set_mode((width,height))
        typingName = None
        buttons = [button15,button16,button17,button18]
        selected = [False,False,False,False]
        playerNames = {0 : "",1 : "",2 : "",3 : ""}

        def choosestarter(players):
            highest = {}
            while True:
                for i in range(len(players)):
                    highest[i] = random.randint(1,6)
                newh = sorted(highest.items(), key=lambda x: (-x[1], x[0]))
                if not newh[0][1] == newh[1][1]:
                    return newh[0][0] # returns 0/3 (the player that starts))



        while True:
            mouse = pygame.mouse.get_pos()
            ev = pygame.event.poll()  # Look for any event
            if ev.type == pygame.QUIT:  # Window close button clicked?
                exit()  # ... leave game loop
            elif ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    switchScreen(title1())
            screen.fill(WHITE)

            for i in range(len(buttons)):
                if not True in selected:
                    if buttons[i].Rect.collidepoint(mouse):
                        if pygame.mouse.get_pressed()[0]:
                            selected[i] = True
                            typingName = i

            for i in range(len(buttons)):
                if selected[i]: buttons[i].DrawButton(screen,buttons[i].lighten())
                else: buttons[i].DrawButton(screen,buttons[i].initColor)
                screen.blit(pimg[i],buttons[i].Size)

            button19.DrawButton(screen,GREEN,BLACK)
            if button19.Rect.collidepoint(mouse):
                button19.DrawButton(screen, button19.lighten())
                if pygame.mouse.get_pressed()[0]:
                    starting_player = choosestarter(playerNames)
                    switchScreen(game(),numberOfPlayers,starting_player,playerNames)
                else:
                    button19.DrawButton(screen, button19.initColor)

            if typingName is not None:
                while 1:
                    event = pygame.event.poll()
                    if event.type == pygame.KEYDOWN:
                        inKey = event.key
                        break
                    else:
                        pass

                if inKey == pygame.K_BACKSPACE:
                    playerNames[typingName] = playerNames[typingName][:-1]
                elif inKey == pygame.K_RETURN:
                    selected[typingName] = False
                    typingName = None
                elif inKey <= 127 and len(playerNames[typingName]) <= 16:
                    playerNames[typingName] += str(chr(inKey))

            for name in playerNames:
                if name != "":
                    textSurf, textRect = text_objects(playerNames[name], smallText, BLACK)
                    textPosition = (buttons[name].Rect.centerx-textRect.w/2,buttons[name].Rect.centery-40)
                    screen.blit(textSurf,textPosition)

            pygame.display.flip()


class game:
    def run(self,numberOfPlayers,starting_player,playerNames = None):
        """ Set up the game and run the main game loop """
        pygame.init()  # Prepare the pygame module for use
        # Create surface of (width, height), and its window.
        main_surface = pygame.display.set_mode((width, height))

        board, startTiles = build_board()
        players = playerInit(numberOfPlayers,startTiles,playerNames)

        # <rect> = (x, y, w, h)
        current_turn = 0
        playerindex = starting_player

        def turn(current_turn,playerindex):
            rolling_dice = True
            current_player = players[playerindex%4]
            if rolling_dice:
                if button8.Rect.collidepoint(mouse):
                    button8.DrawButton(main_surface, BRIGHTBLUE)
                    if pygame.mouse.get_pressed()[0]:
                        a = current_player.rollDice()
                        textColor = BLACK
                        textSurf, textRect = text_objects("You rolled: " + str(a), smallText, textColor)
                        textPosition = (10,30)
                        screen.blit(textSurf, textPosition)
                        current_player.moveToTile(findNewTile(current_player.Tile,board,a))

                        #start checking if actions should happen based on current tile or passed tiles
                        if current_player.Tile == current_player.SpawnTile:
                            current_player.Health += 15
                            if current_player.Health > 100:
                                current_player.Health = 100

                        if current_player.Tile.Type is "fight":
                            superFight(current_player)

                        if current_player.Tile.Type is "spawn" and not current_player.SpawnTile:
                            if current_player.Tile.Image == RED: #Red spawn tile = Player 1
                                normalFight(current_player, players[0])
                            elif current_player.Tile.Image == GREEN: #Green spawn tile = Player 2
                                normalFight(current_player, players[1])
                            elif current_player.Tile.Image == YELLOW: #Yellow spawn tile = PLayer 3
                                normalFight(current_player, players[2])
                            elif current_player.Tile.Image == BLUE: #Blue spawn tile = Player 4
                                normalFight(current_player, players[3])

                        if current_player.Health < 1:
                            die(current_player)

                        current_turn += 1 #Next player starts
                        playerindex += 1
            return current_turn, playerindex, None, None

        def superFight(p1): #TODO
            opponent = SuperFighters[random.randint(0, len(SuperFighters)-1)]
            opponent.A = p1.rollDice()
            if opponent.Damage > p1.Damage: #player needs a damage attribute
                pass


        def normalFight(p1, p2): #TODO
            pass

        def die(p1): #TODO
            pass

        displayConfirmation = 0
        while True:
            mouse = pygame.mouse.get_pos()
            ev = pygame.event.poll()  # Look for any event
            if ev.type == pygame.QUIT:  # Window close button clicked?
                exit()  # ... leave game loop
            elif ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    switchScreen(title1())
            main_surface.fill(WHITE)
            # Update your game objects and data structures here...
            current_turn, playerindex, textSurf, textPosition = turn(current_turn,playerindex)
            if textSurf is not None and textPosition is not None:
                screen.blit(textSurf,textPosition)

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
            text1Surf, text1Rect = text_objects("Current player is ", smallText, textColor)
            text1Position = (10, 10)
            text2Surf, text2Rect = text_objects(str(players[current_turn%4].Name), smallText, textColor)
            text2Position = (10,30)
            text3Surf, text3Rect = text_objects("Turn %s" %current_turn, smallText, textColor)
            text3Position = (10,50)
            text4Surf, text4Rect = text_objects("%f has %s" %(players[0].Name, players[0].Health) + " Health", smallText, textColor)
            text4Position = (10, 100)
            text5Surf, text5Rect = text_objects("%fr has %s" %(players[1].Name, players[1].Health) + " Health", smallText, textColor)
            text5Position = (10, 120)
            text6Surf, text6Rect = text_objects("%f has %s" %(players[2].Name, players[2].Health) + " Health", smallText, textColor)
            text6Position = (10, 140)
            text7Surf, text7Rect = text_objects("%f has %s" %(players[3].Name, players[3].Health) + " Health", smallText, textColor)
            text7Position = (10, 160)
            screen.blit(text1Surf, text1Position)
            screen.blit(text2Surf, text2Position)
            screen.blit(text3Surf, text3Position)
            screen.blit(text4Surf, text4Position)
            screen.blit(text5Surf, text5Position)
            screen.blit(text6Surf, text6Position)
            screen.blit(text7Surf, text7Position)


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