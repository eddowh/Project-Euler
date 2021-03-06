"""
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""

import time
import math


def triangle_number(n):
    """Returns the nth triangle number.

    The nth triangle number is simply the arithmetic sum (1 + 2 + 3 ... n) evaluated at n.

    Parameters
    ----------
    n : int
        This input would be used to evaluate the nth triangle number.

    Returns
    -------
    int
        The nth triangle number.

    """
    return (n * (n + 1)) / 2


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

if __name__ == '__main__':
    # input
    limit = 500
    # initialize running time
    start = time.time()
    # initialize n
    n = 1
    while True:
        n += 1
        current_tri_num = triangle_number(n)
        if len(factors(current_tri_num)) > limit:
            break
    # finalize running time
    stop = time.time()
    # print results
    print "Triangle Number: \t %s" %(current_tri_num)
    print "Running Time:    \t %.2f sec" % (stop - start)
