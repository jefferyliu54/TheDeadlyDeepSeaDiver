#####################################################################
#                                                                   #
#                 ~~~ THE DEADLY DEEP SEA DIVER ~~~                 #
#                       ICS3UI Final Project                        #
#                     Programmer: Jeffery Liu                       #
#                     Last Modified: 1/26/2018                      #
#                                                                   #
#####################################################################

from tkinter import *
from time import *
from math import *
from random import *

root = Tk()
screen = Canvas(root, width=900, height=725, background="#4268f4")
    
def setInitialValues():
    global xDiver, yDiver, diver, xSpeed, ySpeed, diverWidth, diverHeight, width1, width2, height1, height2, plasticBottle, bottleWidth, bottleHeight, bottle
    global gameOver, diverDown, diverUp, diverLeft, diverRight, diverDirection, distanceLeft, distanceBar, floating, xBottle, yBottle, yBottleSpeed
    global leftShark, rightShark, shark2, shark3, boat, numBottles, screenMove, screenTop, sharkWidth, sharkHeight, sharkFollow1, sharkDirection1, xShark1, yShark1
    global screenBottom, sharkMoveLeft, xSharkMove, numShark, xSharkSpeed1, ySharkSpeed1, xSharkSpeed2, ySharkSpeed2, xSharkSpeed3, ySharkSpeed3, oceanBottom, oxygenText
    global xShark2, yShark2, sharkFollow2, sharkDirection2, xShark3, yShark3, sharkFollow3, sharkDirection3, bottom, bottlesLeft, bottleText, height1Constant, timeText
    global timeStart, gameTime, timeBarEnd, oxygenBarEnd, totalTime, totalO2, timeMove, oxygenMove, sharkLevel, swimUpMssg, numBubbles, firstShark, oPressed
    global xDistFromShark1, yDistFromShark1, sharkEnd, timeEnd, oxygenEnd, win, xBubbles, yBubbles, bubbles1, bubbles, sharkMssg, lowO2, noTime
    
    xDiver = 450
    yDiver = 360
    diver = 0
    diverWidth = 70
    diverHeight = 25
    width1 = 0

    width2 = width1 + 900
    height1 = 0
    height1Constant = height1 + 0 
    height2 = height1 + 725
    screenTop = 0 
    screenBottom = 725
    bottleWidth = 30
    bottleHeight = 15
    xBottle = []
    yBottle = [900]
    bottle = [] 
    xBottleSpeed = 0
    yBottleSpeed = 1

    screenMove = 1.5 

    xSpeed = 0
    ySpeed = 0 
    floating = -0.5

    xBubbles = []
    yBubbles = []
    bubbles = []
    numBubbles = 16

    sharkWidth = 125
    sharkHeight = 50

    sharkFollow1 = False

    oPressed = False
    sharkEnd = False
    timeEnd = False
    oxygenEnd = False
    win = False
    gameOver = False

    sharkMssg = 0 
    swimUpMssg = 0
    lowO2 = 0
    noTime = 0

    timeStart = time()
    gameTime = 0
    timeBarEnd = 875
    oxygenBarEnd = 875
    totalTime = 120
    totalO2 = 270
    timeMove = (450/120)/10
    oxygenMove = (450/270)/10

    if level == "easy":
        numBottles = 9
        bottlesLeft = numBottles
        numShark = 1
        sharkLevel = 3
        xShark1 = [150]
        yShark1 = [1700]
        xSharkSpeed1 = [0.5]
        ySharkSpeed1 = [0]
        sharkDirection1 = ["right"]
        firstShark = [0]
        totalTime = 180
        totalO2 = 300
        timeMove = (450/180)/10
        oxygenMove = (450/300)/10

    if level == "medium":
        numBottles = 10
        bottlesLeft = numBottles
        numShark = 2
        sharkLevel = 2
        xShark1 = [150,750]
        yShark1 = [1400,2200]
        xSharkSpeed1 = [0.5, -0.7]
        ySharkSpeed1 = [0,0]
        sharkDirection1 = ["right","left"]
        firstShark = [0,0]
        totalTime = 115
        totalO2 = 170
        timeMove = (450/115)/10
        oxygenMove = (450/170)/10

    if level == "hard":
        numBottles = 11
        bottlesLeft = numBottles
        numShark = 3
        sharkLevel = 1
        xShark1 = [150,750,60]
        yShark1 = [1100,1900,2700]
        xSharkSpeed1 = [0.5, -0.7, 0.9]
        ySharkSpeed1 = [0,0,0]
        sharkDirection1 = ["right","left","right"]
        firstShark = [0,0,0]
        totalTime = 180
        totalO2 = 75
        timeMove = (450/180)/10
        oxygenMove = (450/75)/10

    if level == "extreme":
        numBottles = 12
        bottlesLeft = numBottles
        numShark = 3
        sharkLevel = 1
        xShark1 = [150,750,60]
        yShark1 = [1100,1900,2700]
        xSharkSpeed1 = [0.5, -0.7, 0.9]
        ySharkSpeed1 = [0,0,0]
        sharkDirection1 = ["right","left","right"]
        firstShark = [0,0,0]
        totalTime = 170
        totalO2 = 50
        timeMove = (450/170)/10
        oxygenMove = (450/50)/10

    diverDown = PhotoImage(file="ScubaDiverDOWN.gif")
    diverUp = PhotoImage(file="ScubaDiverUP.gif")
    diverLeft = PhotoImage(file="ScubaDiverLEFT.gif")
    diverRight = PhotoImage(file="ScubaDiverRIGHT.gif")
    diverDirection = "right"

    boat = PhotoImage(file="Boat.gif")
    plasticBottle = PhotoImage(file="PlasticBottle.gif")
    bubbles1 = PhotoImage(file="Bubbles1.gif")

    leftShark = PhotoImage(file="SharkLEFT.gif")
    rightShark = PhotoImage(file="SharkRIGHT.gif")
    
    bottleText = PhotoImage(file="BottlesLeft.gif")
    timeText = PhotoImage(file="TimeLeft.gif")
    oxygenText = PhotoImage(file="OxygenLeft.gif")

