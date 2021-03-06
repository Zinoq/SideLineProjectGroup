from Tile import *
from Player import *
from Button import *
from Cards import *
import time


pygame.init()

#audio bestanden
intro = pygame.mixer.Sound("assets\\sounds\\Intro.wav")
bell = pygame.mixer.Sound("assets\\sounds\\BoxBell.wav")
game1 = pygame.mixer.Sound("assets\\sounds\\Game 1.wav")
game2 = pygame.mixer.Sound("assets\\sounds\\Game 2.wav")
dice = pygame.mixer.Sound("assets\\sounds\\Dice.wav")


# surface_sz = width = height = 480   # Desired physical surface size, in pixels.
width = 1280
height = 720
size = width, height
screen = pygame.display.set_mode(size)
mouse = pygame.mouse.get_pos()
numberOfPlayers = 0

# Scherm opdelen in 16 stukken
if not width == height:
    offset = (width-height)/2
else:
    offset = 0
unit = int(height/16)

# Background 1
unscaled_bg = pygame.image.load("assets\\title4.png")
bg = pygame.transform.scale(unscaled_bg,size)

# Background 2
unscaled_bg2 = pygame.image.load("assets\\notextbg.png")
bg2 = pygame.transform.scale(unscaled_bg2,size)

# WIN screen background
unscaled_win = pygame.image.load("assets\\WIN.png")

#buttonImages
startbutton = pygame.image.load("assets\\buttons\\START-BUTTON.png")
startbuttonlight = pygame.image.load("assets\\buttons\\START-BUTTON-LIGHT.png")
instructionsbutton = pygame.image.load("assets\\buttons\\INSTRUCTIONS-BUTTON.png")
instructionsbuttonlight = pygame.image.load("assets\\buttons\\INSTRUCTIONS-BUTTON-LIGHT.png")
exitbutton = pygame.image.load("assets\\buttons\\EXIT-BUTTON.png")
exitbuttonlight = pygame.image.load("assets\\buttons\\EXIT-BUTTON-LIGHT.png")
settingsbutton = pygame.image.load("assets\\buttons\\SETTINGS-BUTTON.png")
settingsbuttonlight = pygame.image.load("assets\\buttons\\SETTINGS-BUTTON-LIGHT.png")
rolldicebutton = pygame.image.load("assets\\buttons\\ROLLDICE-BUTTON.png")
rolldicebuttonlight = pygame.image.load("assets\\buttons\\ROLLDICE-BUTTON-LIGHT.png")
ingameinstructionsbutton = pygame.image.load("assets\\buttons\\INSTRUCTIONS-BUTTON-INGAME.png")
ingameinstructionsbuttonlight = pygame.image.load("assets\\buttons\\INSTRUCTIONS-BUTTON-INGAME-LIGHT.png")
lowervolumebutton = pygame.image.load("assets\\buttons\\LOWERVOLUME-BUTTON.png") #button25
lowervolumebuttonlight = pygame.image.load("assets\\buttons\\LOWERVOLUME-BUTTON-LIGHT.png")
highervolumebutton = pygame.image.load("assets\\buttons\\HIGHERVOLUME-BUTTON.png") #button26
highervolumebuttonlight = pygame.image.load("assets\\buttons\\HIGHERVOLUME-BUTTON-LIGHT.png")
mutebutton = pygame.image.load("assets\\buttons\\MUTE-BUTTON.png")
mutebuttonlight = pygame.image.load("assets\\buttons\\MUTE-BUTTON-LIGHT.png")
backbutton = pygame.image.load("assets\\buttons\\BACK-BUTTON.png")
backbuttonlight = pygame.image.load("assets\\buttons\\BACK-BUTTON-LIGHT.png")
smallbackbutton = pygame.image.load("assets\\buttons\\SMALL-BACK-BUTTON.png")
smallbackbuttonlight = pygame.image.load("assets\\buttons\\SMALL-BACK-BUTTON-LIGHT.png")


