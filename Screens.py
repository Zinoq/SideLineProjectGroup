from Common import *

pygame.display.set_caption("Super Fight Punch by SideLine")

volume = pygame.mixer.music.set_volume

class title1:
    intro.play()
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


            # button1.DrawButton(screen)
            # button2.DrawButton(screen)
            screen.blit(bg, (0, 0))

            # Start button
            if button1.Rect.collidepoint(mouse):
                # button1.DrawButton(screen, BRIGHTGREEN)
                screen.blit(startbuttonlight,button1.Rect)
                if pygame.mouse.get_pressed()[0]:
                    intro.stop()
                    bell.play()
                    screen.blit(bg2, (0, 0))
                    switchScreen(game(),4,0)
                    # switchScreen(title2())
            else:
                # button1.DrawButton(screen, GREEN)
                screen.blit(startbutton,button1.Rect)

            # Exit button
            if button2.Rect.collidepoint(mouse):
                button2.DrawButton(screen, BRIGHTRED)
                screen.blit(exitbuttonlight,button2.Rect)
                if pygame.mouse.get_pressed()[0]:
                    exit()
            else:
                # button2.DrawButton(screen, RED)
                screen.blit(exitbutton,button2.Rect)

            # Instructions button
            if button12.Rect.collidepoint(mouse):
                # button12.DrawButton(screen, BRIGHTBLUE)
                screen.blit(instructionsbuttonlight,button12.Rect)
                if pygame.mouse.get_pressed()[0]:
                    switchScreen(Instructions())
            else:
                # button12.DrawButton(screen, BLUE)
                screen.blit(instructionsbutton,button12.Rect)

            # Settings button
            if button23.Rect.collidepoint(mouse):
                # button23.DrawButton(screen, YELLOW)
                screen.blit(settingsbuttonlight,button23.Rect)
                if pygame.mouse.get_pressed()[0]:
                    switchScreen(settings())
            else:
                # button23.DrawButton(screen, DARKYELLOW)
                screen.blit(settingsbutton,button23.Rect)

            pygame.display.flip()

class settings:
    def run(self):
        def getVolume(self):
            intro.get_volume()
            bell.get_volume()
            game1.get_volume()
            game2.get_volume()
        def AutoVolume(self):
            intro.set_volume(0.25)
            bell.set_volume(0.25)
            game1.set_volume(0.25)
            game2.set_volume(0.25)
        def Volume1(self):
            intro.set_volume(0.5)
            bell.set_volume(0.5)
            game1.set_volume(0.5)
            game2.set_volume(0.5)
        def Volume2(self):
            intro.set_volume(0.75)
            bell.set_volume(0.75)
            game1.set_volume(0.75)
            game2.set_volume(0.75)
        def Volume3(self):
            intro.set_volume(1)
            bell.set_volume(1)
            game1.set_volume(1)
            game2.set_volume(1)
        def Mute(self):
            intro.set_volume(0.0)
            bell.set_volume(0.0)
            game1.set_volume(0.0)
            game2.set_volume(0.0)
        time.sleep(0.1)
        while True:
            # settingsmusic.play()
            mouse = pygame.mouse.get_pos()
            ev = pygame.event.poll()
            if ev.type == pygame.QUIT:
                exit()
            elif ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    switchScreen(title1())
            screen.blit(bg, (0, 0))


            if button24.Rect.collidepoint(mouse): #Mute
                screen.blit(mutebuttonlight, button24.Rect)
                if pygame.mouse.get_pressed()[0]:
                    getVolume(self)
                    if intro.get_volume() > 0:
                        Mute(self)
                        pygame.event.wait()
            else:
                screen.blit(mutebutton, button24.Rect)


            if button25.Rect.collidepoint(mouse): #Lower Volume
                screen.blit(lowervolumebuttonlight, button25.Rect)
                if pygame.mouse.get_pressed()[0]:
                    getVolume(self)
                    if intro.get_volume() == 0.25:
                        Mute(self)
                        pygame.event.wait()
                    if intro.get_volume() == 0.5:
                        AutoVolume(self)
                        pygame.event.wait()
                    if intro.get_volume() == 0.75:
                        Volume1(self)
                        pygame.event.wait()
                    if intro.get_volume() == 1:
                        Volume2(self)
                        pygame.event.wait()

            else:
                screen.blit(lowervolumebutton, button25.Rect)


            if button26.Rect.collidepoint(mouse): #Higher Volume
                screen.blit(highervolumebuttonlight, button26.Rect)
                if pygame.mouse.get_pressed()[0]:
                    if intro.get_volume() == 0.75:
                        Volume3(self)
                        pygame.event.wait()
                    if intro.get_volume() == 0.5:
                        Volume2(self)
                        pygame.event.wait()
                    if intro.get_volume() == 0.25:
                        Volume1(self)
                        pygame.event.wait()
                    if intro.get_volume() == 0:
                        AutoVolume(self)
                        pygame.event.wait()





            else:
                screen.blit(highervolumebutton, button26.Rect)


            if button27.Rect.collidepoint(mouse): #return to menu
                # button27.DrawButton(screen, BRIGHTBLUE)
                screen.blit(backbuttonlight, button27.Rect)
                if pygame.mouse.get_pressed()[0]:
                    switchScreen(title1())
            else:
                # button27.DrawButton(screen, BLUE)
                screen.blit(backbutton, button27.Rect)


            pygame.display.flip()