def setBottleValues():
    global bottleDepth, xBottle, yBottle, bottle, oceanBottom
    
    for i in range(numBottles):
        bottleDepth = randint(100,300)
        xBottle.append(randint(15,885))
        yBottle.append(yBottle[i] + bottleDepth)
        bottle.append(0)

    oceanBottom = yBottle[-1] + 300

def drawBubbles():
    global bubbles

    for i in range(numBubbles):
        xBubbles.append(randint(width1, width2))
        yBubbles.append(randint(425, oceanBottom))
        bubbles.append(0)
        bubbles[i] = screen.create_image(xBubbles[i],yBubbles[i], image=bubbles1)

def drawScenery():
    global sand, sky, oceanSurface, diverBoat

    sand = screen.create_rectangle(0,height1+oceanBottom-250,915,height1+oceanBottom, fill="#c2b280", outline="#c2b280")
    sky = screen.create_rectangle(0,height1-100,915,height1+390, fill="#bedde8", outline="#bedde8")
    diverBoat = screen.create_image(15,height1+237, image=boat)
    oceanSurface = screen.create_line(-15,height1+378,100,height1+392,200,height1+365,300,height1+382,400,height1+360,500,height1+390,600,
                                      height1+355,700,height1+390,800,height1+355,930,height1+385,fill="#4268f4",width=60,smooth="true")

def drawDiver():
    global diver

    if diverDirection == "down":
        diver = screen.create_image(xDiver, yDiver, image=diverDown)
    elif diverDirection == "up":
        diver = screen.create_image(xDiver, yDiver, image=diverUp)
    elif diverDirection == "left":
        diver = screen.create_image(xDiver, yDiver, image=diverLeft)
    else:
        diver = screen.create_image(xDiver, yDiver, image=diverRight)
        
