"""Custom classes for internally representing the sudoku game as bitboards."""

# TODO consider enums for square positions, cell indices, etc.


class Bitboard:
    """Each number of the sudoku puzzle has its own bitboard.
    The bitboard is an 81 digit number, conceptualized in binary.
    The 81 digits represent the cells of the sudoku board,
    from right to left, bottom to top. This is backwards from
    the way we naturally read in order to make bitwise
    operations and reasoning easy.
    """

    def __init__(self, number: int) -> None:
        self._number = number
        self._value: int = 0

        # since zero represents a blank cell, and we want to initialize the board
        # completely blank, we turn on all the bits in the zero bitboard
        if self._number == 0:
            for i in range(81):
                self.set_bit(i)

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

    def set_bit(self, cell_index: int) -> None:
        """Turns on the bit at the position, if it is off.
        Otherwise, do nothing.
        """
        assert 0 <= cell_index <= 80, "Invalid cell_index"
        if not self._value & 1 << cell_index:
            self._value += 1 << cell_index

    def reset_bit(self, cell_index: int) -> None:
        """Turns off the bit at the position, if it is on.
        Otherwise, do nothing.
        """
        assert 0 <= cell_index <= 80, "Invalid cell_index"
        if self._value & 1 << cell_index:
            self._value -= 1 << cell_index

    def __repr__(self) -> str:
        return f"<bitboard #{self._number}: {self.decimal_value}>"

    def print_bitboard(self):
        """Prints the bitboard in 9x9 form."""
        horizontal_line = " ———————————————————————"
        for i, number in enumerate(self.binary_value):
            if i % 9 == 0:
                print()
                if i % 27 == 0:
                    print(horizontal_line)

                print("|", end="")

            print(f" {number}", end="")

            if (i + 1) % 3 == 0 or (i + 1) % 6 == 0:
                print(" |", end="")
        print(f"\n{horizontal_line} \n")

    def is_in_row(self, row_index: int) -> bool:
        """Returns a boolean indiciating if the number is in the row."""
        shifts = range(row_index * 9, row_index * 9 + 9)
        for shift in shifts:
            if self._value & 1 << shift:
                return True
        return False

    def is_in_column(self, column_index: int) -> bool:
        """Returns a boolean indicating if the number is in the column."""
        shifts = range(column_index, column_index + 73, 9)
        for shift in shifts:
            if self._value & 1 << shift:
                return True
        return False

    def is_in_square(self, square_position) -> bool:
        """Returns a boolean indicating if the number is in the square.
        First, we get the rows and column indices for the square.
        Then, we check if the number is in one of those rows.
        If it isn't, we return False.
        If it is, we check if it is also in one of the columns.
        """
        row_indices = range(square_position // 3 * 3, square_position // 3 * 3 + 3)
        column_indices = range(square_position % 3 * 3, square_position % 3 * 3 + 3)
        in_a_row = any([self.is_in_row(row_index) for row_index in row_indices])
        if in_a_row:
            return any(
                [self.is_in_column(column_index) for column_index in column_indices]
            )
        return False


def _get_square_indices() -> dict[list[tuple]]:
    square_indices = {}
    for square in range(9):
        vertical_offset = square // 3 * 27
        horizontal_offset = square % 3 * 3
        bottom_right_index = horizontal_offset + vertical_offset
        position_indices = [
            (bottom_right_index + offset, bottom_right_index + offset + 3)
            for offset in (0, 9, 18)
        ]
        square_indices[square] = position_indices
    return square_indices


class Board:
    """Class that represents the entirety of the sudoku board."""

    def __init__(self) -> None:
        self._zero = Bitboard(0)
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
            self._zero,
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

    def _bitboard(self, number: int):
        """Returns the bitboard corresponding to the number argument."""
        assert 0 <= number <= 9, "Invalid bitboard selection"
        return self._bitboards[number]

    def to_list(self) -> list[int]:
        """Combines all bitboards into a list of 81 integers. 0 represents a blank cell."""

        # TODO check that bits are not on in multiple boards?
        numbers = [None] * 81
        for bitboard in self._bitboards:
            for cell_index in range(81):
                if bitboard.decimal_value & 1 << cell_index:
                    numbers[cell_index] = bitboard.number
        return numbers

    def print_board(self) -> None:
        """Prints the sudoku board in 9x9 form."""
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
        The position is defined as an integer 0-8, from the bottom right to
        the top left of the board.
        """
        numbers = self.to_list()
        indices = self._square_indices[position]
        rows = [numbers[index_pair[0] : index_pair[1]] for index_pair in indices]
        flattened_rows = [number for row in rows for number in row]
        return set(flattened_rows)

    def generate_random_board(self, difficulty: str = "Medium", solved: bool = False):
        """Generates a random, valid game board, solved or unsolved."""
        pass
