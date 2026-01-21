import json

class Board:
    board: dict
    move: int

    def __init__(self, board=dict):
        self.board = board
        self.putToJson()
        self.move = 1
    
    def putToJson(self):
        with open("curBoard.json", "w") as f:
            json.dump(self.board, f, indent=4)
         

    def get_board(self):
        return self.board
    
    def updateBoard(self, board):
        self.board = board
        self.putToJson()
        
    def setMove(self, move):
        self.move = move


    def printBoard(self):
        print("\n\n                 GAME OF CHESS!     ")
        print(f"\n       move: {self.move}\n")
        board = self.board
        i = 8
        while (i > 0):
            cols = list(board.keys())
            print("    ", end="")
            for col in cols:
                if board[col][i]["piece"] != None:
                    piece = board[col][i]["piece"]
                    print(f"  {symbolPiece(piece)} ")

                if board[col][i]["square"] == "black":
                    print("  □ ", end=" ")
                else:
                    print("  ■ ", end=" ")
            print("\n")
            i-=1
            
    


def initBoard():
    board = {"a": {}, "b": {}, "c": {}, "d": {}, "e": {}, "f": {}, "g": {}, "h": {}}
    alpha = ["a", "b", "c", "d", "e", "f", "g", "h"]
    for i in range(0, 8):
        if i%2 == 0:
            for r in range(1, 9):
                if r%2 == 1:
                    board[alpha[i]].update({r: {"square": "black", "piece": None}})
                else:
                    board[alpha[i]].update({r: {"square": "white", "piece": None}})
        else:
            for r in range(1, 9):
                if r%2 == 1:
                    board[alpha[i]].update({r: {"square": "white", "piece": None}})
                else:
                    board[alpha[i]].update({r: {"square": "black", "piece": None}})
    return board


def symbolPiece(piece):
    color = piece.color()
    ptype = piece.__class__.__name__
    match ptype:
        case "Rook":
            if color == "white":
                return "R"
            else:
                return "r"
        case "Bishop":
            if color == "white":
                return "B"
            else:
                return "b"
        case "Night":
            if color == "white":
                return "N"
            else:
                return "n"
        case "Pawn":
            if color == "white":
                return "P"
            else:
                return "p"
        case "Queen":
            if color == "white":
                return "Q"
            else:
                return "q"
        case "King":
            if color == "white":
                return "K"
            else:
                return "k"
