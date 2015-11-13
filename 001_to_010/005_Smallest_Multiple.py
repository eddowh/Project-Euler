"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
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

if __name__ == '__main__':
    # initialize input values
    limit = 20
    # initialize running time
    start = time.time()
    # generate prime numbers that do not exceed limit
    primes = [2]
    init_prime = 3
    while (init_prime <= limit):
        if (is_prime(init_prime)):
            primes.append(init_prime)
        init_prime += 2
    # find the smallest positive evenly divisible number!
    n = 1
    for prime in primes:
        n *= prime ** int(math.log(limit, prime))
    # finalize running time
    stop = time.time()
    # print results
    print "Primes: \t %s" %(primes)
    print "Result: \t %s" %n
    print "Running Time: \t %.2f seconds" %(stop - start)
