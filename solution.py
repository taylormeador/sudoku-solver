"""Class for finding a solution to a sudoku puzzle."""

from bitboard import Board
from enums import Cells


class Solution:
    """Class for finding a solution to a sudoku puzzle."""

    def __init__(self):
        pass

    @staticmethod
    def _solve_last_cell(numbers: set[int]) -> int:
        """Function expects a set of 8 numbers, 1-9, and returns the
        number 1-9 that is not present in that set.
        """
        return (set(range(1, 10)) - numbers).pop()

    def _find_candidates(self, board: Board, cell: Cells) -> set[int]:
        candidates = set()
        for number in range(1, 10):
            if (
                board.bitboard(number).not_in_row(row_index)
                and board.bitboard(number).not_in_column(column_index)
                and board.bitboard(number).not_in_square(square_position)
            ):
                candidates.add(number)
        return candidates


solution = Solution()
last_cell = solution._solve_last_cell(set([1, 2, 3, 4, 5, 6, 7, 8]))
print(last_cell)
