"""Main."""

from bitboard import Board

if __name__ == "__main__":
    board = Board()
    print("new board")
    board.print_board()
    board._solution.solve_board_with_hints()

    board = Board()
    print("new board")
    board.print_board()
    board._solution.solve_blank_board()

    board = Board()
    board.fill_cell(0, 5)
    print("new board")
    board.print_board()
    board._solution.solve_board_with_hints()

    board = Board()
    board.fill_cell(0, 1)
    board.fill_cell(5, 2)
    board.fill_cell(67, 3)
    board.fill_cell(34, 4)
    board.fill_cell(2, 5)
    print("new board")
    board.print_board()
    board._solution.solve_board_with_hints()

    board = Board()
    board.fill_cell(10, 1)
    board.fill_cell(53, 2)
    board.fill_cell(63, 3)
    board.fill_cell(33, 4)
    board.fill_cell(23, 5)
    print("new board")
    board.print_board()
    board._solution.solve_board_with_hints()
