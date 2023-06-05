"""Custom classes for internally representing the sudoku game as bitboards."""

from solution import Solution
from enums import Squares, Cells, Rows, Columns


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
        self._value = 0

        # since zero represents a blank cell, and we want to initialize the board
        # completely blank, we turn on all the bits in the zero bitboard
        if self._number == 0:
            for cell in Cells:
                self.set_bit(cell.value)

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

    def set_bit(self, cell: int) -> None:
        """Turns on the bit at the cell index, if it is off.
        Otherwise, do nothing.
        """
        assert 0 <= cell <= 80, "Invalid cell index"
        if not self._value & (1 << cell):
            self._value += 1 << cell

    def reset_bit(self, cell: int) -> None:
        """Turns off the bit at the cell index, if it is on.
        Otherwise, do nothing.
        """
        assert 0 <= cell <= 80, "Invalid cell index"
        if self._value & (1 << cell):
            self._value -= 1 << cell

    def __repr__(self) -> str:
        return f"<bitboard #{self._number}: {self.decimal_value}>"

    def print_bitboard(self) -> None:
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

    def is_in_row(self, row: int) -> bool:
        """Returns a boolean indicating if the number is in the row."""
        for index in list(Rows)[row].indices:
            if self._value & (1 << index):
                return True
        return False

    def is_in_column(self, column: int) -> bool:
        """Returns a boolean indicating if the number is in the column."""
        for index in list(Columns)[column].indices:
            if self._value & (1 << index):
                return True
        return False

    def is_in_square(self, square: int) -> bool:
        """Returns a boolean indicating if the number is in the square.
        First, we get the rows and column indices for the square.
        Then, we check if the number is in one of those rows.
        If it isn't, we return False.
        If it is, we check if it is also in one of the columns.
        """
        square = list(Squares)[square]
        for indices in square.indices:
            for index in indices:
                if self._value & (1 << index):
                    return True
        return False

    def is_in_cell(self, cell: int) -> bool:
        """Returns True if the number is in the cell, False otherwise."""
        return bool(self._value & (1 << cell))

    def not_in_row(self, row: int) -> bool:
        """Convenience function to find if number is not in a row."""
        return not self.is_in_row(row)

    def not_in_column(self, column: int) -> bool:
        """Convenience function to find if number is not in a column."""
        return not self.is_in_column(column)

    def not_in_square(self, square: int) -> bool:
        """Convenience function to find if number is not in a square."""
        return not self.is_in_square(square)

    def not_in_cell(self, cell: int) -> bool:
        """Convenience function to find if number is not in a cell."""
        return not self.is_in_cell(cell)


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

        self._solution = Solution(self)

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

    def bitboard(self, number: int) -> Bitboard:
        """Returns the bitboard corresponding to the number argument."""
        assert 0 <= number <= 9, "Invalid bitboard selection"
        return self._bitboards[number]

    def to_list(self) -> list[int]:
        """Combines all bitboards into a list of 81 integers. 0 represents a blank cell."""

        # TODO check that bits are not on in multiple boards?
        numbers = [None] * 81
        for bitboard in self._bitboards:
            for cell in Cells:
                if bitboard.decimal_value & 1 << cell.value:
                    numbers[cell.value] = bitboard.number
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

    def cell_is_empty(self, cell: int) -> bool:
        """Returns True if the cell is empty (0), False otherwise."""
        return bool(self.bitboard(0).decimal_value & (1 << cell))

    def fill_cell(self, cell: int, number: int) -> None:
        """Places the number in the cell on the board by setting the bit in the
        correct bitboard, and also resetting the bit in all other bitboards.
        """
        for bitboard in self._bitboards:
            if bitboard.number != number:
                bitboard.reset_bit(cell)
            else:
                bitboard.set_bit(cell)
