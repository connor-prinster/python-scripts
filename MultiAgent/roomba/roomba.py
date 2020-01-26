from enums.directions import Direction

class Roomba:

    battery = 100
    speed = 1
    direction = Direction.RIGHT

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def changeDirection(self, direction):
        self.direction = direction
    
    def turnUp(self):
        if self.direction != Direction.DOWN:
            self.direction = Direction.UP
    
    def turnDown(self):
        if self.direction != Direction.UP:
            self.direction = Direction.DOWN
    
    def turnLeft(self):
        if self.direction != Direction.RIGHT:
            self.direction = Direction.LEFT
    
    def turnRight(self):
        if self.direction != Direction.LEFT:
            self.direction = Direction.RIGHT
    
    def batteryDec(self):
        self.battery = self.battery - 1