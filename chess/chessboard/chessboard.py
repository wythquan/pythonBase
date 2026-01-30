class Board():
    board: dict
    move: int
    curPlayer: str

    def __init__(self, board=dict):
        if board != None:
            self.board = board
        else: self.board = {}
        self.move = 1
        self.curPlayer = "white"

    def get_board(self):
        return self.board

    def updateState(self, board, putToJson=None):
        self.board = board
        self.move += 1
        board["move"] = self.move
        if self.curPlayer == "white":
            self.curPlayer = "black"
            board["curPlayer"] = self.curPlayer
        else:
            self.curPlayer = "white"
            board["curPlayer"] = self.curPlayer
        if putToJson:
            putToJson(board)

        
        
    def showMove(self, move):
        self.move = move
        # will return deck on move's move
        
    