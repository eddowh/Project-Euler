"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import time
import math

# See how to get from
#       a + b + c = 1000
# to
#       a + b - (a * b) / 1000 = 500


def c_to_ab(a, b, sum):
    """
    Given a + b + c = S, and the Pythagorean theorem,
    Return c in terms of a and b
    """
    return - 1.0 / 2 * (2 * a * b - sum ** 2) / float(sum)

if __name__ == '__main__':
    # input values
    sum_abc = 10000
    # initialize running time
    start = time.time()
    # start guessing and estimate
    # default values
    c = 0
    found = False
    # since a < b < c
    # a cannot be greater than 1 minus 1/3 of total sum
    for a in range(sum_abc / 3 - 1):
        # since b < c, it cannot be greater than (sum - a) / 2
        # it cannot be equal to c hence the minus 1
        for b in range(a + 1, int(math.ceil((sum_abc - a) / 2) - 1)):
            # convert a (or b) to float so the equation doesn't return integer
            a = float(a)
            eq = (a + b) + c_to_ab(a, b, sum_abc)
            if (eq == float(sum_abc)):
                # convert a back to integer
                a = int(a)
                # retain value of a
                found = True
                # retain value of b
                break
        if found:
            c = sum_abc - a - b
            assert a ** 2 + b ** 2 == c ** 2
            break
    # finalize running time
    stop = time.time()
    # print results
    if found:
        print "a, b, c:            \t %s, %s, %s" % (a, b, c)
        print "Product of Triplet: \t %s" % (a * b * c)
    else:
        print "No matches found."
    print "Running Time:       \t %.2f sec" % (stop - start)
