"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

import time
import math


def is_prime(n):
    """
    Assume that the input is larger than 1.
    """
    if (n == 2):
        return True
    elif (n % 2 == 0 or n <= 1):
        return False
    else:
        sqr = int(math.sqrt(n)) + 1
        for divisor in range(3, sqr, 2):
            if (n % divisor == 0):
                return False
    return True


def gen_primes_by_limit(limit):
    primes = [2]
    counter = 3
    while counter < limit:
        if (time.time() - start > 10):
            raise Exception("Timeout: Running of script aborted.")
        if is_prime(counter):
            primes.append(counter)
        counter += 2
    assert primes[-1] <= limit
    return primes


def gen_primes_by_count(n):
    primes = [2]
    counter = 3
    while len(primes) < n:
        if (time.time() - start > 10):
            raise Exception("Timeout: Running of script aborted.")
        if is_prime(counter):
            primes.append(counter)
        counter += 2
    assert len(primes) == n
    return primes

if __name__ == '__main__':
    # initialize running time
    start = time.time()
    print gen_primes_by_count(10001)[-1]
    stop = time.time()
    # print results
    print "Running Time: \t %.2f sec" % (stop - start)
