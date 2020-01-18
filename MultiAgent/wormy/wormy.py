# Wormy (a Nibbles clone)
# By Al Sweigart al@inventwithpython.com
# http://inventwithpython.com/pygame
# Released under a "Simplified BSD" license

import random, pygame, sys,math
from pygame.locals import *

FPS = 10
WINDOWWIDTH = 640
WINDOWHEIGHT = 640
CELLSIZE = 20
RADIUS = math.floor(CELLSIZE/2.5)
assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size."
assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."
CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)

#             R    G    B
WHITE       = (255, 255, 255)
BLACK       = (0,0,   0)
RED         = (255,   0,   0)
GREEN       = (0, 255,   0)
DARKGREEN   = (0, 155,   0)
TEAL        = (0, 191, 178)
DARKTEAL    = (26, 94, 99)
DARKGRAY    = (40,  40,  40)
VERMILLION  = (220, 73, 58)
RAISINBLACK = (38, 38, 38)
SEABLUE     = (0, 100, 148)
HANSAYELLOW = (233, 215, 88)

YELLOW = (255,255,0)
BGCOLOR = BLACK

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

HEAD = 0 # syntactic sugar: index of the worm's head

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('Wormy')

    showStartScreen()
    while True:
        runGame()
        showGameOverScreen()


def runGame():
    turn = 0

    wormOne, wormTwo = startWorms()

    # Start the apple in a random place.
    apple = getRandomLocation()
    apple2 = getRandomLocation()

    while True: # main game loop
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if (event.key == K_LEFT) and wormOne['direction'] != RIGHT:
                    wormOne['direction'] = LEFT
                elif (event.key == K_RIGHT) and wormOne['direction'] != LEFT:
                    wormOne['direction'] = RIGHT
                elif (event.key == K_UP) and wormOne['direction'] != DOWN:
                    wormOne['direction'] = UP
                elif (event.key == K_DOWN) and wormOne['direction'] != UP:
                    wormOne['direction'] = DOWN
                elif (event.key == K_a) and wormTwo['direction'] != RIGHT:
                    wormTwo['direction'] = LEFT
                elif (event.key == K_d) and wormTwo['direction'] != LEFT:
                    wormTwo['direction'] = RIGHT
                elif (event.key == K_w) and wormTwo['direction'] != DOWN:
                    wormTwo['direction'] = UP
                elif (event.key == K_s) and wormTwo['direction'] != UP:
                    wormTwo['direction'] = DOWN
                elif event.key == K_ESCAPE:
                    terminate()
                
# ====== CHECK IF EDGE IS HIT ====== #
        # check if the worm has hit itself or the edge
        if turn > 3:
            if wormOne['wormCoords'][HEAD]['x'] == -1 or wormOne['wormCoords'][HEAD]['x'] == CELLWIDTH or wormOne['wormCoords'][HEAD]['y'] == -1 or wormOne['wormCoords'][HEAD]['y'] == CELLHEIGHT:
                return # game over
            for wormBody in wormOne['wormCoords'][1:]:
                if wormBody['x'] == wormOne['wormCoords'][HEAD]['x'] and wormBody['y'] == wormOne['wormCoords'][HEAD]['y']:
                    return # game over
                    # check if the worm has hit itself or the edge
                
            if wormTwo['wormCoords'][HEAD]['x'] == -1 or wormTwo['wormCoords'][HEAD]['x'] == CELLWIDTH or wormTwo['wormCoords'][HEAD]['y'] == -1 or wormTwo['wormCoords'][HEAD]['y'] == CELLHEIGHT:
                return # game over
            for wormBody in wormTwo['wormCoords'][1:]:
                if wormBody['x'] == wormTwo['wormCoords'][HEAD]['x'] and wormBody['y'] == wormTwo['wormCoords'][HEAD]['y']:
                    return # game over
# ================================ #

# ====== CHECK IF APPLES ARE EATEN ====== #
        # check if worm has eaten an apple
        if wormOne['wormCoords'][HEAD]['x'] == apple['x'] and wormOne['wormCoords'][HEAD]['y'] == apple['y']:
            # don't remove worm's tail segment
            apple = getRandomLocation() # set a new apple somewhere
        elif wormOne['wormCoords'][HEAD]['x'] == apple2['x'] and wormOne['wormCoords'][HEAD]['y'] == apple2['y']:
            apple2 = getRandomLocation()
            # make sure that the two apples don't appear in the exact same place
            while apple['x'] == apple2['x'] and apple['y'] == apple2['y']:
                apple2 = getRandomLocation()
        else:
            del wormOne['wormCoords'][-1] # remove worm's tail segment

        # check if worm has eaten an apple
        if wormTwo['wormCoords'][HEAD]['x'] == apple['x'] and wormTwo['wormCoords'][HEAD]['y'] == apple['y']:
            # don't remove worm's tail segment
            apple = getRandomLocation() # set a new apple somewhere
        elif wormTwo['wormCoords'][HEAD]['x'] == apple2['x'] and wormTwo['wormCoords'][HEAD]['y'] == apple2['y']:
            apple2 = getRandomLocation()
            # make sure that the two apples don't appear in the exact same place
            while apple['x'] == apple2['x'] and apple['y'] == apple2['y']:
                apple2 = getRandomLocation()
        else:
            del wormTwo['wormCoords'][-1] # remove worm's tail segment
# ======================================= #

