class display_class:
    def board_creation(self):
        return [
            ["r", "n", "b", "q", "k", "b", "n", "r"],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["R", "N", "B", "Q", "K", "B", "N", "R"]
        ]

    def display_board(self):
        print()
        print("  --------------------------------")
        for row in range(8):
            print(f"{8-row}", end="")
            for col in range(8):
                piece = self.board[row][col]
                display_piece = self.map_display(piece)
                if (row + col) % 2 == 0:
                    print(f" \033[47m{display_piece}  \033[0m", end="")
                else:
                    print(f" \033[40m{display_piece}  \033[0m", end="")
            print()
        print("   a   b   c   d   e   f   g   h")
        print("  -------------------------------")

    def map_display(self, piece):
        if piece == "r":
            return "♜"
        elif piece == "n":
            return "♞"
        elif piece == "b":
            return "♝"
        elif piece == "q":
            return "♛"
        elif piece == "k":
            return "♚"
        elif piece == "p":
            return "♟" 
        elif piece == "R":
            return "♖"
        elif piece == "N":
            return "♘"
        elif piece == "B":
            return "♗"
        elif piece == "Q":
            return "♕"
        elif piece == "K":
            return "♔"
        elif piece == "P":
            return "♙" 
        else:
            return piece