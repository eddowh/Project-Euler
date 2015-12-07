# -*- coding: utf-8 -*-
# Conventions are according to NumPy Docstring.

"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

import time
import sys
import os
import itertools
# sys.path.append(os.path.dirname(sys.path[0]))

MAX_RUN_TIME = 30

def main():
    # input index
    idx = 1000000
    # initialize running time
    timerStart = time.time()
    # digits
    digits = range(0, 10)
    digitPerms = list(itertools.permutations(digits))
    # sort in lexicographic order
    digitPerms.sort()
    # the nth permutation (as specified in `idx`)
    idxPerm = digitPerms[idx-1]
    # combine tuple into a string
    result = ""
    for num in idxPerm:
        result += str(num)
    ##########################################################
    if (time.time() - timerStart > MAX_RUN_TIME):
        sys.exit("Maximum runtime exceeded. Script aborted.")
    ##########################################################
    # finalize running time
    timerStop = time.time()
    # print results
    title = "The millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9"
    print title
    print "-" * len(title)
    print "Result \t\t : %s" %(result)
    print "Running Time \t : %.4f sec" %(timerStop - timerStart)


if __name__ == '__main__':
    main()
