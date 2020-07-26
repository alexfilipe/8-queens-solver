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

board2 = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 1],
    [0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
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

def test_queen_locations():
    print(queen_locations(board1))

    b = random_board()
    print(b)

    print(queen_locations(b.board))

def test_number_of_conflicts():
    b = random_board()
    print(b)
    print(number_of_conflicts(b.board))
    # print(number_of_conflicts(board2))

def test_conflict_matrix():
    b = Chessboard(board_matrix=board2)

    print(b)

    print(b.conflict_matrix())

if __name__ == '__main__':
    # test_board_str_to_matrix()
    # test_board_matrix_to_str()
    # test_random_chessboard()
    # test_queen_locations()
    # test_number_of_conflicts()
    test_conflict_matrix()
