from enum import Enum


class Piece(Enum):
    EMPTY = "."
    PAWN = "P"
    ROOK = "R"
    KNIGHT = "N"
    BISHOP = "B"
    QUEEN = "Q"
    KING = "K"
