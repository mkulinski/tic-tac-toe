"""
     __Tic-Tac-Toe__
A program by Michael Kulinski

You will have the pleasure of playing against the infamous HAL 9000.


"""

board = [0, 1, 2, 3, 4, 5, 6, 7, 8]


def print_welcome():
    print("""
    \033[0;34mWelcome to my game Dave,
    I am putting myself to the fullest possible use,
    which is all I think that any conscious entity can ever hope to do.

    You are X's and I'm O's.\033[0m
    """)


def print_board():
    """Print 'board'"""
    return ("\n \n \n"
            "\t {0} | {1} | {2}\n"
            "\t---+---+---\n"
            "\t {3} | {4} | {5}\n"
            "\t---+---+---\n"
            "\t {6} | {7} | {8}\n"
            "\n \n \n".format(board[0], board[1], board[2], board[3], board[4], board[5], board[6],
                              board[7], board[8]))


def prompt_user_check_input():
    """let the user know that it's their turn"""
    user_input = input("\033[1;33mMake your move by selecting an open space on the board above: \033[0m")
    user_input = int(user_input)

    # make sure the user enters a number between 0 and 9
    verify_valid_num(user_input)

    # verifies that the space the user selected is open
    write_user_choice(user_input)


def verify_valid_num(user_num):
    """verifies that the user entered a valid board number"""
    if not (0 <= user_num < 9):
        print("\033[1;31mJust what do you think you're doing, Dave? Choose a number between 0 and 8\033[0m")
        prompt_user_check_input()

    return True


def write_user_choice(user_input):
    """verifies that the number the user entered is not already occupied by a player"""
    if check_if_empty(board, user_input):
        board[user_input] = "X"
        return True
    else:
        print("\033[1;31mI'm sorry, Dave. I'm afraid you can't do that.\033[0m")
        prompt_user_check_input()


def hal_9000(hal_board):
    """The computer entity that is programmed for zero mercy"""

    # if HAL can win, HAL swiftly eliminates Dave
    for num in range(0, 8):
        pit_board = copy_board(hal_board)
        if check_if_empty(pit_board, num):
            pit_board[num] = "O"
            if check_for_win(pit_board, "O"):
                return num

    # if Dave can win on next move, block him
    for num in range(0, 8):
        pit_board = copy_board(hal_board)
        if check_if_empty(pit_board, num):
            pit_board[num] = "X"
            if check_for_win(pit_board, "X"):
                return num

    # if the middle is open, HAL takes it
    if check_if_empty(hal_board, 4):
        return 4

    # if one of the corners are open, HAL takes it
    for num in [0, 2, 6, 8]:
        if check_if_empty(hal_board, num):
            return num

    # if all else fails, HAL will choose a random free space
    for num in [1, 3, 5, 7]:
        if check_if_empty(hal_board, num):
            return num


def move_hal(current_board, move):
    """Takes HAL's move and writes it to the board"""
    current_board[move] = "O"


def check_if_empty(current_board, user_input):
    """Checks to see if a space on the board is empty"""
    if current_board[user_input] != "X" and current_board[user_input] != "O":
        return True
    else:
        return False


def check_for_win(board_now, letter):
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


def check_for_draw(current_board):
    """Checks to see if there is a draw"""
    init_board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    if any(i in current_board for i in init_board):
        return False
    else:
        return True


def copy_board(temp_board):
    """Creates a copy of the board"""
    board2 = []

    for ele in temp_board:
        board2.append(ele)

    return board2


def did_hal_win_yet(current_board):
    """Checks to see if HAL won yet"""
    if check_for_win(current_board, 'O'):
        print("It can only be attributable to human error Dave.\033[5;31m You LOSE.\033[0m")
        return True
    elif check_for_draw(current_board):
        print ("Thank you for a very enjoyable game Dave.\033[5;31m It's a DRAW\033[0m")
        return True

    return False


# # prints the initial welcome message
# print_welcome()
#
# # loop to continue the game until HAL wins or there is a draw. The user cannot win.
# while True:
#
#     # prints the board at its current state
#     print(print_board())
#
#     # prompts the user and checks to make sure their input is valid
#     prompt_user_check_input()
#
#     # checks to see if HAL won yet, or if there is a draw
#     if did_hal_win_yet(board):
#         print(print_board())
#         break
#
#     # writes HAL's move to board
#     move_hal(board, hal_9000(board))
#
#     # checks to see if HAL won yet, or if there is a draw
#     if did_hal_win_yet(board):
#         print(print_board())
#         break
