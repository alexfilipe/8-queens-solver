from board import *

board1 = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1]
]

def test_board_str_to_matrix():
    string = "12356347"
    matrix = board_str_to_matrix(string)

    print(matrix)

def test_board_matrix_to_str():
    print(board_matrix_to_str(board1))

def test_random_chessboard():
    b = random_board()
    print(b)


if __name__ == '__main__':
    # test_board_str_to_matrix()
    test_random_chessboard()
