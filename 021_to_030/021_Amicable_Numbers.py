# -*- coding: utf-8 -*-
# Conventions are according to NumPy Docstring.

"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

import time
import sys
import math

MAX_RUN_TIME = 10

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

def d(n):
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

def main():
    # inputs
    upperLimit = 10000
    # initialize running time
    timerStart = time.time()
    # sum of all amicable numbers under the upper limit
    amicableNumbers = set()
    for a in range(1, upperLimit):
        ###
        if (time.time() - timerStart > MAX_RUN_TIME):
            sys.exit("ABORT")
        ###
        if a not in amicableNumbers:
            b = d(a)
            d_b = d(b)
            if (a != b and d_b == a):
                # print a, b
                amicableNumbers.add(a)
                amicableNumbers.add(b)
    # find sum
    amicableSum = sum(amicableNumbers)
    # finalize running time
    timerStop = time.time()
    # print results
    print "Sum of All Amicable Numbers Under %s =" %(upperLimit)
    print "Result \t\t : %s" %(amicableSum)
    print "Running Time \t : %.4f sec" %(timerStop - timerStart)

if __name__ == '__main__':
    main()
