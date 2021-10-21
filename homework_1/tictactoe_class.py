"""
tic-tac-toe terminal game, default 3x3

# Example of game:
game = TicTacToe() # To change dimensional use "dim= " parameter
player1 = Player()
player2 = Player()

while True:
    if game.win:
        clear()
        print(f"***FINAL SCORE***\n\n{player1.name}'s score: {player1.score}\n"
              f"{player2.name}'s score: {player2.score}")
        sys.exit()
    clear()
    game.info(player1, player2)
    game.draw_board(game.board)
    game.board_updater(game.board)
    if game.win_checker(game.board):
        game.stopper(player1, player2)
"""
from os import system, name
import sys


def clear():
    """Function for cleaning window"""
    if name == 'nt':
        _ = system('cls')


class Player:
    """Special class for player"""
    def __init__(self, test=0):
        self.score = 0
        if test == 0:
            while True:
                self.name = input('First player, write '
                                  'your name (max 20 symbols): ').strip().capitalize()
                if len(self.name) > 20:
                    print('Oversize name, try again!')
                elif len(self.name) < 1:
                    print('Blank name!')
                else:
                    break
        elif test == 1:
            self.name = 'test'

    def rename(self, new_name):
        """Special method to rename players, new name can be similar"""
        self.name = new_name

    def set_score(self, new_score):
        """Method to change player score value"""
        try:
            self.score = int(new_score)
        except ValueError:
            print("Digits only!")


class TicTacToe:
    """tic-tac-toe terminal game"""
    def __init__(self, dim=3):
        self.sign = ('x', '0')
        self.win = 0
        self.step_round = 0  # every round we change our players
        self.actual_turn = 0  # if %2 == 0: first player else second player
        self.dim = dim  # dimension of game default 3
        self.board = [' ' for _ in range(self.dim ** 2)]
        self.info_board = list(range(1, self.dim**2 + 1))

    def draw_board(self, board):
        """Method to board printing"""
        pillar_counter = 0
        row_counter = 0
        for i in range(self.dim):
            print('*---', end='')
        print('*')
        for i in board:
            if pillar_counter == 0:
                print('|', end='')
            pillar_counter += 1
            row_counter += 1
            if row_counter % self.dim != 0:
                print(' ' + str(i) + ' |', end='')
            else:
                print(' ' + str(i) + ' |', end='')
                pillar_counter = 0
                print()
        for i in range(self.dim):
            print('*---', end='')
        print('*')

    def info(self, player1, player2):
        """Method for printing info about players"""
        if not (isinstance(player1, Player) and isinstance(player2, Player)):
            print("Wrong data in player!")
            sys.exit()
        print('Board indexing')
        self.draw_board(self.info_board)
        print('-----------------------------------------')
        print(f'Score of {player1.name} is {player1.score}')
        print(f'Score of {player2.name} is {player2.score}')
        print('-----------------------------------------')
        if (self.actual_turn + self.step_round) % 2 == self.step_round % 2:
            print(f'Player {player1.name} '
                  f'({self.sign[(self.actual_turn + self.step_round) % 2]})'
                  f', enter the quadrant number')
        else:
            print(f'Player {player2.name} '
                  f'({self.sign[(self.actual_turn + self.step_round) % 2]})'
                  f', enter the quadrant number')

    def stopper(self, player1, player2):
        """Method for stopping game, when win_checker() detect winning combination"""
        tie = 0
        if not (isinstance(player1, Player) and isinstance(player2, Player)):
            print("Wrong data in player!")
            sys.exit()
        if self.win < 0:
            tie = -1
        self.win = 1
        self.board = [' ' for _ in range(self.dim ** 2)]
        if tie == 0:
            if (self.actual_turn + self.step_round) % 2 == self.step_round % 2:
                print(f'Congratulations, player {player2.name}')    # Changed
                player2.score += 1
            else:
                print(f'Congratulations, player {player1.name}')
                player1.score += 1
        else:
            print('***TIE***')
        while True:
            ans = input('Do you want to continue (yes or y)?: ').lower()
            if ans in ('y', 'yes'):
                self.step_round += 1
                self.win = 0
            return self.win

    def win_checker(self, board):
        """Method, that check winning combinations"""
        for i in range(self.dim):
            if (board[i * self.dim:self.dim * (i + 1)].count('x') == self.dim
                    or board[i * self.dim:self.dim * (i + 1)].count('0') == self.dim):
                return 1
        # Check columns
        for j in range(self.dim):
            buff = []
            for i in range(self.dim):
                buff.append(board[self.dim * i + j])
                if (buff.count('x') == self.dim
                        or buff.count('0') == self.dim):
                    return 1
        # Check diagonals
        buff_poz = []
        buff_neg = []
        for i in range(self.dim):
            buff_poz.append(board[(i + 1) * (self.dim - 1)])
            buff_neg.append(board[i * (self.dim + 1)])
            if (buff_poz.count('x') == self.dim
                    or buff_poz.count('0') == self.dim
                    or buff_neg.count('x') == self.dim
                    or buff_neg.count('0') == self.dim):
                return 1
        # Check tie situation
        if ' ' not in board:
            self.win = -1
            return 1000

    def board_updater(self, board):
        """Method to update board after choosing quadrant"""
        while True:
            quad = input('> ').strip()
            if quad.isdigit():
                if int(quad) in range(1, self.dim ** 2 + 1):
                    if self.board[int(quad) - 1] != ' ':
                        print('This place is already pinned!')
                    else:
                        self.board[int(quad) - 1] = \
                            self.sign[(self.actual_turn + self.step_round) % 2]
                        self.win_checker(board)
                        self.actual_turn += 1
                        return board
                else:
                    print('Out of range!')
            else:
                print('Only digit input!')
