"""
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

** See `./input/013_Large_Sum_Input` **
"""

import time
import os
import sys

if __name__ == '__main__':
    # read input filename
    filename = os.path.dirname(sys.path[0]).replace(
        '\\', '/') + '/input/013_Large_Sum_Input.txt'
    file = open(filename, 'r')
    # initialize running time
    start = time.time()
    # initialize sum
    large_sum = 0
    for line in file.readlines():
        if (time.time() - start > 5):
            raise Exception("Timeout: Running of script aborted.")
        large_sum += int(line[:-1])
    # finalize running time
    stop = time.time()
    # print results
    print "1st 10 Digits of Sum: \t %s" % (str(large_sum)[:10])
    print "Running Time:         \t %.2f sec" % (stop - start)
