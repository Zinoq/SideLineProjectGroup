from Common import *

pygame.display.set_caption("Super Fight Punch by SideLine")

volume = pygame.mixer.music.set_volume

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

            if button23.Rect.collidepoint(mouse):
                button23.DrawButton(screen, YELLOW)
                if pygame.mouse.get_pressed()[0]:
                    switchScreen(settings())
            else:
                button23.DrawButton(screen, DARKYELLOW)

            pygame.display.flip()

class settings:
    def run(self):
        def stopMusic(self):
            pygame.mixer.music.set_volume(0,0)
        def decreaseVolume(self):
            pygame.mixer.music.set_volume(0,5)
        def restoreVolume(self):
            pygame.mixer.music.set_volume(1,0)
        while True:
            mouse = pygame.mouse.get_pos()
            ev = pygame.event.poll()
            if ev.type == pygame.QUIT:
                exit()
            elif ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    switchScreen(title1())
            screen.blit(bg, (0, 0))

            button24.DrawButton(screen)
            if button24.Rect.collidepoint(mouse):
                button24.DrawButton(screen, BRIGHTRED)
                # if pygame.mouse.get_pressed()[0]:
                #     stopMusic(self)
            else:
                button24.DrawButton(screen, RED)

            button25.DrawButton(screen)
            if button25.Rect.collidepoint(mouse):
                button25.DrawButton(screen, YELLOW)
                # if pygame.mouse.get_pressed()[0]:
                #     decreaseVolume(self)
            else:
                button25.DrawButton(screen, DARKYELLOW)

            button26.DrawButton(screen)
            if button26.Rect.collidepoint(mouse):
                button26.DrawButton(screen, BRIGHTGREEN)
                # if pygame.mouse.get_pressed()[0]:
                #     restoreVolume(self)
            else:
                button26.DrawButton(screen, GREEN)


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
        typingName = None
        buttons = [button15,button16,button17,button18]
        selected = [False,False,False,False]
        playerNames = {0 : "",1 : "",3 : "",2 : ""}
        switching = False
        counter = 1

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
                if i == 2:
                    screen.blit(pimg[3],buttons[i].Size)
                elif i == 3:
                    screen.blit(pimg[2],buttons[i].Size)
                else:
                    screen.blit(pimg[i],buttons[i].Size)

            button19.DrawButton(screen,GREEN,BLACK)
            if button19.Rect.collidepoint(mouse) and not switching:
                button19.DrawButton(screen, BRIGHTGREEN)
                if pygame.mouse.get_pressed()[0]:
                    starting_player = choosestarter(playerNames)
                    switching = True
                else:
                    button19.DrawButton(screen, GREEN)

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
                if playerNames[name] != "":
                    textSurf, textRect = text_objects(playerNames[name], smallText, BLACK)
                    textPosition = (buttons[name].Rect.centerx-textRect.w/2,buttons[name].Rect.centery)
                    screen.blit(textSurf,textPosition)
                textSurf, textRect = text_objects("Player %s" % (name+1), smallText, BLACK)
                textPosition = (buttons[name].Rect.centerx-textRect.w/2,buttons[name].Rect.centery-40)
                screen.blit(textSurf,textPosition)

            textColor = BLACK
            textSurf, textRect = text_objects("ENTER A NAME, OR DON'T", largeText, textColor)
            textPosition = (width/2-textRect.w/2,height/12)
            text2Surf, text2Rect = text_objects("Press enter after typing your name.", smallText, textColor)
            text2Position = (width/2-textRect.w/3,height/12*11)
            screen.blit(textSurf, textPosition)
            screen.blit(text2Surf, text2Position)

            if switching:
                counter -= 1
                if counter == 0:
                    text3Surf, text3Rect = text_objects(" First Player ", largeText, textColor)
                    text3Position = (buttons[starting_player].Rect.x,buttons[starting_player].Rect.centery+height/3)
                    screen.blit(text3Surf,text3Position)
                    pygame.display.flip()
                    time.sleep(2)
                    switchScreen(game(),numberOfPlayers,starting_player,playerNames)
                else:
                    text3Surf, text3Rect = text_objects(" First Player ", largeText, textColor)
                    text3Position = (buttons[random.randint(0,3)].Rect.x,buttons[random.randint(0,3)].Rect.centery+height/3)
                    screen.blit(text3Surf,text3Position)
                    time.sleep(0.1)

            pygame.display.flip()


