import piece

class Pawn(piece.Piece):
    moved: None
    canBnPas: None

    def __init__(self, color, pos):
        super().__init__(color, pos)
        self.moved = False
        self.canBnPas = False

    def updateState(self, hasMoved, canBnPas):
        self.hasMoved = hasMoved
        self.canBnPas = canBnPas
    
    def hasMoved(self):
        return self.moved
    
    def couldEnPassanted(self):
        return self.canBnPas

