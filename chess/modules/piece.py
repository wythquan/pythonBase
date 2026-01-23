from chessboard import chessboard as c

class Piece:
    color: None
    pos: None
    board: c.Board
    data: None

    def __init__(self, color=str, pos=list, board=c.Board, data=str):
        self.color = color
        self.pos = pos
        self.board = board
        self.data = data
    
    def getPos(self):
        return self.pos
    
    def getColor(self):
        return self.color
    
    def getBoard(self):
        return self.board
    
    def getData(self):
        return self.data
    
    