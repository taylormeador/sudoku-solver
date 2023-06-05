"""Class for finding a solution to a sudoku puzzle."""

from enums import Cells, Numbers


class Solution:
    """Class for finding a solution to a sudoku puzzle."""

    def __init__(self, board):
        self._board = board

    @staticmethod
    def solve_last_cell(numbers: set[int]) -> int:
        """Function expects a set of 8 numbers, 1-9, and returns the
        number 1-9 that is not present in that set.
        """
        return (set(range(1, 10)) - numbers).pop()

    def _find_candidates(self, cell: int) -> set[int]:
        cell = list(Cells)[cell]
        candidates = set()
        for number in Numbers:
            if (
                self._board.bitboard(number.value).not_in_cell(cell.value)
                and self._board.bitboard(number.value).not_in_row(cell.row)
                and self._board.bitboard(number.value).not_in_column(cell.column)
                and self._board.bitboard(number.value).not_in_square(cell.square)
            ):
                candidates.add(number.value)
        return candidates
