from mixins import moveMixin as m

class PawnManager(m.MoveMixin):
    
    @classmethod
    def avialableMove(cls, pawn, pos2=list):
        Bboard = pawn.getBoard()
        board = Bboard.get_board()
        if pawn.getColor() == "white":
            pos1 = pawn.getPos()
            diff = int(pos2[1]) - int(pos1[1])
            if (diff > 2) or (diff <= 0):
                return False
            col = pos1[0]
            row = int(pos1[1])
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
                        enemy = board[pos2[0]][int(pos2[1])]["piece"]               # regular diagonal take
                        if (enemy != None) and (enemy.getColor() != pawn.getColor()):
                            return True
                        enemy = board[pos2[0]][int(pos1[1])]["piece"]               # en passant take
                        if (enemy != None) and (enemy.__class__.__name__ == "Pawn") and (enemy.getColor() != pawn.getColor()) and (enemy.canBnPas == True):
                            ePos = enemy.getPos()
                            board[ePos[0]][int(ePos[1])]["piece"] = None
                            return True
                        else:
                            return False
                    else:
                        return False
                    
        if pawn.getColor() == "black":
            pos1 = pawn.getPos()
            diff = int(pos1[1]) - int(pos2[1])
            if (diff > 2) or (diff <= 0):
                return False
            col = pos1[0]
            row = int(pos1[1])
            if diff == 2:
                if (pawn.hasMoved() == True) or (pos1[0] != pos2[0]):
                    return False
                else:
                    if (board[col][row-1]["piece"]==None) and (board[col][row-2]["piece"]==None):
                        return True
            elif diff == 1:
                if col == pos2[0]:
                    if board[col][row-1]["piece"]==None:
                        return True
                    else:
                        return False
                else:
                    cols = list(board.keys())
                    xcol = cols.index(col)
                    if (pos2[0] == (cols[xcol+1])) or (pos2[0] == (cols[xcol-1])):
                        enemy = board[pos2[0]][int(pos2[1])]["piece"]               # regular diagonal take
                        if (enemy != None) and (enemy.getColor() != pawn.getColor()):
                            return True
                        enemy = board[pos2[0]][int(pos1[1])]["piece"]               # en passant take
                        if (enemy != None) and (enemy.__class__.__name__ == "Pawn") and (enemy.getColor() != pawn.getColor()) and (enemy.canBnPas == True):
                            ePos = enemy.getPos()
                            board[ePos[0]][int(ePos[1])]["piece"] = None
                            return True
                        else:
                            return False
                    else:
                        return False
                    
    @classmethod
    def move(cls, pawn, pos2=list):
        board = pawn.getBoard()
        pos1 = pawn.getPos()
        super().move(pos1, pos2, board)
        if pawn.hasMoved() == False:
            pawn.canBnPas = True
        else:
            pawn.canBnPas = False
        pawn.moved = True

    @classmethod
    def updateEnPassantTech(cls, pos=list, board=dict):
        if board[pos[0]][int(pos[1])]["piece"] != None:
            board[pos[0]][int(pos[1])]["piece"].canBnPas = False