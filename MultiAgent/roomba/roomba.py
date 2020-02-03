import random, pygame, sys,math
from enums.directions import Direction
from obstacles.walls import Wall
from obstacles.dirts import Dirt
from enums.consts import Consts

class Roomba:

    dead = False
    health = 3
    speed = 1
    direction = Direction.RIGHT
    stalled = False
    score = 0

    def __init__(self, x, y, walls, dropOffs, dirts, superDirts, furnitures, area, ids):
        self.x = x
        self.y = y
        self.initX = x
        self.initY = y
        self.walls = walls
        self.dropOffs = dropOffs
        self.dirts = dirts
        self.superDirts = superDirts
        self.furnitures = furnitures
        self.area = area
        self.ids = ids
    
    def decreaseHealth(self):
        self.health -= 1
        if self.health <= 0:
            self.x = self.initX
            self.y = self.initY
            self.dead = True
    
    def increaseScore(self):
        self.score += 1

    def getHealth(self):
        return self.health

    def getPos(self):
        return {'x': self.x, 'y': self.y}

    def moveUp(self):
        self.direction = Direction.UP
        newY = self.y - 1
        if self.canMove(self.x, newY):
            self.y = newY
    
    def moveDown(self):
        self.direction = Direction.DOWN
        newY = self.y + 1
        if self.canMove(self.x, newY):
            self.y = newY

    def moveLeft(self):
        self.direction = Direction.LEFT
        newX = self.x - 1
        if self.canMove(newX, self.y):
            self.x = newX
    
    def moveRight(self):
        self.direction = Direction.RIGHT
        newX = self.x + 1
        if self.canMove(newX, self.y):
            self.x = newX

    def canMove(self, newX, newY):
        for wall in self.walls:
            if wall.x == newX and wall.y == newY:
                self.turnLeft()
                self.moveForward()
                return False
        for furniture in self.furnitures:
            if furniture.x == newX and furniture.y == newY:
                self.turnLeft()
                self.moveForward()
                return False
        for dropOffs in self.dropOffs:
            if dropOffs.x == newX and dropOffs.y == newY:
                self.bounce()
                return False
        return True
    
    def moveForward(self):

        if self.dead == True:
            return self.removeDirt()

        if self.stalled == True:
            self.stalled = False
            return self.removeDirt()

        if self.isNextDirty() == False: # kind of like a random turn
            self.turnLeft()

        if self.isClean() == 4:
            rando = random.randint(0, 10)
            for i in range (0, rando):
                self.turnRight()

        if self.direction == Direction.UP:
            self.moveUp()
        elif self.direction == Direction.DOWN:
            self.moveDown()
        elif self.direction == Direction.LEFT:
            self.moveLeft()
        else:
            self.moveRight()

        return self.removeDirt()

    def removeDirt(self):
        for dirt in self.dirts:
            if self.x == dirt.x and self.y == dirt.y:
                self.dirts.remove(dirt)
                self.increaseScore()
        for superDirt in self.superDirts:
            if self.x == superDirt.x and self.y == superDirt.y:
                self.stalled = True
                self.superDirts.remove(superDirt)
                self.increaseScore()
        return self.dirts, self.superDirts

    def isNextDirty(self):

        upPos = Dirt(self.x, self.y - 1)
        downPos = Dirt(self.x, self.y + 1)
        leftPos = Dirt(self.x - 1, self.y)
        rightPos = Dirt(self.x + 1, self.y)

        if self.direction == Direction.UP:
            return self.checkObstacle(upPos, self.dirts)
        elif self.direction == Direction.DOWN:
            return self.checkObstacle(downPos, self.dirts)
        elif self.direction == Direction.LEFT:
            return self.checkObstacle(leftPos, self.dirts)
        else:
            return self.checkObstacle(rightPos, self.dirts)

    def bounce(self):
        if self.direction == Direction.UP:
            self.moveDown()
        elif self.direction == Direction.DOWN:
            self.moveUp()
        elif self.direction == Direction.LEFT:
            self.moveRight()
        else:
            self.moveLeft()

        self.turnLeft()
    
    def turnLeft(self):
        # below is following turning left based on a compass
        #       up
        # left      right
        #       down
        if self.direction == Direction.UP:
            self.direction = Direction.LEFT
        elif self.direction == Direction.LEFT:
            self.direction = Direction.DOWN
        elif self.direction == Direction.DOWN:
            self.direction = Direction.RIGHT
        else:
            self.direction = Direction.UP
        
    def updateDirts(self, dirts, superDirts):
        self.dirts = dirts
        self.superDirts = superDirts


    def turnRight(self):
        self.turnLeft()
        self.turnLeft()
        self.turnLeft()
    

    def turnAround(self):
        self.turnLeft()
        self.turnLeft()


    def batteryDec(self):
        self.battery = self.battery - 1
    

    def checkObstacle(self, test, arr):
        for obstacle in arr:
            if test.x == obstacle.x and test.y == obstacle.y:
                return True
        return False


    def isClean(self):
        clean = 0

        upPos = Dirt(self.x, self.y - 1)
        downPos = Dirt(self.x, self.y + 1)
        leftPos = Dirt(self.x - 1, self.y)
        rightPos = Dirt(self.x + 1, self.y)

        if self.checkObstacle(upPos, self.dirts) == False:
            clean += 1
        if self.checkObstacle(downPos, self.dirts) == False:
            clean += 1
        if self.checkObstacle(leftPos, self.dirts) == False:
            clean += 1
        if self.checkObstacle(rightPos, self.dirts) == False:
            clean += 1

        return clean
    
    def collision(self, otherRoomba):
        if otherRoomba.x == self.x and otherRoomba.y == self.y:
            self.turnLeft()