# -*- coding: utf-8 -*-
# Conventions are according to NumPy Docstring.

"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

import time
import sys
import os

ALPHABET_VALUE = {"A": 1,
                  "B": 2,
                  "C": 3,
                  "D": 4,
                  "E": 5,
                  "F": 6,
                  "G": 7,
                  "H": 8,
                  "I": 9,
                  "J": 10,
                  "K": 11,
                  "L": 12,
                  "M": 13,
                  "N": 14,
                  "O": 15,
                  "P": 16,
                  "Q": 17,
                  "R": 18,
                  "S": 19,
                  "T": 20,
                  "U": 21,
                  "V": 22,
                  "W": 23,
                  "X": 24,
                  "Y": 25,
                  "Z": 26}

MAX_RUN_TIME = 10

def alphabeticalValue(string):
    """Find alphabetical value of input string.

    Parameters
    ----------
    string : str
        Input string of which the alphabetical numerical value will be computed.

    Returns
    -------
    int
        The alphabetical numerical value.

    Raises
    ------
    Exception
        when input string does not contain only alphabetical letters.

    Examples
    --------
    >>> print alphabeticalValue("COLIN")
    53
    >>> print alphabeticalValue("COL123")
    Exception: String must only contain alphabetical letters.
    """
    stringCopy = string.upper()
    result = 0
    for char_idx in range(len(stringCopy)):
        char = string[char_idx]
        if char not in ALPHABET_VALUE:
            raise Exception("String must only contain alphabetical letters.")
        result += ALPHABET_VALUE[char]
    return result

def main():
    # read in file
    filename = os.path.dirname(sys.path[0]).replace(
        '\\', '/') + '/input/022_names.txt'
    file = open(filename, 'r')
    names = file.read().replace('"', "").split(",")
    # find numerical values of each name
    nameValues = []
    for name in names:
        nameValues.append((name, alphabeticalValue(name)))
    nameValues.sort()
    # name scores are just name values multipled by index number
    nameScores = []
    for valueIndex in range(len(nameValues)):
        nameValue = nameValues[valueIndex]
        nameScores.append((nameValue[0], nameValue[1] * (valueIndex + 1)))
    # find total name score
    totalNameScore = 0
    for nameScore in nameScores:
        totalNameScore += nameScore[1]
    # initialize running time
    timerStart = time.time()
    # interrupt if...
    if (time.time() - timerStart > MAX_RUN_TIME):
        sys.exit()
        # raise Exception("Timeout: Running of script aborted.")
    # finalize running time
    timerStop = time.time()
    # print results
    title = "Name Scores"
    print title
    print "-" * len(title)
    print "Result \t\t : %s" %(totalNameScore)
    print "Running Time \t : %.4f sec" % (timerStop - timerStart)


if __name__ == '__main__':
    main()
