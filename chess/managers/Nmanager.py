from mixins.moveMixin import MoveMixin
from modules.night import Night

class NightManager(MoveMixin):

    @classmethod
    def avialableMove(cls, night=Night, pos2=list):
        pos1 = night.getPos()
        Bboard = night.getBoard()
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
        if (diffCol == 2 and diffRow == 1) or (diffCol == 1 and diffRow == 2):
            if board[pos2[0]][row2]["piece"] == None:
                return True
            elif board[pos2[0]][row2]["piece"].getColor() != night.getColor():
                return True
            else:
                return False
        else:
            return False