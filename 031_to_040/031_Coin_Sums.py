# -*- coding: utf-8 -*-
# Conventions are according to NumPy Docstring.

"""
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""

import time
import sys
# import os
# sys.path.append(os.path.dirname(sys.path[0]))

PENCE_PER_POUND = 100
POUND_PER_PENCE = 1.0 / PENCE_PER_POUND

MAX_RUN_TIME = 30
COINS = [1, 2, 5, 10, 20, 50, 100, 200]


def poundEquation(A, B, C, D, E, F, G, H):
    return (A * 1 + B * 2 + C * 5 + D * 10 + E * 20 + F * 50 + G * 100 + H * 200)

def ways(target, avc):
    if avc <= 1:
        return 1
    res = 0
    while target >= 0:
        res += ways(target, avc - 1)
        target -= COINS[avc - 1]
    return res

def main():
    # given variables
    target = 200  # in pence
    # initialize running time
    timerStart = time.time()
    # find total ways
    totalWays = ways(target, 8)
    # store answer into result
    result = totalWays
    # finalize running time
    timerStop = time.time()
    # print results
    title = "Different ways can £2 be made using any number of coins"
    print title
    print "-" * len(title)
    print "Result \t\t : %s" % (result)
    print "Running Time \t : %.4f sec" % (timerStop - timerStart)


if __name__ == '__main__':
    main()
