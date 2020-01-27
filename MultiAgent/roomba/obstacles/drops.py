class DropOffs:
    def returnDropOffs(self):
        return [
            DropOff(30, 2),
            DropOff(30, 3),
            DropOff(30, 4),
            DropOff(30, 5),
            DropOff(30, 6),
            DropOff(30, 7),
            DropOff(30, 8),
            DropOff(30, 15),
            DropOff(30, 16),
            DropOff(30, 17),
            DropOff(30, 18),
            DropOff(30, 19),
            DropOff(30, 20)
        ]


class DropOff:
    def __init__(self, x, y):
        self.x = x
        self.y = y