from mixins.moveMixin import MoveMixin
from modules.rook import Rook

class RookManager(MoveMixin):

    @classmethod
    def avialableMove(cls, rook=Rook, pos2=list):
        Bboard = rook.getBoard()
        board = Bboard.get_board()
        pos1 = rook.getPos()
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
        if (diffCol != 0) and (diffRow != 0):
            return False
        if diffCol == 0:
            step = 1 if row2 > row1 else -1
            for r in range(row1 + step, row2, step):
                if board[pos1[0]][r]["piece"] != None:
                    return False
            if board[pos2[0]][row2]["piece"] == None:
                return True
            elif board[pos2[0]][row2]["piece"].getColor() != rook.getColor():
                return True
            else:
                return False
        elif diffRow == 0:
            step = 1 if col2 > col1 else -1
            for c in range(col1 + step, col2, step):
                if board[cols[c]][row1]["piece"] != None:
                    return False
            if board[pos2[0]][row2]["piece"] == None:
                return True
            elif board[pos2[0]][row2]["piece"].getColor() != rook.getColor():
                return True
            else:
                return False

    @classmethod
    def move(cls, rook=Rook, pos2=list):
        board = rook.getBoard()
        pos1 = rook.getPos()
        super().move(pos1, pos2, board)
        rook.hasMoved = True