def drawBottles():
    for i in range(numBottles):
        bottle[i] = screen.create_image(xBottle[i], yBottle[i], image=plasticBottle)     
        
def drawSharks():
    global firstShark, xShark1, yShark1, sharkFollow1, sharkDirection1, xDistFromShark1, yDistFromShark1, gameOver, sharkEnd, sharkMssg7
    global timeEnd, oxygenEnd, win, xSharkSpeed1, ySharkSpeed1

    for i in range(numShark):
        if sharkDirection1[i] == "left":
            firstShark[i] = screen.create_image(xShark1[i],yShark1[i], image=leftShark)
        elif sharkDirection1[i] == "right":
            firstShark[i] = screen.create_image(xShark1[i],yShark1[i], image=rightShark)
        elif sharkDirection1[i] == "up":
            firstShark[i] = screen.create_image(xShark1[i],yShark1[i], image=rightShark)
        else:
            firstShark[i] = screen.create_image(xShark1[i],yShark1[i], image=leftShark)

        xDistFromShark1 = xDiver - xShark1[i]
        yDistFromShark1 = yDiver - yShark1[i]

        if -205 < xDistFromShark1 < 205 and -140 < yDistFromShark1 < 140:
            sharkFollow1 = True

        if yShark1[i] < height1+400:
            yShark1[i] = height1+400
        if yShark1[i] >= 2920:
            yShark1[i] = 2920

        if sharkFollow1 == True:
            if xShark1[i] > xDiver+10:
                sharkDirection1[i] = "left" 
                xSharkSpeed1[i] = -0.5
            elif xShark1[i] < xDiver-10:
                sharkDirection1[i] = "right"
                xSharkSpeed1[i] = 0.5
            else:
                if yShark1[i] > yDiver+10:
                    sharkDirection1[i] = "up"
                    xSharkSpeed1[i] = 0
                    ySharkSpeed1[i] = -0.5
                if yShark1[i] < yDiver-10:
                    sharkDirection1[i] = "down"
                    xSharkSpeed1[i] = 0
                    ySharkSpeed1[i] = 0.5
        
            if yShark1[i] > yDiver+10:
                sharkDirection1[i] = "up"
                ySharkSpeed1[i] = -0.5
            elif yShark1[i] < yDiver-10:
                sharkDirection1[i] = "down"
                ySharkSpeed1[i] = 0.5
            else:
                if xShark1[i] > xDiver+10:
                    sharkDirection1[i] = "right"
                    xSharkSpeed1[i] = -0.5
                    ySharkSpeed1[i] = 0
                if xShark1[i] < xDiver-10:
                    sharkDirection1[i] = "left"
                    xSharkSpeed1[i] = 0.5
                    ySharkSpeed1[i] = 0

            if -125 < xDistFromShark1 < 125 and -48 < yDistFromShark1 < 50:
                sharkEnd = True
                timeEnd = False
                oxygenEnd = False
                win = False
                gameOver = True
                
        else:
            if xShark1[i] < width1:
                sharkDirection1[i] = "right"
                xSharkSpeed1[i] = -xSharkSpeed1[i]
            if xShark1[i] > width2:
                sharkDirection1[i] = "left"
                xSharkSpeed1[i] = -xSharkSpeed1[i]

        xShark1[i] = xShark1[i] + xSharkSpeed1[i]
        yShark1[i] = yShark1[i] + ySharkSpeed1[i]
        xShark1.append(xShark1[i])
        yShark1.append(yShark1[i])
        
