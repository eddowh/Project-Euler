# -*- coding: utf-8 -*-
# Conventions are according to NumPy Docstring.

"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

import time
import sys
import math

MAX_RUN_TIME = 30

def sumDigitFactorials(num):
    """Return sum of the factorial of digits of a number.

    Parameters
    ----------
    num : int
        An integer value of the number. Doesn't accept a float value.

    """
    return sum([math.factorial(int(char)) for char in list(str(num))])

def isCurious(num):
    return num == sumDigitFactorials(num)

def main():
    # initialize running time
    timerStart = time.time()
    # running total
    curiousNums = []
    for i in range(10, 100000):
        if isCurious(i):
            curiousNums.append(i)
    ##########################################################
    if (time.time() - timerStart > MAX_RUN_TIME):
        sys.exit("Maximum runtime exceeded. Script aborted.")
    ##########################################################
    # store answer into result
    result = sum(curiousNums)
    # finalize running time
    timerStop = time.time()
    # print results
    title = "Sum of All Curious Numbers"
    print title
    print "-" * len(title)
    print "Result \t\t : %s" % (result)
    print "Running Time \t : %.4f sec" % (timerStop - timerStart)

if __name__ == '__main__':
    main()