class title2:
    def run(self):
        while True:
            ev = pygame.event.poll()
            if ev.type == pygame.QUIT:
                exit()
            elif ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    intro.play()
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
                    switchScreen(game(),numberOfPlayers,0)
                    # switchScreen(whostarts(),numberOfPlayers)
            else:
                button3.DrawButton(screen, RED)

            # 2 PLayers
            if button4.Rect.collidepoint(mouse):
                button4.DrawButton(screen, PINK)
                if pygame.mouse.get_pressed()[0]:
                    numberOfPlayers = 2
                    switchScreen(game(),numberOfPlayers,0)
                    # switchScreen(whostarts(),numberOfPlayers)
            else:
                button4.DrawButton(screen, RED)

            # 3 Players
            if button5.Rect.collidepoint(mouse):
                button5.DrawButton(screen, PINK)
                if pygame.mouse.get_pressed()[0]:
                    numberOfPlayers = 3
                    switchScreen(game(),numberOfPlayers,0)
                    # switchScreen(whostarts(),numberOfPlayers)
            else:
                button5.DrawButton(screen, RED)

            # 4 Players
            if button6.Rect.collidepoint(mouse):
                button6.DrawButton(screen, PINK)
                if pygame.mouse.get_pressed()[0]:
                    numberOfPlayers = 4
                    switchScreen(game(),numberOfPlayers,0)
                    # switchScreen(whostarts(),numberOfPlayers)
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
        time.sleep(1)
        if random.randint(0,1) == 0:
            game1.play()
        else:
            game2.play()
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
                        # button8.DrawButton(main_surface, BRIGHTBLUE)
                        screen.blit(rolldicebuttonlight,button8.Rect)
                        if pygame.mouse.get_pressed()[0]:
                            a = current_player.rollDice()
                            current_player.moveToTile(findNewTile(board,a,current_player))
                        else:
                            a = None

                        #start checking if actions should happen based on current tile or passed tiles
                        if current_player.Tile.Type is "spawn" and current_player.Tile.image == current_player.Color:
                            current_player.Health += 15
                            if current_player.Health > 100:
                                current_player.Health = 100

                        if current_player.Tile.Type is "fight":
                            switchScreen(fight(),players,playerindex,"super")

                        if (current_player.Tile.Type is "spawn" or current_player.Tile.Type is "spawn2") and not current_player.Tile.image == current_player.Color:
                            if current_player.Tile.image == RED: #Red spawn tile = Player 1
                                switchScreen(fight(),players,playerindex,"normal",0)
                            elif current_player.Tile.image == GREEN: #Green spawn tile = Player 2
                                switchScreen(fight(),players,playerindex,"normal",1)
                            elif current_player.Tile.image == YELLOW: #Yellow spawn tile = PLayer 3
                                switchScreen(fight(),players,playerindex,"normal",2)
                            elif current_player.Tile.image == BLUE: #Blue spawn tile = Player 4
                                switchScreen(fight(),players,playerindex,"normal",3)

                        if current_player.Health < 1:
                            pass

                        if a is not None:
                            current_turn += 1 #Next player starts
                            playerindex += 1
                    else:
                        a = None
                        # button8.DrawButton(main_surface, BLUE)
                        screen.blit(rolldicebutton,button8.Rect)
                else:
                    a = None
                    # button8.DrawButton(main_surface, BLUE)
                    screen.blit(rolldicebutton,button8.Rect) #Rolldice
            else: #if the player is dead
                button8.DrawButton(main_surface, BLUE)
                current_turn += 1
                playerindex += 1
                a = None

            return current_turn, playerindex, a

        instructions = 0
        displayConfirmation = 0
        showroll = 0
        while True:
            mouse = pygame.mouse.get_pos()
            ev = pygame.event.poll()  # Look for any event
            if ev.type == pygame.QUIT:  # Window close button clicked?
                exit()  # ... leave game loop
            elif ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    switchScreen(title1())
            # main_surface.fill(WHITE)
            main_surface.blit(bg2, (0,0))
            # Update your game objects and data structures here...
            current_turn, playerindex, playerroll = turn(current_turn,playerindex)
            if playerroll is not None:
                Rolled = playerroll
                showroll = 1
            if showroll:
                textColor = WHITE
                textSurf, textRect = text_objects("The last player: %s" % players[playerindex%4-1].Name, smallText, textColor)
                textPosition = (10,height-120)
                main_surface.blit(textSurf, textPosition)
                textColor = WHITE
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

            textColor = WHITE
            textColor0 = RED
            textColor1 = GREEN
            textColor2 = YELLOW
            textColor3 = BLUE
            text1Surf, text1Rect = text_objects("Current player is ", smallText, textColor)
            text1Position = (10, 10)
            text2Surf, text2Rect = text_objects(str(players[playerindex%4].Name), smallText, players[playerindex%4].Color)
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





            # EXIT BUTTON
            if button7.Rect.collidepoint(mouse):
                # button7.DrawButton(main_surface, PINK)
                screen.blit(exitbuttonlight,button7.Rect)
                if pygame.mouse.get_pressed()[0]:
                    displayConfirmation = 1
            else:
                # button7.DrawButton(main_surface, RED)
                screen.blit(exitbutton,button7.Rect)

            #ingame Instructions
            # button20.DrawButton(main_surface, BLUE)
            screen.blit(ingameinstructionsbutton,button20.Rect) #Instructions
            if button20.Rect.collidepoint(mouse):
                # button20.DrawButton(main_surface, BRIGHTBLUE)
                screen.blit(ingameinstructionsbuttonlight,button20.Rect) #Instructions
                if pygame.mouse.get_pressed()[0]:
                    instructions += 1
            if instructions == 1:
                screen.blit(bg, (0,0))
                button22.DrawButton(main_surface, BLUE)
                if button22.Rect.collidepoint(mouse):
                    button22.DrawButton(main_surface, BRIGHTBLUE)
                    if pygame.mouse.get_pressed()[0]:
                        instructions -= 1

                # button7.DrawButton(main_surface, RED)
                screen.blit(exitbutton,button7.Rect)
                if button7.Rect.collidepoint(mouse):
                    # button7.DrawButton(main_surface, BRIGHTRED)
                    screen.blit(exitbuttonlight,button7.Rect)
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
                button10.DrawButton(main_surface, GREEN) #keep playing
                button11.DrawButton(main_surface, RED) #exit button
                # screen.blit(exitbutton,button11.Rect) #exit button
                if button10.Rect.collidepoint(mouse): #Keep playing
                    button10.DrawButton(main_surface, BRIGHTGREEN)
                    if pygame.mouse.get_pressed(button10.Rect)[0]:
                        displayConfirmation = 0
                if button11.Rect.collidepoint(mouse): #exit button
                    button11.DrawButton(main_surface, BRIGHTRED)

                    if pygame.mouse.get_pressed(button11.Rect)[0]:
                        game1.stop()
                        game2.stop()
                        intro.play()
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
                    intro.stop()
                    bell.play()
                    switchScreen(title2())

            if button14.Rect.collidepoint(mouse):
                button14.DrawButton(screen, BRIGHTRED)
                if pygame.mouse.get_pressed()[0]:
                    switchScreen(title1())

            # Now the surface is ready, tell pygame to display it!
            pygame.display.flip()

        pygame.quit()  # Once we leave the loop, close the window.

