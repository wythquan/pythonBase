import modules.piece as p
from managers.Nmanager import NightManager
from chessboard.chessboard import Board

class Night(p.Piece, NightManager):

    def __init__(self, color=str, pos=list, board=Board, data=str):
        super().__init__(color, pos, board, data)