# A color is a mix of (Red, Green, Blue)
# <color> = (r, g, b)
WHITE = (255,255,255)
BLACK = (0,0,0)
GRAY = (100,100,100)
LIGHTGRAY = (200,200,200)
RED = (200,60,60)
DARKRED = (160,80,80)
BRIGHTRED = (255,0,0)
GREEN = (80,200,80)
DARKGREEN = (80,160,80)
BRIGHTGREEN = (0,255,0)
BLUE = (80,80,200)
DARKBLUE = (80,80,160)
YELLOW = (200,200,80)
DARKYELLOW = (160,160,80)
PINK = (200,100,100)
BRIGHTBLUE = (51,153,255)

# Doorloopbare lijst aan kleuren voor spelerTiles en normale Tiles
PlayerColors = [RED,GREEN,BLUE,YELLOW]
PlayerColors2 = [DARKRED,DARKGREEN,DARKBLUE,DARKYELLOW]
TileColors = [LIGHTGRAY,GRAY]

# Spelerplaatjes in doorloopbare lijst
pimg = player_images = [
        pygame.transform.scale(pygame.image.load("assets\\player1.png"),(int(unit/2), int(unit/2))),
        pygame.transform.scale(pygame.image.load("assets\\player4.png"),(int(unit/2), int(unit/2))),
        pygame.transform.scale(pygame.image.load("assets\\player2.png"),(int(unit/2), int(unit/2))),
        pygame.transform.scale(pygame.image.load("assets\\player3.png"),(int(unit/2), int(unit/2)))
        ]
