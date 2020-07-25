"""board.py -- implements methods and classes to represent a chessboard and
heuristic/entropy measurements
"""
import random

def board_str_to_matrix(string):
    """Returns a matrix representation of a string of n characters, each of
    which representing the position of the ith queen in the jth row"""
    n = len(string)
    matrix = [[0 for i in range(n)] for j in range(n)]

    for j, c in enumerate(string):
        i = int(c)
        matrix[i][j] = 1

    return matrix

def board_matrix_to_str(matrix):
    """Returns the string representation of an n x n board where each of the
    characters of the string represents the jth position of the ith queen by
    column"""
    string = ""
    n = len(matrix)

    for j in range(n):
        i = 0
        while i < n and matrix[i][j] != 1:
            i += 1

        string += str(i)

    return string

def random_board(n=8):
    """Returns a random n-queen chessboard.

    Args:
        n (int): The dimension of the n x n board.
    """
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    for j in range(n):
        i = random.randint(0, n - 1)
        matrix[i][j] = 1

    return Chessboard(board_matrix=matrix)

class Chessboard:
    """Represents a n x n board with n queens.

    Args:
        n (int): The dimension of the n x n board.
    """
    def __init__(self, n=8, board_matrix=None):

        if board_matrix:
            self.board = board_matrix

        # Defines an empty board.
        else:
            # The matrix representation of the board.
            self.board = [[0 for i in range(n)] for j in range(n)]

            # Places queens in the first row of the board.
            for i in range(n):
                self.board[0][i] = 1

        self.__update_state()

    def __update_state(self):
        """Updates the internal variables of this board."""

    def __repr__(self):
        return str(self.board)

    def __str__(self):
        """Returns the representation of this board."""
        rows = []
        for r in self.board:
            s = " ".join(str(s) for s in r)
            rows.append(s)
        return "\n".join(rows)
