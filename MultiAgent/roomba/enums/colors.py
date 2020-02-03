import enum

class Color(enum.Enum):
    ROOMBA_INNER = (47, 57, 77)
    ROOMBA_OUTER = (112, 108, 97)
    ROOMBA_CHARGER= (0, 255, 0)

    GRID_INNER = (248, 244, 227)
    GRID_OUTER = (40, 40, 40)

    DIRT_LIGHT = (238, 224, 203)
    DIRT_DARK = (165, 144, 126)

    ANIMAL_INNER = (105, 20, 14)
    ANIMAL_OUTER = (230, 175, 46)

    WALL = (252, 223, 166)

    DROP_OFF = (2, 2, 2)
    DANGER = (179, 0, 27)

    CHAIR = (140, 188, 185)
    CHAIR_OUTER = (34, 116, 165)
    TABLE = (164, 66, 0)
    COUCH = (153, 194, 77)

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    DARKGREEN = (0, 155, 0)
    DARKGRAY  = (40, 40, 40)
    YELLOW = (255, 255, 0)