def keyDownHandler(event):
    global xSpeed, ySpeed, diverDirection, height1, gameOver, xDistFromBottle, yDistFromBottle, win 
    global screenBottom, sharkFollow1, sharkFollow2, sharkFollow3, bottlesLeft, totalO2, oPressed, sharkEnd, timeEnd, oxygenEnd
    
    if event.keysym == "Down":
        diverDirection = "down"
        xSpeed = 0
        ySpeed = 1.5
        height1 = height1 - screenMove
        screenBottom = screenBottom + screenMove
        xShark1 = 150
        for i in range(numBottles):
            yBottle[i] = yBottle[i] - screenMove
        for i in range(numShark):
            yShark1[i] = yShark1[i] - screenMove
        for i in range(numBubbles):
            yBubbles[i] = yBubbles[i] - screenMove
                    
    elif event.keysym == "Up":
        diverDirection = "up"
        xSpeed = 0
        ySpeed = -1.5
        height1 = height1 + screenMove
        screenBottom = screenBottom - screenMove
        for i in range(numBottles):
            yBottle[i] = yBottle[i] + screenMove
        for i in range(numShark):
            yShark1[i] = yShark1[i] + screenMove
        for i in range(numBubbles):
            yBubbles[i] = yBubbles[i] + screenMove
            
    elif event.keysym == "Left":
        diverDirection = "left"
        xSpeed = -1.5
        ySpeed = 0
        
    elif event.keysym == "Right":
        diverDirection = "right"
        xSpeed = 1.5
        ySpeed = 0
        
    elif event.keysym == "space":
        for i in range(numBottles):
            xDistFromBottle = xDiver - xBottle[i]
            yDistFromBottle = yDiver - yBottle[i]
            if -70 < xDistFromBottle < 70 and -70 < yDistFromBottle < 70:
                xBottle.remove(xBottle[i])
                yBottle.remove(yBottle[i])
                xBottle.append(-100)
                yBottle.append(0)
                bottlesLeft -= 1 
                
    elif event.keysym == "o" or event.keysym == "O":
        if yDiver <= height1+400:
            oPressed = True

    elif event.keysym == "Return":
        if xDiver <= 600 and yDiver <= height1+400 and bottlesLeft == 0:
            if bottlesLeft == 0:
                win = True
                sharkEnd = False
                timeEnd = False
                oxygenEnd = False 
                gameOver = True
            
    elif event.keysym == "Escape":
        endGame()

def keyUpHandler(event):
    global xSpeed, ySpeed

    xSpeed = 0
    ySpeed = floating

def updateDiverPosition():
    global xSpeed, ySpeed, xDiver, yDiver, screenMove, floating
    global leftBoundary, rightBoundary, topBoundary, bottomBoundary

    leftBoundary = xDiver - diverWidth
    rightBoundary = xDiver + diverWidth
    topBoundary = yDiver - diverHeight
    bottomBoundary = yDiver + diverHeight

    #Sets left and right boundaries for diver
    if diverDirection == "left" and leftBoundary < width1-25:
        xDiver = width1-25 + diverWidth
    elif diverDirection == "right" and rightBoundary > width2+25:
        xDiver = width2+25 - diverWidth
    #Sets top and bottom boundaries for diver
    elif diverDirection == "down" and bottomBoundary > height2-175:
        screenMove = 1.5
        yDiver = height2-175 - diverHeight
        #Stops diver from swimming deeper after certain distance
        if screenBottom >= oceanBottom:
            screenMove = 0
            yDiver = height2-175 - diverHeight
    elif topBoundary < screenTop+175:
        screenMove = 1.5
        yDiver = screenTop+175 + diverHeight
    elif topBoundary < height1+345:
        if height1 >= screenTop:
            screenMove = 0
            floating = 0 
            yDiver = height1+345 + diverHeight
        else: #Moves screen to the very top 
            screenMove = 1.5
            yDiver = height1+345 + diverHeight
    #Sets regular movement for diver 
    else:
        xDiver = xDiver + xSpeed
        yDiver = yDiver + ySpeed
        floating = -0.5

