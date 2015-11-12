"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import time
import math

def is_prime(n):
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
            if (n % (f+2) == 0):
                return False
            f += 6
        return True

def gen_primes_by_limit(limit):
    primes = [2]
    counter = 3
    while counter < limit:
        if (time.time() - start > 30):
            raise Exception("Timeout: Running of script aborted.")
        if is_prime(counter):
            primes.append(counter)
        counter += 2
    assert primes[-1] <= limit
    return primes

if __name__ == '__main__':
    # initialize running time
    start = time.time()
    primes = gen_primes_by_limit(2 * (10 ** 6))
    sum_primes = sum(primes)
    # finalize running time
    stop = time.time()
    # print results
    print "Sum of Primes < 2 Mil.: \t %s" %(sum_primes)
    print "Running Time:           \t %.2f sec" %(stop - start)