class fight:
    def run(self,players,playerindex,type,opponent=SuperFighters[random.randint(0, len(SuperFighters)-1)]):

        def superFight(phase,sf,p1,roll=None,choice=None):
            if phase == 1:
                sf.Dice = random.randint(1,6)
                sf.calculateDamage()
            elif phase == 2:
                roll = p1.rollDice()
                return roll
            elif phase == 3:
                p1.calculateDamage(roll,choice)
                if sf.Damage > p1.Damage: #player needs a damage attribute
                    p1.Health = p1.Health - (sf.Damage - p1.Damage)
                else: #if player does more damage than superfighter, the attacks gets blocked therefor no damage will be taken
                    pass

        def normalFight(phase,p2,p1,roll=None,choice=None):
            if phase == 1:
                roll2 = p2.rollDice()
                return roll2
            elif phase == 2:
                p2.calculateDamage(roll, choice)
            elif phase == 3:
                roll = p1.rollDice()
                return roll
            elif phase == 4:
                p1.calculateDamage(roll,choice)
            elif phase == 5:
                if p1.Damage > p2.Damage:
                    p2.Health = p2.Health - (p1.Damage - p2.Damage)
                elif p2.Damage > p1.Damage:
                    p1.Health = p1.Health - (p2.Damage - p1.Damage)
                else:
                    pass

        text1Surf,text1Pos,text2Surf,text2Pos,text3Surf,text3Pos = None,None,None,None,None,None
        text4Surf,text4Pos,text5Surf,text5Pos,text6Surf,text6Pos = None,None,None,None,None,None
        current_player = players[playerindex%4]
        if type is "normal":
            opponent = players[opponent]
        phase = 6

        if type is "super":
            p2card = pygame.transform.scale(pygame.image.load("assets//cards//" + opponent.Name + ".png"),(500,650))
            p2rect = p2card.get_rect()
        elif type is "normal":
            p2card = pygame.transform.scale(pygame.image.load("assets//scorecards//sc"+str(opponent.Pnr)+".png"),(500,650))
            p2rect = p2card.get_rect()

        p1card = pygame.transform.scale(pygame.image.load("assets//scorecards//sc"+str(current_player.Pnr)+".png"),(500,650))
        p1rect = p1card.get_rect()
        while phase > 0:
            ev = pygame.event.poll()  # Look for any event
            if ev.type == pygame.QUIT:  # Window close button clicked?
                exit()
            mouse = pygame.mouse.get_pos()
            screen.blit(bg2, (0, 0))
            button30.DrawButton(screen,DARKBLUE)
            button31.DrawButton(screen,DARKBLUE)
            button32.DrawButton(screen,DARKBLUE)
            button33.DrawButton(screen,DARKBLUE)


            button34.DrawButton(screen,DARKRED)
            button35.DrawButton(screen,DARKRED)
            button36.DrawButton(screen,DARKRED)
            button37.DrawButton(screen,DARKRED)

            screen.blit(p2card,(width - p2rect.w*1.04, p1rect.h/16))
            screen.blit(p1card,(width/2 - p1rect.w*1.24, p1rect.h/16))

            if phase == 6:
                if button37.Rect.collidepoint(mouse):
                    button37.DrawButton(screen, BRIGHTRED)
                    if pygame.mouse.get_pressed()[0]:
                        if type is "super":
                            superFight(1,opponent,current_player)
                        elif type is "normal":
                            p2roll = normalFight(1,opponent,current_player)
                        phase -= 1
            if phase <= 5:
                if type == "super":
                    text1Surf, text1rect = text_objects(opponent.Name,smallText,WHITE)
                    text1Pos = (width/2-text1rect.w/2,unit*5+10)
                    text2Surf, text2rect = text_objects("Threw %s, and will do:" % opponent.Dice, smallText,WHITE)
                    text2Pos = (width/2-text2rect.w/2,unit*5+30)
                    text3Surf, text3rect = text_objects("%s Damage" % opponent.Damage, largeText,WHITE)
                    text3Pos = (width/2-text3rect.w/2,unit*5+50)
                    if phase == 5: phase -= 1
                elif type == "normal" and phase == 5:
                    text1Surf, text1rect = text_objects("Choose one of three choices", smallText,WHITE)
                    text1Pos = (width/2-text1rect.w/2,unit*5+10)
                    text2Surf, text2rect = text_objects("for your dice throw:",smallText,WHITE)
                    text2Pos = (width/2-text2rect.w/2,unit*5+30)
                    text3Surf, text3rect = text_objects(str(p2roll),largeText,WHITE)
                    text3Pos = (width/2-text3rect.w/2,unit*5+50)

            if phase == 5:
                if button34.Rect.collidepoint(mouse):
                    button34.DrawButton(screen, BRIGHTRED)
                    if pygame.mouse.get_pressed()[0]:
                        normalFight(2,opponent,current_player,p2roll,1)
                        phase -= 1
                else:
                    button34.DrawButton(screen,RED)
                if button35.Rect.collidepoint(mouse):
                    button35.DrawButton(screen, BRIGHTRED)
                    if pygame.mouse.get_pressed()[0]:
                        normalFight(2,opponent,current_player,p2roll,2)
                        phase -= 1
                else:
                    button35.DrawButton(screen,RED)
                if button36.Rect.collidepoint(mouse):
                    button36.DrawButton(screen, BRIGHTRED)
                    if pygame.mouse.get_pressed()[0]:
                        normalFight(2,opponent,current_player,p2roll,3)
                        phase -= 1
                else:
                    button36.DrawButton(screen,RED)
            if phase <= 4 and type is "normal":
                text1Surf, text1rect = text_objects(opponent.Name, smallText,WHITE)
                text1Pos = (width/2-text1rect.w/2,unit*5+10)
                text2Surf, text2rect = text_objects("Will do:",smallText,WHITE)
                text2Pos = (width/2-text2rect.w/2,unit*5+30)
                text3Surf, text3rect = text_objects("%s Damage" % str(opponent.Damage),largeText,WHITE)
                text3Pos = (width/2-text3rect.w/2,unit*5+50)
                screen.blit(text1Surf,text1Pos)
                screen.blit(text2Surf,text2Pos)
                screen.blit(text3Surf,text3Pos)

            if phase == 4:
                if button33.Rect.collidepoint(mouse):
                    button33.DrawButton(screen, BRIGHTBLUE)
                    if pygame.mouse.get_pressed()[0]:
                        if type is "super":
                            p1roll = superFight(2,opponent,current_player)
                            phase -= 1
                        elif type is "normal":
                            p1roll = normalFight(3,opponent,current_player)
                            phase -= 1
                else:
                    button33.DrawButton(screen,BLUE)
            if phase <= 3:
                text4Surf, text4rect = text_objects("Choose one of three choices", smallText,WHITE)
                text4Pos = (width/2-text4rect.w/2,height-(unit*5+70))
                text5Surf, text5rect = text_objects("for your dice throw:",smallText,WHITE)
                text5Pos = (width/2-text5rect.w/2,height-(unit*5+50))
                text6Surf, text6rect = text_objects(str(p1roll),largeText,WHITE)
                text6Pos = (width/2-text6rect.w/2,height-(unit*5+30))

            if phase == 3:
                if button30.Rect.collidepoint(mouse):
                    button30.DrawButton(screen, BRIGHTBLUE)
                    if pygame.mouse.get_pressed()[0]:
                        if type is "super":
                            superFight(3,opponent,current_player,p1roll,1)
                        elif type is "normal":
                            normalFight(4,opponent,current_player,p1roll,1)
                        phase -= 1
                else:
                    button30.DrawButton(screen,BLUE)
                if button31.Rect.collidepoint(mouse):
                    button31.DrawButton(screen, BRIGHTBLUE)
                    if pygame.mouse.get_pressed()[0]:
                        if type is "super":
                            superFight(3,opponent,current_player,p1roll,2)
                        elif type is "normal":
                            normalFight(4,opponent,current_player,p1roll,2)
                        phase -= 1
                else:
                    button31.DrawButton(screen,BLUE)
                if button32.Rect.collidepoint(mouse):
                    button32.DrawButton(screen, BRIGHTBLUE)
                    if pygame.mouse.get_pressed()[0]:
                        if type is "super":
                            superFight(3,opponent,current_player,p1roll,3)
                        elif type is "normal":
                            normalFight(4,opponent,current_player,p1roll,3)
                        phase -= 1
                else:
                    button32.DrawButton(screen,BLUE)

            if phase <= 2:
                text4Surf, text4rect = text_objects(current_player.Name, smallText,WHITE)
                text4Pos = (width/2-text4rect.w/2,height-(unit*5+70))
                text5Surf, text5rect = text_objects("Will do:",smallText,WHITE)
                text5Pos = (width/2-text5rect.w/2,height-(unit*5+50))
                text6Surf, text6rect = text_objects("%s Damage" % str(current_player.Damage),largeText,WHITE)
                text6Pos = (width/2-text6rect.w/2,height-(unit*5+30))


            if not None in [text1Surf,text1Pos,text2Surf,text2Pos,text3Surf,text3Pos]:
                screen.blit(text1Surf,text1Pos)
                screen.blit(text2Surf,text2Pos)
                screen.blit(text3Surf,text3Pos)
            if not None in [text4Surf,text4Pos,text5Surf,text5Pos,text6Surf,text6Pos]:
                screen.blit(text4Surf,text4Pos)
                screen.blit(text5Surf,text5Pos)
                screen.blit(text6Surf,text6Pos)


            pygame.display.flip()


title1().run()