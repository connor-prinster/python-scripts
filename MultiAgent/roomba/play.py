# Wormy (a Nibbles clone)
# By Al Sweigart al@inventwithpython.com
# http://inventwithpython.com/pygame
# Released under a "Simplified BSD" license

import random, pygame, sys,math
from pygame.locals import *

from roomba import Roomba
from enums.colors import Color
from enums.consts import Consts

from obstacles.walls import Walls
from obstacles.drops import DropOffs
from obstacles.furniture import Furnitures
from obstacles.dirts import Dirts, SuperDirt
from obstacles.animal import Animal

FPS = Consts.FPS.value
WINDOWWIDTH = Consts.WINDOWWIDTH.value
WINDOWHEIGHT = Consts.WINDOWHEIGHT.value
CELLSIZE = Consts.CELLSIZE.value
RADIUS = Consts.RADIUS.value
CELLWIDTH = Consts.CELLWIDTH.value
CELLHEIGHT = Consts.CELLHEIGHT.value
AREA = Consts.AREA.value

walls = Walls().returnWall()
dropOffs = DropOffs().returnDropOffs()
dirts = Dirts().returnDirts()
furnitures = Furnitures().returnFurnitures()
superDirts = []

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('Wormy')

    showStartScreen()
    while True:
        roombas = runGame()
        showGameOverScreen(roombas)


def runGame():

    walls = Walls().returnWall()
    dropOffs = DropOffs().returnDropOffs()
    dirts = Dirts().returnDirts()
    superDirts = generateSuperDirts()

    roombas = generateRoombas(walls, dropOffs, dirts, superDirts, furnitures)
    animals = generateAnimals(walls, dropOffs)
    animal = Animal(2, 2, walls, dropOffs)

    timeLeft = generateEstimatedTime(dirts, superDirts, roombas)

    while True:
        if timeLeft <= 0:
            return roombas
        # event handling loop
        for event in pygame.event.get(): 
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()

        for roomba in roombas:
            roomba.updateDirts(dirts, superDirts)
            dirts, superDirts = roomba.moveForward()
        for animal in animals:
            animal.moveForward()
        for roomba in roombas:
            for animal in animals:
                roomba, animal = animalVersusRoomba(roomba, animal)
        
        for roomba1 in roombas:
            for roomba2 in roombas:
                if roomba1.ids != roomba2.ids:
                    roomba1.collision(roomba2)
                    roomba2.collision(roomba1)

        DISPLAYSURF.fill(Color.GRID_INNER.value)
        drawDirts(dirts, superDirts)
        drawGrid()
        drawWalls()
        drawDrops()
        drawFurnitures()
        
        for roomba in roombas:
            drawRoomba(roomba)
        for animal in animals:
            drawAnimal(animal)

        timeLeft -= 1
        drawScore(timeLeft)
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def drawPressKeyMsg():
    pressKeySurf = BASICFONT.render('Press a key to run Roomba.', True, Color.YELLOW.value)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH - 200, WINDOWHEIGHT - 30)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)

def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()

    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key


def showStartScreen():
    titleFont = pygame.font.Font('freesansbold.ttf', 100)
    titleSurf1 = titleFont.render('Zoomies', True, Color.WHITE.value, Color.DARKGREEN.value)
    titleSurf2 = titleFont.render('Roomie', True, Color.GREEN.value)

    degrees1 = 0
    degrees2 = 0
    while True:
        DISPLAYSURF.fill(Color.BLACK.value)
        rotatedSurf1 = pygame.transform.rotate(titleSurf1, degrees1)
        rotatedRect1 = rotatedSurf1.get_rect()
        rotatedRect1.center = (math.floor(WINDOWWIDTH / 2), math.floor(WINDOWHEIGHT / 2))
        DISPLAYSURF.blit(rotatedSurf1, rotatedRect1)

        rotatedSurf2 = pygame.transform.rotate(titleSurf2, degrees2)
        rotatedRect2 = rotatedSurf2.get_rect()
        rotatedRect2.center = (math.floor(WINDOWWIDTH / 2), math.floor(WINDOWHEIGHT / 2))
        DISPLAYSURF.blit(rotatedSurf2, rotatedRect2)

        drawPressKeyMsg()

        if checkForKeyPress():
            pygame.event.get() # clear event queue
            return
            
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        degrees1 += 3 # rotate by 3 degrees each frame
        degrees2 += 7 # rotate by 7 degrees each frame


def terminate():
    pygame.quit()
    sys.exit()


def getRandomLocation():
    return {'x': random.randint(0, CELLWIDTH - 1), 'y': random.randint(0, CELLHEIGHT - 1)}


def showGameOverScreen(roombas):
    ctr = 1
    string = ""
    total = 0
    for roomba in roombas:
        total += roomba.score

    gameOverFont = pygame.font.Font('freesansbold.ttf', 100)
    gameSurf = gameOverFont.render("Total Score:", True, Color.BLACK.value)
    overSurf = gameOverFont.render(str(total), True, Color.BLACK.value)
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (math.floor(WINDOWWIDTH / 2), 10)
    overRect.midtop = (math.floor(WINDOWWIDTH / 2), gameRect.height + 10 + 25)

    DISPLAYSURF.blit(gameSurf, gameRect)
    DISPLAYSURF.blit(overSurf, overRect)
    drawPressKeyMsg()
    pygame.display.update()
    pygame.time.wait(500)
    checkForKeyPress() # clear out any key presses in the event queue

    while True:
        if checkForKeyPress():
            pygame.event.get() # clear event queue
            return

