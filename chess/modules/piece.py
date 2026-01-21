from chessboard import chessboard as c

class Piece:
    color: None
    pos: None
    board: c.Board | None

    def __init__(self, color, pos=list, board=c.Board):
        self.color = color
        self.pos = pos
        self.board = board
    
    def getPos(self):
        return self.pos
    
    def getColor(self):
        return self.color
    
    def getBoard(self):
        return self.board
    