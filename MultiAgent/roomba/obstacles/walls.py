class Walls:

    def returnWall(self):
        return [
            Wall(0, 0),  Wall(1, 0),  Wall(2, 0),  Wall(3, 0),  Wall(4, 0),  Wall(5, 0),  Wall(6, 0),  Wall(7, 0),  Wall(8, 0),  Wall(9, 0),  Wall(10, 0),  Wall(11, 0),  Wall(12, 0),  Wall(13, 0),  Wall(14, 0),  Wall(15, 0),  Wall(16, 0),  Wall(17, 0),  Wall(18, 0),  Wall(19, 0),  Wall(20, 0),  Wall(21, 0),  Wall(22, 0),  Wall(23, 0),  Wall(24, 0),  Wall(25, 0),  Wall(26, 0),  Wall(27, 0), Wall(28, 0), Wall(29, 0), Wall(30, 0), Wall(31, 0),
            Wall(0, 1), Wall(27, 1), Wall(28, 1), Wall(29, 1), Wall(30, 1), Wall(31, 1),
            Wall(0, 2), Wall(31, 2),
            Wall(0, 3), Wall(31, 3),
            Wall(0, 4), Wall(31, 4),
            Wall(0, 5), Wall(31, 5),
            Wall(0, 6), Wall(31, 6),
            Wall(0, 7), Wall(31, 7),
            Wall(0, 8), Wall(31, 8),
            Wall(0, 9), Wall(27, 9), Wall(28, 9), Wall(29, 9), Wall(30, 9), Wall(31, 9),
            Wall(0, 10), Wall(27, 10), Wall(28, 10), Wall(29, 10), Wall(30, 10), Wall(31, 10),
            Wall(0, 11), Wall(1, 11), Wall(2, 11), Wall(3, 11), Wall(27, 11), Wall(28, 11), Wall(29, 11), Wall(30, 11), Wall(31, 11),
            Wall(0, 12), Wall(1, 12), Wall(2, 12), Wall(3, 12), Wall(27, 12), Wall(28, 12), Wall(29, 12), Wall(30, 12), Wall(31, 12),
            Wall(0, 13), Wall(1, 13), Wall(2, 13), Wall(3, 13), Wall(27, 13), Wall(28, 13), Wall(29, 13), Wall(30, 13), Wall(31, 13),
            Wall(0, 14), Wall(1, 14), Wall(2, 14), Wall(3, 14), Wall(27, 14), Wall(28, 14), Wall(29, 14), Wall(30, 14), Wall(31, 14),
            Wall(0, 15), Wall(1, 15), Wall(2, 15), Wall(3, 15), Wall(31, 15),
            Wall(0, 16), Wall(1, 16), Wall(2, 16), Wall(31, 16),
            Wall(0, 17), Wall(1, 17), Wall(2, 17), Wall(31, 17),
            Wall(0, 18), Wall(31, 18),
            Wall(0, 19), Wall(31, 19),
            Wall(0, 20), Wall(31, 20),
            Wall(0, 21), Wall(24, 21), Wall(25, 21), Wall(26, 21), Wall(27, 21), Wall(28, 21), Wall(29, 21), Wall(30, 21),Wall(31, 21),
            Wall(0, 22), Wall(1, 22), Wall(2, 22), Wall(3, 22), Wall(24, 22), Wall(25, 22), Wall(26, 22), Wall(27, 22), Wall(28, 22), Wall(29, 22), Wall(30, 22), Wall(31, 22), 
            Wall(0, 23), Wall(1, 23), Wall(2, 23), Wall(3, 23), Wall(4, 23),  Wall(5, 23),  Wall(6, 23),  Wall(7, 23),  Wall(8, 23),  Wall(9, 23),  Wall(10, 23),  Wall(11, 23),  Wall(12, 23),  Wall(13, 23),  Wall(14, 23),  Wall(15, 23),  Wall(16, 23),  Wall(17, 23),  Wall(18, 23),  Wall(19, 23),  Wall(20, 23),  Wall(21, 23),  Wall(22, 23),  Wall(23, 23), Wall(24, 23), Wall(25, 23), Wall(26, 23), Wall(27, 23), Wall(28, 23), Wall(29, 23), Wall(30, 23), Wall(31, 23)   
        ]
        

class Wall:
    def __init__(self, x, y):
        self.x = x
        self.y = y