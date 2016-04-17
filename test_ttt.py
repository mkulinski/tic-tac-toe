import unittest
import tic_tac_toe


class TestBoard(unittest.TestCase):
    def test_if_board_displays(self):
        self.assertEqual(tic_tac_toe.print_board(), "\n \n \n"
                                                    "\t 0 | 1 | 2\n"
                                                    "\t---+---+---\n"
                                                    "\t 3 | 4 | 5\n"
                                                    "\t---+---+---\n"
                                                    "\t 6 | 7 | 8\n"
                                                    "\n \n \n")


class TestVerifyValidNum(unittest.TestCase):
    def test_if_only_numbers_0_to_8_are_accepted(self):
        test_value = tic_tac_toe.verify_valid_num(4)
        self.assertTrue(test_value)


class TestWriteUserChoice(unittest.TestCase):
    def test_if_writes_to_space(self):
        test_input = tic_tac_toe.write_user_choice(1)
        self.assertTrue(test_input)


class TestCheckForWin(unittest.TestCase):
    def test_if_it_can_find_a_winner(self):
        test_board = [0, 1, 2, 3, 4, 5, "X", "X", "X"]
        test_value = tic_tac_toe.check_for_win(test_board, "X")
        self.assertTrue(test_value)


class TestCheckForDraw(unittest.TestCase):
    def test_if_it_can_find_a_draw(self):
        test_board = ["X", "O", "X", "O", "X", "O", "O", "X", "X"]
        test_value = tic_tac_toe.check_for_draw(test_board)
        self.assertTrue(test_value)


class TestCopyBoard(unittest.TestCase):
    def test_if_board_is_copied_correctly(self):
        test_board = [0, "X", 2, 3, "O", 5, 6, 7, 8]
        test_value = tic_tac_toe.copy_board(test_board)
        self.assertEqual(test_board, test_value)


class TestDidHALWinYet(unittest.TestCase):
    def test_if_hal_knows_he_won(self):
        test_board = [0, 1, 2, 3, 4, 5, "O", "O", "O"]
        test_value = tic_tac_toe.did_hal_win_yet(test_board)
        self.assertTrue(test_value)


class TestCheckIfEmpty(unittest.TestCase):
    def test_if_it_can_find_an_empty_space(self):
        test_board = [0, "X", "O", "O", 4, 5, 6, 7, 8]
        test_value = tic_tac_toe.check_if_empty(test_board, 4)
        self.assertTrue(test_value)


class TestMoveHAL(unittest.TestCase):
    def test_if_hal_can_move(self):
        test_board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        tic_tac_toe.move_hal(test_board, 1)
        self.assertEqual(test_board, [0, "O", 2, 3, 4, 5, 6, 7, 8])


def main():
    unittest.main()


if __name__ == "__main__":
    main()
