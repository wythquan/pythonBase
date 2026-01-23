from mixins.moveMixin import MoveMixin
from modules.king import King
from modules.rook import Rook

class KingManager(MoveMixin):

    @classmethod
    def avialableMove(cls, king=King, pos2=list, **kwargs):
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
            return True
        elif diffCol == 2 and diffRow == 0:
            if (kwargs[0].__class__.__name__ == "Rook") and (not king.hasMoved) and (not kwargs[0].hasMoved) and (kwargs[0].getColor() == king.getColor()):
                rcol = kwargs[0].getPos()[0]
                if (col1 < col2):
                    #kingside
                    if (board[col1+1][row1]["piece"] == None) and (board[col1+2][row1]["piece"] == None):
                        return cls.castlingMove(king, pos2, kwargs[0])
                    else:
                        # print("\nblocked")
                        return False
                if (col1 > col2):
                    #queenside
                    if (board[col1-1][row1]["piece"] == None) and (board[col1-2][row1]["piece"] == None) and (board[col1-3][row1]["piece"] == None):
                        return cls.castlingMove(king, pos2, kwargs[0])
                    else:
                        # print("\nblocked")
                        return False
            else:
                return False
        
    @classmethod
    def castlingMove(cls, king=King, pos2=list, rook=Rook):
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
        if (col1 > col2):
            #queenside
            newRookCol = cols[col2 + 1]
            rookNewPos = [newRookCol, str(pos1[1])]
            MoveMixin.movePiece(rook.getPos(), rookNewPos, board)
            MoveMixin.movePiece(pos1, pos2, board)
            return True
        else:
            #kingside
            newRookCol = cols[col2 - 1]
            rookNewPos = [newRookCol, str(pos1[1])]
            MoveMixin.movePiece(rook.getPos(), rookNewPos, board)
            MoveMixin.movePiece(pos1, pos2, board)
            return True
        
    @classmethod
    def move(cls, king=King, pos2=list):
        board = king.getBoard()
        pos1 = king.getPos()
        super().move(pos1, pos2, board)
        king.hasMoved = True