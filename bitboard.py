"""Custom classes for internally representing the sudoku game as bitboards."""


from enum import Enum


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
    def binary_value(self):  # TODO type hint
        """Returns the 81 digit binary number with leading zeroes."""
        return format(self._value, "b").zfill(81)

    @property
    def number(self) -> int:
        return self._number

    def set_bit(self, position: int) -> None:
        """Turns on the bit at the position, if it is off.
        Otherwise, do nothing.
        """
        assert 0 <= position <= 80, "Invalid position"
        if not (self._value & 1 << position):
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


class Board:
    """Class that represents the entirety of the sudoku board."""

    def __init__(self) -> None:
        # TODO should these be private?
        self._one = Bitboard(1)
        self._two = Bitboard(2)
        self._three = Bitboard(3)
        self._four = Bitboard(4)
        self._five = Bitboard(5)
        self._six = Bitboard(6)
        self._seven = Bitboard(7)
        self._eight = Bitboard(8)
        self._nine = Bitboard(9)

    @property
    def bitboards(self) -> tuple[Bitboard]:
        """Returns a tuple of the bitboards."""
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
        assert 1 <= number <= 9, "Invalid bitboard selection"
        return self.bitboards[number - 1]

    def listify(self):
        """Combines all bitboards into a list of 81 integers. 0 represents a blank square."""
        numbers = [0] * 81
        for bitboard in self.bitboards:
            for bit in range(81):
                if bitboard.decimal_value & 1 << bit:
                    numbers[80 - bit] = bitboard.number
        return numbers

    def print_board(self) -> None:
        """Prints the sudoku board in human readable form."""
        horizontal_line = " ———————————————————————"
        numbers = self.listify()
        for i, number in enumerate(numbers):
            if i % 9 == 0:
                print()
                if i % 27 == 0:
                    print(horizontal_line)

                print("|", end="")

            print(f" {number}", end="")

            if (i + 1) % 3 == 0 or (i + 1) % 6 == 0:
                print(" |", end="")
        print(f"\n {horizontal_line} \n")

    def __repr__(self) -> str:
        """String representation of Board object."""
        string_ = "\n"
        for bitboard in self._bitboards:
            string_ += f"{bitboard}\n"
        return string_