class game:
    def run(self,numberOfPlayers,starting_player,playerNames = None):
        """ Set up the game and run the main game loop """
        # Prepare the pygame module for use
        # Create surface of (width, height), and its window.
        main_surface = pygame.display.set_mode(size)

        board, startTiles = build_board()
        players = playerInit(numberOfPlayers,startTiles,playerNames)

        # <rect> = (x, y, w, h)
        current_turn = 0
        playerindex = starting_player

        # current_player = players[playerindex%(len(players))]
        def turn(current_turn,playerindex):
            rolling_dice = True
            current_player = players[playerindex%4]
            if current_player.Pnr == 2 and current_player.Health < 1:
                print("lol")
            if current_player.Health >= 1:
                if rolling_dice:
                    if button8.Rect.collidepoint(mouse):
                        button8.DrawButton(main_surface, BRIGHTBLUE)
                        if pygame.mouse.get_pressed()[0]:
                            a = current_player.rollDice()
                            current_player.moveToTile(findNewTile(board,a,current_player))
                        else:
                            a = None

                        #start checking if actions should happen based on current tile or passed tiles
                        if current_player.Tile.Type is "spawn" and current_player.Tile.image == PlayerColors[current_player.Pnr-1]:
                            current_player.Health += 15
                            if current_player.Health > 100:
                                current_player.Health = 100

                        if current_player.Tile.Type is "fight":
                            superFight(current_player)

                        if (current_player.Tile.Type is "spawn" or current_player.Tile.Type is "spawn2") and not current_player.SpawnTile:
                            if current_player.Tile.image == RED: #Red spawn tile = Player 1
                                normalFight(current_player, players[0])
                            elif current_player.Tile.image == GREEN: #Green spawn tile = Player 2
                                normalFight(current_player, players[1])
                            elif current_player.Tile.image == YELLOW: #Yellow spawn tile = PLayer 3
                                normalFight(current_player, players[2])
                            elif current_player.Tile.image == BLUE: #Blue spawn tile = Player 4
                                normalFight(current_player, players[3])

                        if current_player.Health < 1:
                            pass

                        if a is not None:
                            current_turn += 1 #Next player starts
                            playerindex += 1
                    else:
                        a = None
                        button8.DrawButton(main_surface, BLUE)
                else:
                    a = None
                    button8.DrawButton(main_surface, BLUE)
            else: #if the player is dead
                button8.DrawButton(main_surface, BLUE)
                current_turn += 1
                playerindex += 1
                a = None

            return current_turn, playerindex, a

        def superFight(p1): #TODO
            #Should make it display something if attack of superfighter got blocked TODO
            #Take off Condition Points TODO
            opponent = SuperFighters[random.randint(0, len(SuperFighters)-1)]
            opponent.A = p1.rollDice()
            dmg = 5 #p1.calculateDamage(p1.rollDice())
            if opponent.Damage > p1.Damage: #player needs a damage attribute
                p1.Health = p1.Health - (opponent.Damage - dmg)
            else: #if player does more damage than superfighter, the attacks gets blocked therefor no damage will be taken
                pass

        def normalFight(p1, p2): #TODO
            #display a fancy button which shows the 'fight' TODO
            #Take off Condition Points TODO
            numb = random.randint(1,6)
            damageP1 = p1.calculateDamage(numb)
            damageP2 = p2.calculateDamage(numb)
            if damageP1 > damageP2:
                p2.Health = p2.Health - (damageP1 - damageP2)
            elif damageP2 > damageP1:
                p1.Health = p1.Health - (damageP2 - damageP1)
            else:
                pass

        instructions = 0
        displayConfirmation = 0
        fighting = 0
        showroll = 0
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
            current_turn, playerindex, playerroll = turn(current_turn,playerindex)
            if playerroll is not None:
                Rolled = playerroll
                showroll = 1
            if showroll:
                textColor = BLACK
                textSurf, textRect = text_objects("The last player: %s" % players[playerindex%4-1].Name, smallText, textColor)
                textPosition = (10,height-120)
                main_surface.blit(textSurf, textPosition)
                textColor = BLACK
                textSurf, textRect = text_objects("Rolled: " + str(Rolled), smallText, textColor)
                textPosition = (10,height-100)
                main_surface.blit(textSurf, textPosition)
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
            textColor0 = RED
            textColor1 = GREEN
            textColor2 = YELLOW
            textColor3 = BLUE
            text1Surf, text1Rect = text_objects("Current player is ", smallText, textColor)
            text1Position = (10, 10)
            if playerindex % 4 == 3:
                text2Surf, text2Rect = text_objects(str(players[3].Name), smallText, PlayerColors[2])
            elif playerindex % 4 == 2:
                text2Surf, text2Rect = text_objects(str(players[2].Name), smallText, PlayerColors[3])
            else:
                text2Surf, text2Rect = text_objects(str(players[playerindex%4].Name), smallText, PlayerColors[playerindex%4])
            text2Position = (10,30)
            text3Surf, text3Rect = text_objects("Turn %s" % current_turn, smallText, textColor)
            text3Position = (10,50)
            text4Surf, text4Rect = text_objects("%s has:"  %(players[0].Name), smallText, textColor0)
            text4Position = (10, 100)
            text4v2Surf, text4v2Rect = text_objects("%s Health; %s Condition"  %(players[0].Health, players[0].Condition), smallText, textColor)
            text4v2Position = (10, 120)
            text5Surf, text5Rect = text_objects("%s has:" %(players[1].Name), smallText, textColor1)
            text5Position = (10, 150)
            text5v2Surf, text5v2Rect = text_objects("%s Health; %s Condition" %(players[1].Health, players[1].Condition), smallText, textColor)
            text5v2Position = (10, 170)
            text6Surf, text6Rect = text_objects("%s has:" %(players[2].Name), smallText, textColor2)
            text6Position = (10, 200)
            text6v2Surf, text6v2Rect = text_objects("%s Health; %s Condition" %(players[2].Health, players[2].Condition), smallText, textColor)
            text6v2Position = (10, 220)
            text7Surf, text7Rect = text_objects("%s has:" %(players[3].Name), smallText, textColor3)
            text7Position = (10, 250)
            text7v2Surf, text7v2Rect = text_objects("%s Health; %s Condition" %(players[3].Health, players[3].Condition), smallText, textColor)
            text7v2Position = (10, 270)

            try:
                screen.blit(text1Surf, text1Position)
                screen.blit(text2Surf, text2Position)
                screen.blit(text3Surf, text3Position)
                screen.blit(text4Surf, text4Position)
                screen.blit(text4v2Surf, text4v2Position)
                screen.blit(text5Surf, text5Position)
                screen.blit(text5v2Surf, text5v2Position)
                screen.blit(text6Surf, text6Position)
                screen.blit(text6v2Surf, text6v2Position)
                screen.blit(text7Surf, text7Position)
                screen.blit(text7v2Surf, text7v2Position)
            except IndexError:
                text8Surf, text8Rect = text_objects("%s Health; %s Condition" %(0, 0), smallText, textColor)
                text8Position = (10, 290)
                screen.blit(text8Surf, text8Position)



            button7.DrawButton(main_surface)

            # EXIT BUTTON
            if button7.Rect.collidepoint(mouse):
                button7.DrawButton(main_surface, PINK)
                if pygame.mouse.get_pressed()[0]:
                    displayConfirmation = 1
            else:
                button7.DrawButton(main_surface, RED)

            button20.DrawButton(main_surface, BLUE)
            if button20.Rect.collidepoint(mouse):
                button20.DrawButton(main_surface, BRIGHTBLUE)
                if pygame.mouse.get_pressed()[0]:
                    instructions += 1
            if instructions == 1:
                screen.blit(bg, (0,0))
                button22.DrawButton(main_surface, BLUE)
                if button22.Rect.collidepoint(mouse):
                    button22.DrawButton(main_surface, BRIGHTBLUE)
                    if pygame.mouse.get_pressed()[0]:
                        instructions -= 1

                button7.DrawButton(main_surface, RED)
                if button7.Rect.collidepoint(mouse):
                      button7.DrawButton(main_surface, BRIGHTRED)
                textColor = WHITE

                for i in range(0, len(text)):  # this prints out the tekst list in a readable order
                    textSurf, textRect = text_objects(text[i], smallText, textColor)
                    textPosition = ((10), (250 + (20 * i)))
                    screen.blit(textSurf, textPosition)




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

        while True:
            ev = pygame.event.poll()
            if ev.type == pygame.QUIT:
                exit()
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    switchScreen(title1())
            mouse = pygame.mouse.get_pos()
            screen.blit(bg, (0, 0))
            #pygame.Surface.fill(screen, WHITE)

            # Display some text
            textColor = WHITE

            for i in range(0, len(text)):  # this prints out the tekst list in a readable order
                textSurf, textRect = text_objects(text[i], smallText, textColor)
                textPosition = ((10), (250 + (20 * i)))
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