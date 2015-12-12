# -*- coding: utf-8 -*-
# Conventions are according to NumPy Docstring.

"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

import time
import sys
import math

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

def generatePrimes(limit):
    primes = [2]
    counter = 3
    while counter < limit:
        if isPrime(counter):
            primes.append(counter)
        counter += 2
    assert primes[-1] <= limit
    return primes

def shiftString(string, numOfRotations):
    return string[len(string) - numOfRotations:] + string[:len(string) - numOfRotations]

def isCircularPrime(n):
    assert isPrime(n)
    nToString = str(n)
    for char_idx in range(len(nToString)):
        shiftedString = shiftString(nToString, char_idx)
        if not isPrime(int(shiftedString)):
            return False
    return True

def main():
    # given variables
    upperLimit = 1 * 10 ** 6
    # initialize running time
    timerStart = time.time()
    # filter circular primes from all primes below upper limit
    circularPrimes = filter(isCircularPrime, generatePrimes(upperLimit))
    # store answer into result
    result = len(circularPrimes)
    # finalize running time
    timerStop = time.time()
    # print results
    title = "Circular Primes Below %s" %(upperLimit)
    print title
    print "-" * len(title)
    print "Result \t\t : %s" % (result)
    print "Running Time \t : %.4f sec" % (timerStop - timerStart)

if __name__ == '__main__':
    main()
