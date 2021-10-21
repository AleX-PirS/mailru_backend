import tictactoe_class
import unittest


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = tictactoe_class.TicTacToe()

    def test_win_checker(self):
        board = ['x', '0', '0', 'x', 'x', 'x', '0', '0', ' ']
        self.assertEqual(tictactoe_class.TicTacToe().win_checker(board), 1)
        board = ['0', '0', 'x', 'x', 'x', '0', '0', 'x', '0']
        self.assertEqual(tictactoe_class.TicTacToe().win_checker(board), 1000)
        board = ['0', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ']
        self.assertEqual(tictactoe_class.TicTacToe().win_checker(board), None)

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
