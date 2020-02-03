import random
from enums.directions import Direction

class Animal:

    direction = Direction.UP

    def __init__(self, x, y, walls, dropOffs):
        self.x = x
        self.y = y
        self.walls = walls
        self.dropOffs = dropOffs

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
                # self.moveForward()
                self.turnRandom()
                return False
        for dropOffs in self.dropOffs:
            if dropOffs.x == newX and dropOffs.y == newY:
                self.bounce()
                return False
        return True
    
    def moveForward(self):
        if self.direction == Direction.UP:
            self.moveUp()
        elif self.direction == Direction.DOWN:
            self.moveDown()
        elif self.direction == Direction.LEFT:
            self.moveLeft()
        else:
            self.moveRight()
    
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

    def turnRight(self):
        self.turnLeft()
        self.turnLeft()
        self.turnLeft()
    
    def bounce(self):
        self.turnRandom()

    def turnRandom(self):
        rand = random.randint(1, 100)
        for i in range(0, rand):
            self.turnLeft()
            self.moveForward()