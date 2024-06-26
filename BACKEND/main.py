from move_module import move_class
from move_val_module import move_val_class
from capture_module import capture_class
from display_module import display_class
from is_win_module import is_win_class
class Anti_Chess_by_PICE(move_val_class,display_class,capture_class,move_class,is_win_class):
    def __init__(self):
        self.board = self.board_creation()
        self.player_1 = "White"
        self.player_2 = "Black"
        self.move_counter = 0

    def play(self):
        while True:
            self.display_board()
            print(f"{self.player_1}'s turn")

            captures = self.all_captures()
            if captures:
                print("You must capture a piece.")
                for i, ((start_row, start_col), (end_row, end_col)) in enumerate(captures):
                    print(f"{i + 1}. {chr(start_col + ord('a'))}{8 - start_row} to {chr(end_col + ord('a'))}{8 - end_row}")

            move = input("Please Enter Your Choice : (to display the board in CLI press 'display') (to quit press 'quit') (or enter your move): ").strip()
            if move.lower() == "display":
                self.display_board()
                continue
            elif move.lower() == "quit":
                print(f"{self.player_2} wins!")
                break

            parsed_move = self.parse_move(move)
            if parsed_move:
                start, end = parsed_move
                if captures:
                    if (start, end) not in captures:
                        print("You must make a capture. Try again.")
                        continue
                is_valid, message = self.move_validation(start, end)
                if is_valid:
                    self.make_move(start, end)
                    winner = self.win_check()
                    if winner:
                        self.display_board()
                        print(f"{winner} wins!")
                        break
                    self.switch_players()
                else:
                    print(f"Invalid move: {message}")
            else:
                print("Invalid input. Try again.")

if __name__ == "__main__":
    object = Anti_Chess_by_PICE()
    object.play()