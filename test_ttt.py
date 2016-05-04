"""
This is the test file for tic_tac_toe.py.
"""

import unittest
import tic_tac_toe


class TestBoard(unittest.TestCase):
    def test_if_board_displays(self):
        test_value = tic_tac_toe.PlayTicTacToe()
        self.assertEqual(test_value.print_board(), "\n \n \n"
                                                   "\t 0 | 1 | 2\n"
                                                   "\t---+---+---\n"
                                                   "\t 3 | 4 | 5\n"
                                                   "\t---+---+---\n"
                                                   "\t 6 | 7 | 8\n"
                                                   "\n \n \n")


class TestVerifyValidNum(unittest.TestCase):
    def test_if_only_numbers_0_to_8_are_accepted(self):
        test_value = tic_tac_toe.PlayTicTacToe()
        self.assertTrue(test_value.verify_valid_num(4))

    def test_if_num_outside_of_0_8_returns_false(self):
        test_value = tic_tac_toe.PlayTicTacToe()
        self.assertFalse(test_value.verify_valid_num(10))


class TestWriteUserChoice(unittest.TestCase):
    def test_if_writes_to_space(self):
        test_value = tic_tac_toe.PlayTicTacToe()
        self.assertTrue(test_value.write_user_choice(1))


class TestCheckForWin(unittest.TestCase):
    def test_if_it_can_find_a_middle_winner(self):
        test_board = [0, 1, 2, "O", "O", "O", 6, 7, 8]
        test_value = tic_tac_toe.PlayTicTacToe().check_for_win(test_board, "O")
        self.assertTrue(test_value)

    def test_if_it_can_find_top_winner(self):
        test_board = ["O", "O", "O", 3, 4, 5, 6, 7, 8]
        test_value = tic_tac_toe.PlayTicTacToe().check_for_win(test_board, "O")
        self.assertTrue(test_value)

    def test_if_it_can_find_bottom_winner(self):
        test_board = [0, 1, 2, 3, 4, 5, "O", "O", "O"]
        test_value = tic_tac_toe.PlayTicTacToe().check_for_win(test_board, "O")
        self.assertTrue(test_value)

    def test_if_it_can_find_diag_up_winner(self):
        test_board = [0, 1, "O", 3, "O", 5, "O", 7, 8]
        test_value = tic_tac_toe.PlayTicTacToe().check_for_win(test_board, "O")
        self.assertTrue(test_value)

    def test_if_it_can_find_diag_down_winner(self):
        test_board = ["O", 1, 2, 3, "O", 5, 6, 7, "O"]
        test_value = tic_tac_toe.PlayTicTacToe().check_for_win(test_board, "O")
        self.assertTrue(test_value)

    def test_if_returns_false_for_no_winner_HAL(self):
        test_board = ["O", "O", "X", 3, 4, 5, 6, 7, 8]
        test_value = tic_tac_toe.PlayTicTacToe().check_for_win(test_board, "O")
        self.assertFalse(test_value)

    def test_if_returns_false_for_no_winner_user(self):
        test_board = ["X", "X", "O", 3, 4, 5, 6, 7, 8]
        test_value = tic_tac_toe.PlayTicTacToe().check_for_win(test_board, "X")
        self.assertFalse(test_value)

    def test_if_returns_true_for_winner_user(self):
        test_board = ["X", "X", "X", 3, 4, 5, 6, 7, 8]
        test_value = tic_tac_toe.PlayTicTacToe().check_for_win(test_board, "X")
        self.assertTrue(test_value)


