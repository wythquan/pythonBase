import json
import copy

from modules import bishop as b
from modules import night as n
from modules import king as k
from modules import pawn as p
from modules import queen as q
from modules import rook as r
from chessboard.chessboard import Board

class BoardManager():

    @classmethod
    def setStartPieces(cls, Bboard=Board):
        board = Bboard.get_board()
        #white
        board["a"][1]["piece"] = r.Rook("white", ["a", 1], Bboard, data="WR")
        board["h"][1]["piece"] = r.Rook("white", ["h", 1], Bboard, data="WR")
        board["b"][1]["piece"] = n.Night("white", ["b", 1], Bboard, data="WN")
        board["g"][1]["piece"] = n.Night("white", ["g", 1], Bboard, data="WN")
        board["c"][1]["piece"] = b.Bishop("white", ["c", 1], Bboard, data="WB")
        board["f"][1]["piece"] = b.Bishop("white", ["f", 1], Bboard, data="WB")
        board["d"][1]["piece"] = q.Queen("white", ["d", 1], Bboard, data="WQ")
        board["e"][1]["piece"] = k.King("white", ["e", 1], Bboard, data="WK")

        board["a"][2]["piece"] = p.Pawn("white", ["a", 2], Bboard, data="WP")
        board["b"][2]["piece"] = p.Pawn("white", ["b", 2], Bboard, data="WP")
        board["c"][2]["piece"] = p.Pawn("white", ["c", 2], Bboard, data="WP")
        board["d"][2]["piece"] = p.Pawn("white", ["d", 2], Bboard, data="WP")
        board["e"][2]["piece"] = p.Pawn("white", ["e", 2], Bboard, data="WP")
        board["f"][2]["piece"] = p.Pawn("white", ["f", 2], Bboard, data="WP")
        board["g"][2]["piece"] = p.Pawn("white", ["g", 2], Bboard, data="WP")
        board["h"][2]["piece"] = p.Pawn("white", ["h", 2], Bboard, data="WP")

        #black
        board["a"][7]["piece"] = p.Pawn("black", ["a", 7], Bboard, data="BP")
        board["b"][7]["piece"] = p.Pawn("black", ["b", 7], Bboard, data="BP")
        board["c"][7]["piece"] = p.Pawn("black", ["c", 7], Bboard, data="BP")
        board["d"][7]["piece"] = p.Pawn("black", ["d", 7], Bboard, data="BP")
        board["e"][7]["piece"] = p.Pawn("black", ["e", 7], Bboard, data="BP")
        board["f"][7]["piece"] = p.Pawn("black", ["f", 7], Bboard, data="BP")
        board["g"][7]["piece"] = p.Pawn("black", ["g", 7], Bboard, data="BP")
        board["h"][7]["piece"] = p.Pawn("black", ["h", 7], Bboard, data="BP")

        board["a"][8]["piece"] = r.Rook("black", ["a", 8], Bboard, data="BR")
        board["h"][8]["piece"] = r.Rook("black", ["h", 8], Bboard, data="BR")
        board["b"][8]["piece"] = n.Night("black", ["b", 8], Bboard, data="BN")
        board["g"][8]["piece"] = n.Night("black", ["g", 8], Bboard, data="BN")
        board["c"][8]["piece"] = b.Bishop("black", ["c", 8], Bboard, data="BB")
        board["f"][8]["piece"] = b.Bishop("black", ["f", 8], Bboard, data="BB")
        board["d"][8]["piece"] = q.Queen("black", ["d", 8], Bboard, data="BQ")
        board["e"][8]["piece"] = k.King("black", ["e", 8], Bboard, data="BK")

        return board

    @classmethod
    def initBoard(cls):
        board = {"a": {}, "b": {}, "c": {}, "d": {}, "e": {}, "f": {}, "g": {}, "h": {}, "move": 1, "curPlayer": "white"}
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
    
    @classmethod
    def printBoard(cls, Bboard):
        board = Bboard.get_board()
        move = Bboard.move
        print("\n\n                 GAME OF CHESS!     ")
        print(f"\n      move: {move}")
        print(f"      current player: {Bboard.curPlayer}\n\n")
        i = 8
        while (i > 0):
            cols = list(board.keys())
            print("    ", end="")
            for col in cols:
                if (col == "move") or (col == "curPlayer"): continue
                if board[col][i]["piece"] != None:
                    piece = board[col][i]["piece"]
                    print(f"  {cls.symbolPiece(piece)} ", end=" ")

                elif board[col][i]["square"] == "black":
                    print("  □ ", end=" ")
                else:
                    print("  ■ ", end=" ")
            print("\n")
            i-=1

    @staticmethod
    def symbolPiece(piece):
        color = piece.getColor()
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
                
    @classmethod
    def putToJson(cls, board):
        with open("curBoard.json", "w") as f:
            prepared = cls.prepareForJson(board)
            json.dump(prepared, f, indent=4)

    @staticmethod
    def prepareForJson(board):
        temp = copy.deepcopy(board)
        for i in temp.keys():
            if (i == "move") or (i == "curPlayer"): continue
            for row in temp[i].keys():
                for piece in temp[i][row].keys():
                    if (piece == "piece") and (temp[i][row][piece] != None):
                        data = temp[i][row][piece]
                        temp[i][row][piece] = data.getData()
        
        return temp
    

    @classmethod
    def gotChecked(cls, Bboard):
        board = Bboard.get_board()
        pass
    
    @classmethod
    def gotMated(cls):
        pass