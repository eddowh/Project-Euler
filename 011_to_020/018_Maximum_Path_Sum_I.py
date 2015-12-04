"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)
"""

import time
import sys
import os
sys.path.append(os.path.dirname(sys.path[0]))
import operator
from classes.Grid import Grid


def possibleRoutes(triangle, rowIndex):
    # iterate over the given rowIndex
    for i in range(len(triangle[rowIndex])):
        triangle[rowIndex][i] += max(triangle[rowIndex + 1][i],
                                     triangle[rowIndex + 1][i + 1])
    # print Grid(triangle)
    # base case - reached the top of the triangle
    if len(triangle[rowIndex]) == 1:
        return triangle[rowIndex][0]
    else:
        return possibleRoutes(triangle, rowIndex - 1)

if __name__ == '__main__':
    # read input filename
    filename = os.path.dirname(sys.path[0]).replace(
        '\\', '/') + '/input/018_Maximum_Path_Sum_I.txt'
    file = open(filename, 'r')
    # parse as grid
    input_triangle = []
    for line in file.readlines():
        row = [int(elem) for elem in line.rstrip("\n").split(" ")]
        input_triangle.append(row)
    # initialize running time
    start = time.time()
    # print triangle in grid form
    print "Original Input Triangle:"
    print Grid(input_triangle)
    # result
    result = possibleRoutes(input_triangle, len(input_triangle) - 2)
    # finalize running time
    stop = time.time()
    # print results
    print "Result of Triangle with %s Rows: \t %s" %(len(input_triangle), result)
    print "Running Time:                    \t %.2f sec" % (stop - start)
