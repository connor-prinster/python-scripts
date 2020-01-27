import enum
import math

class Consts(enum.Enum):
    FPS = 10
    WINDOWWIDTH = 640
    WINDOWHEIGHT = 480
    CELLSIZE = 20
    assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size."
    assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."

    RADIUS = math.floor(CELLSIZE/2.5)
    CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
    CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)
    AREA = CELLWIDTH * CELLHEIGHT

    NUM_ROOMBAS = 3
    NUM_ANIMALS = 2

    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'