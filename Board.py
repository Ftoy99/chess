class Board:
    board = []

    def __init__(self):
        self.board = [
            # H G F E D C B A
            ["R", "N", "B", "Q", "K", "B", "N", "R"],  # 1
            ["P", "P", "P", "P", "P", "P", "P", "P"],  # 2
            [".", ".", ".", ".", ".", ".", ".", "."],  # 3
            [".", ".", ".", ".", ".", ".", ".", "."],  # 4
            [".", ".", ".", ".", ".", ".", ".", "."],  # 5
            [".", ".", ".", ".", ".", ".", ".", "."],  # 6
            ["P", "P", "P", "P", "P", "P", "P", "P"],  # 7
            ["R", "N", "B", "Q", "K", "B", "N", "R"],  # 8
        ]

    def __str__(self):
        boardStr = ""
        for row in self.board:
            for col in row:
                boardStr += col
            boardStr += "\n"
        return boardStr


if __name__ == '__main__':
    board = Board()
    print(board)