def timeLeft():
    global win, gameOver, timeBarEnd, timeLeftText, timeTotalBar, timeLeftBar, sharkEnd, timeEnd, oxygenEnd, win

    timeLeftText = screen.create_image(375,35, image=timeText)
    timeTotalBar = screen.create_rectangle(423,19,877,52, fill="#191970", outline="#191970")
    timeLeftBar = screen.create_rectangle(425,21,timeBarEnd,50, fill="#ff6c6c", outline="#ff6c6c")

    if totalTime <= 0:
        timeEnd = True
        sharkEnd = False
        oxygenEnd = False
        win = False 
        gameOver = True
    
def oxygenLeft(): 
    global win, gameOver, oxygenLeftText, oxygenTotalBar, oxygenLeftBar, sharkEnd, timeEnd, oxygenEnd, win
    
    oxygenLeftText = screen.create_image(353,77, image=oxygenText)
    oxygenTotalBar = screen.create_rectangle(423,60,877,94, fill="#191970", outline="#191970")
    oxygenLeftBar = screen.create_rectangle(425,62,oxygenBarEnd,92, fill="#fffa78", outline="#fffa78")

    if totalO2 <= 0:
        oxygenEnd = True
        sharkEnd = False
        timeEnd = False
        win = False 
        gameOver = True
        
def bottlesLeftCount():
    global win, gameOver, bottlesLeftText, bottlesLeftNum, sharkMssg, swimUpMssg
    
    bottlesLeftText = screen.create_image(120,35, image=bottleText)
    bottlesLeftNum = screen.create_text(262,35, text=bottlesLeft, fill="#0bff01", font="Helvetica 45 bold")

def printMessages():
    global sharkMssg, swimUpMssg, lowO2, noTime
    
    if sharkFollow1 == True:
            sharkMssg = screen.create_text(143,100, text="The sharks are following you!", fill="#ff0000", font="Helvetica 15")

    if totalTime <= 30:
        noTime = screen.create_text(555,115, text="TIME IS RUNNING OUT", fill="#ff6c6c", font="Helvetica 18 bold")
        
    if level != "extreme" and totalO2 <= 30:
        lowO2 = screen.create_text(798,115, text="LOW OXYGEN", fill="#ffb000", font="Helvetica 18 bold")
    if level == "extreme" and totalO2 <= 17:
        lowO2 = screen.create_text(798,115, text="LOW OXYGEN", fill="#ffb000", font="Helvetica 18 bold")
        
    if bottlesLeft == 0:
        if xDiver >= 600 and yDiver <= height1+400:
            swimUpMssg = screen.create_text(130,75, text="Get closer to the boat!", fill="#ffb000", font="Helvetica 15 bold")
        elif xDiver <= 600 and yDiver <= height1+400:
            swimUpMssg = screen.create_text(130,75, text="Press Enter!", fill="#ff0000", font="Helvetica 15 bold")            
        else:
            swimUpMssg = screen.create_text(130,75, text="Swim back to the boat!", fill="#ff0000", font="Helvetica 15 bold")
    
def mouseClickHandler(event):
    global xMouse, yMouse, level, page

    xMouse = event.x
    yMouse = event.y
    
    if page == 1:
        if 83 <= xMouse <= 370 and 415 <= yMouse <= 690:
            startButtonPressed()
        if 525 <= xMouse <= 815 and 415 <= yMouse <= 690:
            instructionsPressed()
            
    if page == 3:
        if 50 <= xMouse <= 177 and 570 <= yMouse <= 690:
            screen.delete(firstScreen,instructions)
            introScreen()

    if page == 0:
        if 83 <= xMouse <= 370 and 415 <= yMouse <= 690:
            None
        if 525 <= xMouse <= 815 and 415 <= yMouse <= 690:
            None
        if 83 <= xMouse <= 370 and 415 <= yMouse <= 690:
            None
        if 525 <= xMouse <= 815 and 415 <= yMouse <= 690:
            None
        if 60 <= xMouse <= 315 and 160 <= yMouse <= 415:
            None
        if 435 <= xMouse <= 662 and 147 <= yMouse <= 370:
            None
        if 275 <= xMouse <= 480 and 449 <= yMouse <= 645:
            None
        if 590 <= xMouse <= 840 and 422 <= yMouse <= 670:
            None
        if 50 <= xMouse <= 177 and 570 <= yMouse <= 690:
            None

