from chessboard import chessboard as c

class MoveMixin():
    
    @classmethod
    def movePiece(cls, pos1, pos2, Bboard=c.Board):
        board = Bboard.getBoard()
        
        col1 = pos1[0]
        row1 = pos1[1]
        col2 = pos2[0]
        row2 = pos2[1]

        sPiece = board[col1][row1]["piece"]
        board[col2][row2]["piece"] = sPiece
        board[col1][row1]["piece"] = None
        
        Bboard.updateBoard(board)

        return "moved successfully"