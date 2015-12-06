# -*- coding: utf-8 -*-
# Conventions are according to NumPy Docstring.

"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

import time
import math
import sys
import os

MAX_RUN_TIME = 30

def factors(n):
    """List out the factors of the specified number.

    Parameters
    ----------
    n : int
        The number whose factors will be listed out.
        If input is float, parse it into integer first.

    Returns
    -------
    Set([int])
        A set of all the factors (meaning no duplicates).

    """
    n = int(n)
    results = set()
    for i in xrange(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            results.add(i)
            results.add(n / i)
    return results

def sumOfProperDivisors(n):
    """Sum of proper divisors of n.

    Also can be calculated as the sum of all factors of n minus n itself.

    Parameters
    ----------
    n : int
        The number whose sum of proper divisors will be evaluated.

    Returns
    -------
    int
        Sum of proper divisors of n.

    """
    return sum(factors(n)) - n

def abundancy(n):
    """The difference between sum of proper divisors of n and n itself.

    If abundancy is:
        - < 0, it is deficient.
        - == 0, it is perfect.
        - > 0, it is abundant.

    Parameters
    ----------
    n : int

    Returns
    -------
    int
        The difference between the sum of proper divisors of n and n itself.

    Examples
    --------
    >>> print abundancy(28)
    0
    >>> print abundancy(12)
    4
    >>> print abundancy(284)
    -64
    >>> print abundancy(220)
    64
    """
    return sumOfProperDivisors(n) - n

def main():
    # upper limit given, inclusive
    upperLimit = 28123
    # initialize running time
    timerStart = time.time()
    # find abundant numbers up to upper limit
    abundantNums = filter(lambda n : abundancy(n) > 0, (range(upperLimit + 1)))
    # find positive integers up to upper limit
    # that can be written as the sum of two abundant numbers
    abundantSums = set()
    for i in range(len(abundantNums)):
        ##########################################################
        if (time.time() - timerStart > MAX_RUN_TIME):
            sys.exit("Maximum runtime exceeded. Script aborted.")
        ##########################################################
        for j in range(i, len(abundantNums)):
            s = abundantNums[i] + abundantNums[j]
            if (s <= upperLimit):
                abundantSums.add(s)
    # find positive integers up to upper limit that are not in the set above
    posIntList = set(range(upperLimit + 1)).difference(abundantSums)
    # sum the positive integers together
    result = sum(list(posIntList))
    # finalize running time
    timerStop = time.time()
    # print results
    title = "Sum of all the positive integers which cannot be written as the sum of two abundant numbers"
    print title
    print "-" * len(title)
    print "Result \t\t : %s" %(result)
    print "Running Time \t : %.4f sec" %(timerStop - timerStart)


if __name__ == '__main__':
    main()
