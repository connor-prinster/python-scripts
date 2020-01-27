from enums.colors import Color

class Furnitures:
    def returnFurnitures(self):
        return [
            # table in couches
            Furniture(13, 9, Color.TABLE.value), Furniture(14, 9, Color.TABLE.value), Furniture(15, 9, Color.TABLE.value),
            Furniture(13, 10, Color.TABLE.value), Furniture(14, 10, Color.TABLE.value), Furniture(15, 10, Color.TABLE.value),
            Furniture(13, 11, Color.TABLE.value), Furniture(14, 11, Color.TABLE.value), Furniture(15, 11, Color.TABLE.value),
            # couches
            Furniture(14, 8, Color.COUCH.value), Furniture(15, 8, Color.COUCH.value), Furniture(16, 8, Color.COUCH.value),
            Furniture(16, 9, Color.COUCH.value),
            Furniture(12, 10, Color.COUCH.value), Furniture(16, 10, Color.COUCH.value),
            Furniture(12, 11, Color.COUCH.value),
            Furniture(12, 12, Color.COUCH.value), Furniture(13, 12, Color.COUCH.value), Furniture(14, 12, Color.COUCH.value),
            # chairs
            # Furniture(10, 17, Color.CHAIR.value),
            Furniture(12, 18, Color.CHAIR.value),
            Furniture(9, 19, Color.CHAIR.value),
            # Furniture(11, 20, Color.CHAIR.value),
            # table
            Furniture(10, 18, Color.TABLE.value), Furniture(11, 18, Color.TABLE.value), 
            Furniture(10, 19, Color.TABLE.value), Furniture(11, 19, Color.TABLE.value),
            
        ]
    
class Furniture:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color