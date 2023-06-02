"""Main."""

from bitboard import Board

if __name__ == "__main__":
    board = Board()
    for i in board._bitboards:
        i.set_bit(i.number)

    board.print_board()
    for i in range(9):
        print(board.square(i))
