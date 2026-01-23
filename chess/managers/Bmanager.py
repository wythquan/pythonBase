from mixins.moveMixin import MoveMixin
from modules.bishop import Bishop

class BishopManager(MoveMixin):

    @classmethod
    def avialableMove(cls, bishop=Bishop, pos2=list):
        pos1 = bishop.getPos()
        Bboard = bishop.getBoard()
        board = Bboard.get_board()
        cols = []
        for i in board.keys():
            if (i == "move") or (i == "curPlayer"): continue
            cols.append(i)
        col1 = cols.index(pos1[0])
        col2 = cols.index(pos2[0])
        diffCol = abs(col2 - col1)
        row1 = int(pos1[1])
        row2 = int(pos2[1])
        diffRow = abs(row2 - row1)
        if diffCol != diffRow:
            return False
        stepCol = 1 if col2 > col1 else -1
        stepRow = 1 if row2 > row1 else -1
        for step in range(1, diffCol-1):
            intermediateCol = cols[col1 + step * stepCol]
            intermediateRow = row1 + step*stepRow
            if board[intermediateCol][intermediateRow]["piece"] != None:
                return False
        if board[pos2[0]][row2]["piece"] == None:
            return True
        elif board[pos2[0]][row2]["piece"].getColor() != bishop.getColor():
            return True
        else:
            return False