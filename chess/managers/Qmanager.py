from mixins.moveMixin import MoveMixin
from managers.Bmanager import BishopManager
from managers.Rmanager import RookManager

class QueenManager(MoveMixin):

    @classmethod
    def avialableMove(cls, queen, pos2=list):
        Bboard = queen.getBoard()
        board = Bboard.get_board()
        pos1 = queen.getPos()
        cols = []
        for i in board.keys():
            if (i == "move") or (i == "curPlayer"):
                continue
            cols.append(i)
        col1 = cols.index(pos1[0])
        col2 = cols.index(pos2[0])
        row1 = int(pos1[1])
        row2 = int(pos2[1])
        diffCol = abs(col2 - col1)
        diffRow = abs(row2 - row1)
        if (diffCol == diffRow) and (diffCol != 0):
            #diagonal move
            return BishopManager.avialableMove(bishop=queen, pos2=pos2)
        else:
            #straight move
            return RookManager.avialableMove(rook=queen, pos2=pos2)
        
    @classmethod
    def move(cls, queen, pos2=list):
        board = queen.getBoard()
        pos1 = queen.getPos()
        super().move(pos1, pos2, board)