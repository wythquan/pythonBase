import modules.piece as p
from managers.Qmanager import QueenManager
from chessboard.chessboard import Board

class Queen(p.Piece, QueenManager):

    def __init__(self, color=str, pos=list, board=Board, data=str):
        super().__init__(color, pos, board, data)