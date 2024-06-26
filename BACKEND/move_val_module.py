class move_val_class:
    def move_validation(self, start, end):
        start_row, start_col = start
        end_row, end_col = end
        piece = self.board[start_row][start_col]
        
        if piece == '.':
            return False, "No piece at the starting square."
        if not (0 <= start_row < 8 and 0 <= start_col < 8 and 0 <= end_row < 8 and 0 <= end_col < 8):
            return False, "Move out of board bounds."
        if piece.isupper() and self.player_1 != "White":
            return False, "It's not your turn."
        if piece.islower() and self.player_1 != "Black":
            return False, "It's not your turn."
        if self.board[end_row][end_col] != '.' and self.board[end_row][end_col].isupper() == piece.isupper():
            return False, "Cannot capture your own piece."
        
        valid = False
        piece_type = piece.lower()

        if piece_type == 'p':
            direction = -1 if piece.isupper() else 1
            if start_col == end_col:
                if start_row + direction == end_row and self.board[end_row][end_col] == '.':
                    valid = True
                elif start_row == (1 if direction == 1 else 6) and start_row + 2 * direction == end_row and self.board[end_row][end_col] == '.' and self.board[start_row + direction][start_col] == '.':
                    valid = True
            elif abs(start_col - end_col) == 1 and start_row + direction == end_row and self.can_capture(start, end):
                valid = True
        elif piece_type == 'r':
            if start_row == end_row or start_col == end_col:
                if start_row == end_row:
                    step = 1 if end_col > start_col else -1
                    for col in range(start_col + step, end_col, step):
                        if self.board[start_row][col] != '.':
                            return False, "Rook cannot jump over pieces."
                    valid = True
                if start_col == end_col:
                    step = 1 if end_row > start_row else -1
                    for row in range(start_row + step, end_row, step):
                        if self.board[row][start_col] != '.':
                            return False, "Rook cannot jump over pieces."
                    valid = True
        elif piece_type == 'n':
            if (abs(start_row - end_row), abs(start_col - end_col)) in [(2, 1), (1, 2)]:
                valid = True
        elif piece_type == 'b':
            if abs(start_row - end_row) == abs(start_col - end_col):
                row_step = 1 if end_row > start_row else -1
                col_step = 1 if end_col > start_col else -1
                for i in range(1, abs(start_row - end_row)):
                    if self.board[start_row + i * row_step][start_col + i * col_step] != '.':
                        return False, "Bishop cannot jump over pieces."
                valid = True
        elif piece_type == 'q':
            if start_row == end_row or start_col == end_col:
                return self.move_validation(start, end, 'r')
            elif abs(start_row - end_row) == abs(start_col - end_col):
                return self.move_validation(start, end, 'b')
        elif piece_type == 'k':
            if abs(start_row - end_row) <= 1 and abs(start_col - end_col) <= 1:
                valid = True

        if not valid:
            return False, "Illegal move for the piece."
        return True, None