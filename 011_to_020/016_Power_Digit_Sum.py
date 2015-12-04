"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?"""

import time
import sys
import math

if __name__ == '__main__':
    # input exponential
    exp = 1000
    # initialize running time
    start = time.time()
    # parse integer to string
    power_digits = str(2 ** exp)
    # calculate sum of digits
    total = 0
    for i in range(len(power_digits)):
        total += int(power_digits[i])
    if (time.time() - start > 30):
        raise Exception("Timeout: Running of script aborted.")
    # finalize running time
    stop = time.time()
    # print results
    print "Sum of Digits of (2 ^ %s): \t %s" %(exp, total)
    print "Running Time:              \t %.2f sec" %(stop - start)
