# -*- coding: utf-8 -*-
# Conventions are according to NumPy Docstring.

class Grid:
    """This grid classes represents a N by N grid represented with nested arrays/lists.

    Attributes
    ----------
    grid : list
        Nested list of two depths representing the grid.
    nrow : int
        Number of rows in the grid.
    ncol : int
        Number of columns in the grid.

    """

    def __init__(self, grid):
        """Initializer method

        Raises exception if lengths of nested list are not equal.

        Parameters
        ----------
        grid : List[List[<any type>]]
            A grid input containing a nested list of two depths,
            where the nested lists exhibit the same length.
            This equates to each row containing the same number of columns.

        """
        # if len(set([len(row) for row in grid])) != 1:
        #     raise Exception("Invalid grid input.")
        # else:
        self._grid = grid
        self._nrow = len(grid)
        self._ncol = len(grid[0])

    def __str__(self):
        """Return multi-line string representation of the grid."""
        ans = ""
        for row_idx in range(self.get_nrow()):
            # for col_idx in range(self.get_ncol()):
            #     ans += str(self.get_value(row_idx, col_idx)) + " \t "
            ans += str(self.get_row_number(row_idx))
            ans += "\n"
        return ans

    def get_nrow(self):
        """int: Get the number of rows in the grid"""
        return self._nrow

    def get_ncol(self):
        """int: Get the number of columns in the grid"""
        return self._ncol

    def get_dim(self):
        """Tuple(int): Get the dimensions (nrow, ncol) of the grid"""
        return (self.get_nrow(), self.get_ncol())

    def is_square(self):
        """Checks whether the grid is 1:1 ratio.

        Returns
        -------
        bool
            True if number of rows is equal to number of columns.
            False if otherwise.

        """
        return self.get_nrow() == self.get_ncol()

    def get_row_number(self, row_idx):
        """Isolates and gets the row of the grid, given the index specified.

        The input row index is zero-based.

        Parameters
        ----------
        row_idx : int
            The row index to be isolated and accessed.

        Returns
        -------
        List[<any type>]
            The row of the grid.

        Raises
        ------
        IndexError
            when row index input exceeds the number of rows available.

        """
        if (row_idx >= self.get_nrow()):
            raise IndexError(
                "Out of Bounds: input row index exceeded number of rows in grid.")
        else:
            return self._grid[row_idx]

    def get_column_number(self, col_idx):
        """Isolates and gets the column of the grid, given the index specified.

        The input column index is zero-based.

        Parameters
        ----------
        col_idx : int
            The column index to be isolated and accessed.

        Returns
        -------
        List[<any type>]
            The column of the grid.

        Raises
        ------
        IndexError
            when column index input exceeds the number of columns available.

        """
        if (col_idx >= self.get_ncol()):
            raise IndexError(
                "Out of Bounds: input column index exceeded number of columns in grid.")
        else:
            return [self.get_value(row, col_idx) for row in range(self.get_nrow())]

    def get_diagonal(self, row_idx, col_idx, method="down"):
        """Gets the diagonal starting from the row and col input.

        The input indices are zero-based.

        Parameters
        ----------
        row_idx : int
            The row index to be accessed.
        col_idx : int
            The column index to be accessed.
        method : Optional['up' | 'down']
            Specify method of traversing the diagonal.
            'up' would correspond to the diagonal traversing right/upwards.
            'down' would correspond to the diagonal traversing right/downwards.

        Returns
        -------
        List[<any type>]
            The diagonal starting from the input indices and traversing
            in the specified direction until it hits an edge of the grid.

        """
        assert method == "down" or method == "up"
        diag = []
        # specify conditions of when to stop traversing
        if method == "down":
            while (row_idx < self.get_nrow() and
                   col_idx < self.get_ncol()):
                diag.append(self.get_value(row_idx, col_idx))
                row_idx += 1
                col_idx += 1
        else:
            while (row_idx >= 0 and
                   col_idx < self.get_ncol()):
                diag.append(self.get_value(row_idx, col_idx))
                row_idx -= 1
                col_idx += 1
        return diag

    def get_value(self, row_idx, col_idx):
        """Return a value of the grid given the row and column input.

        The input indices are zero-based.

        Parameters
        ----------
        row_idx : int
            The row index to be accessed.
        col_idx : int
            The column index to be accessed.

        Returns
        -------
        <any type>
            The value at the specified row and column indices.

        Raises
        ------
        IndexError
            when either the row or column input is out of bounds.

        """
        if (row_idx >= self.get_nrow() or
                col_idx >= self.get_ncol()):
            raise IndexError()
        else:
            return self._grid[row_idx][col_idx]

    def clone(self):
        """Clone the existing grid and creates a new Grid object.

        Note that this method is useful when the user does not want to
        change the original object.

        Returns
        -------
        Grid
            A new, identical (but not equal) Grid object.

        """
        new_grid = Grid(list(self._grid))
        return new_grid
