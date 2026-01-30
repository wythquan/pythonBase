import modules.piece as p
from chessboard.chessboard import Board
from managers.Kmanager import KingManager

class King(p.Piece, KingManager):

    hasMoved: None

    def __init__(self, color=str, pos=list, board=Board, data=str):
        super().__init__(color, pos, board, data)
        self.hasMoved = False

    