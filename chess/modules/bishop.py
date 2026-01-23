import modules.piece as p
from chessboard.chessboard import Board

class Bishop(p.Piece):
    

    def __init__(self, color=str, pos=list, board=Board, data=str):
        super().__init__(color, pos, board, data)
