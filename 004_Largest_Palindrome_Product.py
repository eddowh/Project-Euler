"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import time
from itertools import product

def isPalindrome(number):
    number = str(number)
    reversed = number[::-1]
    if number == reversed:
        return True
    else:
        return False

if __name__ == '__main__':
    # values
    lo = 100
    hi = 999
    maxPalindrome = 0;
    # initialize running time
    start = time.time()
    # start from the top
    for i, j in product(range(hi, lo - 1, -1), range(hi, lo - 1, -1)):
        if (time.time() - start > 3):
            raise Exception("Timeout: Running of script aborted.")
            break
        prod = i * j
        if (isPalindrome(prod) and prod > maxPalindrome):
            maxPalindrome = prod
    # finalize running time
    stop = time.time()
    # print results
    print "Largest Palindrome: ", maxPalindrome
    print "Running Time: ", "%.2f" %(stop - start)
