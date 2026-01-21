from modules import pawn as p
from mixins import moveMixin as m

class PawnManager(m.MoveMixin):
    
    @classmethod
    def avialableMove(cls, pawn=p.Pawn, pos2=list):
        Bboard = pawn.getBoard()
        board = Bboard.get_board()
        if pawn.getColor() == "white":
            pos1 = pawn.getPos()
            diff = int(pos2[1]) - int(pos1[1])
            if diff > 2:
                return False
            col = pos1[0]
            row = pos1[1]
            if diff == 2:
                if (pawn.hasMoved() == True) or (pos1[0] != pos2[0]):
                    return False
                else:
                    if (board[col][row+1]["piece"]==None) and (board[col][row+2]["piece"]==None):
                        return True
            elif diff == 1:
                if col == pos2[0]:
                    if board[col][row+1]["piece"]==None:
                        return True
                    else:
                        return False
                else:
                    cols = list(board.keys())
                    xcol = cols.index(col)
                    if (pos2[0] == (cols[xcol+1])) or (pos2[0] == (cols[xcol-1])):
                        if (board[pos2[0]][pos2[1]]["piece"] != None) and (board[pos2[0]][pos2[1]]["piece"].getColor() != pawn.getColor()):
                            return True
                        else:
                            return False