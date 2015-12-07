# -*- coding: utf-8 -*-
# Conventions are according to NumPy Docstring.

"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

import time
import sys
import os

MAX_RUN_TIME = 30

def main():
    # input spiral size
    spiralSize = 1001
    assert spiralSize % 2 == 1
    # initialize running time
    timerStart = time.time()
    # total
    diagonalSum = 0
    N = spiralSize
    while N >= 3:
        ##########################################################
        if (time.time() - timerStart > MAX_RUN_TIME):
            sys.exit("Maximum runtime exceeded. Script aborted.")
        ##########################################################
        # if spiral is 5x5, the outer border is 25 + 21 + 17 + 13
        # and the inner border is 9 + 7 + 5 + 3
        # we see a pattern emerge where given a border is N by N
        # sum of the corners is 4 * (N ** 2) - 6 * (N - 1)
        # i.e. 25 + 21 + 17 + 13
        # = 25 + (25 - 4) + (25 - 8) + (25 - 12)
        # = 25 * 4 - (4 + 8 + 12)
        # = 25 * 4 - (6 * 4)
        # = 4 * (5 ** 2) - 6 * (5 - 1)
        diagonalSum += (4 * N ** 2) - 6 * (N - 1)
        N -= 2
    # account for center (which is always 1)
    diagonalSum += 1
    # finalize running time
    timerStop = time.time()
    # print results
    title = "Diagonal Sum in a 1001 x 1001 Spiral"
    print title
    print "-" * len(title)
    print "Result \t\t : %s" %(diagonalSum)
    print "Running Time \t : %.4f sec" %(timerStop - timerStart)


if __name__ == '__main__':
    main()