text = [
            "Diegene die het hoogst gooit begint met het spel, elke speler heeft zijn eigen hoek (3 vakjes) en start vanaf die hoek met de klok mee.",
            "Elke speler begint met 100 Levenspunten en 15 Conditiepunten en heeft een Scorekaart van zijn Character en een bijpassende pion",
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

_button_images = {
    1 : [pygame.image.load("assets\\buttons\\1-BUTTON.png"),pygame.image.load("assets\\buttons\\1-BUTTON-PLAYER1.png"),pygame.image.load("assets\\buttons\\1-BUTTON-PLAYER2.png")],
    2 : [pygame.image.load("assets\\buttons\\2-BUTTON.png"),pygame.image.load("assets\\buttons\\2-BUTTON-PLAYER1.png"),pygame.image.load("assets\\buttons\\2-BUTTON-PLAYER2.png")],
    3 : [pygame.image.load("assets\\buttons\\3-BUTTON.png"),pygame.image.load("assets\\buttons\\3-BUTTON-PLAYER1.png"),pygame.image.load("assets\\buttons\\3-BUTTON-PLAYER2.png")]
}

roll_buttons = [pygame.image.load("assets\\buttons\\ROLL-BUTTON.png"),pygame.image.load("assets\\buttons\\ROLL-BUTTON-PLAYER1.png"),pygame.image.load("assets\\buttons\\ROLL-BUTTON-PLAYER2.png")]
button_images = {}
for i in range(len(_button_images)):
    lst = []
    for j in range(3):
        lst.append(pygame.transform.scale(_button_images[i+1][j],(unit,unit)))
    button_images[i+1] = lst

# Alle Buttons:
# TITLE SCREEN
#Start
button1 = Button("START!", GREEN, (180, 350, 250, 75),((180+125), (350+(75/2))))

#Exit
button2 = Button("EXIT", RED,(850, 350, 250, 75), ((850+125), (350+(75/2))))

#Instructions
button12 = Button("INSTRUCTIONS", BLUE,(490, 350, 300, 75), ((490+150), (350+(75/2)))) #changed size

#Player amount selection screen
#1 Player
button3 = Button("1 PLAYER", PINK, (180, 250, 250, 75),((180+125), (250+(75/2))))

#2 Players
button4 = Button("2 PLAYERS", PINK, (515, 250, 250, 75),((515+125), (250+(75/2))))

#3 Players
button5 = Button("3 PLAYERS", PINK, (850, 250, 250, 75),((850+125), (250+(75/2))))

#4 Players
button6 = Button("4 PLAYERS", PINK, (515, 350, 250, 75), ((515+125), (350+(75/2))))

# GAME SCREEN
# Exitbutton game
button7 = Button("EXIT", RED,(1020, 640, 250, 75), ((1020+125), (640+(75/2))))

# Roll dice
button8 = Button("Roll Dice", BLUE,(10,640,250,75),((10+125),(640+(75/2))))

# Pop-up screen
button9 = Button("Are you sure you want to quit?", WHITE, (340, 235, 600, 250), ((340+300), (150+125)))

# Keep playing
button10 = Button("Keep playing", GREEN,(350,425,250,50),((350+125),(425+25)))

# Exit anyway
button11 = Button("Quit", RED,(680,425,250,50),((680+125),(425+25)))

# Fight 'Screen'
# Player 2 in SuperFighter en Normal Fights
button30 = Button("1", BLUE,(width/2 - unit * 2, height-unit*2,unit,unit),(width/2-unit*1.5,height-unit*1.5))
button31 = Button("2", BLUE,(width/2 - unit/2, height-unit*2,unit,unit),(width/2,height-unit*1.5))
button32 = Button("3", BLUE,(width/2 + unit, height-unit*2,unit,unit),(width/2+unit*1.5,height-unit*1.5))
button33 = Button("ROLL", BLUE,(width/2 - unit*1.5, height-unit*5,unit*3,unit*2),(width/2,height-unit*4))
#Player 1 in normalFights
button34 = Button("1", RED,(width/2 - unit * 2, unit*1,unit,unit),(width/2-unit*1.5,unit*1.5))
button35 = Button("2", RED,(width/2 - unit/2, unit*1,unit,unit),(width/2,unit*1.5))
button36 = Button("3", RED,(width/2 + unit, unit*1,unit,unit),(width/2+unit*1.5,unit*1.5))
button37 = Button("ROLL", RED,(width/2 - unit*1.5, unit*3,unit*3,unit*2),(width/2,unit*4))

#instructionscreen
#start
button13 = Button("START!", GREEN, (210, 620, 250, 75),((210+125), (620+(75/2))))

#back
button14 = Button("BACK", RED,(820, 620, 250, 75), ((820+125), (620+(75/2))))

# PlayerOrder screen
button15 = Button("", PlayerColors[0],(width/2-width/3,height/5,width/6,height/5),((width/12*3)+175,(height/3*2)+125))
button16 = Button("", PlayerColors[1],(width/2-width/6,height/5,width/5.9,height/5),((width/12*5)+175,(height/3*2)+125))
button17 = Button("", PlayerColors[3],(width/2,height/5,width/6,height/5),((width/12*7)+175,(height/3*2)+125))
button18 = Button("", PlayerColors[2],(width/2+width/6,height/5,width/6,height/5),((width/12*9)+175,(height/3*2)+125))
button19 = Button("START!", GREEN,(width/2-150,height/5*4,300,75),((width/2-150)+150,(height/5*4)+37))

#SuperfightScreen
# button25 = Button("", WHITE, (20, 500, 500, 500), ((20+250),(500+(500/2))))

#ingame instructions button
button20 = Button("Instructions", BLUE,(1020, 550, 250, 75), ((1020+125), (550+(75/2))))
button21 = Button("", WHITE, (0, 0, 1280, 720), (640, 360))

#instructions menu buttons
button22 = Button("Return to game", GREEN,(390, 640, 500, 75), ((390+250), (640+75/2)))

#Settings menu
button23 = Button("Settings", YELLOW, (490, 450, 300, 75), ((490+150), (450+75/2)))

#Volume buttons
button24 = Button("Mute", RED, (490, 400, 300, 75), ((490+150), (400+75/2)))
button25 = Button("Decrease Volume", YELLOW, (320, 500, 300, 75), ((320+150), (500+75/2)))
button26 = Button("Restore Volume", GREEN, (660, 500, 300, 75), ((660+150), (500+75/2)))
button27 = Button("Return to menu", BLUE, (490, 600, 300, 75), ((490+150), (600+75/2)))


#CARDS, SuperFighters
SuperFighters = [
    Card("Agua Man", 12, 15, 9, 7, 7, 13),
    Card("Bruce Hee", 20, 15, 5, 7, 8, 26),
    Card("Chack Norris", 15, 28, 27, 25, 29, 30),
    Card("Dexter", 9, 8, 7, 15, 13, 9),
    Card("Ernold Schwarzenegger", 25, 25, 20, 15, 15, 10),
    Card("Jackie Chen", 12, 10, 15, 9, 10, 25),
    Card("James Bend", 25, 15, 15, 7, 20, 25),
    Card("Jason Statham", 15, 17, 19, 21, 23, 26),
    Card("Jet Ri", 10, 30, 12, 25, 14, 23),
    Card("John Cena", 10, 6, 25, 7, 8, 11),
    Card("Pariz Hilten", 12, 8, 7, 15, 13, 9),
    Card("Steve Seagal", 10, 15, 12, 11, 25, 20),
    Card("Super Merio", 10, 10, 30, 30, 15, 15),
    Card("Terry Crews", 10, 15, 25, 20, 15, 10),
    Card("The Roch", 13, 28, 30, 17, 10, 7),
    Card("Vin Dieser", 20, 25, 30, 25, 20, 15),
    Card("Wesley Sniper", 10, 12, 14, 16, 14, 12)
]



def build_board():
    board = []
    startTiles = []
    pc = 0
    tc = 1
    for j in range(16):
        for i in range(16):
            if (0<=j<=2 or 13<=j<=14) and (0<=i<=2 or 13<=i<=14):
                if (j == 0 and i == 0) or (j == 0 and i == 14) or (j == 14 and i == 0) or (j == 14 and i == 14):
                    board.append(Tile(Point(i,j),"spawn",PlayerColors[pc],unit,offset))
                    startTiles.append(Tile(Point(i,j),"spawn",PlayerColors[pc],unit,offset))
                    pc += 1
                elif (j == 1 and i == 2) or (j == 2 and i == 1):
                    board.append(Tile(Point(i,j),"spawn2", PlayerColors2[0],unit,offset))
                elif (j == 13 and i == 1) or (j == 14 and i == 2):
                    board.append(Tile(Point(i,j),"spawn2", PlayerColors2[2],unit,offset))
                elif (j == 1 and i == 13) or (j == 2 and i == 14):
                    board.append(Tile(Point(i,j),"spawn2", PlayerColors2[1],unit,offset))
                elif (j == 13 and i == 14) or (j == 14 and i == 13):
                    board.append(Tile(Point(i,j),"spawn2", PlayerColors2[3],unit,offset))
            elif (j == 1 and i == 7) or (j == 14 and i == 7):
                board.append(Tile(Point(i,j),"fight",PINK,unit,offset,0))
            elif (j == 7 and i == 1) or (j == 7 and i == 14):
                board.append(Tile(Point(i,j),"fight",PINK,unit,offset,1))
            elif j == 1:
                if 1<i<7:
                    board.append(Tile(Point(i,j),"neutral",TileColors[tc%2-1],unit,offset))
                elif 8<i<14:
                    board.append(Tile(Point(i,j),"neutral",TileColors[tc%2-1],unit,offset))
                tc += 1
            elif j == 14:
                if 1<i<7:
                    board.append(Tile(Point(i,j),"neutral",TileColors[tc%2],unit,offset))
                elif 8<i<14:
                    board.append(Tile(Point(i,j),"neutral",TileColors[tc%2],unit,offset))
                tc += 1
            elif i == 1:
                if 1<j<7:
                    board.append(Tile(Point(i,j),"neutral",TileColors[tc%2],unit,offset))
                elif 8<j<14:
                    board.append(Tile(Point(i,j),"neutral",TileColors[tc%2],unit,offset))
            elif i == 14:
                if 1<j<7:
                    board.append(Tile(Point(i,j),"neutral",TileColors[tc%2],unit,offset))
                elif 8<j<14:
                    board.append(Tile(Point(i,j),"neutral",TileColors[tc%2],unit,offset))
                tc += 1
    return board, startTiles


def playerInit(humans,startTiles,names = None): #give names as a list, in order of players
    names = [
        "Badr Heri",
        "Rocky Belboa",
        "Mike Tysen",
        "Manny Pecquiao"
    ]
    players = []
    pnr = 0
    if names is None:
        while pnr < 4:
            if pnr < humans:
                if pnr == 2:
                    players.append(Player(100,startTiles[3],15,startTiles[3],pimg[3],True,"Player %s" % (3),3,PlayerColors[3]))
                elif pnr == 3:
                    players.append(Player(100,startTiles[2],15,startTiles[2],pimg[2],True,"Player %s" % (4),4,PlayerColors[2]))
                else:
                    players.append(Player(100,startTiles[pnr],15,startTiles[pnr],pimg[pnr],True,"Player %s" % (pnr+1),pnr+1,PlayerColors[pnr]))
            else:
                if pnr == 2:
                    players.append(Player(100,startTiles[3],15,startTiles[3],pimg[3],False,"Player %s" % (3),3,PlayerColors[3]))
                elif pnr == 3:
                    players.append(Player(100,startTiles[2],15,startTiles[2],pimg[2],False,"Player %s" % (4),4,PlayerColors[2]))
                else:
                    players.append(Player(100,startTiles[pnr],15,startTiles[pnr],pimg[pnr],False,"Player %s" % (pnr+1),pnr+1,PlayerColors[pnr]))
            pnr += 1
    else:
        while pnr < 4:
            if names[pnr] == "":
                names[pnr] = "Player %s" % (pnr+1)
            if pnr < humans:
                if pnr == 2:
                    players.append(Player(100,startTiles[3],15,startTiles[3],pimg[3],True,names[2],3,PlayerColors[3]))
                elif pnr == 3:
                    players.append(Player(100,startTiles[2],15,startTiles[2],pimg[2],True,names[3],4,PlayerColors[2]))
                else:
                    players.append(Player(100,startTiles[pnr],15,startTiles[pnr],pimg[pnr],True,names[pnr],pnr+1,PlayerColors[pnr]))
            else:
                if pnr == 2:
                    players.append(Player(100,startTiles[3],15,startTiles[3],pimg[3],False,names[2],3,PlayerColors[3]))
                elif pnr == 3:
                    players.append(Player(100,startTiles[2],15,startTiles[2],pimg[2],False,names[3],4,PlayerColors[2]))
                else:
                    players.append(Player(100,startTiles[pnr],15,startTiles[pnr],pimg[pnr],False,names[pnr],pnr+1,PlayerColors[pnr]))
            pnr += 1
    return players


def findNewTile(board,n,player):
    current = player.Tile
    X1 = current.Position.X - 1
    Y1 = current.Position.Y - 1
    gotcondition = False
    if n > 0:
        if Y1 == 0: # upper line
            if X1+n >= 13: # hit upper-right corner, moving right then down
                if player.Pnr == 2 and X1 != 13:
                    gotcondition = True
                X2 = 13
                Y2 = n - (13 - X1)
            else: # moving right
                X2 = X1+n
                Y2 = Y1
        elif Y1 == 13: # lower line
            if X1-n <= 0:  # hit lower-left corner, moving left then up
                if player.Pnr == 4 and X1 != 0:
                    gotcondition = True
                X2 = 0
                Y2 = 13 - (n-X1)
            else: # moving left
                X2 = X1-n
                Y2 = Y1
        elif 0<Y1<13: # sides
            if X1 == 0: # left side
                if Y1-n <= 0: # hit upper-left corner, moving up then right
                    if player.Pnr == 1 and Y1 != 0:
                        gotcondition = True
                    Y2 = 0
                    X2 = n-Y1
                else: # moving up
                    Y2 = Y1-n
                    X2 = X1
            elif X1 == 13: # right side
                if Y1+n >= 13: # hit lower-right corner, moving down then left
                    if player.Pnr == 3 and Y1 != 13:
                        gotcondition = True
                    Y2 = 13
                    X2 = 13 - (n - (13-Y1))
                else:
                    Y2 = Y1+n
                    X2 = X1
    else: # if user somehow gets a 0 roll
        X2,Y2 = X1,Y1
    if X2 != 7: # fight tiles zijn 2 lang, spelers kunnen alleen op de eerste van de 2 coordinaten staan
        X2 += 1
    if Y2 != 7: # same here
        Y2 += 1
    for tile in board:
        if tile.Position.X == X2 and tile.Position.Y == Y2:
            return tile,gotcondition


def switchScreen(screen,optArg1 = None,optArg2 = None,optArg3 = None,optArg4=None):
    if optArg1 is None:
        screen.run()
    else:
        if optArg2 is None:
            screen.run(optArg1)
        else:
            if optArg3 is None:
                screen.run(optArg1,optArg2)
            else:
                if optArg4 is None:
                    screen.run(optArg1,optArg2,optArg3)
                else:
                    screen.run(optArg1,optArg2,optArg3,optArg4)
