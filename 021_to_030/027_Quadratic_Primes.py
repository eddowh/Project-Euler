# -*- coding: utf-8 -*-
# Conventions are according to NumPy Docstring.

"""
Euler discovered the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n² + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |−4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
"""

import time
import sys
import os
import math
# sys.path.append(os.path.dirname(sys.path[0]))

MAX_RUN_TIME = 30


def isPrime(n):
    """
    Assume that the input is larger than 1.
    """
    if (n == 1):
        return False
    elif (n < 4):
        # 2 and 3 are primes
        return True
    elif (n % 2 == 0):
        return False
    elif (n < 9):
        # we have already excluded 4,6,8
        return True
    elif (n % 3 == 0):
        return False
    else:
        r = math.floor(math.sqrt(n))
        f = 5
        while f <= r:
            if (n % f == 0):
                return False
            if (n % (f + 2) == 0):
                return False
            f += 6
        return True


def quadraticPrime(a, b, n):
    return abs(n ** 2 + a * n + b)


def main():
    # given variables
    upperLimit = 1000
    # initialize running time
    timerStart = time.time()
    # initializing
    aMax, bMax, nMax = 0, 0, 0
    for a in range(-upperLimit, upperLimit + 1, 1):
        for b in range(-upperLimit, upperLimit + 1, 1):
            ##########################################################
            if (time.time() - timerStart > MAX_RUN_TIME):
                sys.exit("Maximum runtime exceeded. Script aborted.")
            ##########################################################
            n = 0
            while isPrime(quadraticPrime(a, b, n)):
                n += 1
            if n > nMax:
                aMax = a
                bMax = b
                nMax = n
    # finalize running time
    timerStop = time.time()
    # print results
    title = "Quadratic prime formula that produces the maximum number of consecutive primes"
    print title
    print "-" * len(title)
    print "a, b, n \t : %s, %s, %s" %(aMax, bMax, nMax)
    print "Result \t\t : %s" % (aMax * bMax)
    print "Running Time \t : %.4f sec" % (timerStop - timerStart)


if __name__ == '__main__':
    main()