def mouseClickHandler2(event):
    global xMouse, yMouse, level

    xMouse = event.x
    yMouse = event.y
    
    if page == 2:
        if 60 <= xMouse <= 315 and 160 <= yMouse <= 415:
            level = "easy"
            screen.delete(firstScreen,difficultySelect)
            runGame()
        if 435 <= xMouse <= 662 and 147 <= yMouse <= 370:
            level = "medium"
            screen.delete(firstScreen,difficultySelect)
            runGame()
        if 275 <= xMouse <= 480 and 449 <= yMouse <= 645:
            level = "hard"
            screen.delete(firstScreen,difficultySelect)
            runGame()
        if 590 <= xMouse <= 840 and 422 <= yMouse <= 670:
            level = "extreme"
            screen.delete(firstScreen,difficultySelect)
            runGame()
        if 50 <= xMouse <= 177 and 570 <= yMouse <= 690:
            screen.delete(firstScreen,difficultySelect)
            introScreen()
            
def introScreen():
    global page, intro, firstScreen, startButton

    page = 1

    intro = PhotoImage(file="IntroScreen.gif")
    firstScreen = screen.create_image(450,362.5, image=intro)

    screen.bind("<Button-1>", mouseClickHandler)

def startButtonPressed():
    global page, difficulty, difficultySelect

    page = 2
    
    difficulty = PhotoImage(file="SelectDifficulty.gif")
    difficultySelect = screen.create_image(450,362.5, image=difficulty)

    screen.bind("<Button-1>", mouseClickHandler2)

def instructionsPressed():
    global page, rules, instructions

    page = 3
    
    rules = PhotoImage(file="Instructions.gif")
    instructions = screen.create_image(450,362.5, image=rules)

    screen.bind("<Button-1>", mouseClickHandler)

def GameOver():
    global sharkScreen, sharkEndScreen, timeScreen, timeEndScreen, oxygenScreen, oxygenEndScreen, winScreen, winEndScreen
    global playAgainButton, quitButton, gameOver, sharkEnd, timeEnd, oxygenEnd, win, gameOver

    gameOver = True
    sharkEnd = True
    
    if gameOver == True:
        if sharkEnd == True:
            sharkScreen = PhotoImage(file="EndScreenShark.gif")
            sharkEndScreen = screen.create_image(450,362.5, image=sharkScreen)

            playAgainButton = Button(root, text="PLAY AGAIN", fg="#cc0000", bg="#c7d5ed", font="Helvetica 30 bold", command=playAgainButtonPressed, anchor=CENTER)
            playAgainButton.pack()
            playAgainButton.place(x=45, y=480, width=270, height=100)

            quitButton = Button(root, text="QUIT", fg="#cc0000", bg="#c7d5ed", font="Helvetica 30 bold", command=endGame, anchor=CENTER)
            quitButton.pack()
            quitButton.place(x=595, y=480, width=260, height=100)

        if timeEnd == True:
            timeScreen = PhotoImage(file="EndScreenTime.gif")
            timeEndScreen = screen.create_image(450,362.5, image=timeScreen)

            playAgainButton = Button(root, text="PLAY AGAIN", fg="#445bff", bg="#c7d5ed", font="Helvetica 20 bold", command=playAgainButtonPressed, anchor=CENTER)
            playAgainButton.pack()
            playAgainButton.place(x=175, y=360, width=230, height=75)

            quitButton = Button(root, text="QUIT", fg="#445bff", bg="#c7d5ed", font="Helvetica 20 bold", command=endGame, anchor=CENTER)
            quitButton.pack()
            quitButton.place(x=555, y=360, width=150, height=75)
            
        if oxygenEnd == True:
            oxygenScreen = PhotoImage(file="EndScreenOxygen.gif")
            oxygenEndScreen = screen.create_image(450,362.5, image=oxygenScreen)

            playAgainButton = Button(root, text="PLAY AGAIN", fg="#e8e6d0", bg="#494b4f", font="Helvetica 25 bold", command=playAgainButtonPressed, anchor=CENTER)
            playAgainButton.pack()
            playAgainButton.place(x=70, y=390, width=230, height=75)

            quitButton = Button(root, text="QUIT", fg="#e8e6d0", bg="#494b4f", font="Helvetica 25 bold", command=endGame, anchor=CENTER)
            quitButton.pack()
            quitButton.place(x=630, y=390, width=150, height=75)
            
        if win == True: 
            winScreen = PhotoImage(file="EndScreenWin.gif")
            winEndScreen = screen.create_image(450,362.5, image=winScreen)

            playAgainButton = Button(root, text="PLAY AGAIN", fg="#91ffff", bg="#ffcd4f", font="Helvetica 25 bold", command=playAgainButtonPressed, anchor=CENTER)
            playAgainButton.pack()
            playAgainButton.place(x=140, y=435, width=230, height=75)

            quitButton = Button(root, text="QUIT", fg="#91ffff", bg="#ffcd4f", font="Helvetica 25 bold", command=endGame, anchor=CENTER)
            quitButton.pack()
            quitButton.place(x=530, y=435, width=200, height=75)

