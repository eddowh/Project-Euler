# -*- coding: utf-8 -*-
# Conventions are according to NumPy Docstring.

"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

import time
import sys
# import os
# sys.path.append(os.path.dirname(sys.path[

MAX_RUN_TIME = 30


def sumPowerOfDigits(m, n):
    """Sum the n-th powers of the digits of m.

    Parameters
    ----------
    m : int
        The number whose nth power of digits will be summed up.
        If input is float, round down to nearest integer (also known as floor).
    n : int
        The specified power.
        If input is float, round down to nearest integer (also known as floor).

    Returns
    -------
    int
        The sum of nth powers of m's digits.

    """
    # parse as integers
    m = int(m)
    n = int(n)
    return sum([int(i) ** n for i in str(m)])

def isSumPowerOfDigits(m, n):
    """Check whether `m` can be written as the sum of n-th powers of m's digits.

    Parameters
    ----------
    m : int
        The number whose nth power of digits will be summed up.
        If input is float, round down to nearest integer (also known as floor).
    n : int
        The specified power.
        If input is float, round down to nearest integer (also known as floor).

    Returns
    -------
    bool
        True if m can be written as the sum of n-th powers of m's digits,
            with the exception of numbers with 1 digit.
        False otherwise.

    """
    # parse as integers
    m = int(m)
    n = int(n)
    return (m >= 10 and m == sumPowerOfDigits(m, n))

def main():
    # given variables
    numDigits = 5
    # initialize running time
    timerStart = time.time()
    # valid numbers
    digitFifthPowers = set()
    for m in range(10, sumPowerOfDigits(999999, numDigits)):
        if isSumPowerOfDigits(m, numDigits):
            digitFifthPowers.add(m)
    # print digitFifthPowers
    ##########################################################
    if (time.time() - timerStart > MAX_RUN_TIME):
        sys.exit("Maximum runtime exceeded. Script aborted.")
    ##########################################################
    # finalize running time
    timerStop = time.time()
    # print results
    title = "Sum of all the numbers that can be written as the sum of fifth powers of their digits"
    print title
    print "-" * len(title)
    print "Result \t\t : %s" % (sum(digitFifthPowers))
    print "Running Time \t : %.4f sec" % (timerStop - timerStart)


if __name__ == '__main__':
    main()
