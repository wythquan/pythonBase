from chessboard.chessboard import Board

class Piece:
    color: None
    pos: None
    board: None
    data: None

    def __init__(self, color=str, pos=list, board=Board, data=str):
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
    
    