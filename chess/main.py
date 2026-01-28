from chessboard import chessboard as c
from managers.BoardManager import BoardManager as BM
from managers.Bmanager import BishopManager
from managers.Kmanager import KingManager
from managers.Nmanager import NightManager
from managers.Pmanager import PawnManager
from managers.Qmanager import QueenManager
from managers.Rmanager import RookManager


def getManager(piece):
    match piece.__class__.__name__:
        case "Rook":
            return RookManager
        case "Pawn":
            return PawnManager
        case "Night":
            return NightManager
        case "Bishop":
            return BishopManager
        case "Queen":
            return QueenManager
        case "King":
            return KingManager


initBoard = BM.initBoard()
Bboard = c.Board(initBoard)
BM.setStartPieces(Bboard)

# board = Bboard.get_board()
# BM.putToJson(board)
# BM.printBoard(Bboard)

def whiteTurn():
    cols = ["a", "b", "c", "d", "e", "f", "g", "h"]
    while 1:
        board = Bboard.get_board()
        BM.putToJson(board)
        BM.printBoard(Bboard)

        pFrom = input("\n    Pick piece\n")

        if len(pFrom) != 2:
            print("\n    !! Pick a valid square !!\n")
            continue
        if not pFrom[1].isdigit():
            print("\n    !! Pick a valid square !!\n")
            continue
        
        pos1 = [pFrom[0], pFrom[1]]
        if (pos1[0].lower() not in cols) or ((int(pos1[1]) > 8) or (int(pos1[1]) < 1)):
            print("\n    !! Pick a valid square !!\n")
            continue
        piece = board[pos1[0]][int(pos1[1])]["piece"]
        if piece == None:
            print("\n    !! Pick a valid piece !!\n")
            continue
        if piece.getColor() != "white":
            print("\n    !! Pick white piece !!\n")
            continue
        
        pTo = input("\n    Pick destination\n")

        if len(pTo) != 2:
            print("\n    !! Pick a valid square !!\n")
            continue
        if not pTo[1].isdigit():
            print("\n    !! Pick a valid square !!\n")
            continue

        pos2 = [pTo[0], pTo[1]]
        if (pos2[0].lower() not in cols) or ((int(pos2[1]) > 8) or (int(pos2[1]) < 1)):
            print("\n    !! Pick a valid square !!\n")
            continue
        
        pieceManager = getManager(piece)
        validMove = pieceManager.avialableMove(piece, pos2)
        if not validMove:
            print("\n    Move is not valid.\n")
            continue
        pieceManager.move(piece, pos2)
        if (piece.__class__.__name__ == "Pawn") and (piece.canBnPas == True):
            return pos2
        return "done"


def blackTurn():
    cols = ["a", "b", "c", "d", "e", "f", "g", "h"]
    while 1:
        board = Bboard.get_board()
        BM.putToJson(board)
        BM.printBoard(Bboard)
        
        pFrom = input("\n    Pick piece\n")

        if len(pFrom) != 2:
            print("\n    !! Pick a valid square !!\n")
            continue
        if not pFrom[1].isdigit():
            print("\n    !! Pick a valid square !!\n")
            continue
        
        pos1 = [pFrom[0], pFrom[1]]
        if (pos1[0].lower() not in cols) or ((int(pos1[1]) > 8) or (int(pos1[1]) < 1)):
            print("\n    !! Pick a valid square !!\n")
            continue
        piece = board[pos1[0]][int(pos1[1])]["piece"]
        if piece == None:
            print("\n    !! Pick a valid piece !!\n")
            continue
        if piece.getColor() != "black":
            print("\n    !! Pick white piece !!\n")
            continue
        
        pTo = input("\n    Pick destination\n")

        if len(pTo) != 2:
            print("\n    !! Pick a valid square !!\n")
            continue
        if not pTo[1].isdigit():
            print("\n    !! Pick a valid square !!\n")
            continue
        
        pos2 = [pTo[0], pTo[1]]
        if (pos2[0].lower() not in cols) or ((int(pos2[1]) > 8) or (int(pos2[1]) < 1)):
            print("\n    !! Pick a valid square !!\n")
            continue
        
        pieceManager = getManager(piece)
        validMove = pieceManager.avialableMove(piece, pos2)
        if not validMove:
            print("\n    Move is not valid.\n")
            continue
        pieceManager.move(piece, pos2)
        if (piece.__class__.__name__ == "Pawn") and (piece.canBnPas == True):
            return pos2
        return "done"


def game():
    whiteTurnResult = whiteTurn()
    while 1:
        blackTurnResult = blackTurn()
        if (type(whiteTurnResult) == list) and (blackTurnResult == "done"):     # this means white pushed their pawn 2 squares ahead
            PawnManager.updateEnPassantTech(whiteTurnResult, Bboard.get_board())        # if white's pawn wasnt taken it will update possibility of En Passant this pawn

        whiteTurnResult = whiteTurn()
        if (type(blackTurnResult) == list) and (whiteTurnResult == "done"):     # this means black pushed their pawn 2 squares ahead
            PawnManager.updateEnPassantTech(blackTurnResult, Bboard.get_board())        # if black's pawn wasnt taken it will update possibility of En Passant this pawn

            
    
game()