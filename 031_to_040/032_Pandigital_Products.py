# -*- coding: utf-8 -*-
# Conventions are according to NumPy Docstring.

"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

import time
import itertools
import math
import sys

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


def product(aList):
    """Multiplies each number in a list.

    Parameters
    ----------
    aList : List[int | float]
        A list of numbers.

    Returns
    -------
    int | float
        The resulting product of all the numbers in the list.

    """
    res = 1
    for elem in aList:
        res *= elem
    return res


def listOfPossibleMultiplications(n, numOfMultiplicands):
    """Lists out the possible ways to multiply a number, given the number of
    multipliers and multiplicands. Depends on `itertools`.

    Parameters
    ----------
    n : int
        The number of which the multiplications will be listed out.
    numOfMultiplicands : int
        The number of multipliers and multiplicands, which has to be at least 2.

    Returns
    -------
    Tuple(int)
        Tuple containing the numbers which will multiply into `n`.
        The length of the tuple is the number of multipliers and multiplicands.

    Raises
    ------
    AssertionError
        when number of multipliers and multiplicands is less than 2.

    """
    # parse the inputs as integers in case it was float or otherwise
    n = int(n)
    numOfMultiplicands = int(numOfMultiplicands)
    # number of multipliers and multiplicands has to be at least 2
    assert numOfMultiplicands >= 2
    # leave only those which factors would multiply to the product
    return filter(lambda x: product(x) == n,
                  list(itertools.combinations(factors(n), numOfMultiplicands)))


def pandigitalMultiplications(n, numOfMultiplicands, lo, hi):
    """Returns the set of multiplications and product that results in pandigital-ism.
    Depends on `itertools`.

    Parameters
    ----------
    n : int
        The number of which the multiplications will be listed out.
    numOfMultiplicands : int
        The number of multipliers and multiplicands, which has to be at least 2.
    lo : int
        The lower limit of the pandigital qualification range.
    hi : int
        The upper limit of the pandigital qualification range.

    Returns
    -------
    Set(Tuple(int), int)
        A set containing a tuple of the multipliers and multiplicands,
        and the product itself.

    Raises
    ------
    AssertionError
        when lower limit of the pandigital qualification range is higher than
        the upper limit.

    """
    # parse the inputs as integers in case it was float or otherwise
    n, numOfMultiplicands = int(n), int(numOfMultiplicands)
    lo, hi = int(lo), int(hi)
    # assert that lo is lower than hi
    assert lo <= hi
    # using itertools, get a combination of all multiplications given
    # the number of multipliers + multiplicands
    multiplicationList = listOfPossibleMultiplications(n, numOfMultiplicands)
    # this set is used for comparison, which contains numbers
    rangeSet = set([str(num) for num in xrange(lo, hi + 1)])
    # set which contains all possible multiplications to pandigital
    pandigitalSet = set()
    for mult in multiplicationList:
        # store the characters of the string of the numbers
        # for later comparison
        pandigitalString = ""
        for elem in mult:
            pandigitalString += str(elem)
        pandigitalString += str(n)
        # if length of the string is the length of the range set
        if (len(pandigitalString) == len(rangeSet) and
                # and the sets are equal
                set(list(pandigitalString)) == rangeSet):
            # add to the pandigital set a tuple containing:
            #   - multipliers/multiplicands
            #   - the product itself
            pandigitalSet.add((mult, n))
    return pandigitalSet


def isUniqueChars(aString):
    """Check whether the input is unique in characters.

    Having the characteristic of being unique in characters mean
    not one character can be repeated. This includes spaces, dashes,
    punctuation marks, etc.

    Parameters
    ----------
    aString : str
        A valid string, containing any characters in UTF-8 encoding.

    Returns
    -------
    bool
        True if the string is unique in characters.
        False otherwise.

    Raises
    ------
    TypeError
        when the input is not of <string> type.

    Examples
    --------
    >>> print [isUniqueChars(elem) for elem in ['abc', 'a b c', 'abba', 'a-b c!d']]
    [True, False, False, True]

    """
    if (type(aString) is not str):
        raise TypeError("Input must be of <string> type.")
    # split each character into an element of a list
    stringList = list(aString)
    # check whether unique by comparing cardinality of the set with original
    # list
    return len(stringList) == len(set(stringList))


def checkForChars(aString, charList):
    """Check whether any character in a character list exists in the input string.

    Parameters
    ----------
    aString : string
        A string which will be checked for whether characters in the character list
        exist.
    charList : List(str)
        A list of string characters to check whether any of them exist in the string.

    Returns
    -------
    bool
        True if any of the character in the character list exists in the string.
        False if otherwise.

    Raises
    ------
    TypeError
        - if any element of the character list is not of <string> type
        - if the input is not of <string> type

    Examples
    --------
    >>> aString = "01234"
    >>> charLists = [['0', '5', '05'], ['0'], ['5'], ['05']]
    >>> print [checkForChars(aString, charList) for charList in charLists]
    [True, True, False, False]
    """
    # check if input is of string type
    if (type(aString) is not str):
        raise TypeError("Input must be of <string> type.")
    # check if any element in the list of characters is not of string type
    if False in [(type(char) is str for char in charList)]:
        raise TypeError("Character list should only contain string types.")
    # convert character list into set to avoid iterating over duplicates
    charList = set([str(char) for char in charList])
    for char in charList:
        if char in aString:
            return True
    return False

def main():
    # given variables
    lo = 1
    hi = 9
    # initialize running time
    timerStart = time.time()
    # filter out numbers below 10000 that aren't unique in characters
    possibleNums = filter(lambda x: isUniqueChars(str(x)), range(10000))
    # filter out numbers from above that have numbers not included in the
    # pandigital range
    possibleNums = filter(lambda x: not checkForChars(str(x), [str(n) for n in range(lo)]),
                          possibleNums)
    # store valid numbers in a set, and then sum it up all later
    resultSet = set()
    for num in possibleNums:
        ##########################################################
        if (time.time() - timerStart > MAX_RUN_TIME):
            sys.exit("Maximum runtime exceeded. Script aborted.")
        ##########################################################
        pandigitalMults = pandigitalMultiplications(num, 2, 1, 9)
        if len(pandigitalMults) > 0:
            resultSet.add(list(pandigitalMults)[0][1])
    # store answer into result
    result = sum(resultSet)
    # finalize running time
    timerStop = time.time()
    # print results
    title = "Sum of all products that can be written as a 1 through 9 pandigital"
    print title
    print "-" * len(title)
    print "Result \t\t : %s" % (result)
    print "Running Time \t : %.4f sec" % (timerStop - timerStart)

if __name__ == '__main__':
    main()
