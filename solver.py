from board import *
import random
from copy import deepcopy

class Solver:
    """A solver for the n-queens problem."""
    def __init__(self, board=None, n=8):
        if board is None:
            board = random_board(n)

        self.n = n
        self.board = board

    def solve(self):
        raise NotImplementedError

class HillClimbingSolver(Solver):
    def solve(self):
        """Returns the solved hill climbing matrix or failure."""
        return self.hill_climbing()

    def hill_climbing(self):
        """Returns the local minimum of the queen state."""
        current_board = deepcopy(self.board)
        next_board = self.board

        while True:
            self.board.random_minimal_successor()

            # Local minimum reached
            if self.board.conflicts() >= current_board.conflicts():
                return current_board

            current_board = deepcopy(self.board)


def temperature(time):
    """Temperature function for the simulated annealing algorithm."""

class SimulatedAnnealingSolver(Solver):

    def simulated_annealing(self):
        pass
