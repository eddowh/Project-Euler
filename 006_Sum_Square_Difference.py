"""
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

import time
import math

def sum_of_squares(lo, hi):
    """
    Returns the sum of squares,
    i.e. 1^2 + 2^2 + ... + n^2
    """
    return ((2 * hi + 1) * (hi + 1) * hi - (2 * (lo - 1) + 1) * lo * (lo - 1)) / 6

def square_of_sum(lo, hi):
    """
    Returns the square of sums,
    i.e. (1 + 2 + .. + n)^2
    """
    # just square the arithmetic sums formula
    return (hi * (hi + 1) / 2 - lo * (lo - 1) / 2) ** 2

if __name__ == '__main__':
    # input values
    lo = 1
    hi = 100
    # initialize running time
    start = time.time()
    diff = square_of_sum(lo, hi) - sum_of_squares(lo, hi)
    stop = time.time()
    # print results
    print "Difference: \t %s" %(diff)
    print "Running Time: \t %.2f sec" %(stop - start)
