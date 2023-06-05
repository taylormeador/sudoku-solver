"""Class for finding a solution to a sudoku puzzle."""


class Solution:
    """Class for finding a solution to a sudoku puzzle."""

    def __init__(self):
        pass

    def _find_last_cell(self, numbers: set[int]) -> int:
        """Function expects a set of 8 numbers, 1-9, and returns the
        number 1-9 that is not present in that set.
        """
        return (set(range(1, 10)) - numbers).pop()


solution = Solution()
last_cell = solution._find_last_cell(set([1, 2, 3, 4, 5, 6, 7, 8]))
print(last_cell)
