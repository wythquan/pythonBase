So right now this is a classic chess game but in terminal.
Right now there are just few files that i almost finished. They are: chessboard.py (includes class Board),
piece.py (includes class Piece which is a parent for all other pieces), moveMixin.py (includes only 1 classmethod move()),
Pmanager.py (includes checks for avialable moves), pawn.py (includes class Pawn with additional parameters such
as "hasMoved" and "canBnPas" to track if this pawn can move 2 squares forwand and if it could be taken with En Passant move)

The plan is next:
	1. There is chessboard, which has board as a dictionary type parameter, which includes all squares and pieces on the board.
	2. There is curBoard.json, which has the same data as board for current move
	3. There will be allBoards.json, which will have all moves players did in this game (it means players can return to previous move
if they mousslipped)
	4. Move will be done by using MoveMixin.move() method in piece's manager (example: for bishop its Bmanager.py)
	5. Visuals will be made later using PyGame, for now it'll be just text symbols

Thats all for now.
