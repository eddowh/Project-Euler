"""
In the 20 x 20 grid below, four numbers along a diagonal line have been marked in red.

08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

The product of these numbers is 26 * 63 * 78 * 14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20 * 20 grid?
"""

import time
import sys
import os
sys.path.append(os.path.dirname(sys.path[0]))
import operator
from classes.Grid import Grid

OPS = {"+": operator.add,
       "-": operator.sub,
       "*": operator.mul,
       "/": operator.div}

def max_result(lst, num_adj, operator):
    """Find the maximum product of N adjacent numbers in a list.

    Parameters
    ----------
    lst : List[int]
        The list containing the numbers to be operated on.
    num_adj : int
        The number of adjacent items to be operated on.
    operator : string
        The operator to be used on the list.

    Returns
    -------
    Tuple((int, int, int, int), int)
        A tuple containing a tuple of the numbers operated on to find the greatest product, and the greatest product itself.

    Raises
    ------
    IndexError
        when specified number of adjacent items to be operated on exceeds the number of elements in the list.

    Examples
    --------
    >>> grid = [[1,2,3,4,5,6,7,8,9,10],
                [1,3,5,7,9,2,4,6,8,10]]
    >>> print max_result(grid[0], 4)
    5040
    >>> print max_result(grid[1], 2)
    80
    >>> print max_result(grid[1], 0)
    None
    >>> print max_result(grid[0], 1)
    10

    """
    if num_adj == 0:
        return
    elif num_adj == 1:
        return max(lst)
    elif num_adj > len(lst):
        raise IndexError("")
    else:
        # clone the list so original input isn't changed
        lst_clone = list(lst)
        # operator
        op = OPS[operator]
        # initialize values
        max_res = 0
        max_res_nums = ""
        for i in range(len(lst_clone) - (num_adj - 1)):
            res = lst_clone[i]
            res_nums = str(res)
            for j in range(i + 1, i + num_adj):
                res = op(res, lst_clone[j])
                res_nums += " " + str(lst_clone[j])
            if res > max_res:
                max_res = res
                max_res_nums = res_nums
        max_res_nums = tuple([int(elem) for elem in max_res_nums.split()])
        return (max_res, max_res_nums)


if __name__ == '__main__':
    # read input filename
    filename = os.path.dirname(sys.path[0]).replace(
        '\\', '/') + '/input/011_Largest_Product_in_a_Grid_Input.txt'
    file = open(filename, 'r')
    # parse as grid
    input_grid = []
    for line in file.readlines():
        row = [int(elem) for elem in line[:-1].split()]
        input_grid.append(row)
    # initialize running time
    start = time.time()
    # create new Grid object
    grid = Grid(input_grid)
    print grid
    # number of adjacent items to be operated on
    num_adj = 4
    # initialize max products
    max_products = []
    # rows first
    for row_idx in range(grid.get_nrow()):
        lst = grid.get_row_number(row_idx)
        max_products.append(max_result(lst, num_adj, "*"))
    # then columns
    for col_idx in range(grid.get_ncol()):
        lst = grid.get_column_number(col_idx)
        max_products.append(max_result(lst, num_adj, "*"))
    # diagonals in column 0
    for row_idx in range(grid.get_nrow() - (num_adj - 1)):
        down = grid.get_diagonal(row_idx, 0, 'down')
        up = grid.get_diagonal((grid.get_nrow() - 1) - row_idx, 0, 'up')
        max_products.append(max_result(down, num_adj, "*"))
        max_products.append(max_result(up, num_adj, "*"))
    # diagonals from row edges
    for col_idx in range(1, grid.get_ncol() - (num_adj - 1)):
        down = grid.get_diagonal(0, col_idx, 'down')
        up = grid.get_diagonal(grid.get_nrow() - 1, col_idx, 'up')
        max_products.append(max_result(down, num_adj, "*"))
        max_products.append(max_result(up, num_adj, "*"))
    # find the maximum
    max_prod = max(max_products)
    # finalize running time
    stop = time.time()
    # print results
    print "Max Product:  \t %s" %(max_prod[0])
    print "Numbers:      \t %s" %(", ".join([str(num) for num in max_prod[1]]))
    print "Running Time: \t %.2f sec" %(stop - start)
