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
        """Returns a set of candidate numbers for a cell. It does not take anything into account
        other than if the cell, row, column, or square already contains that number.
        """
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

    def find_single_candidate_solutions(self) -> dict[int, int]:
        """Returns a dictionary of cell indices as keys and solutions as values.
        Loops through all cells and gets the candidate numbers. If the cell can only
        contain one number, then that number is the solution for the cell.
        """
        solutions = {}
        for cell in Cells:
            if self._board.cell_is_empty(cell.value):
                candidates = self._find_candidates(cell.value)
                if len(candidates) == 1:
                    solutions[cell.value] = candidates.pop()
        return solutions
