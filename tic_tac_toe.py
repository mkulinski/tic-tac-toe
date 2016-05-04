"""
    __Tic-Tac-Toe__
A program by Michael Kulinski
You will have the pleasure of playing against the infamous HAL 9000.
"""


class PlayTicTacToe:
    def __init__(self):
        # the board that both players are manipulating
        self.board = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    def print_welcome(self):
        """Prints out a welcome message for the player"""
        print("""
        \033[0;34mWelcome to my game Dave,
        I am putting myself to the fullest possible use,
        which is all I think that any conscious entity can ever hope to do.
        You are X's and I am O's.\033[0m
        """)

    def print_board(self):
        """Print 'board'"""
        return ("\n \n \n"
                "\t {0} | {1} | {2}\n"
                "\t---+---+---\n"
                "\t {3} | {4} | {5}\n"
                "\t---+---+---\n"
                "\t {6} | {7} | {8}\n"
                "\n \n \n".format(self.board[0], self.board[1], self.board[2], self.board[3], self.board[4],
                                  self.board[5], self.board[6],
                                  self.board[7], self.board[8]))

    def prompt_user_check_input(self):
        """let the user know that it's their turn"""
        user_input = 0
        # grabs user input and changes it to an int
        while True:
            try:
                user_input = int(
                    input("\033[1;33mMake your move by entering the number of an open space on the board: \033[0m"))
            except ValueError:
                print("Why do you refuse to enter a number, Dave?")
                continue
            else:
                break

        # makes sure the user enters a number 0-8 and verifies that the space the user selected is open
        if self.verify_valid_num(user_input) and self.write_user_choice(user_input):
            return True
        else:
            self.prompt_user_check_input()

    def verify_valid_num(self, user_num):
        """verifies that the user entered a valid board number"""
        if not self.range_between_0_and_9(user_num):
            print("\033[1;31mJust what do you think you're doing, Dave? Choose a number between 0 and 8\033[0m")
            return False

        return True

    def range_between_0_and_9(self, user_num):
        """Verifies a given number is between 0 and 9"""
        if 0 <= user_num < 9:
            return True
        else:
            return False

    def write_user_choice(self, user_input):
        """Writes the user's input to the board as long as it's an open space"""
        if self.check_if_empty(self.board, user_input):
            self.board[user_input] = "X"
            return True
        else:
            print("\033[1;31mI'm sorry, Dave. I'm afraid you can't do that.\033[0m")
            return False

    def hal_9000(self, hal_board):
        """The computer entity that is programmed for zero mercy"""

        # if HAL can win, HAL swiftly eliminates Dave
        for num in range(0, 8):
            pit_board = self.copy_board(hal_board)
            if self.check_if_empty(pit_board, num):
                pit_board[num] = "O"
                if self.check_for_win(pit_board, "O"):
                    return num

        # if Dave can win on next move, block him
        for num in range(0, 8):
            pit_board = self.copy_board(hal_board)
            if self.check_if_empty(pit_board, num):
                pit_board[num] = "X"
                if self.check_for_win(pit_board, "X"):
                    return num

        # if the middle is open, HAL takes it
        if self.check_if_empty(hal_board, 4):
            return 4

        # if one of the corners are open, HAL takes it
        for num in [0, 2, 6, 8]:
            if self.check_if_empty(hal_board, num):
                return num

        # if all else fails, HAL will choose a random free space
        for num in [1, 3, 5, 7]:
            if self.check_if_empty(hal_board, num):
                return num

    def move_hal(self, current_board, move):
        """Takes HAL's move and writes it to the board if there is an open space"""
        # checks for an open space on the board
        if self.check_for_draw(current_board):
            return False
        # if there is an open space, hal writes his move there
        else:
            current_board[move] = "O"
            return True

    def check_if_empty(self, current_board, user_input):
        """Checks to see if a space on the board is empty"""
        if current_board[user_input] != "X" and current_board[user_input] != "O":
            return True
        else:
            return False

    def check_for_win(self, board_now, letter):
        """Checks to see if there is a winner"""
        if ((board_now[6] == letter and board_now[7] == letter and board_now[8] == letter) or
                (board_now[3] == letter and board_now[4] == letter and board_now[5] == letter) or
                (board_now[0] == letter and board_now[1] == letter and board_now[2] == letter) or
                (board_now[6] == letter and board_now[3] == letter and board_now[0] == letter) or
                (board_now[7] == letter and board_now[4] == letter and board_now[1] == letter) or
                (board_now[8] == letter and board_now[5] == letter and board_now[2] == letter) or
                (board_now[6] == letter and board_now[4] == letter and board_now[2] == letter) or
                (board_now[8] == letter and board_now[4] == letter and board_now[0] == letter)):
            return True
        return False

    def check_for_draw(self, current_board):
        """Checks to see if there is a draw"""
        init_board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        if any(i in current_board for i in init_board):
            return False
        else:
            return True

    def copy_board(self, temp_board):
        """Creates a copy of the board"""
        board2 = []

        for ele in temp_board:
            board2.append(ele)

        return board2

    def did_hal_win_yet(self, current_board):
        """Checks to see if HAL won yet or if there is a draw"""
        if self.check_for_win(current_board, 'O'):
            print("It can only be attributable to human error, Dave.\033[5;31m You LOSE.\033[0m")
            return True
        elif self.check_for_draw(current_board):
            print("Thank you for a very enjoyable game, Dave.\033[5;31m It's a DRAW\033[0m")
            return True

        return False

    def run_program(self):
        """Loop to continue the game until HAL wins or there is a draw. The user cannot win."""

        # prints the initial welcome message
        self.print_welcome()

        while True:

            # prints the board at its current state
            print(self.print_board())

            # prompts the user and checks to make sure their input is valid
            self.prompt_user_check_input()

            # writes HAL's move to board
            self.move_hal(self.board, self.hal_9000(self.board))

            # checks to see if HAL won yet, or if there is a draw
            if self.did_hal_win_yet(self.board):
                print(self.print_board())
                break


# runs the game
if __name__ == "__main__":
    new_game = PlayTicTacToe()
    new_game.run_program()
