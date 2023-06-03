"""Main."""

from bitboard import Board
import random

if __name__ == "__main__":
    board = Board()
    for i in board._bitboards:
        i.set_bit(i.number)
        for j in range(10):
            random_number = random.randint(0, 80)
            i.set_bit(random_number)

    board.print_board()
    for bitboard in board._bitboards:
        print(bitboard)
        bitboard.print_bitboard()

    board.print_board()
