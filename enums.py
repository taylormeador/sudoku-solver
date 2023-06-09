# pylint: disable=invalid-name
"""Module that contains enums used to represent and solve the sudoku puzzle."""

from enum import Enum
from typing import Iterable


class Squares(Enum):
    """The square positions are 0-8, from bottom right to top left.

     -----------
    | 8 | 7 | 6 |
     -----------
    | 5 | 4 | 3 |
     -----------
    | 2 | 1 | 0 |
     -----------

    """

    zero = 0
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8

    def __init__(self, position) -> None:
        self._indices = self._calculate_square_indices()
        self._position = position

    @staticmethod
    def _calculate_square_indices() -> dict[list[Iterable]]:
        """Method that pre computes the cell indices in a square and stores them in a dict.
        The list contains three tuples.

        square_indices[0] = [range(0, 3), range(9, 12), range(18, 21)]

        """
        square_indices = {}
        for position in range(9):
            vertical_offset = position // 3 * 27
            horizontal_offset = position % 3 * 3
            bottom_right_index = horizontal_offset + vertical_offset
            position_indices = [
                range(bottom_right_index + offset, bottom_right_index + offset + 3)
                for offset in (0, 9, 18)
            ]
            square_indices[position] = position_indices
        return square_indices

    @property
    def indices(self) -> list[tuple]:
        """Returns a list of tuples which represent the start and end ranges
        of the indices in the square.
        """
        return self._indices[self.value]

    @property
    def rows(self) -> Iterable[int]:
        """Returns a range which is the indices of the rows that are in the square."""
        return range(self.value // 3 * 3, self.value // 3 * 3 + 3)

    @property
    def columns(self):
        """Returns a range which is the indices of the columns that are in the square."""
        return range(self.value % 3 * 3, self.value % 3 * 3 + 3)


class Cells(Enum):
    """The cells are indexed 0-80, from bottom right to top left.

    80  79  78 | 77  76  75 | 74  73  72
    71  70  69 | 68  67  66 | 65  64  63
    62  61  60 | 59  58  57 | 56  55  54
    ------------------------------------
    53  52  51 | 50  49  48 | 47  46  45
    44  43  42 | 41  40  39 | 38  37  36
    35  34  33 | 32  31  30 | 29  28  27
    ------------------------------------
    26  25  24 | 23  22  21 | 20  19  18
    17  16  15 | 14  13  12 | 11  10  9
    8   7   6  | 5   4   3  | 2   1   0

    """

    zero = 0
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
    ten = 10
    eleven = 11
    twelve = 12
    thirteen = 13
    fourteen = 14
    fifteen = 15
    sixteen = 16
    seventeen = 17
    eighteen = 18
    nineteen = 19
    twenty = 20
    twenty_one = 21
    twenty_two = 22
    twenty_three = 23
    twenty_four = 24
    twenty_five = 25
    twenty_six = 26
    twenty_seven = 27
    twenty_eight = 28
    twenty_nine = 29
    thirty = 30
    thirty_one = 31
    thirty_two = 32
    thirty_three = 33
    thirty_four = 34
    thirty_five = 35
    thirty_six = 36
    thirty_seven = 37
    thirty_eight = 38
    thirty_nine = 39
    forty = 40
    forty_one = 41
    forty_two = 42
    forty_three = 43
    forty_four = 44
    forty_five = 45
    forty_six = 46
    forty_seven = 47
    forty_eight = 48
    forty_nine = 49
    fifty = 50
    fifty_one = 51
    fifty_two = 52
    fifty_three = 53
    fifty_four = 54
    fifty_five = 55
    fifty_six = 56
    fifty_seven = 57
    fifty_eight = 58
    fifty_nine = 59
    sixty = 60
    sixty_one = 61
    sixty_two = 62
    sixty_three = 63
    sixty_four = 64
    sixty_five = 65
    sixty_six = 66
    sixty_seven = 67
    sixty_eight = 68
    sixty_nine = 69
    seventy = 70
    seventy_one = 71
    seventy_two = 72
    seventy_three = 73
    seventy_four = 74
    seventy_five = 75
    seventy_six = 76
    seventy_seven = 77
    seventy_eight = 78
    seventy_nine = 79
    eighty = 80

    @property
    def row(self) -> int:
        """Returns the index of the row that the cell belongs to."""
        return self.value // 9

    @property
    def column(self) -> int:
        """Returns the index of the column that the cell belongs to."""
        return self.value % 9

    @property
    def square(self) -> int:
        """Returns the index of the square that the cell belongs to."""
        return (self.row // 3 * 3) + (self.column // 3)


class Rows(Enum):
    """The rows are indexed 0-8 from bottom to top.

      +---+---+---+---+---+---+---+---+---+
    8 |   |   |   |   |   |   |   |   |   |
      +---+---+---+---+---+---+---+---+---+
    7 |   |   |   |   |   |   |   |   |   |
      +---+---+---+---+---+---+---+---+---+
    6 |   |   |   |   |   |   |   |   |   |
      +---+---+---+---+---+---+---+---+---+
    5 |   |   |   |   |   |   |   |   |   |
      +---+---+---+---+---+---+---+---+---+
    4 |   |   |   |   |   |   |   |   |   |
      +---+---+---+---+---+---+---+---+---+
    3 |   |   |   |   |   |   |   |   |   |
      +---+---+---+---+---+---+---+---+---+
    2 |   |   |   |   |   |   |   |   |   |
      +---+---+---+---+---+---+---+---+---+
    1 |   |   |   |   |   |   |   |   |   |
      +---+---+---+---+---+---+---+---+---+
    0 |   |   |   |   |   |   |   |   |   |
      +---+---+---+---+---+---+---+---+---+
    """

    zero = 0
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8

    @property
    def indices(self) -> Iterable[int]:
        """Returns a range of the cell indices for the row."""
        return range(self.value * 9, self.value * 9 + 9)


class Columns(Enum):
    """The columns are indexed 0-8 from right to left.

    +---+---+---+---+---+---+---+---+---+
    |   |   |   |   |   |   |   |   |   |
    +---+---+---+---+---+---+---+---+---+
    |   |   |   |   |   |   |   |   |   |
    +---+---+---+---+---+---+---+---+---+
    |   |   |   |   |   |   |   |   |   |
    +---+---+---+---+---+---+---+---+---+
    |   |   |   |   |   |   |   |   |   |
    +---+---+---+---+---+---+---+---+---+
    |   |   |   |   |   |   |   |   |   |
    +---+---+---+---+---+---+---+---+---+
    |   |   |   |   |   |   |   |   |   |
    +---+---+---+---+---+---+---+---+---+
    |   |   |   |   |   |   |   |   |   |
    +---+---+---+---+---+---+---+---+---+
    |   |   |   |   |   |   |   |   |   |
    +---+---+---+---+---+---+---+---+---+
    |   |   |   |   |   |   |   |   |   |
    +---+---+---+---+---+---+---+---+---+
      8   7   6   5   4   3   2   1   0
    """

    zero = 0
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8

    @property
    def indices(self) -> Iterable[int]:
        """Returns a range of the cell indices for the column."""
        return range(self.value, self.value + 73, 9)


class Numbers(Enum):
    """Enum for representing the numbers in the game, 1-9."""

    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
