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


class BruteForceSolution(Solution):
    """This class will implement a brute force method of finding a solution to a puzzle.
    The algorithm will work as follows:
    1. Loop through all the cells
    2. If the cell is empty, put a 1 there.
    3. Check if the 1 is valid.
    4. If it is, move to the next cell. If it isn't increment it by 1 and check again.
    5. If no number is valid, then back up one cell and increment it until you get a
       new valid number for that cell.
    """

    def solve_blank_board(self):
        """Main function for finding a brute force solution."""
        solved = False
        cell = 0
        number = 1
        previous_cell_value = 0
        while not solved:
            if self._board.cell_is_empty(cell):  # check if cell is empty
                # loop through the numbers, looking for a valid one
                cell_is_solved = False
                while number < 10:
                    if self._board.cell_can_contain(cell, number):
                        # fill the cell if the number was valid, then continue to the next cell
                        self._board.fill_cell(cell, number)
                        previous_cell_value = number
                        cell_is_solved = True
                        break
                    number += 1

                if not cell_is_solved:
                    # getting here means none of the numbers were valid, so we want
                    # to leave the cell blank, and backup to the previous cell and increment it.
                    # To backup, we need to remember what number it currently is, and start
                    # with the next number. The cell needs to be blank so that the algorithm tries to
                    # solve it.
                    number = 1 + previous_cell_value
                    previous_cell_value = self._board.get_cell_value(cell - 2)
                    self._board.fill_cell(cell - 1, 0)
                    cell -= 1
                    continue

            # we solved this cell, so we increment the cell index so we can solve the next
            cell += 1
            number = 1
            # self._board.print_board()

            # terminal case
            if cell == 81:
                solved = True
                self._board.print_board()
                print("Puzzle solved.\n")
