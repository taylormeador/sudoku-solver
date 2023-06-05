"""Main."""

from bitboard import Board

if __name__ == "__main__":
    board = Board()
    board.bitboard(1).set_bit(0)
    board.print_board()
    print(board._solution._find_candidates(0))
