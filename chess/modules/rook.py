import piece

class Rook(piece.Piece):
    
    hasMoved: None

    def __init__(self, color, pos):
        super().__init__(color, pos)
        self.hasMoved = False

    
