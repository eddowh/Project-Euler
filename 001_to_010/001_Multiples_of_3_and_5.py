"""
Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

import time

def main():
    # input values
    multiples = (3,5)
    upper_limit = 5 * (10 ** 6)
    # slow method
    slow_start = time.time()
    sum_multiples(multiples, upper_limit)
    slow_stop = time.time()
    # fast method
    fast_start = time.time()
    result = fast_sum_multiples(multiples, upper_limit)
    fast_stop = time.time()
    # results
    print "Result: ", result
    print "Slow Method: ", "%.2f" %(slow_stop - slow_start)
    print "Fast Method: ", "%.2f" %(fast_stop - fast_start)

def sum_multiples(multiples, upper_limit):
    total = 0
    for i in range(upper_limit):
        if (ormap(lambda x: i % x == 0, multiples)):
            total += i
    return total

def fast_sum_multiples(multiples, upper_limit):
    # upper limit is not inclusive
    upper_limit -= 1
    # initiate running total
    total = 0
    # add to total the sum of the multiples
    for num in multiples:
        total += sum_divisible_by(num, upper_limit)
    # Inclusion-Exlusion Theorem:
    # do not include intersection of both multiples (subtract it out)
    prod_multiples = product(multiples)
    if prod_multiples <= upper_limit:
        total -= sum_divisible_by(prod_multiples, upper_limit)
    return total

# HELPER FUNCTIONS
# =======================================

def ormap(fn, lst):
    if True in map(fn, lst):
        return True
    else:
        return False

def product(lst):
    total = 1
    for num in lst:
        total *= num
    return total

def sum_divisible_by(n, upper_limit):
    p = upper_limit / n
    return int(n * (p * (p + 1)) / 2)

# RUN
# =======================================

main()
