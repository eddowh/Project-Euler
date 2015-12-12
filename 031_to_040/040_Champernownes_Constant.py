# -*- coding: utf-8 -*-
# Conventions are according to NumPy Docstring.

"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If d_n represents the nth digit of the fractional part, find the value of the following expression.

d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000
"""

import time
import sys

def concatenateDigits(lengthLimit):
    """Concatenate positive digits until desired length of string is met.

    Parameters
    ----------
    lengthLimit : int
        The maximum length of the concatenated string.

    Returns
    -------
    str
        A string of positive integers in sequence, concatenated together.

    """
    i = 1
    intString = ""
    while len(intString) < lengthLimit:
        intString += str(i)
        i += 1
    return intString


def main():
    # given variables
    indexes = [1, 10, 100, 1000, 10000, 100000, 1000000]
    # initialize running time
    timerStart = time.time()
    # generate string
    fractionalPart = concatenateDigits(max(indexes))
    # multiply the indices of the string
    champernownesConstant = 1
    for idx in indexes:
        champernownesConstant *= int(fractionalPart[idx - 1])
    # store answer into result
    result = champernownesConstant
    # finalize running time
    timerStop = time.time()
    # print results
    title = "d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000"
    print title
    print "-" * len(title)
    print "Result \t\t : %s" % (result)
    print "Running Time \t : %.4f sec" % (timerStop - timerStart)

if __name__ == '__main__':
    main()
