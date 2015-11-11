"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
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
    # input value
    n = 600851475143
    # initialize running time
    start = time.time()
    # The Pollard-Rho Algorithm
    # https://en.wikipedia.org/wiki/Integer_factorization#Factoring_algorithms
    prime_factors = [2]
    i = 3
    while (math.sqrt(i) < n):
        if (time.time() - start > 10):
            raise Exception("Timeout: Running of script aborted.")
            break
        if (n % i == 0):
            n /= i
            prime_factors.append(i)
        i += 2
    stop = time.time()
    print "Prime Factors: ", prime_factors
    print "Maximum Prime Factor: ", max(prime_factors)
    print "Running Time: ", "%.2f" %(stop - start)
