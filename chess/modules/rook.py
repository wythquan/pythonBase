import modules.piece as p
from managers.Rmanager import RookManager
from chessboard.chessboard import Board

class Rook(p.Piece, RookManager):
    
    hasMoved: None

    def __init__(self, color=str, pos=list, board=Board, data=str):
        super().__init__(color, pos, board, data)
        self.hasMoved = False

    
