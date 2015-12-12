# -*- coding: utf-8 -*-
# Conventions are according to NumPy Docstring.

"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

import time
import sys

MAX_RUN_TIME = 30

def toBinary(num):
    return bin(num)[2:]

def isPalindrome(string):
    return string == string[::-1]

def main():
    # given variables
    upperLimit = 1 * 10 ** 6
    # initialize running time
    timerStart = time.time()
    # create empty list and fill it with palindromes
    palindromes = []
    for n in range(upperLimit):
        ##########################################################
        if (time.time() - timerStart > MAX_RUN_TIME):
            sys.exit("Maximum runtime exceeded. Script aborted.")
        ##########################################################
        if isPalindrome(str(n)) and isPalindrome(toBinary(n)):
            palindromes.append(n)
    # store answer into result
    result = sum(palindromes)
    # finalize running time
    timerStop = time.time()
    # print results
    title = "Number of Double-Base Palindromes Less Than %s" %(upperLimit)
    print title
    print "-" * len(title)
    print "Result \t\t : %s" % (result)
    print "Running Time \t : %.4f sec" % (timerStop - timerStart)

if __name__ == '__main__':
    main()
