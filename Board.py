verticalPos = {
    'a': 7,
    'b': 6,
    'c': 5,
    'd': 4,
    'e': 3,
    'f': 2,
    'g': 1,
    'h': 0,
}


class Board:
    def __init__(self):
        self.turn = 1
        self.board = [
            # h g f e d c b a
            ["R", "N", "B", "Q", "K", "B", "N", "R"],  # 1
            ["P", "P", "P", "P", "P", "P", "P", "P"],  # 2
            [".", ".", ".", ".", ".", ".", ".", "."],  # 3
            [".", ".", ".", ".", ".", ".", ".", "."],  # 4
            [".", ".", ".", ".", ".", ".", ".", "."],  # 5
            [".", ".", ".", ".", ".", ".", ".", "."],  # 6
            ["P", "P", "P", "P", "P", "P", "P", "P"],  # 7
            ["R", "N", "B", "Q", "K", "B", "N", "R"],  # 8
        ]

    def get(self, position):
        return self.board[verticalPos.get(position[0])][int(position[1])-1]

    def move(self, move: str):
        # increase turn counter
        self.turn += 1
        # TODO capture bcc3 maybe lower case letter
        if len(move) == 2:
            self.move_pawn(move)
        if move.startswith("N"):
            self.move_knight(move)
        if move.startswith("B"):
            self.move_bishop(move)
        if move.startswith("Q"):
            self.move_queen(move)
        if move.startswith("K"):
            self.move_king(move)
        if move.startswith("R"):
            self.move_rook(move)
        if move == "0-0":
            self.move_castle_kingside(move)
        if move == "0-0-0":
            self.move_castle_queenside(move)

    def isWhiteTurn(self):
        if self.turn % 1:
            return True
        return False

    def __str__(self):
        boardStr = ""
        for row in self.board:
            for col in row:
                boardStr += col
            boardStr += "\n"
        return boardStr

    def move_pawn(self, move):
        # e4
        if self.isWhiteTurn():
            pass

    def move_knight(self, move):
        pass

    def move_bishop(self, move):
        pass

    def move_queen(self, move):
        pass

    def move_king(self, move):
        pass

    def move_rook(self, move):
        pass

    def move_castle_kingside(self, move):
        pass

    def move_castle_queenside(self, move):
        pass


if __name__ == '__main__':
    board = Board()
    print(board)

    print(board.get("a1"))
