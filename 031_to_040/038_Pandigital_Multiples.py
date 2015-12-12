# -*- coding: utf-8 -*-
# Conventions are according to NumPy Docstring.

"""
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""

import time
import sys
import math


MAX_RUN_TIME = 30


def pandigital(n, lo, hi):
    assert (lo >= 1 and hi <= 9 and lo <= hi)
    result = ""
    for mult in range(lo, hi + 1):
        result += str(n * mult)
    return result

def isPandigital(numString, lo, hi):
    pandigitalSet = set(range(lo, hi + 1))
    resultSet = set([int(elem) for elem in list(numString)])
    return (len(numString) == len(pandigitalSet) and
            resultSet == pandigitalSet)

def main():
    # given variables
    upperLimit = 1000000000
    lo = 1
    hi = 9
    # initialize running time
    timerStart = time.time()
    # initialize max
    pandigitalDict = dict()
    for i in xrange(10000):
        ##########################################################
        if (time.time() - timerStart > MAX_RUN_TIME):
            sys.exit("Maximum runtime exceeded. Script aborted.")
        ##########################################################
        maxNum = int(math.ceil(float(9) / len(str(i))))
        candidates = [pandigital(i, 1, m) for m in range(2, maxNum + 1)]
        validCandidates = filter(lambda x: len(x) == 9, candidates)
        if (len(validCandidates) > 0 and isPandigital(validCandidates[0], lo, hi)):
            pandigitalDict[i] = validCandidates[0]
    # store answer into result
    result = max(pandigitalDict.values())
    # finalize running time
    timerStop = time.time()
    # print results
    title = "Largest 1 to 9 9-digit Pandigital Number"
    print title
    print "-" * len(title)
    print "Result \t\t : %s" % (result)
    print "Running Time \t : %.4f sec" % (timerStop - timerStart)

if __name__ == '__main__':
    main()
