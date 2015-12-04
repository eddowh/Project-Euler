"""
Starting in the top left corner of a 2 x 2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
"""

import time

def count_routes(m, n, cache = {}):
    """Count number of possible routes from top left corner to bottom right corner in a m by n grid.

    Assume the possible routes are only traversed in down and right directions.

    Parameters
    ----------
    m : int
        The number of rows in the grid
    n : int
        The number of columns in the grid
    cache : dict
        Cached dictionary of number of possible routes at one point of the grid.

    Returns
    -------
    int
        The number of possible routes.

    Raises
    ------
    IndexError
        when number of rows or columns do not exceed 0.

    """
    if m < 0 or n < 0:
        raise IndexError("")
    if m == 0 or n == 0:
        return 1
    if (m,n) in cache:
        return cache[(m,n)]
    cache[(m,n)] = count_routes(m, n - 1, cache) + count_routes(m - 1, n, cache)
    return cache[(m,n)]

if __name__ == '__main__':
    # input grid size
    grid_size = 20
    # initialize running time
    start = time.time()
    for i in range(1, 20 + 1):
        if (time.time() - start > 5):
            raise Exception("Timeout: Running of script aborted.")
        # print i, count_routes(i, i)
    # finalize running time
    stop = time.time()
    # print results
    print "Routes in a %s x %s grid: \t %s" %(grid_size, grid_size, count_routes(grid_size, grid_size))
    print "Running Time:             \t %.2f sec" % (stop - start)