def drawScore(timeLeft):
    scoreSurf = BASICFONT.render('Time Left: %s' % (timeLeft), True, Color.BLUE.value)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH - 150, 10)
    DISPLAYSURF.blit(scoreSurf, scoreRect)

def drawRoomba(roomba):
    drawCharger(roomba.initX, roomba.initY)

    x = roomba.x * CELLSIZE
    y = roomba.y * CELLSIZE
    roombaInnerSegmentRect = pygame.Rect(x + 4, y + 4, CELLSIZE - 8, CELLSIZE - 8)
    pygame.draw.rect(DISPLAYSURF, Color.ROOMBA_INNER.value, roombaInnerSegmentRect)
    
def drawAnimal(animal):
    x = animal.x * CELLSIZE
    y = animal.y * CELLSIZE
    animalInnerSegmentRect = pygame.Rect(x + 4, y + 4, CELLSIZE - 8, CELLSIZE - 8)
    pygame.draw.rect(DISPLAYSURF, Color.ANIMAL_INNER.value, animalInnerSegmentRect)
    animalOuterSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
    pygame.draw.rect(DISPLAYSURF, Color.ANIMAL_OUTER.value, animalOuterSegmentRect)

def drawCharger(passx, passy):
    x = passx * CELLSIZE
    y = passy * CELLSIZE
    chargerSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
    pygame.draw.rect(DISPLAYSURF, Color.ROOMBA_CHARGER.value, chargerSegmentRect)

def drawWalls():
    for wall in walls:
        x = wall.x * CELLSIZE
        y = wall.y * CELLSIZE
        wallSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        pygame.draw.rect(DISPLAYSURF, Color.WALL.value, wallSegmentRect)

def drawDrops():
    for dropOff in dropOffs:
        x = dropOff.x * CELLSIZE
        y = dropOff.y * CELLSIZE
        dropSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        pygame.draw.rect(DISPLAYSURF, Color.DROP_OFF.value, dropSegmentRect)

def drawApple(coord):
    x = coord['x'] * CELLSIZE
    y = coord['y'] * CELLSIZE
    xcenter = coord['x'] * CELLSIZE + math.floor(CELLSIZE/2)
    ycenter = coord['y'] * CELLSIZE+ math.floor(CELLSIZE/2)
    pygame.draw.circle(DISPLAYSURF, Color.RED.value ,(xcenter,ycenter),RADIUS)

def drawDirts(dirts, superDirts):
    for dirt in dirts:
        x = dirt.x * CELLSIZE
        y = dirt.y * CELLSIZE
        dirtSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        pygame.draw.rect(DISPLAYSURF, Color.DIRT_LIGHT.value, dirtSegmentRect)

    for superDirt in superDirts:
        x = superDirt.x * CELLSIZE
        y = superDirt.y * CELLSIZE
        dirtSegmentRect = pygame.Rect(x + 4, y + 4, CELLSIZE - 8, CELLSIZE - 8)
        pygame.draw.rect(DISPLAYSURF, Color.DIRT_DARK.value, dirtSegmentRect)

def drawFurnitures():
    for furniture in furnitures:
        x = furniture.x * CELLSIZE
        y = furniture.y * CELLSIZE
        furnitureSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        pygame.draw.rect(DISPLAYSURF, furniture.color, furnitureSegmentRect)

def drawGrid():
    for x in range(0, WINDOWWIDTH, CELLSIZE): # draw vertical lines
        pygame.draw.line(DISPLAYSURF, Color.GRID_OUTER.value, (x, 0), (x, WINDOWHEIGHT))
    for y in range(0, WINDOWHEIGHT, CELLSIZE): # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, Color.GRID_OUTER.value, (0, y), (WINDOWWIDTH, y))

def generateSuperDirts():
    superDirts = []

    for i in range(CELLWIDTH):
        for j in range(CELLHEIGHT):
            rando = random.randint(0, 10)
            if rando % 7 == 0:
                superDirts.append(SuperDirt(i, j))
    
    return superDirts
    
def animalVersusRoomba(roomba, animal):
    animalPos = animal.getPos()
    roombaPos = roomba.getPos()

    if animalPos['x'] == roombaPos['x'] and animalPos['y'] == roombaPos['y']:
        roomba.decreaseHealth()
        
    return roomba, animal

def generateRoombas(walls, dropOffs, dirts, superDirts, furnitures):
    roombas = []
    for i in range(Consts.NUM_ROOMBAS.value):
        startx = random.randint(5, CELLWIDTH - 6)
        starty = random.randint(5, CELLHEIGHT - 6)
        roombas.append(
            Roomba(
                startx, starty, 
                walls, dropOffs, 
                dirts, superDirts, 
                furnitures, AREA,
                i
            )
        )

    return roombas

def generateAnimals(walls, dropOffs):
    animals = []
    for i in range(Consts.NUM_ANIMALS.value):
        startx = random.randint(5, CELLWIDTH - 6)
        starty = random.randint(5, CELLHEIGHT - 6)
        animals.append(
            Animal(startx, starty, walls, dropOffs)
        )
    return animals

def generateEstimatedTime(dirts, superDirts, roombas):
    timeLeft = 0
    timeLeft += len(dirts)
    timeLeft += (2 * len(superDirts))
    if len(roombas) >= 1:
        timeLeft /= (len(roombas) - 1)
    return int(timeLeft)
        


if __name__ == '__main__':
    main()