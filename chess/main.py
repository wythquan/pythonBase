from chessboard import chessboard as c
from managers.BoardManager import BoardManager as BM

from modules.bishop import Bishop
from modules.pawn import Pawn
from modules.king import King
from modules.night import Night
from modules.queen import Queen
from modules.rook import Rook



def getManager(piece):
    match piece.__class__.__name__:
        case "Rook":
            return Rook
        case "Pawn":
            return Pawn
        case "Night":
            return Night
        case "Bishop":
            return Bishop
        case "Queen":
            return Queen
        case "King":
            return King


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
        return True


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
        return True


def game():
    whiteTurnResult = whiteTurn()
    while 1:
        blackTurnResult = blackTurn()
        if (type(whiteTurnResult) == list) and (blackTurnResult == True):     # this means white pushed their pawn 2 squares ahead
            Pawn.updateEnPassantTech(whiteTurnResult, Bboard.get_board())        # if white's pawn wasnt taken it will update possibility of En Passant this pawn
        
        whiteTurnResult = whiteTurn()
        if (type(blackTurnResult) == list) and (whiteTurnResult == True):     # this means black pushed their pawn 2 squares ahead
            Pawn.updateEnPassantTech(blackTurnResult, Bboard.get_board())        # if black's pawn wasnt taken it will update possibility of En Passant this pawn

            
    
game()