"""
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

import time
import math

if __name__ == '__main__':
    # input limit
    limit = 1 * 10 ** 6
    # initialize running time
    start = time.time()
    # initialize maximum length
    max_starting_number, max_chain_length = 1, 1
    # initialize a cache
    collatz_cache = {1 : 1}
    for i in range(2, limit):
        n = i
        collatz_length = 0
        # we know that once the sequence number reaches a number below the starting,
        # it has already been calculated, so we extract the info from the cache
        # hence the loop stopping once it reaches below the starting number
        while (n != 1 and n >= i):
            collatz_length += 1
            if n % 2 == 0:
                n /= 2
            else:
                n = 3 * n + 1
        collatz_cache[i] = collatz_length + collatz_cache[n]
        if collatz_cache[i] > max_chain_length:
            max_starting_number, max_chain_length = i, collatz_cache[i]
    # finalize running time
    stop = time.time()
    # print results
    print "Number with Longest Chain: \t %s" %(max_starting_number)
    print "Longest Chain Length:      \t %s" %(max_chain_length)
    print "Running Time:              \t %.2f sec" %(stop - start)