# ====== MOVE WORMS ====== #
        # move the first worm by adding a segment in the direction it is moving
        if wormOne['direction'] == UP:
            newHead = {'x': wormOne['wormCoords'][HEAD]['x'], 'y': wormOne['wormCoords'][HEAD]['y'] - 1}
        elif wormOne['direction'] == DOWN:
            newHead = {'x': wormOne['wormCoords'][HEAD]['x'], 'y': wormOne['wormCoords'][HEAD]['y'] + 1}
        elif wormOne['direction'] == LEFT:
            newHead = {'x': wormOne['wormCoords'][HEAD]['x'] - 1, 'y': wormOne['wormCoords'][HEAD]['y']}
        elif wormOne['direction'] == RIGHT:
            newHead = {'x': wormOne['wormCoords'][HEAD]['x'] + 1, 'y': wormOne['wormCoords'][HEAD]['y']}
        wormOne['wormCoords'].insert(0, newHead)   #have already removed the last segment

        # move the second worm by adding a segment in the direction it is moving        
        if wormTwo['direction'] == UP:
            newHead = {'x': wormTwo['wormCoords'][HEAD]['x'], 'y': wormTwo['wormCoords'][HEAD]['y'] - 1}
        elif wormTwo['direction'] == DOWN:
            newHead = {'x': wormTwo['wormCoords'][HEAD]['x'], 'y': wormTwo['wormCoords'][HEAD]['y'] + 1}
        elif wormTwo['direction'] == LEFT:
            newHead = {'x': wormTwo['wormCoords'][HEAD]['x'] - 1, 'y': wormTwo['wormCoords'][HEAD]['y']}
        elif wormTwo['direction'] == RIGHT:
            newHead = {'x': wormTwo['wormCoords'][HEAD]['x'] + 1, 'y': wormTwo['wormCoords'][HEAD]['y']}
        wormTwo['wormCoords'].insert(0, newHead) 
# ======================== #

# ====== DRAW SCREEN ====== #
        DISPLAYSURF.fill(BGCOLOR)
        drawGrid()
        drawWorm(wormOne['wormCoords'], DARKGREEN, GREEN)
        drawWorm(wormTwo['wormCoords'], DARKTEAL, TEAL)
        drawApple(apple, RED)
        drawApple(apple2, WHITE)
        drawScore(len(wormOne['wormCoords']) - 3)
        pygame.display.update()
        turn = turn + 1
        FPSCLOCK.tick(FPS)
# ========================= #

def drawPressKeyMsg():
    pressKeySurf = BASICFONT.render('Press a key to play.', True, YELLOW)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH - 200, WINDOWHEIGHT - 30)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)

def startWorms():
    wormOne = {}
    wormOne['x'] = random.randint(5, CELLWIDTH - 6)
    wormOne['y'] = random.randint(5, CELLHEIGHT - 6)
    wormOne['wormCoords'] = [
                {'x': wormOne['x'],     'y': wormOne['y']},
                {'x': wormOne['x'] - 1, 'y': wormOne['y']},
                {'x': wormOne['x'] - 2, 'y': wormOne['y']}
                    ]
    wormOne['direction'] = RIGHT

    wormTwo = {}
    wormTwo['x'] = random.randint(5, CELLWIDTH - 6)
    wormTwo['y'] = random.randint(5, CELLHEIGHT - 6)
    while wormOne['x'] == wormTwo['x'] and wormOne['y'] == wormTwo['y']:
        wormTwo['x'] = random.randint(5, CELLWIDTH - 6)
        wormTwo['y'] = random.randint(5, CELLHEIGHT - 6)
    wormTwo['wormCoords'] = [
                {'x': wormOne['x'],     'y': wormOne['y']},
                {'x': wormOne['x'] - 1, 'y': wormOne['y']},
                {'x': wormOne['x'] - 2, 'y': wormOne['y']}
                    ]
    wormTwo['direction'] = LEFT

    return wormOne, wormTwo

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
    titleSurf1 = titleFont.render('Noodles', True, HANSAYELLOW, VERMILLION)
    titleSurf2 = titleFont.render('Danger', True, SEABLUE)

    degrees1 = 0
    degrees2 = 0
    while True:
        DISPLAYSURF.fill(BGCOLOR)
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


def showGameOverScreen():
    gameOverFont = pygame.font.Font('freesansbold.ttf', 150)
    gameSurf = gameOverFont.render('Game', True, WHITE)
    overSurf = gameOverFont.render('Over', True, WHITE)
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

def drawScore(score):
    scoreSurf = BASICFONT.render('Score: %s' % (score), True, WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH - 120, 10)
    DISPLAYSURF.blit(scoreSurf, scoreRect)


def drawWorm(wormCoords, colorOuter, colorInner):
    for coord in wormCoords:
        x = coord['x'] * CELLSIZE
        y = coord['y'] * CELLSIZE
        wormSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        pygame.draw.rect(DISPLAYSURF, colorOuter, wormSegmentRect)
        wormInnerSegmentRect = pygame.Rect(x + 4, y + 4, CELLSIZE - 8, CELLSIZE - 8)
        pygame.draw.rect(DISPLAYSURF, colorInner, wormInnerSegmentRect)


def drawApple(coord, color):
    x = coord['x'] * CELLSIZE
    y = coord['y'] * CELLSIZE
    xcenter = coord['x'] * CELLSIZE + math.floor(CELLSIZE/2)
    ycenter = coord['y'] * CELLSIZE+ math.floor(CELLSIZE/2)
    #appleRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
    #pygame.draw.rect(DISPLAYSURF, RED, appleRect)
    pygame.draw.circle(DISPLAYSURF, color, (xcenter,ycenter), RADIUS)


def drawGrid():
    for x in range(0, WINDOWWIDTH, CELLSIZE): # draw vertical lines
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (x, 0), (x, WINDOWHEIGHT))
    for y in range(0, WINDOWHEIGHT, CELLSIZE): # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (0, y), (WINDOWWIDTH, y))


if __name__ == '__main__':
    main()