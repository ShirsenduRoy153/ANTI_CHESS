class move_class:
    def parse_move(self, move):
        # Convert move like "A2 B3" to board indices
        try:
            start, end = move.split()
            start_col = ord(start[0].lower()) - ord('a')
            start_row = 8 - int(start[1])
            end_col = ord(end[0].lower()) - ord('a')
            end_row = 8 - int(end[1])
            return (start_row, start_col), (end_row, end_col)
        except Exception as e:
            print("Error parsing move. Please use the format 'A2 B3'.")
            return None

    def make_move(self, start, end):
        start_row, start_col = start
        end_row, end_col = end
        self.board[end_row][end_col] = self.board[start_row][start_col]
        self.board[start_row][start_col] = "."
        if self.board[end_row][end_col].lower() == 'p' and (end_row == 0 or end_row == 7):
            self.pawn_promotion(end_row, end_col)
    
    def pawn_promotion(self, row, col):
        while True:
            promotion = input("Promote pawn to (q, r, b, n, k): ").lower()
            if promotion in ['q', 'r', 'b', 'n', 'k']:
                self.board[row][col] = promotion.upper() if self.player_1 == "White" else promotion.lower()
                break
            else:
                print("Invalid choice. Choose again.")

    def switch_players(self):
        self.player_1, self.player_2 = self.player_2, self.player_1