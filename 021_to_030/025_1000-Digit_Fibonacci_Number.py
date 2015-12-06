# -*- coding: utf-8 -*-
# Conventions are according to NumPy Docstring.

"""
The Fibonacci sequence is defined by the recurrence relation:

F_n = F_{n−1} + F_{n−2}, where F_1 = 1 and F_2 = 1.
Hence the first 12 terms will be:

F_1 = 1
F_2 = 1
F_3 = 2
F_4 = 3
F_5 = 5
F_6 = 8
F_7 = 13
F_8 = 21
F_9 = 34
F_10 = 55
F_11 = 89
F_12 = 144

The 12th term, F_12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

import time
import sys
import os
# sys.path.append(os.path.dirname(sys.path[0]))

MAX_RUN_TIME = 10


def fib(n, memo_dict):
    """
    Memoized Fibonacci function
    """
    if n in memo_dict:
        return memo_dict[n]
    else:
        sum1 = fib(n - 1, memo_dict)
        sum2 = fib(n - 2, memo_dict)
        sum_total = sum1 + sum2
        memo_dict[n] = sum_total
        return sum_total

def main():
    # initialize running time
    timerStart = time.time()
    # given variables
    numDigits = 1000
    fibDict = {1: 1, 2: 1}
    # which index is the first Fibonacci term to contain N digits?
    i = 1
    F_i = fib(i, fibDict)
    while len(str(F_i)) < numDigits:
        ##########################################################
        if (time.time() - timerStart > MAX_RUN_TIME):
            sys.exit("Maximum runtime exceeded. Script aborted.")
        ##########################################################
        i += 1
        F_i = fib(i, fibDict)
    # finalize running time
    timerStop = time.time()
    # print results
    title = "Index of the first term in the Fibonacci sequence to contain 1000 digits"
    print title
    print "-" * len(title)
    print "Result \t\t : %s" %(i)
    print "Running Time \t : %.4f sec" % (timerStop - timerStart)

if __name__ == '__main__':
    main()

# # Alternative Solution (Courtesy of `merliecat` on ProjectEuler)
# # Note the use of a length two array and how it is indexed idx=i%2 so there's no need to copy values around.
# n = 10**999
# a = [1, 1]
# i = 2
# idx = 0
# while a[idx] < n:
#     i += 1
#     idx = i%2
#     a[idx] = sum(a)
# print i
