# -*- coding: utf-8 -*-
# Conventions are according to NumPy Docstring.

"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

import time
import sys

MAX_RUN_TIME = 30


def recurringFractionLength(n):
    """Find the length of the recurring cycle in the decimal fraction part of (1 / n).

    Parameters
    ----------
    n : int
        The denominator.

    Returns
    -------
    int
        Length of the recurring cycle in the decimal fraction part of (1/n).
        
    """
    # initial remainder
    rem = 1 % n
    foundRemainders = [rem]
    while True:
        rem *= 10
        rem %= n
        if rem not in foundRemainders:
            foundRemainders.append(rem)
        else:
            break
    # print foundRemainders
    return len(foundRemainders)


def main():
    # given variables
    upperLimit = 1000
    # initialize running time
    timerStart = time.time()
    # initialize maximum
    d = 1
    maxChain = 1
    for i in range(1, upperLimit):
        ##########################################################
        if (time.time() - timerStart > MAX_RUN_TIME):
            sys.exit("Maximum runtime exceeded. Script aborted.")
        ##########################################################
        currentChain = recurringFractionLength(i)
        if currentChain > maxChain:
            maxChain = currentChain
            d = i
    # finalize running time
    timerStop = time.time()
    # print results
    title = "The value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part"
    print title
    print "-" * len(title)
    print "Result \t\t : %s" % (d)
    print "Running Time \t : %.4f sec" % (timerStop - timerStart)


if __name__ == '__main__':
    main()
