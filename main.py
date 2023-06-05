"""Main."""

from bitboard import Board

if __name__ == "__main__":
    board = Board()
    board.fill_cell(0, 1)
    board.fill_cell(1, 2)
    board.fill_cell(2, 3)
    board.fill_cell(3, 4)
    board.fill_cell(4, 5)
    board.fill_cell(5, 6)
    board.fill_cell(6, 7)
    board.fill_cell(7, 8)
    board.print_board()
    print(board._solution.find_single_candidate_solutions())

    board.fill_cell(9, 9)
    board.fill_cell(18, 8)
    board.fill_cell(27, 7)
    board.fill_cell(36, 6)
    board.fill_cell(45, 5)
    board.fill_cell(54, 4)
    board.fill_cell(63, 3)
    board.print_board()
    print(board._solution.find_single_candidate_solutions())

    board.fill_cell(10, 4)
    board.fill_cell(11, 5)
    board.fill_cell(19, 6)
    board.print_board()
    print(board._solution.find_single_candidate_solutions())
