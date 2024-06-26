class is_win_class:  
    def win_check(self):
        player1_pieces = any(piece.isupper() for row in self.board for piece in row)
        player2_pieces = any(piece.islower() for row in self.board for piece in row)
        if not player1_pieces:
            return "Black"
        if not player2_pieces:
            return "White"
        return None