from mixins.moveMixin import MoveMixin

class KingManager(MoveMixin):

    @classmethod
    def avialableMove(cls, king, pos2=list):
        pos1 = king.getPos()
        Bboard = king.getBoard()
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
        if (diffCol <= 1) and (diffRow <= 1):
            if (diffCol == 0) and (diffRow == 0):
                return False
            return True
        elif diffCol == 2 and diffRow == 0:
            if (col1 < col2):
                #kingside
                rook = board["h"][row1]["piece"]
                if rook and (rook.__class__.__name__ == "Rook") and (rook.hasMoved == False) and (rook.getColor() == king.getColor()):
                    if (board[cols[col1+1]][row1]["piece"] == None) and (board[cols[col1+2]][row1]["piece"] == None):
                        return cls.castlingMove(king=king, pos2=pos2, rook=rook)
                else:
                    # print("\nblocked")
                    return False
            else:
                #queenside
                rook = board["a"][row1]["piece"]
                if rook and (rook.__class__.__name__ == "Rook") and (rook.hasMoved == False) and (rook.getColor() == king.getColor()):
                    if (board[cols[col1-1]][row1]["piece"] == None) and (board[cols[col1-2]][row1]["piece"] == None) and (board[cols[col1-3]][row1]["piece"] == None):
                        return cls.castlingMove(king=king, pos2=pos2, rook=rook)
                else:
                    # print("\nblocked")
                    return False
        
    @classmethod
    def castlingMove(cls, king, rook, pos2=list):
        pos1 = king.getPos()
        Bboard = king.getBoard()
        board = Bboard.get_board()
        cols = []
        for i in board.keys():
            if (i == "move") or (i == "curPlayer"): continue
            cols.append(i)
        col1 = cols.index(pos1[0])
        col2 = cols.index(pos2[0])
        if (col1 > col2):
            #queenside
            newRookCol = cols[col2 + 1]
            rookNewPos = [newRookCol, str(pos1[1])]
            MoveMixin.move(rook.getPos(), rookNewPos, Bboard)
            MoveMixin.move(pos1, pos2, Bboard)
            return True
        else:
            #kingside
            newRookCol = cols[col2 - 1]
            rookNewPos = [newRookCol, str(pos1[1])]
            MoveMixin.move(rook.getPos(), rookNewPos, Bboard)
            MoveMixin.move(pos1, pos2, Bboard)
            return True
        
    @classmethod
    def move(cls, king, pos2=list):
        board = king.getBoard()
        pos1 = king.getPos()
        if (pos1 != pos2):
            super().move(pos1, pos2, board)
            king.hasMoved = True