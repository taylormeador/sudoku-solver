"""Main."""

from bitboard import Board

if __name__ == "__main__":
    board = Board()
    for i in board._bitboards:
        i.set_bit(i.number)

    board.print_board()
    for bitboard in board._bitboards:
        print(bitboard)
        for i in range(9):
            print(f"square #{i} ******************** {bitboard.is_in_square(i)}")
