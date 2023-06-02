"""Custom classes for internally representing the sudoku game as bitboards."""


class Bitboard:
    """Each number of the sudoku puzzle has its own bitboard.
    The bitboard is an 81 digit binary number.
    The 81 digits represent the squares of the sudoku board,
    from right to left, bottom to top. This is backwards from
    the way we naturally read in order to make bitwise
    operations and reasoning easy.
    """

    def __init__(self, number: int) -> None:
        self._number = number
        self._value: int = 0

    @property
    def decimal_value(self) -> int:
        """Returns the decimal number equivalent to the 81 digit binary number."""
        return self._value

    @property
    def binary_value(self) -> str:
        """Returns the 81 digit binary number with leading zeroes."""
        return format(self._value, "b").zfill(81)

    @property
    def number(self) -> int:
        """Returns the number (1-9) that this bitboard represents."""
        return self._number

    def set_bit(self, position: int) -> None:
        """Turns on the bit at the position, if it is off.
        Otherwise, do nothing.
        """
        assert 0 <= position <= 80, "Invalid position"
        if not self._value & 1 << position:
            self._value += 1 << position

    def reset_bit(self, position: int) -> None:
        """Turns off the bit at the position, if it is on.
        Otherwise, do nothing.
        """
        assert 0 <= position <= 80, "Invalid position"
        if self._value & 1 << position:
            self._value -= 1 << position

    def __repr__(self) -> str:
        return f"<bitboard #{self._number}: {self.decimal_value}>"


def _get_square_indices() -> dict[list[tuple]]:
    square_indices = {}
    for position in range(9):
        vertical_offset = position // 3 * 27
        horizontal_offset = position % 3 * 3
        bottom_right_index = horizontal_offset + vertical_offset
        position_indices = [
            (bottom_right_index + offset, bottom_right_index + offset + 3)
            for offset in (0, 9, 18)
        ]
        square_indices[position] = position_indices
    return square_indices


class Board:
    """Class that represents the entirety of the sudoku board."""

    def __init__(self) -> None:
        self._one = Bitboard(1)
        self._two = Bitboard(2)
        self._three = Bitboard(3)
        self._four = Bitboard(4)
        self._five = Bitboard(5)
        self._six = Bitboard(6)
        self._seven = Bitboard(7)
        self._eight = Bitboard(8)
        self._nine = Bitboard(9)

        self._square_indices = _get_square_indices()

    @property
    def _bitboards(self) -> tuple[Bitboard]:
        """Returns a tuple of all the bitboards."""
        bitboards = (
            self._one,
            self._two,
            self._three,
            self._four,
            self._five,
            self._six,
            self._seven,
            self._eight,
            self._nine,
        )
        return bitboards

    def bitboard(self, number: int):
        """Returns the bitboard corresponding to the number argument."""
        assert 1 <= number <= 9, "Invalid bitboard selection"
        return self._bitboards[number - 1]

    def to_list(self) -> list[int]:
        """Combines all bitboards into a list of 81 integers. 0 represents a blank cell."""
        numbers = [0] * 81
        for bitboard in self._bitboards:
            for cell in range(81):
                if bitboard.decimal_value & 1 << cell:
                    numbers[cell] = bitboard.number
        return numbers

    def print_board(self) -> None:
        """Prints the sudoku board in human readable form."""
        horizontal_line = " ———————————————————————"
        numbers = self.to_list()
        for i, number in enumerate(numbers[::-1]):
            if i % 9 == 0:
                print()
                if i % 27 == 0:
                    print(horizontal_line)

                print("|", end="")

            print(f" {number}", end="")

            if (i + 1) % 3 == 0 or (i + 1) % 6 == 0:
                print(" |", end="")
        print(f"\n{horizontal_line} \n")

    def __repr__(self) -> str:
        """String representation of Board object."""
        string_ = "\n"
        for bitboard in self._bitboards:
            string_ += f"{bitboard}\n"
        return string_

    def _row(self, row_index: int) -> set[int]:
        """Returns a set of the numbers in a row. The row_index is an
        integer 0-8, representing the rows of the board, from bottom to top.
        """
        numbers = self.to_list()
        indices = (row_index * 9, row_index * 9 + 9)
        return set(numbers[indices[0] : indices[1]])

    def _column(self, column_index: int) -> set[int]:
        """Returns a set of the numbers in a column. The col_index is an
        integer 0-8, representing the rows of the board, from right to left.
        """
        numbers = self.to_list()
        indices = [column_index + offset for offset in range(0, 81, 9)]
        return set([numbers[index] for index in indices])

    def _square(self, position: int) -> set[int]:
        """Returns a set containing the numbers in the position's square.
        The position is defined as an integer 0-8, from the bottom left to
        the top right of the board.
        """
        numbers = self.to_list()
        indices = self._square_indices[position]
        rows = [numbers[index_pair[0] : index_pair[1]] for index_pair in indices]
        flattened_rows = [number for row in rows for number in row]
        return set(flattened_rows)

    def generate_random_board(self, difficulty: str = "Medium", solved: bool = False):
        """Generates a random, valid game board, solved or unsolved."""
        pass
