class capture_class:
    def is_capture(self, start, end):
        start_row, start_col = start
        end_row, end_col = end
        start_piece = self.board[start_row][start_col]
        end_piece = self.board[end_row][end_col]
        if start_piece.isupper() and end_piece.islower():
            return True
        if start_piece.islower() and end_piece.isupper():
            return True
        return False

    def all_captures(self):
        captures = []
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece != ".":
                    if (self.player_1 == "White" and piece.isupper()) or (self.player_1 == "Black" and piece.islower()):
                        moves = self.all_possible_captures(row, col)
                        for move in moves:
                            if self.is_capture((row, col), move):
                                captures.append(((row, col), move))
        return captures

    def all_possible_captures(self, row, col):
        piece = self.board[row][col].lower()
        moves = []

        if piece == 'p':
            direction = -1 if self.board[row][col].isupper() else 1
            capture_moves = [(direction, -1), (direction, 1)]
            for dr, dc in capture_moves:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    if self.is_capture((row, col), (new_row, new_col)):
                        moves.append((new_row, new_col))
        else:
            directions = []
            if piece == 'r':
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            elif piece == 'n':
                directions = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
            elif piece == 'b':
                directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
            elif piece == 'q':
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
            elif piece == 'k':
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                while 0 <= new_row < 8 and 0 <= new_col < 8:
                    if self.board[new_row][new_col] == ".":
                        break
                    if self.is_capture((row, col), (new_row, new_col)):
                        moves.append((new_row, new_col))
                        break
                    new_row += dr
                    new_col += dc

        return moves