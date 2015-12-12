# -*- coding: utf-8 -*-
# Conventions are according to NumPy Docstring.

"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""

import time
import sys
import math

MAX_RUN_TIME = 30

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

def removeLastCharacter(string, char):
    assert len(char) == 1
    for char_idx in range(len(string) - 1, -1, -1):
        if char == string[char_idx]:
            string = string[:char_idx] + string[char_idx + 1:]
            return string

def isCuriousFraction(numerator, denominator):
    numeratorChars = list(str(numerator))
    denominatorChars = list(str(denominator))
    return len(set(numeratorChars).intersection(set(denominatorChars))) != 0

def curiousSimplify(numerator, denominator):
    numeratorString = str(numerator)
    denominatorString = str(denominator)
    for char_idx in range(len(numeratorString) - 1, -1, -1):
        if numeratorString[char_idx] in denominatorString:
            denominatorString = removeLastCharacter(denominatorString, numeratorString[char_idx])
            numeratorString = numeratorString[:char_idx] + numeratorString[char_idx + 1:]
    if numeratorString == '':
        numeratorString = None
    else:
        numeratorString = int(numeratorString)
    if denominatorString == '':
        denominatorString = None
    else:
        denominatorString = int(denominatorString)
    return (numeratorString, denominatorString)

def gcd(x,y):
    return max(factors(x).intersection(factors(y)))

def simplify(numerator, denominator):
    divisor = gcd(numerator, denominator)
    return (numerator / divisor, denominator / divisor)

def main():
    # given variables
    numDigits = 2
    # initialize running time
    timerStart = time.time()
    # initialize product of four fractions
    numerator = 1
    denominator = 1
    digitRange = range(10 ** (numDigits - 1), 10 ** (numDigits))
    for i in digitRange:
        for j in digitRange:
            if isCuriousFraction(i,j) and not (i % 10 == 0 and j % 10 == 0):
                curiousFraction = curiousSimplify(i,j)
                if None not in curiousFraction and curiousFraction[1] != 0:
                    originalValue = float(i) / j
                    curiousValue = float(curiousFraction[0]) / curiousFraction[1]
                    if originalValue == curiousValue and originalValue < 1.0:
                        numerator *= curiousFraction[0]
                        denominator *= curiousFraction[1]
                        # print "%s/%s -> %s/%s" %(i,j,curiousFraction[0],curiousFraction[1])
    # simplify the fraction
    simplifiedFraction = simplify(numerator, denominator)
    # store answer into result
    result = "%s/%s" %(simplifiedFraction[0], simplifiedFraction[1])
    # finalize running time
    timerStop = time.time()
    # print results
    title = "Denominator of the Product of Curious Fractions"
    print title
    print "-" * len(title)
    print "Result \t\t : %s" % (result)
    print "Running Time \t : %.4f sec" % (timerStop - timerStart)

if __name__ == '__main__':
    main()
