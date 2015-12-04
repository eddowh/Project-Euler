# -*- coding: utf-8 -*-
# Conventions are according to NumPy Docstring.

"""
n! means n * (n − 1) * ... * 3 * 2 * 1

For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

import time
import math

if __name__ == '__main__':
    # input factorial number
    inputNum = 100
    # initialize running time
    start = time.time()
    numFactorial = math.factorial(inputNum)
    numFactorialString = str(numFactorial)
    # sum of the digits initialized
    sumDigits = 0
    for char_idx in range(len(numFactorialString)):
        sumDigits += int(numFactorialString[char_idx])
    # finalize running time
    stop = time.time()
    # print results
    print "Sum of Digits of %s!: \t %s" %(inputNum, sumDigits)
    print "Running Time:         \t %.2f sec" %(stop - start)
