# -*- coding: utf-8 -*-
# Conventions are according to NumPy Docstring.

"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

import time
import sys
import math
import itertools

def isPrime(n):
    """Assesses whether a given number is a prime number.

    Parameters
    ----------
    n : int
        A nonnegative integer.

    Returns
    -------
    bool
        True if `n` is prime.
        False if otherwise.

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


def isTruncatablePrime(n):
    """Assesses whether a given number is a trunctable prime.

    Parameters
    ----------
    n : int
        A nonnegative integer.

    Returns
    -------
    bool
        True if it is prime and truncatable.
        False if otherwise.

    """
    # check if the number itself is prime, if not stop right away
    if not isPrime(n):
        return False
    # truncate from the right
    if False in map(isPrime, [n / (10 ** i) for i in xrange(1, len(str(n)))]):
        return False
    # truncate from the left
    if False in map(isPrime, [n % (10 ** i) for i in xrange(1, len(str(n)))]):
        return False
    # if pass all conditions, return True
    return True


def truncatablePrimes(count):
    """Generate a number of truncatable primes.

    Parameters
    ----------
    count : int
        A number between 1 and 11 (maximum number of truncatable prime), inclusive.

    Returns
    -------
    List[int]
        A list of truncatable primes, with the length of `count`.

    Raises
    ------
    AssertionError
        when `count` is not [1,11].

    """
    # it can't be over 11 or below 1
    assert 1 <= count and count <= 11
    # initialize empty list of truncatable primes
    truncatablePrimes = []
    odds = [1, 3, 5, 7, 9]
    # truncatable primes can only start with these base primes
    basePrimes = [2, 3, 5, 7]
    # truncatable primes can only end with these ending primes
    endPrimes = [3, 7]
    # multiplier of 10, used for tracking digits
    tenMultiplier = 1
    while True:
        for b in basePrimes:
            for e in endPrimes:
                num = (b * 10 ** tenMultiplier) + e
                oddSeq = tenMultiplier - 1
                for p in list(itertools.product(odds, repeat=oddSeq)):
                    candidate = num
                    for i in range(len(p)):
                        candidate += 10 ** (oddSeq - i) * p[i]
                    if isTruncatablePrime(candidate):
                        truncatablePrimes.append(candidate)
                        if len(truncatablePrimes) == count:
                            return truncatablePrimes
        # move on to the next digit
        tenMultiplier += 1


def main():
    # given variables
    primeCount = 11
    # initialize running time
    timerStart = time.time()
    # store answer into result - the sum of numbers in a list
    result = sum(truncatablePrimes(primeCount))
    # finalize running time
    timerStop = time.time()
    # print results
    title = "The Only Eleven Truncatable Primes"
    print title
    print "-" * len(title)
    print "Result \t\t : %s" % (result)
    print "Running Time \t : %.4f sec" % (timerStop - timerStart)

if __name__ == '__main__':
    main()