def playAgainButtonPressed():
    global sharkEnd, timeEnd, oxygenEnd, win, gameOver
    
    if sharkEnd == True:
        screen.delete(sharkEndScreen)
        sharkEnd = False
    if timeEnd == True: 
        screen.delete(timeEndScreen)
        timeEnd = False
    if oxygenEnd == True:
        screen.delete(oxygenEndScreen)
        oxygenEnd = False
    if win == True:
        screen.delete(winEndScreen)
        win = False

    gameOver = False  
    playAgainButton.destroy()
    quitButton.destroy()
    introScreen()
            
def endGame():
    root.destroy()
    
def runGame():
    global page, gameTime, timeStart, totalTime, totalO2, timeBarEnd, oxygenBarEnd, oPressed

    page = 0
    
    setInitialValues()
    setBottleValues()
 
    while gameOver == False:
        drawScenery()
        drawBubbles()
        drawBottles()
        updateDiverPosition()
        drawDiver()
        drawSharks()
        bottlesLeftCount()
        timeLeft()
        oxygenLeft()
        printMessages()
        timeNow = time()
        timeElapsed = timeNow - timeStart

        if timeElapsed >= 0.1:
            totalTime -= 0.1
            totalO2 -= 0.1
            timeBarEnd -= timeMove
            oxygenBarEnd -= oxygenMove
            timeStart = time()

            if oPressed == True:
                oxygenBarEnd = 875
                if level == "easy":
                    totalO2 = 300
                elif level == "medium":
                    totalO2 = 170
                elif level == "hard":
                    totalO2 = 75
                else:
                    totalO2 = 50
                oPressed = False

        screen.update()
        sleep(0.01)
        screen.delete(sand,sky,oceanSurface,diverBoat,diver,bottlesLeftNum,timeLeftBar,oxygenLeftBar,timeLeftText,
                      timeTotalBar,oxygenLeftText,oxygenTotalBar,bottlesLeftText,swimUpMssg,sharkMssg,lowO2,noTime)

        for i in range(numShark):
            screen.delete(firstShark[i])
        for i in range(numBottles):
            screen.delete(bottle[i])
        for i in range(numBubbles):
            screen.delete(bubbles[i])

    GameOver()
    
root.after(0,GameOver)
screen.bind("<Key>", keyDownHandler)
screen.bind("<KeyRelease>", keyUpHandler)
screen.bind( "<Button-1>", mouseClickHandler)

screen.pack()
screen.focus_set()
root.mainloop()


