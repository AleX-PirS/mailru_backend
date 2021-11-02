import tictactoe_class
import unittest


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = tictactoe_class.TicTacToe()

    def test_win_checker(self):

        board = ['x', '0', '0', 'x', 'x', 'x', '0', '0', ' ']
        self.assertEqual(tictactoe_class.TicTacToe().win_checker(board), 'WIN')

        board = ['x', '0', '0', '0', 'x', '0', 'x', 'x', 'x']
        self.assertEqual(tictactoe_class.TicTacToe().win_checker(board), 'WIN')

        board = ['x', ' ', '0', ' ', 'x', ' ', ' ', '0', 'x']
        self.assertEqual(tictactoe_class.TicTacToe().win_checker(board), 'WIN')

        board = ['x', 'x', '0', ' ', '0', ' ', '0', ' ', ' ']
        self.assertEqual(tictactoe_class.TicTacToe().win_checker(board), 'WIN')

        board = ['x', '0', '0', 'x', ' ', ' ', 'x', ' ', ' ']
        self.assertEqual(tictactoe_class.TicTacToe().win_checker(board), 'WIN')

        board = ['0', '0', 'x', ' ', ' ', 'x', ' ', ' ', 'x']
        self.assertEqual(tictactoe_class.TicTacToe().win_checker(board), 'WIN')

        board = ['0', '0', 'x', 'x', 'x', '0', '0', 'x', '0']
        self.assertEqual(tictactoe_class.TicTacToe().win_checker(board), 'TIE')

        board = ['0', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ']
        self.assertEqual(tictactoe_class.TicTacToe().win_checker(board), 'NO_WIN')

    def test_input_checker(self):

        board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        quad = '1'
        self.assertEqual(tictactoe_class.TicTacToe().input_checker(quad, board)[0], 'done')

        board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        quad = '9'
        self.assertEqual(tictactoe_class.TicTacToe().input_checker(quad, board)[0], 'done')

        board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        quad = '10'
        self.assertEqual(tictactoe_class.TicTacToe().input_checker(quad, board), 'Out of range!')

        board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        quad = '0'
        self.assertEqual(tictactoe_class.TicTacToe().input_checker(quad, board), 'Out of range!')

        board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        quad = '-10'
        self.assertEqual(tictactoe_class.TicTacToe().input_checker(quad, board), 'Only digit input!')

        board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        quad = '4а'
        self.assertEqual(tictactoe_class.TicTacToe().input_checker(quad, board), 'Only digit input!')

        board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        quad = 'zero'
        self.assertEqual(tictactoe_class.TicTacToe().input_checker(quad, board), 'Only digit input!')

        board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        quad = 'a'
        self.assertEqual(tictactoe_class.TicTacToe().input_checker(quad, board), 'Only digit input!')

        board = ['0', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        quad = '1'
        self.assertEqual(tictactoe_class.TicTacToe().input_checker(quad, board), 'This place is already pinned!')

        board = [' ', ' ', ' ', ' ', '0', ' ', ' ', ' ', ' ']
        quad = '5'
        self.assertEqual(tictactoe_class.TicTacToe().input_checker(quad, board), 'This place is already pinned!')

    def test_rename(self):

        player = tictactoe_class.Player(test=1)
        self.assertEqual(tictactoe_class.Player(test=1).name, 'test')

        player.rename('Alice')
        self.assertEqual(player.name, 'Alice')

    def test_set_score(self):

        player = tictactoe_class.Player(test=1)
        self.assertEqual(player.score, 0)

        player.set_score(50)
        self.assertEqual(player.score, 50)


if __name__ == "__main__":
    unittest.main()
