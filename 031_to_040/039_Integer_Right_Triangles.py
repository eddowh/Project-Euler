# -*- coding: utf-8 -*-
# Conventions are according to NumPy Docstring.

"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""

import time
import sys
import math

MAX_RUN_TIME = 30


def pythagoreanTriplets(limit):
    triplets = set()
    for a in xrange(1, limit + 1):
        for b in xrange(a, limit + 1):
            if a + b > limit:
                break
            c = math.sqrt(a ** 2 + b ** 2)
            if c == int(c):
                if a + b + c <= limit:
                    triplets.add((a,b,int(c)))
    return triplets

def main():
    # given variables
    upperLimit = 840
    # initialize running time
    timerStart = time.time()
    # initialize values
    pythagoreanSolutions = [sum(sol) for sol in pythagoreanTriplets(upperLimit)]
    # store answer into result
    result = max(pythagoreanSolutions, key = pythagoreanSolutions.count)
    # finalize running time
    timerStop = time.time()
    # print results
    title = "The Value of P for Maximized Number of solutions"
    print title
    print "-" * len(title)
    print "Result \t\t : %s" % (result)
    print "Running Time \t : %.4f sec" % (timerStop - timerStart)

if __name__ == '__main__':
    main()