class TestCheckForDraw(unittest.TestCase):
    def test_if_it_can_find_a_draw(self):
        test_board = ["X", "O", "X", "O", "X", "O", "O", "X", "X"]
        test_value = tic_tac_toe.PlayTicTacToe().check_for_draw(test_board)
        self.assertTrue(test_value)

    def test_if_it_can_return_false_when_not_a_draw(self):
        test_board = ["X", "O", "X", "O", "X", "O", "O", "X", 8]
        test_value = tic_tac_toe.PlayTicTacToe().check_for_draw(test_board)
        self.assertFalse(test_value)

    def test_if_return_false_when_win_on_board(self):
        test_board = ["O", "O", "O", "O", "X", "O", "O", "O", 8]
        test_value = tic_tac_toe.PlayTicTacToe().check_for_draw(test_board)
        self.assertFalse(test_value)


class TestCopyBoard(unittest.TestCase):
    def test_if_board_is_copied_correctly(self):
        test_board = [0, "X", 2, 3, "O", 5, 6, 7, 8]
        test_value = tic_tac_toe.PlayTicTacToe().copy_board(test_board)
        self.assertEqual(test_board, test_value)


class TestDidHALWinYet(unittest.TestCase):
    def test_if_it_can_find_a_middle_winner(self):
        test_board = [0, 1, 2, "O", "O", "O", 6, 7, 8]
        test_value = tic_tac_toe.PlayTicTacToe().check_for_win(test_board, "O")
        self.assertTrue(test_value)

    def test_if_it_can_find_top_winner(self):
        test_board = ["O", "O", "O", 3, 4, 5, 6, 7, 8]
        test_value = tic_tac_toe.PlayTicTacToe().check_for_win(test_board, "O")
        self.assertTrue(test_value)

    def test_if_it_can_find_bottom_winner(self):
        test_board = [0, 1, 2, 3, 4, 5, "O", "O", "O"]
        test_value = tic_tac_toe.PlayTicTacToe().check_for_win(test_board, "O")
        self.assertTrue(test_value)

    def test_if_it_can_find_diag_up_winner(self):
        test_board = [0, 1, "O", 3, "O", 5, "O", 7, 8]
        test_value = tic_tac_toe.PlayTicTacToe().check_for_win(test_board, "O")
        self.assertTrue(test_value)

    def test_if_it_can_find_diag_down_winner(self):
        test_board = ["O", 1, 2, 3, "O", 5, 6, 7, "O"]
        test_value = tic_tac_toe.PlayTicTacToe().check_for_win(test_board, "O")
        self.assertTrue(test_value)

    def test_if_returns_false_for_no_winner_HAL(self):
        test_board = ["O", "O", "X", 3, 4, 5, 6, 7, 8]
        test_value = tic_tac_toe.PlayTicTacToe().check_for_win(test_board, "O")
        self.assertFalse(test_value)

    def test_if_returns_false_for_no_winner_user(self):
        test_board = ["X", "X", "O", 3, 4, 5, 6, 7, 8]
        test_value = tic_tac_toe.PlayTicTacToe().check_for_win(test_board, "X")
        self.assertFalse(test_value)


class TestCheckIfEmpty(unittest.TestCase):
    def test_if_it_can_find_an_empty_space(self):
        test_board = [0, "X", "O", "O", 4, 5, 6, 7, 8]
        test_value = tic_tac_toe.PlayTicTacToe().check_if_empty(test_board, 4)
        self.assertTrue(test_value)


class TestMoveHAL(unittest.TestCase):
    def test_if_hal_can_move(self):
        test_board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        tic_tac_toe.PlayTicTacToe().move_hal(test_board, 1)
        self.assertEqual(test_board, [0, "O", 2, 3, 4, 5, 6, 7, 8])


class TestRangeBetween0and9(unittest.TestCase):
    def test_if_range_between_0_and_9_returns_true(self):
        test_num = 8
        test_value = tic_tac_toe.PlayTicTacToe().range_between_0_and_9(test_num)
        self.assertTrue(test_value)

    def test_if_range_between_0_and_9_returns_false(self):
        test_num = 9
        test_value = tic_tac_toe.PlayTicTacToe().range_between_0_and_9(test_num)
        self.assertFalse(test_value)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
