import modules.piece as p
from chessboard.chessboard import Board

class Pawn(p.Piece):
    moved: None
    canBnPas: None

    def __init__(self, color=str, pos=list, board=Board, data=str):
        super().__init__(color, pos, board, data)
        self.moved = False
        self.canBnPas = False

    def updateState(self, hasMoved, canBnPas):
        self.hasMoved = hasMoved
        self.canBnPas = canBnPas
    
    def hasMoved(self):
        return self.moved
    
    def couldEnPassanted(self):
        return self.canBnPas
    